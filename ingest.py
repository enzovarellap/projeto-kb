"""Ingestão local: converte arquivos externos em conceitos OKF.

Uso:
    python ingest.py --src <pasta> --out kb/<subpasta> [--type <Tipo>]

Formatos suportados: .pdf, .docx, .md, .txt, .pptx, .csv
Requer: markitdown, python-frontmatter
"""
import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import frontmatter
except ImportError:
    print("ERRO: instale python-frontmatter  →  pip install python-frontmatter")
    sys.exit(2)

try:
    from markitdown import MarkItDown
except ImportError:
    print("ERRO: instale markitdown  →  pip install markitdown")
    sys.exit(2)

SUPPORTED = {".pdf", ".docx", ".md", ".txt", ".pptx", ".csv"}

_mid = MarkItDown()


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug(name: str) -> str:
    """Converte nome de arquivo em slug OKF (id do conceito)."""
    stem = Path(name).stem
    slug = stem.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug or "sem-titulo"


def _extract_title(body: str, fallback: str) -> str:
    """Tenta extrair o primeiro heading H1 do markdown."""
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _convert(src_path: Path) -> str:
    """Converte arquivo para markdown usando markitdown."""
    if src_path.suffix.lower() == ".md":
        return src_path.read_text(encoding="utf-8", errors="replace")
    result = _mid.convert(str(src_path))
    return result.text_content or ""


def _update_log(kb_root: Path, message: str) -> None:
    log_path = kb_root / "log.md"
    if not log_path.exists():
        return
    post = frontmatter.load(log_path)
    today = _now_iso()[:10]
    entry = f"\n## {today}\n\n- {message}\n"
    # Evita duplicar a mesma entrada no mesmo dia
    if message not in post.content:
        post.content = post.content.rstrip() + entry
        log_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def _update_index(out_dir: Path, concepts: list[dict]) -> None:
    """Cria ou atualiza o index.md da subpasta de saída."""
    index_path = out_dir / "index.md"
    subfolder = out_dir.name

    links = "\n".join(
        f"- [{c['title']}]({Path(c['path']).name}) — {c['description']}"
        for c in concepts
    )
    body = f"# Índice — {subfolder}\n\nConceitos importados por `ingest.py`.\n\n{links}\n"

    meta = {
        "type": "Índice",
        "title": f"Índice — {subfolder}",
        "description": f"Índice gerado automaticamente para a subpasta '{subfolder}'.",
        "resource": "",
        "tags": ["índice", subfolder],
        "timestamp": _now_iso(),
    }
    post = frontmatter.Post(body, **meta)
    index_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def ingest(src: Path, out: Path, tipo: str = "Conceito") -> list[Path]:
    """Processa todos os arquivos suportados de src e gera conceitos OKF em out.

    Idempotente: re-processar os mesmos arquivos atualiza o conceito existente.
    Retorna lista de caminhos gerados.
    """
    out.mkdir(parents=True, exist_ok=True)
    kb_root = out.parent
    while not (kb_root / "log.md").exists() and kb_root != kb_root.parent:
        kb_root = kb_root.parent

    generated: list[dict] = []
    now = _now_iso()

    files = [f for f in sorted(src.iterdir()) if f.is_file() and f.suffix.lower() in SUPPORTED]
    if not files:
        print(f"Nenhum arquivo suportado encontrado em '{src}'.")
        return []

    for src_file in files:
        slug = _slug(src_file.name)
        dest = out / f"{slug}.md"

        try:
            body = _convert(src_file)
        except Exception as exc:
            print(f"  AVISO: não foi possível converter '{src_file.name}': {exc}")
            continue

        title = _extract_title(body, src_file.stem.replace("-", " ").replace("_", " ").title())
        description = f"Importado de '{src_file.name}'."

        if dest.exists():
            # Atualiza conteúdo mantendo metadados originais onde possível
            existing = frontmatter.load(dest)
            existing.content = body
            existing["timestamp"] = now
            existing["resource"] = str(src_file.resolve())
            dest.write_text(frontmatter.dumps(existing), encoding="utf-8")
            action = "atualizado"
        else:
            meta = {
                "type": tipo,
                "title": title,
                "description": description,
                "resource": str(src_file.resolve()),
                "tags": [],
                "timestamp": now,
            }
            post = frontmatter.Post(body, **meta)
            dest.write_text(frontmatter.dumps(post), encoding="utf-8")
            action = "criado"

        print(f"  {action}: {dest.relative_to(Path.cwd()) if dest.is_relative_to(Path.cwd()) else dest}")
        generated.append({"path": str(dest), "title": title, "description": description})
        _update_log(kb_root, f"{action} conceito `{slug}` a partir de `{src_file.name}`.")

    _update_index(out, generated)
    print(f"\nTotal: {len(generated)} conceito(s) em '{out}'.")
    return [Path(c["path"]) for c in generated]


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingere arquivos locais no bundle OKF.")
    parser.add_argument("--src", required=True, help="Pasta com arquivos a ingerir.")
    parser.add_argument("--out", required=True, help="Subpasta de saída dentro do bundle (ex.: kb/importados).")
    parser.add_argument("--type", default="Conceito", dest="tipo", help="Tipo OKF dos conceitos gerados (padrão: Conceito).")
    args = parser.parse_args()

    src = Path(args.src)
    out = Path(args.out)

    if not src.is_dir():
        print(f"ERRO: '{src}' não é um diretório válido.")
        sys.exit(1)

    ingest(src, out, args.tipo)


if __name__ == "__main__":
    main()
