import functools
import json
import logging
import os
import re
import time
import unicodedata
from collections import defaultdict
from pathlib import Path

import frontmatter
from fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import BaseModel
from rapidfuzz import fuzz
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("projeto-kb")

# ---------------------------------------------------------------------------
# Observabilidade (Fase 6.2) — logs JSON estruturados + tracing opcional
# ---------------------------------------------------------------------------
#
# Decisão registrada no TODO.md: logs JSON estruturados (sempre ligados,
# pesquisáveis no dashboard do Render) + OpenTelemetry via Logfire (free tier,
# opt-in via LOGFIRE_TOKEN) para tracing de verdade. Prometheus+Grafana foi
# descartado por ser trabalho de infra que não se paga no volume deste
# projeto (~100 req/dia). Ver justificativa completa no TODO.md.
#
# Logfire é opcional: só é usado se (a) o pacote estiver instalado e (b)
# LOGFIRE_TOKEN estiver definida. Sem isso, o código abaixo é um no-op — o
# FastMCP já emite spans OTEL nativamente (tool/resource/prompt), então
# ligar o Logfire é só uma questão de chamar `logfire.configure(...)`.
try:
    import logfire
except ImportError:
    logfire = None

_LOGFIRE_TOKEN = os.environ.get("LOGFIRE_TOKEN", "")
if logfire is not None and _LOGFIRE_TOKEN:
    logfire.configure(service_name="projeto-kb")
    log.info("Logfire configurado — tracing OTEL ativo")
else:
    log.info("Logfire desligado (defina LOGFIRE_TOKEN e instale `logfire` para ativar tracing)")


def log_event(**kw) -> None:
    """Emite um evento estruturado em JSON (uma linha) via o logger padrão.

    Nunca deve derrubar a chamada que o originou: qualquer falha ao
    serializar/logar é engolida silenciosamente (best-effort). Não logue
    payloads sensíveis (API keys, conteúdo bruto de queries/documentos) —
    prefira tamanhos/contagens/ids.
    """
    try:
        log.info(json.dumps({"ts": time.time(), **kw}, default=str))
    except Exception:
        pass


def _log_tool_call(tool_name: str, metrics=None):
    """Decorator para wrappers `@mcp.tool`: mede latência e loga um evento
    estruturado por chamada (status ok/error). Não deve ser aplicado às
    funções `_*_impl`, que também são chamadas internamente por outras tools
    (ex: fallback de `semantic_search` para `_search_impl`) — logar ali
    duplicaria eventos.

    `metrics`, se fornecido, é `f(*args, **kwargs) -> dict` chamado com os
    mesmos argumentos da tool para extrair metadados baratos e não-sensiveis
    (tamanhos, ids, contagens — nunca query/conteúdo bruto) a incluir no
    evento. Falhas ao extrair métricas nunca devem quebrar a chamada."""

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            extra = {}
            if metrics is not None:
                try:
                    extra = metrics(*args, **kwargs) or {}
                except Exception:
                    extra = {}
            start = time.perf_counter()
            try:
                result = fn(*args, **kwargs)
            except Exception:
                latency_ms = (time.perf_counter() - start) * 1000
                log_event(tool=tool_name, status="error", latency_ms=round(latency_ms, 2), **extra)
                raise
            latency_ms = (time.perf_counter() - start) * 1000
            log_event(tool=tool_name, status="ok", latency_ms=round(latency_ms, 2), **extra)
            return result

        return wrapper

    return decorator


KB = Path(os.environ.get("KB_PATH", Path(__file__).parent / "kb"))
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8000"))
MAX_RESULTS = int(os.environ.get("MAX_RESULTS", "50"))
MAX_QUERY_LENGTH = int(os.environ.get("MAX_QUERY_LENGTH", "500"))

