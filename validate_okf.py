"""Validador de conformidade OKF para o bundle em kb/."""
import sys
from pathlib import Path
import datetime
import re

try:
    import frontmatter
except ImportError:
    print("ERRO: instale python-frontmatter  →  pip install python-frontmatter")
    sys.exit(2)

KB = Path(__file__).parent / "kb"
ISO_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$"
)


def _is_iso8601(value) -> bool:
    # python-frontmatter pode retornar datetime diretamente
    if isinstance(value, (datetime.datetime, datetime.date)):
        return True
    return bool(ISO_RE.match(str(value).strip()))


def _resolve_link(source: Path, href: str, kb_root: Path) -> bool:
    """Verifica se um link aponta para um .md existente.

    Links que começam com '/' são raiz-relativos ao bundle (kb_root).
    Links sem '/' são relativos ao diretório do arquivo-fonte.
    """
    if href.startswith(("http://", "https://", "drive://", "mailto:")):
        return True
    if href.startswith("/"):
        # /pasta/arquivo.md → kb_root/pasta/arquivo.md
        target = (kb_root / href.lstrip("/")).resolve()
    else:
        target = (source.parent / href).resolve()
    return target.exists()


def validate(kb_root: Path = KB) -> list[str]:
    errors: list[str] = []

    md_files = sorted(kb_root.glob("**/*.md"))
    if not md_files:
        errors.append(f"ERRO: nenhum arquivo .md encontrado em '{kb_root}'.")
        return errors

    for path in md_files:
        rel = path.relative_to(kb_root.parent)
        prefix = f"[{rel}]"

        try:
            post = frontmatter.load(path)
        except Exception as exc:
            errors.append(f"{prefix} frontmatter não parseou: {exc}")
            continue

        # type é obrigatório
        if not post.get("type"):
            errors.append(f"{prefix} campo 'type' ausente ou vazio.")

        # timestamp deve ser ISO 8601 se presente
        ts = post.get("timestamp")
        if ts and not _is_iso8601(ts):
            errors.append(
                f"{prefix} 'timestamp' inválido (deve ser ISO 8601): '{ts}'."
            )

        # cross-links devem apontar para .md existentes
        links = re.findall(r"\]\(([^)]+\.md[^)]*)\)", post.content)
        for raw_link in links:
            href = raw_link.split("#")[0]  # ignora fragmentos
            if not _resolve_link(path, href, kb_root):
                errors.append(
                    f"{prefix} link quebrado: '{href}' não existe no disco."
                )

    return errors


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Valida conformidade OKF do bundle.")
    parser.add_argument(
        "--kb", default=str(KB), help="Caminho raiz do bundle OKF (padrão: ./kb)."
    )
    args = parser.parse_args()

    kb_root = Path(args.kb)
    if not kb_root.is_dir():
        print(f"ERRO: '{kb_root}' não é um diretório válido.")
        sys.exit(2)

    errors = validate(kb_root)

    if errors:
        print(f"Validação FALHOU — {len(errors)} problema(s):\n")
        for e in errors:
            print(f"  • {e}")
        sys.exit(1)
    else:
        md_count = len(list(kb_root.glob("**/*.md")))
        print(f"Validação OK — {md_count} arquivo(s) .md sem erros.")
        sys.exit(0)


if __name__ == "__main__":
    main()
