# server.py — MCP server de contexto sobre um bundle OKF (search + fetch)
# Navegacao-primeiro: sem embeddings. Le markdown + frontmatter direto do disco.
from pathlib import Path
import re
import frontmatter            # pip install python-frontmatter
from fastmcp import FastMCP   # pip install fastmcp

KB = Path(__file__).parent / "kb"   # raiz do bundle OKF

mcp = FastMCP(
    name="projeto-kb",
    instructions=(
        "Base de conhecimento compartilhada em formato OKF (markdown + frontmatter). "
        "Use 'search' para localizar conceitos e 'fetch' para ler um conceito pelo id "
        "(caminho relativo sem .md). Comece pelos index.md e siga os outgoing_links."
    ),
)

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


# Wrappers registrados como tools MCP (assinatura contratual: secao 5.2 do handoff).

@mcp.tool
def search(query: str, limit: int = 8) -> list[dict]:
    """Procura conceitos por palavra-chave em title, description, tags e corpo.
    Retorna {id, type, title, description}. Ids terminados em 'index' sao
    paginas-indice (bons pontos de entrada para navegar)."""
    return _search_impl(query, limit)

@mcp.tool
def fetch(id: str) -> dict:
    """Retorna o conceito completo pelo id, com outgoing_links (ids dos conceitos
    referenciados no corpo) para a IA continuar navegando o grafo."""
    return _fetch_impl(id)


if __name__ == "__main__":
    # streamable-http = transporte remoto esperado por Claude/ChatGPT.
    # Local: http://127.0.0.1:8000/mcp
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