mcp = FastMCP(
    name="projeto-kb",
    instructions=(
        "Base de conhecimento compartilhada do projeto SDE 2026.2 / grupo Trituradora FDM "
        "(disciplina ESMA001-23, UFABC) em formato OKF (markdown + frontmatter). Se a "
        "pergunta mencionar 'SDE', 'trituradora', 'extrusora', ESMA001, UFABC ou qualquer "
        "tema de engenharia do projeto, use estas tools ANTES de responder ou pedir mais "
        "contexto ao usuario — nao peca link de repositorio/documentacao, a resposta "
        "provavelmente ja esta aqui. Todas as tools sao somente leitura. Fluxo recomendado:\n"
        "1. Sem saber exatamente o que procurar? Comece por 'list_topics' (arvore completa) "
        "ou 'get_index' (detalhe de uma secao) para se orientar.\n"
        "2. Sabe termos especificos (nomes tecnicos, siglas, pecas)? Use 'search' primeiro "
        "— busca por palavra-chave, tolera acentos e typos.\n"
        "3. 'search' nao achou nada util, ou a pergunta e conceitual/parafraseada (nao usa "
        "os termos exatos do KB)? Use 'semantic_search' como proximo passo.\n"
        "4. Achou o id certo? Sempre chame 'fetch' para ler o conteudo completo antes de "
        "responder — search/semantic_search/list_topics/get_index retornam so id, titulo "
        "e um resumo curto, nunca o texto completo.\n"
        "5. Pergunta sobre o que mudou recentemente? Use 'get_log'. Pergunta sobre tamanho/"
        "composicao do bundle (quantos conceitos, quais tipos)? Use 'get_stats'.\n"
        "Depois do fetch, siga os outgoing_links retornados para continuar navegando o "
        "grafo de conhecimento."
    ),
)

# ---------------------------------------------------------------------------
# Rate limiting simples (in-memory, por IP/session)
# ---------------------------------------------------------------------------

RATE_LIMIT_MAX = int(os.environ.get("RATE_LIMIT_MAX", "60"))
RATE_LIMIT_WINDOW = int(os.environ.get("RATE_LIMIT_WINDOW", "60"))

_rate_counts: dict[str, list[float]] = defaultdict(list)


def _check_rate_limit(caller: str = "global") -> bool:
    """Retorna True se dentro do limite, False se excedeu."""
    now = time.time()
    window_start = now - RATE_LIMIT_WINDOW
    _rate_counts[caller] = [t for t in _rate_counts[caller] if t > window_start]
    if len(_rate_counts[caller]) >= RATE_LIMIT_MAX:
        return False
    _rate_counts[caller].append(now)
    return True


# ---------------------------------------------------------------------------
# Cache com invalidacao por mtime
# ---------------------------------------------------------------------------

_cache: list[dict] = []
_cache_mtime: float = 0.0


def _normalize(text: str) -> str:
    """Minuscula + remove acentos (e.g. 'trituração' → 'trituracao')."""
    text = text.lower()
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def _id(path: Path) -> str:
    return str(path.relative_to(KB)).replace("\\", "/").replace(".md", "")


# ---------------------------------------------------------------------------
# Compatibilidade com o contrato search/fetch do ChatGPT Deep Research (Fase 5.2)
# ---------------------------------------------------------------------------
#
# Não existe URL HTTP publica para os documentos do bundle (sao apenas arquivos
# markdown identificados por `id`). Para preencher o campo `url` exigido pelo
# contrato de Deep Research, usamos um esquema de URI interno "kb://<id>",
# seguindo o mesmo padrao ja usado pelo campo `resource` deste bundle para
# referenciar arquivos de origem (ex: "drive://<id>", ver ingest_drive.py).
# Este NAO e um link clicavel/HTTP — e apenas um identificador opaco que,
# resolvido via `fetch(id)`, retorna o documento completo.
_KB_URI_SCHEME = "kb://"


def _kb_url(doc_id: str) -> str:
    """Monta a pseudo-URL kb://<id> usada nos campos `url` de search/fetch."""
    return f"{_KB_URI_SCHEME}{doc_id}" if doc_id else ""


_SNIPPET_LENGTH = 300


