import logging
import os
import re
import time
import unicodedata
from collections import defaultdict
from pathlib import Path

import frontmatter
from fastmcp import FastMCP
from rapidfuzz import fuzz

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("projeto-kb")

KB = Path(os.environ.get("KB_PATH", Path(__file__).parent / "kb"))
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "8000"))
MAX_RESULTS = int(os.environ.get("MAX_RESULTS", "50"))
MAX_QUERY_LENGTH = int(os.environ.get("MAX_QUERY_LENGTH", "500"))

mcp = FastMCP(
    name="projeto-kb",
    instructions=(
        "Base de conhecimento compartilhada em formato OKF (markdown + frontmatter). "
        "Use 'search' para localizar conceitos e 'fetch' para ler um conceito pelo id "
        "(caminho relativo sem .md). Use 'list_topics' para ver a arvore de navegacao, "
        "'get_log' para o historico de mudancas, e 'get_stats' para estatisticas do bundle. "
        "Use 'get_index' para ver o conteudo de um indice especifico. "
        "Comece pelos index e siga os outgoing_links."
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
        return [{"id": "", "type": "", "title": "Query muito longa",
                 "description": f"Limite de {MAX_QUERY_LENGTH} caracteres. Reduza a consulta."}]

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
            log.info("fetch(%r) → %s", id, result["title"])
            return result
    log.warning("fetch(%r) → não encontrado", id)
    return {
        "id": id,
        "title": "Nao encontrado",
        "body": f"Sem conceito '{id}'.",
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
                    children.append({
                        "id": child_doc["id"],
                        "title": child_doc["title"],
                        "type": child_doc["type"],
                        "description": child_doc["description"],
                    })
                else:
                    children.append({"id": child_id, "title": child_id, "type": "?", "description": ""})
            log.info("get_index(%r) → %s (%d filhos)", id, d["title"], len(children))
            return {
                "id": d["id"],
                "title": d["title"],
                "type": d["type"],
                "description": d["description"],
                "children": children,
            }

    log.warning("get_index(%r) → não encontrado", id)
    return {"id": id, "title": "Índice não encontrado",
            "children": []}


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
        return [{"id": "", "type": "", "title": "Query vazia",
                 "description": "Forneça pelo menos um termo de busca."}]

    if len(raw) > MAX_QUERY_LENGTH:
        return [{"id": "", "type": "", "title": "Query muito longa",
                 "description": f"Limite de {MAX_QUERY_LENGTH} caracteres."}]

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
            if kr["id"] not in seen_ids and kr.get("title") not in ("Nada encontrado", "Query vazia"):
                hits.append(kr)
                seen_ids.add(kr["id"])
            if len(hits) >= limit:
                break

    log.info("semantic_search(%r) → %d resultados", raw, len(hits))
    return hits or [{"id": "", "type": "", "title": "Nada encontrado",
                     "description": f"Sem resultado para '{raw}'."}]


# ---------------------------------------------------------------------------
# Wrappers registrados como tools MCP
# ---------------------------------------------------------------------------


@mcp.tool
def search(query: str, limit: int = 8, offset: int = 0) -> list[dict]:
    """Procura conceitos por palavra-chave em title, description, tags e corpo.
    Suporta multiplos termos (AND): 'motor eletrico' exige ambas as palavras.
    Tolerante a acentos ('trituracao' → 'trituração') e typos ('triturdora' → 'trituradora').
    Resultados ordenados por relevancia. Use offset para paginar."""
    return _search_impl(query, limit, offset)


@mcp.tool
def semantic_search(query: str, limit: int = 5) -> list[dict]:
    """Busca semântica por similaridade vetorial. Encontra conceitos relevantes
    mesmo quando os termos exatos não aparecem no texto (ex: 'triturar plástico'
    encontra documentos sobre 'granulador de polímeros'). Retorna resultados
    ordenados por score de similaridade (0-1). Faz fallback automático para
    busca por keyword se o índice semântico não estiver disponível."""
    return _semantic_search_impl(query, limit)


@mcp.tool
def fetch(id: str) -> dict:
    """Retorna o conceito completo pelo id, com outgoing_links (ids dos conceitos
    referenciados no corpo) para a IA continuar navegando o grafo."""
    return _fetch_impl(id)


@mcp.tool
def list_topics() -> list[dict]:
    """Retorna a arvore de navegacao do bundle: cada indice com seus filhos.
    Bom ponto de partida para explorar a base de conhecimento."""
    return _list_topics_impl()


@mcp.tool
def get_log(last_n: int = 20) -> dict:
    """Retorna as ultimas N entradas do historico de mudancas do bundle."""
    return _get_log_impl(last_n)


@mcp.tool
def get_stats() -> dict:
    """Retorna estatisticas do bundle: total de conceitos, contagem por tipo,
    pastas existentes e timestamp da ultima atualizacao."""
    return _get_stats_impl()


@mcp.tool
def get_index(id: str = "index") -> dict:
    """Retorna o conteudo de um indice (index.md) especifico com seus filhos resolvidos.
    Cada filho inclui id, title, type e description. Atalho para navegacao sem precisar
    fazer fetch generico. Aceita id com ou sem '/index' (ex: 'metodos' ou 'metodos/index')."""
    return _get_index_impl(id)


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@mcp.custom_route("/health", ["GET"])
async def health_check(request):
    from starlette.responses import JSONResponse
    doc_count = len(_all())
    return JSONResponse({"status": "ok", "documents": doc_count})


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host=HOST, port=PORT)
