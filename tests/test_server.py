"""Testes para as tools search e fetch do server.py."""
import textwrap
from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(autouse=True)
def kb_de_teste(tmp_path: Path, monkeypatch):
    """Substitui KB do server por um bundle de teste em tmp_path."""
    (tmp_path / "conceitos").mkdir()

    (tmp_path / "conceitos" / "alpha.md").write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Alpha
        description: Primeiro conceito de escopo.
        resource: ""
        tags: [escopo, alpha]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Alpha
        Conceito alpha com link para [Beta](conceitos/beta.md).
        """),
        encoding="utf-8",
    )
    (tmp_path / "conceitos" / "beta.md").write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Beta
        description: Segundo conceito de contexto.
        resource: ""
        tags: [contexto, beta]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Beta
        Conceito beta sem links externos.
        """),
        encoding="utf-8",
    )

    import server as srv
    monkeypatch.setattr(srv, "KB", tmp_path)
    yield tmp_path


def test_search_hit():
    import server as srv
    resultados = srv._search_impl("escopo")
    ids = [r["id"] for r in resultados]
    assert "conceitos/alpha" in ids


def test_search_miss():
    import server as srv
    resultados = srv._search_impl("xyzzy-inexistente")
    assert resultados[0]["title"] == "Nada encontrado"


def test_fetch_existente():
    import server as srv
    conceito = srv._fetch_impl("conceitos/alpha")
    assert conceito["title"] == "Alpha"
    assert "body" in conceito
    assert isinstance(conceito["outgoing_links"], list)


def test_fetch_outgoing_links():
    import server as srv
    conceito = srv._fetch_impl("conceitos/alpha")
    # alpha linka para beta
    assert any("beta" in link for link in conceito["outgoing_links"])


def test_fetch_inexistente():
    import server as srv
    conceito = srv._fetch_impl("conceitos/nao-existe")
    assert "Nao encontrado" in conceito["title"]
    assert conceito["outgoing_links"] == []