def _snippet(doc: dict) -> str:
    """Texto curto para o campo `text` de search: description, ou um trecho do
    corpo se a description estiver vazia (fallback para compatibilidade com
    ChatGPT Deep Research, que exige um snippet por resultado)."""
    if doc.get("description"):
        return doc["description"]
    body = (doc.get("body") or "").strip()
    if not body:
        return ""
    excerpt = " ".join(body.split())[:_SNIPPET_LENGTH]
    return excerpt


def _load(path: Path) -> dict:
    try:
        post = frontmatter.load(path)
    except Exception as exc:
        log.warning("Falha ao carregar %s: %s", path, exc)
        return {
            "id": _id(path),
            "type": "Erro",
            "title": path.name,
            "description": f"Erro ao ler: {exc}",
            "resource": "",
            "tags": [],
            "timestamp": "",
            "body": "",
        }
    return {
        "id": _id(path),
        "type": post.get("type", "Conceito"),
        "title": post.get("title", _id(path)),
        "description": post.get("description", ""),
        "resource": post.get("resource", ""),
        "tags": post.get("tags", []),
        "timestamp": str(post.get("timestamp", "")),
        "body": post.content,
    }


def _all() -> list[dict]:
    global _cache, _cache_mtime
    md_files = sorted(KB.glob("**/*.md"))
    if not md_files:
        _cache, _cache_mtime = [], 0.0
        return _cache
    current_mtime = max(f.stat().st_mtime for f in md_files)
    if current_mtime != _cache_mtime or not _cache:
        log.info("Recarregando bundle (%d arquivos)", len(md_files))
        _cache = [_load(p) for p in md_files]
        _cache_mtime = current_mtime
    return _cache


def invalidate_cache() -> None:
    """Força recarga na próxima chamada (útil em testes)."""
    global _cache, _cache_mtime
    _cache, _cache_mtime = [], 0.0


# ---------------------------------------------------------------------------
# Busca semantica (lazy-load do indice)
# ---------------------------------------------------------------------------

_semantic_index = None


def _get_semantic_index():
    global _semantic_index
    if _semantic_index is not None:
        return _semantic_index
    try:
        from embeddings import CHROMA_DIR, SemanticIndex

        chroma_path = Path(CHROMA_DIR)
        if chroma_path.exists():
            _semantic_index = SemanticIndex(kb_root=KB, chroma_dir=chroma_path)
            if _semantic_index.count() > 0:
                log.info("Índice semântico carregado (%d docs)", _semantic_index.count())
                return _semantic_index
            _semantic_index = None
    except Exception as exc:
        log.warning("Índice semântico indisponível: %s", exc)
        _semantic_index = None
    return None


_SEMANTIC_SCORE_THRESHOLD = 0.25


def _semantic_search_impl(query: str, limit: int = 5) -> list[dict]:
    """Busca semântica com fallback para keyword."""
    raw = query.strip()
    if not raw:
        return [
            {
                "id": "",
                "type": "",
                "title": "Query vazia",
                "description": "Forneça pelo menos um termo de busca.",
            }
        ]

    idx = _get_semantic_index()
    if idx is None:
        log.info("semantic_search fallback → keyword search")
        return _search_impl(raw, limit)

    hits = idx.query(raw, n_results=limit)
    log.info("semantic_search(%r) → %d hits", raw, len(hits))

    if hits and hits[0]["score"] < _SEMANTIC_SCORE_THRESHOLD:
        keyword_results = _search_impl(raw, limit)
        seen_ids = {h["id"] for h in hits}
        for kr in keyword_results:
            if kr["id"] not in seen_ids:
                hits.append(kr)
                seen_ids.add(kr["id"])
            if len(hits) >= limit:
                break

    return hits or [
        {
            "id": "",
            "type": "",
            "title": "Nada encontrado",
            "description": f"Sem resultado para '{raw}'.",
        }
    ]


# ---------------------------------------------------------------------------
# Scoring de relevancia
# ---------------------------------------------------------------------------

