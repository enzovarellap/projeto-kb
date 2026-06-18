# server.py — MCP server de contexto sobre um bundle OKF
from pathlib import Path
import logging
import re
import frontmatter
from fastmcp import FastMCP

KB = Path(__file__).parent / "kb"

log = logging.getLogger("projeto-kb")

mcp = FastMCP(
    name="projeto-kb",
    instructions=(
        "Base de conhecimento compartilhada em formato OKF (markdown + frontmatter). "
        "Use 'search' para busca por palavra-chave, 'semantic_search' para busca por "
        "similaridade semântica, e 'fetch' para ler um conceito pelo id "
        "(caminho relativo sem .md). Comece pelos index.md e siga os outgoing_links."
    ),
)

_semantic_index = None


def _get_semantic_index():
    """Lazy-load do índice semântico (carrega apenas na primeira chamada)."""
    global _semantic_index
    if _semantic_index is None:
        try:
            from embeddings import SemanticIndex, CHROMA_DIR
            chroma_path = CHROMA_DIR
            if chroma_path.exists():
                _semantic_index = SemanticIndex(kb_root=KB)
                if _semantic_index.count() == 0:
                    _semantic_index = None
                    log.warning("Índice semântico vazio — use 'make index' para indexar.")
            else:
                log.info("Índice semântico não encontrado — semantic_search indisponível.")
        except ImportError:
            log.info("chromadb/sentence-transformers não instalados — semantic_search indisponível.")
    return _semantic_index

def _id(path: Path) -> str:
    return str(path.relative_to(KB)).replace("\\", "/").replace(".md", "")

def _load(path: Path) -> dict:
    post = frontmatter.load(path)
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
    # Rele a cada chamada -> reflete edicoes na hora ("sempre atualizado").
    return [_load(p) for p in sorted(KB.glob("**/*.md"))]


# Implementacoes puras (sem decorador) — utilizadas diretamente nos testes.

def _search_impl(query: str, limit: int = 8) -> list[dict]:
    """Procura conceitos por palavra-chave em title, description, tags e corpo."""
    q = query.lower().strip()
    hits = []
    for d in _all():
        hay = f"{d['title']} {d['description']} {' '.join(map(str, d['tags']))} {d['body']}".lower()
        if q in hay:
            hits.append({
                "id": d["id"], "type": d["type"],
                "title": d["title"], "description": d["description"],
            })
    return hits[:limit] or [{"id": "", "type": "", "title": "Nada encontrado",
                             "description": f"Sem resultado para '{query}'."}]


def _fetch_impl(id: str) -> dict:
    """Retorna o conceito completo pelo id, com outgoing_links resolvidos."""
    for d in _all():
        if d["id"] == id:
            links = re.findall(r"\]\(([^)]+\.md)\)", d["body"])
            d["outgoing_links"] = [l.replace(".md", "").lstrip("/") for l in links]
            return d
    return {"id": id, "title": "Nao encontrado",
            "body": f"Sem conceito '{id}'.", "outgoing_links": []}


def _semantic_search_impl(query: str, limit: int = 5) -> list[dict]:
    """Busca semântica com fallback para keyword search."""
    from embeddings import SCORE_THRESHOLD

    idx = _get_semantic_index()
    if idx is None:
        return _search_impl(query, limit)

    hits = idx.query(query, n_results=limit)

    if not hits or hits[0]["score"] < SCORE_THRESHOLD:
        keyword_hits = _search_impl(query, limit)
        seen = {h["id"] for h in hits}
        for kh in keyword_hits:
            if kh["id"] not in seen and kh["id"]:
                hits.append({**kh, "score": 0.0})
                seen.add(kh["id"])

    result = hits[:limit]
    return result or [
        {
            "id": "",
            "type": "",
            "title": "Nada encontrado",
            "description": f"Sem resultado para '{query}'.",
            "score": 0.0,
        }
    ]


# Wrappers registrados como tools MCP.

@mcp.tool
def search(query: str, limit: int = 8) -> list[dict]:
    """Procura conceitos por palavra-chave em title, description, tags e corpo.
    Retorna {id, type, title, description}. Ids terminados em 'index' sao
    paginas-indice (bons pontos de entrada para navegar)."""
    return _search_impl(query, limit)

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


if __name__ == "__main__":
    # streamable-http = transporte remoto esperado por Claude/ChatGPT.
    # Local: http://127.0.0.1:8000/mcp
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
