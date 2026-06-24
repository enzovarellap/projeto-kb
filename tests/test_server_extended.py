"""Testes estendidos para server.py — edge cases, limites, get_index, semantic_search."""
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(autouse=True)
def kb_de_teste(tmp_path: Path, monkeypatch):
    """Bundle de teste para os testes estendidos."""
    import server as srv

    (tmp_path / "conceitos").mkdir()
    (tmp_path / "metodos").mkdir()

    (tmp_path / "index.md").write_text(
        textwrap.dedent("""\
        ---
        type: Indice
        title: KB Raiz
        description: Indice raiz do bundle.
        resource: ""
        tags: [indice]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # KB Raiz
        - [Conceitos](conceitos/index.md)
        - [Métodos](metodos/index.md)
        """),
        encoding="utf-8",
    )

    (tmp_path / "conceitos" / "index.md").write_text(
        textwrap.dedent("""\
        ---
        type: Indice
        title: Conceitos
        description: Indice de conceitos.
        resource: ""
        tags: [indice]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Conceitos
        - [Alpha](conceitos/alpha.md)
        - [Beta](conceitos/beta.md)
        """),
        encoding="utf-8",
    )

    (tmp_path / "conceitos" / "alpha.md").write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Alpha
        description: Primeiro conceito.
        resource: ""
        tags: [escopo, alpha]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Alpha
        Conceito alpha com link para [Beta](conceitos/beta.md).
        Motor elétrico de trituração.
        """),
        encoding="utf-8",
    )

    (tmp_path / "conceitos" / "beta.md").write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Beta
        description: Segundo conceito.
        resource: ""
        tags: [contexto, beta]
        timestamp: 2026-06-18T10:00:00Z
        ---
        # Beta
        Conceito beta.
        """),
        encoding="utf-8",
    )

    (tmp_path / "metodos" / "index.md").write_text(
        textwrap.dedent("""\
        ---
        type: Indice
        title: Métodos de Trituração
        description: Comparativo de métodos.
        resource: ""
        tags: [indice, metodos]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Métodos
        - [Duplo Rotor](metodos/duplo-rotor.md)
        """),
        encoding="utf-8",
    )

    (tmp_path / "metodos" / "duplo-rotor.md").write_text(
        textwrap.dedent("""\
        ---
        type: Método
        title: Duplo Rotor
        description: Trituração por duplo rotor.
        resource: ""
        tags: [metodo, rotor]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Duplo Rotor
        Método de trituração com dois rotores.
        """),
        encoding="utf-8",
    )

    (tmp_path / "log.md").write_text(
        textwrap.dedent("""\
        ---
        type: Log
        title: Histórico
        description: Log do bundle.
        resource: ""
        tags: [log]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Log

        - **2026-06-17** — Bundle criado.
        """),
        encoding="utf-8",
    )

    monkeypatch.setattr(srv, "KB", tmp_path)
    srv.invalidate_cache()
    yield tmp_path


# ---------------------------------------------------------------------------
# get_index — nova tool
# ---------------------------------------------------------------------------

class TestGetIndex:
    def test_root_index(self):
        import server as srv
        result = srv._get_index_impl("index")
        assert result["title"] == "KB Raiz"
        assert len(result["children"]) == 2

    def test_index_by_folder_name(self):
        import server as srv
        result = srv._get_index_impl("conceitos")
        assert result["title"] == "Conceitos"
        assert len(result["children"]) == 2

    def test_index_with_slash_suffix(self):
        import server as srv
        result = srv._get_index_impl("metodos/")
        assert result["title"] == "Métodos de Trituração"

    def test_index_full_path(self):
        import server as srv
        result = srv._get_index_impl("metodos/index")
        assert result["title"] == "Métodos de Trituração"

    def test_children_have_metadata(self):
        import server as srv
        result = srv._get_index_impl("conceitos")
        child = next(c for c in result["children"] if c["id"] == "conceitos/alpha")
        assert child["title"] == "Alpha"
        assert child["type"] == "Conceito"

    def test_nonexistent_index(self):
        import server as srv
        result = srv._get_index_impl("nao-existe")
        assert "não encontrado" in result["title"].lower() or result["children"] == []

    def test_empty_string_returns_root(self):
        import server as srv
        result = srv._get_index_impl("")
        assert result["title"] == "KB Raiz"


# ---------------------------------------------------------------------------
# Timeout e limites
# ---------------------------------------------------------------------------

class TestQueryLimits:
    def test_very_long_query_rejected(self):
        import server as srv
        long_query = "a " * 300
        result = srv._search_impl(long_query)
        assert result[0]["title"] == "Query muito longa"

    def test_limit_capped_at_max(self):
        import server as srv
        result = srv._search_impl("conceito", limit=1000)
        assert len(result) <= srv.MAX_RESULTS

    def test_semantic_search_long_query_rejected(self):
        import server as srv
        long_query = "a " * 300
        result = srv._semantic_search_impl(long_query)
        assert result[0]["title"] == "Query muito longa"

    def test_semantic_search_empty_query(self):
        import server as srv
        result = srv._semantic_search_impl("")
        assert result[0]["title"] == "Query vazia"

    def test_semantic_search_spaces_query(self):
        import server as srv
        result = srv._semantic_search_impl("   ")
        assert result[0]["title"] == "Query vazia"


# ---------------------------------------------------------------------------
# Caracteres especiais
# ---------------------------------------------------------------------------

class TestSpecialCharacters:
    def test_search_with_regex_chars(self):
        import server as srv
        result = srv._search_impl("motor.*eletrico")
        assert isinstance(result, list)

    def test_search_with_brackets(self):
        import server as srv
        result = srv._search_impl("[alpha]")
        assert isinstance(result, list)

    def test_search_with_parentheses(self):
        import server as srv
        result = srv._search_impl("(conceito)")
        assert isinstance(result, list)

    def test_search_with_unicode(self):
        import server as srv
        result = srv._search_impl("café résumé naïve")
        assert isinstance(result, list)

    def test_fetch_with_special_chars(self):
        import server as srv
        result = srv._fetch_impl("conceitos/<script>")
        assert "Nao encontrado" in result["title"]


# ---------------------------------------------------------------------------
# Semantic search fallback
# ---------------------------------------------------------------------------

class TestSemanticSearchFallback:
    def test_fallback_when_no_index(self, monkeypatch):
        import server as srv
        monkeypatch.setattr(srv, "_load_semantic_index", lambda: None)
        result = srv._semantic_search_impl("alpha")
        assert len(result) > 0
        assert any(r.get("id") == "conceitos/alpha" for r in result)

    def test_semantic_search_returns_list(self, monkeypatch):
        import server as srv
        monkeypatch.setattr(srv, "_load_semantic_index", lambda: None)
        result = srv._semantic_search_impl("motor")
        assert isinstance(result, list)


# ---------------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------------

class TestEnvVars:
    def test_defaults_loaded(self):
        import server as srv
        assert srv.MAX_RESULTS == 50
        assert srv.MAX_QUERY_LENGTH == 500