_WEIGHT_TITLE = 8
_WEIGHT_TAGS = 4
_WEIGHT_DESCRIPTION = 2
_WEIGHT_BODY = 1
_FUZZY_THRESHOLD = 80
_FUZZY_PENALTY = 0.6


def _term_in_field(term: str, field: str) -> float:
    """Retorna 1.0 para match exato, 0 < x < 1 para fuzzy, 0 para sem match."""
    if term in field:
        return 1.0
    words = field.split()
    if not words:
        return 0.0
    best = max(fuzz.ratio(term, w) for w in words)
    if best >= _FUZZY_THRESHOLD:
        return (best / 100.0) * _FUZZY_PENALTY
    return 0.0


def _score(doc: dict, terms: list[str]) -> float:
    """Retorna score > 0 se TODOS os termos aparecem no documento (AND).
    Aceita match fuzzy (typos) com penalidade no score."""
    title = _normalize(doc["title"])
    tags = _normalize(" ".join(map(str, doc["tags"])))
    desc = _normalize(doc["description"])
    body = _normalize(doc["body"])

    total = 0.0
    for term in terms:
        t_score = 0.0
        t_score += _term_in_field(term, title) * _WEIGHT_TITLE
        t_score += _term_in_field(term, tags) * _WEIGHT_TAGS
        t_score += _term_in_field(term, desc) * _WEIGHT_DESCRIPTION
        t_score += _term_in_field(term, body) * _WEIGHT_BODY
        if t_score == 0:
            return 0
        total += t_score
    return total


# ---------------------------------------------------------------------------
# Implementacoes puras (sem decorador) — utilizadas diretamente nos testes.
# ---------------------------------------------------------------------------


def _search_impl(query: str, limit: int = 8, offset: int = 0) -> list[dict]:
    """Procura conceitos por palavra-chave. Suporta multiplos termos (AND)."""
    raw = query.strip()
    if not raw:
        return [
            {
                "id": "",
                "type": "",
                "title": "Query vazia",
                "description": "Forneça pelo menos um termo de busca.",
            }
        ]

    if len(raw) > MAX_QUERY_LENGTH:
        return [
            {
                "id": "",
                "type": "",
                "title": "Query muito longa",
                "description": f"Limite de {MAX_QUERY_LENGTH} caracteres. Reduza a consulta.",
            }
        ]

    limit = min(limit, MAX_RESULTS)

    terms = _normalize(raw).split()
    scored: list[tuple[float, dict]] = []
    for d in _all():
        s = _score(d, terms)
        if s > 0:
            scored.append(
                (
                    s,
                    {
                        "id": d["id"],
                        "type": d["type"],
                        "title": d["title"],
                        "description": d["description"],
                        # Campos adicionais para compatibilidade com o contrato
                        # search/fetch do ChatGPT Deep Research (Fase 5.2).
                        "text": _snippet(d),
                        "url": _kb_url(d["id"]),
                    },
                )
            )

    scored.sort(key=lambda x: x[0], reverse=True)
    hits = [item for _, item in scored]

    page = hits[offset : offset + limit]
    log.info("search(%r) → %d total, retornando %d (offset=%d)", raw, len(hits), len(page), offset)

    return page or [
        {
            "id": "",
            "type": "",
            "title": "Nada encontrado",
            "description": f"Sem resultado para '{raw}'.",
        }
    ]


def _fetch_impl(id: str) -> dict:
    """Retorna o conceito completo pelo id, com outgoing_links resolvidos."""
    id = id.strip()
    for d in _all():
        if d["id"] == id:
            links = re.findall(r"\]\(([^)]+\.md)\)", d["body"])
            result = dict(d)
            result["outgoing_links"] = [lnk.replace(".md", "").lstrip("/") for lnk in links]
            # Campos adicionais para compatibilidade com o contrato search/fetch
            # do ChatGPT Deep Research (Fase 5.2): `text` reaproveita o corpo
            # completo (mesmo conteudo de `body`, que permanece por compat com
            # consumidores existentes) e `url` usa o esquema kb://<id> (ver
            # _kb_url acima). `metadata` agrupa os campos "extras" do frontmatter
            # no formato que o Document.metadata de Deep Research espera.
            result["text"] = result["body"]
            result["url"] = _kb_url(result["id"])
            result["metadata"] = {
                "type": result["type"],
                "tags": result["tags"],
                "timestamp": result["timestamp"],
                "resource": result["resource"],
            }
            log.info("fetch(%r) → %s", id, result["title"])
            return result
    log.warning("fetch(%r) → não encontrado", id)
    return {
        "id": id,
        "title": "Nao encontrado",
        "body": f"Sem conceito '{id}'.",
        "text": f"Sem conceito '{id}'.",
        "url": _kb_url(id),
        "metadata": None,
        "outgoing_links": [],
    }


