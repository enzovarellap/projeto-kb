"""Testes para ingest.py — conversão de arquivos locais em conceitos OKF."""
import sys
from pathlib import Path

import frontmatter
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def kb_bundle(tmp_path):
    """Cria um bundle OKF mínimo com log.md."""
    kb = tmp_path / "kb"
    kb.mkdir()
    out = kb / "importados"
    out.mkdir()

    log_post = frontmatter.Post(
        "# Log\n\n- **2026-06-17** — Bundle inicial.",
        type="Log",
        title="Histórico",
        description="Log do bundle.",
        resource="",
        tags=["log"],
        timestamp="2026-06-17T12:00:00Z",
    )
    (kb / "log.md").write_text(frontmatter.dumps(log_post), encoding="utf-8")
    return kb, out


@pytest.fixture
def src_dir(tmp_path):
    """Cria pasta de origem com arquivos de teste."""
    src = tmp_path / "sources"
    src.mkdir()
    return src


class TestSlug:
    def test_basic_slug(self):
        from ingest import _slug
        assert _slug("Relatório Final.pdf") == "relatório-final"

    def test_slug_removes_special_chars(self):
        from ingest import _slug
        assert _slug("hello@world!.txt") == "helloworld"

    def test_slug_dotfile_produces_stem(self):
        from ingest import _slug
        assert _slug(".hidden") == "hidden"

    def test_slug_underscores(self):
        from ingest import _slug
        assert _slug("meu_arquivo_teste.md") == "meu-arquivo-teste"


class TestExtractTitle:
    def test_extracts_h1(self):
        from ingest import _extract_title
        assert _extract_title("# Meu Título\n\nCorpo.", "fallback") == "Meu Título"

    def test_fallback_when_no_h1(self):
        from ingest import _extract_title
        assert _extract_title("Sem heading.\n\nTexto.", "Fallback") == "Fallback"

    def test_ignores_h2(self):
        from ingest import _extract_title
        assert _extract_title("## Sub-heading\n\nTexto.", "Fallback") == "Fallback"


class TestConvert:
    def test_md_passthrough(self, src_dir):
        from ingest import _convert
        md_file = src_dir / "teste.md"
        md_file.write_text("# Título\n\nConteúdo.", encoding="utf-8")
        result = _convert(md_file)
        assert "Título" in result
        assert "Conteúdo" in result

    def test_txt_passthrough(self, src_dir):
        from ingest import _convert
        txt_file = src_dir / "teste.txt"
        txt_file.write_text("Texto simples aqui.", encoding="utf-8")
        result = _convert(txt_file)
        assert "Texto simples" in result


class TestIngest:
    def test_ingests_md_file(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "conceito-a.md").write_text(
            "# Conceito A\n\nDescrição do conceito A.", encoding="utf-8"
        )

        result = ingest(src_dir, out)
        assert len(result) == 1
        assert result[0].exists()

        post = frontmatter.load(result[0])
        assert post["title"] == "Conceito A"
        assert post["type"] == "Conceito"

    def test_ingests_txt_file(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "nota.txt").write_text(
            "Texto de uma nota simples.", encoding="utf-8"
        )

        result = ingest(src_dir, out)
        assert len(result) == 1

    def test_custom_type(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "metodo.md").write_text("# Método\n\nDetalhe.", encoding="utf-8")

        result = ingest(src_dir, out, tipo="Método")
        post = frontmatter.load(result[0])
        assert post["type"] == "Método"

    def test_idempotent_update(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "doc.md").write_text("# Doc\n\nVersão 1.", encoding="utf-8")
        ingest(src_dir, out)

        (src_dir / "doc.md").write_text("# Doc\n\nVersão 2.", encoding="utf-8")
        result = ingest(src_dir, out)

        post = frontmatter.load(result[0])
        assert "Versão 2" in post.content

    def test_creates_index(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "a.md").write_text("# A\n\nTexto A.", encoding="utf-8")
        ingest(src_dir, out)

        index = out / "index.md"
        assert index.exists()
        post = frontmatter.load(index)
        assert post["type"] == "Índice"

    def test_empty_source_returns_empty(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle
        result = ingest(src_dir, out)
        assert result == []

    def test_ignores_unsupported_format(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "imagem.png").write_bytes(b"\x89PNG\r\n")
        result = ingest(src_dir, out)
        assert result == []

    def test_updates_log(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "novo.md").write_text("# Novo\n\nConteúdo.", encoding="utf-8")
        ingest(src_dir, out)

        log_content = (kb / "log.md").read_text()
        assert "novo" in log_content.lower()

    def test_multiple_files(self, kb_bundle, src_dir):
        from ingest import ingest
        kb, out = kb_bundle

        (src_dir / "a.md").write_text("# A\n\nTexto A.", encoding="utf-8")
        (src_dir / "b.md").write_text("# B\n\nTexto B.", encoding="utf-8")
        (src_dir / "c.txt").write_text("Texto C.", encoding="utf-8")

        result = ingest(src_dir, out)
        assert len(result) == 3