def _list_topics_impl() -> list[dict]:
    """Retorna a arvore de pastas/indices do bundle para navegacao."""
    topics: list[dict] = []
    for d in _all():
        if d["id"].endswith("index") or d["id"] == "index":
            children = []
            links = re.findall(r"\]\(([^)]+\.md)\)", d["body"])
            for lnk in links:
                child_id = lnk.replace(".md", "").lstrip("/")
                children.append(child_id)
            topics.append(
                {
                    "id": d["id"],
                    "title": d["title"],
                    "type": d["type"],
                    "children": children,
                }
            )
    log.info("list_topics → %d indices", len(topics))
    return topics


def _get_log_impl(last_n: int = 20) -> dict:
    """Retorna o conteúdo do log.md com as últimas N entradas."""
    for d in _all():
        if d["id"] == "log":
            lines = d["body"].strip().splitlines()
            entries = [ln for ln in lines if ln.strip().startswith("- ")]
            return {
                "id": "log",
                "title": d["title"],
                "total_entries": len(entries),
                "entries": entries[-last_n:],
            }
    return {"id": "log", "title": "Log não encontrado", "total_entries": 0, "entries": []}


def _get_stats_impl() -> dict:
    """Retorna estatísticas do bundle."""
    docs = _all()
    by_type: dict[str, int] = {}
    latest_ts = ""
    for d in docs:
        t = d["type"]
        by_type[t] = by_type.get(t, 0) + 1
        if d["timestamp"] and d["timestamp"] > latest_ts:
            latest_ts = d["timestamp"]

    folders = sorted({d["id"].rsplit("/", 1)[0] for d in docs if "/" in d["id"]})
    return {
        "total_concepts": len(docs),
        "by_type": by_type,
        "folders": folders,
        "latest_timestamp": latest_ts,
    }


def _get_index_impl(id: str) -> dict:
    """Retorna o conteúdo de um index.md específico com seus links resolvidos."""
    id = id.strip().rstrip("/")
    if not id.endswith("index"):
        id = f"{id}/index" if id else "index"

    for d in _all():
        if d["id"] == id:
            links = re.findall(r"\]\(([^)]+\.md)\)", d["body"])
            children = []
            for lnk in links:
                child_id = lnk.replace(".md", "").lstrip("/")
                child_doc = next((doc for doc in _all() if doc["id"] == child_id), None)
                if child_doc:
                    children.append(
                        {
                            "id": child_doc["id"],
                            "title": child_doc["title"],
                            "type": child_doc["type"],
                            "description": child_doc["description"],
                        }
                    )
                else:
                    children.append(
                        {"id": child_id, "title": child_id, "type": "?", "description": ""}
                    )
            log.info("get_index(%r) → %s (%d filhos)", id, d["title"], len(children))
            return {
                "id": d["id"],
                "title": d["title"],
                "type": d["type"],
                "description": d["description"],
                "children": children,
            }

    log.warning("get_index(%r) → não encontrado", id)
    return {"id": id, "title": "Índice não encontrado", "children": []}


# ---------------------------------------------------------------------------
# Busca semantica (embeddings)
# ---------------------------------------------------------------------------

_semantic_index = None


def _load_semantic_index():
    """Lazy-load do índice semântico."""
    global _semantic_index
    if _semantic_index is not None:
        return _semantic_index
    try:
        from embeddings import CHROMA_DIR, SemanticIndex

        chroma_path = Path(CHROMA_DIR)
        if chroma_path.exists():
            _semantic_index = SemanticIndex(kb_root=KB)
            if _semantic_index.count() > 0:
                log.info("Índice semântico carregado (%d docs)", _semantic_index.count())
                return _semantic_index
            _semantic_index = None
    except Exception as exc:
        log.warning("Não foi possível carregar índice semântico: %s", exc)
        _semantic_index = None
    return None


def _semantic_search_impl(query: str, limit: int = 5) -> list[dict]:
    """Busca semântica com fallback para keyword search."""
    raw = query.strip()
    if not raw:
        return [
            {
                "id": "",
                "type": "",
                "title": "Query vazia",
                "description": "Forneça pelo menos um termo de busca.",
            }
        ]

    if len(raw) > MAX_QUERY_LENGTH:
        return [
            {
                "id": "",
                "type": "",
                "title": "Query muito longa",
                "description": f"Limite de {MAX_QUERY_LENGTH} caracteres.",
            }
        ]

    limit = min(limit, MAX_RESULTS)

    idx = _load_semantic_index()
    if idx is None:
        log.info("semantic_search(%r) → fallback para keyword", raw)
        return _search_impl(raw, limit)

    hits = idx.query(raw, n_results=limit)

    from embeddings import SCORE_THRESHOLD

    if not hits or hits[0].get("score", 0) < SCORE_THRESHOLD:
        keyword_results = _search_impl(raw, limit)
        seen_ids = {h["id"] for h in hits}
        for kr in keyword_results:
            if kr["id"] not in seen_ids and kr.get("title") not in (
                "Nada encontrado",
                "Query vazia",
            ):
                hits.append(kr)
                seen_ids.add(kr["id"])
            if len(hits) >= limit:
                break

    log.info("semantic_search(%r) → %d resultados", raw, len(hits))
    return hits or [
        {
            "id": "",
            "type": "",
            "title": "Nada encontrado",
            "description": f"Sem resultado para '{raw}'.",
        }
    ]


# ---------------------------------------------------------------------------
# Modelos Pydantic — contrato search/fetch exigido pelo ChatGPT Deep Research
# ---------------------------------------------------------------------------
#
# Deep Research valida o "shape" da resposta de `search`/`fetch` e espera
# especificamente `{"results": [...]}` para search (chave no PLURAL) e um
# objeto Document "achatado" para fetch. FastMCP so gera esse envelope exato
# quando a tool retorna um modelo Pydantic com um campo `results`: uma tool
# anotada com `-> list[dict]` e automaticamente empacotada pelo FastMCP como
# `{"result": [...]}` (singular, ver fastmcp.tools.function_parsing.
# _WrappedResult) — confirmado empiricamente com fastmcp 3.4.2 — o que NAO
# bate com o contrato do Deep Research. Por isso os wrappers `search`/`fetch`
# abaixo retornam estes modelos tipados (que o FastMCP serializa via
# `.model_dump()` tanto em `structuredContent` quanto em `content`), enquanto
# `_search_impl`/`_fetch_impl` continuam retornando list[dict]/dict simples
# para não quebrar os consumidores/testes existentes que chamam essas
# funções puras diretamente.


class SearchResult(BaseModel):
    id: str
    type: str | None = None
    title: str
    description: str | None = None
    text: str | None = None
    url: str | None = None


class SearchResults(BaseModel):
    results: list[SearchResult]


class Document(BaseModel):
    id: str
    type: str | None = None
    title: str
    description: str | None = None
    resource: str | None = None
    tags: list | None = None
    timestamp: str | None = None
    body: str
    text: str
    url: str | None = None
    metadata: dict | None = None
    outgoing_links: list[str] = []


# ---------------------------------------------------------------------------
# Wrappers registrados como tools MCP
# ---------------------------------------------------------------------------


_READ_ONLY = ToolAnnotations(readOnlyHint=True, idempotentHint=True, openWorldHint=False)


@mcp.tool(title="Buscar por palavra-chave", annotations=_READ_ONLY)
@_log_tool_call(
    "search",
    metrics=lambda query, limit=8, offset=0: {
        "query_len": len(query),
        "limit": limit,
        "offset": offset,
    },
)
def search(query: str, limit: int = 8, offset: int = 0) -> SearchResults:
    """PRIMEIRA ESCOLHA quando você já sabe termos específicos que devem aparecer
    no texto (nomes técnicos, siglas, nomes de peças/métodos). Procura por
    palavra-chave em title, description, tags e corpo.
    Suporta multiplos termos (AND): 'motor eletrico' exige ambas as palavras.
    Tolerante a acentos ('trituracao' → 'trituração') e typos ('triturdora' → 'trituradora').
    Resultados ordenados por relevancia. Use offset para paginar.

    Retorna apenas id/título/snippet — NÃO o conteúdo completo. Depois de achar
    o id certo, chame 'fetch' para ler o documento inteiro antes de responder.
    Se não encontrar nada útil, ou se a pergunta for conceitual/parafraseada
    (não usa os termos exatos do KB), tente 'semantic_search' em seguida.

    Compatível com o contrato search/fetch do ChatGPT Deep Research: cada
    resultado inclui `text` (snippet) e `url` (kb://<id>), e a resposta vem
    envelopada como {"results": [...]}."""
    hits = _search_impl(query, limit, offset)
    return SearchResults(results=[SearchResult(**h) for h in hits])


@mcp.tool(title="Busca semântica (similaridade)", annotations=_READ_ONLY)
@_log_tool_call(
    "semantic_search",
    metrics=lambda query, limit=5: {
        "query_len": len(query),
        "limit": limit,
    },
)
def semantic_search(query: str, limit: int = 5) -> list[dict]:
    """SEGUNDA ESCOLHA: use quando 'search' (palavra-chave) não encontrar nada
    relevante, ou quando a pergunta é conceitual/parafraseada e pode não usar as
    mesmas palavras do texto original (ex: 'triturar plástico' encontra
    documentos sobre 'granulador de polímeros'). Busca por similaridade vetorial
    (embeddings) — mais tolerante a diferenças de vocabulário, porém mais lenta
    e menos previsível que 'search' para termos técnicos exatos que você já
    conhece. Retorna resultados ordenados por score de similaridade (0-1) e faz
    fallback automático para busca por keyword se o índice semântico não estiver
    disponível.

    Retorna apenas id/título/resumo — NÃO o conteúdo completo. Depois de achar
    o id certo, chame 'fetch' para ler o documento inteiro antes de responder."""
    return _semantic_search_impl(query, limit)


@mcp.tool(title="Ler conceito completo", annotations=_READ_ONLY)
@_log_tool_call("fetch", metrics=lambda id: {"id_len": len(id)})
def fetch(id: str) -> Document:
    """Retorna o conceito COMPLETO pelo id (obtido via search/semantic_search/
    list_topics/get_index). Chame esta tool sempre antes de responder com
    conteúdo do KB — as outras tools retornam só id/título/snippet, nunca o
    texto integral. A resposta inclui outgoing_links (ids dos conceitos
    referenciados no corpo) para continuar navegando o grafo de conhecimento.

    Compatível com o contrato search/fetch do ChatGPT Deep Research: o campo
    `text` traz o conteúdo completo (igual a `body`), `url` usa o esquema
    kb://<id>, e `metadata` agrupa type/tags/timestamp/resource."""
    return Document(**_fetch_impl(id))


@mcp.tool(title="Árvore de navegação completa", annotations=_READ_ONLY)
@_log_tool_call("list_topics")
def list_topics() -> list[dict]:
    """Retorna a árvore de navegação COMPLETA do bundle: todos os índices
    (index.md de cada pasta) com a lista de ids dos filhos. Bom ponto de
    partida quando o usuário não especificou um conceito exato e é preciso
    entender a estrutura geral do KB antes de buscar. Para ver detalhes
    (título/tipo/descrição) dos filhos de UM índice específico em vez de só
    os ids, use 'get_index' — mais barato que dar fetch em cada filho."""
    return _list_topics_impl()


@mcp.tool(title="Histórico de mudanças", annotations=_READ_ONLY)
@_log_tool_call("get_log", metrics=lambda last_n=20: {"last_n": last_n})
def get_log(last_n: int = 20) -> dict:
    """Retorna as últimas N entradas do histórico de mudanças do bundle
    (log.md). Use quando a pergunta for sobre o que mudou recentemente, sobre
    decisões/eventos registrados ao longo do tempo, ou para checar se há
    atualizações desde a última consulta. Não é uma tool de busca de
    conteúdo — para isso use 'search' ou 'semantic_search'."""
    return _get_log_impl(last_n)


@mcp.tool(title="Estatísticas do bundle", annotations=_READ_ONLY)
@_log_tool_call("get_stats")
def get_stats() -> dict:
    """Retorna estatísticas agregadas do bundle: total de conceitos, contagem
    por tipo, pastas existentes e timestamp da última atualização. Use para
    uma visão geral rápida do tamanho/composição do KB (ex: "quantos
    documentos existem", "que tipos de conteúdo tem") — não retorna
    conteúdo, só números."""
    return _get_stats_impl()


@mcp.tool(title="Detalhe de um índice", annotations=_READ_ONLY)
@_log_tool_call("get_index", metrics=lambda id="index": {"id_len": len(id)})
def get_index(id: str = "index") -> dict:
    """Retorna o conteúdo de UM índice (index.md) específico com os filhos já
    resolvidos (id, title, type e description de cada um) — mais informativo
    que 'list_topics' para navegar uma seção, porém cobre só aquele índice
    (não a árvore inteira). Atalho para navegação sem precisar fazer fetch
    genérico em cada filho. Aceita id com ou sem '/index' (ex: 'metodos' ou
    'metodos/index'); sem argumento retorna o índice raiz."""
    return _get_index_impl(id)


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------


@mcp.custom_route("/health", ["GET"])
async def health_check(request):
    doc_count = len(_all())
    return JSONResponse({"status": "ok", "documents": doc_count})


# ---------------------------------------------------------------------------
# Autenticação — API key estática via header (opcional, ver Fase 4.3 TODO.md)
# ---------------------------------------------------------------------------


def _load_valid_api_keys() -> set[str]:
    """Lê MCP_API_KEYS (lista separada por virgula). Vazio/ausente = auth desligada."""
    raw = os.environ.get("MCP_API_KEYS", "")
    return {key.strip() for key in raw.split(",") if key.strip()}


class ApiKeyMiddleware(BaseHTTPMiddleware):
    """Exige X-API-Key ou Authorization: Bearer <key> em todas as rotas, exceto /health."""

    def __init__(self, app, valid_keys: set[str]):
        super().__init__(app)
        self.valid_keys = valid_keys

    async def dispatch(self, request, call_next):
        if request.url.path == "/health":
            return await call_next(request)

        api_key = request.headers.get("x-api-key")
        if not api_key:
            auth_header = request.headers.get("authorization", "")
            if auth_header.lower().startswith("bearer "):
                api_key = auth_header[len("bearer ") :].strip()

        if api_key not in self.valid_keys:
            return JSONResponse({"error": "unauthorized"}, status_code=401)

        return await call_next(request)


def _build_middleware() -> list[Middleware]:
    """Monta a lista de middleware ASGI. Auth só entra se MCP_API_KEYS estiver definida."""
    valid_keys = _load_valid_api_keys()
    if not valid_keys:
        log.info("MCP_API_KEYS não definida — autenticação desligada")
        return []
    log.info("Autenticação por API key ativada (%d chave(s))", len(valid_keys))
    return [Middleware(ApiKeyMiddleware, valid_keys=valid_keys)]


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host=HOST,
        port=PORT,
        middleware=_build_middleware(),
    )
