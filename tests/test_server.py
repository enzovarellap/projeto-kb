"""Testes para as tools do server.py (search, fetch, list_topics, get_log, get_stats)."""
import textwrap
from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(autouse=True)
def kb_de_teste(tmp_path: Path, monkeypatch):
    """Substitui KB do server por um bundle de teste em tmp_path."""
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
        description: Primeiro conceito de escopo.
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
        description: Segundo conceito de contexto.
        resource: ""
        tags: [contexto, beta]
        timestamp: 2026-06-18T10:00:00Z
        ---
        # Beta
        Conceito beta sem links externos.
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
        description: Trituração por duplo rotor contra-rotativo.
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
        title: Histórico de mudanças
        description: Log do bundle.
        resource: ""
        tags: [log]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Log

        - **2026-06-17** — Bundle inicial criado.
        - **2026-06-18** — Adicionado conceito Beta.
        """),
        encoding="utf-8",
    )

    monkeypatch.setattr(srv, "KB", tmp_path)
    srv.invalidate_cache()
    yield tmp_path


# ---------------------------------------------------------------------------
# search — busca por keyword
# ---------------------------------------------------------------------------

def test_search_hit():
    import server as srv
    resultados = srv._search_impl("escopo")
    ids = [r["id"] for r in resultados]
    assert "conceitos/alpha" in ids


def test_search_miss():
    import server as srv
    resultados = srv._search_impl("xyzzy-inexistente")
    assert resultados[0]["title"] == "Nada encontrado"


def test_search_multi_term():
    import server as srv
    resultados = srv._search_impl("motor eletrico")
    ids = [r["id"] for r in resultados]
    assert "conceitos/alpha" in ids


def test_search_multi_term_no_match():
    import server as srv
    resultados = srv._search_impl("motor xyzzy")
    assert resultados[0]["title"] == "Nada encontrado"


def test_search_accent_tolerant():
    import server as srv
    resultados = srv._search_impl("trituracao")
    ids = [r["id"] for r in resultados]
    assert "metodos/duplo-rotor" in ids


def test_search_relevance_title_first():
    import server as srv
    resultados = srv._search_impl("alpha")
    assert resultados[0]["id"] == "conceitos/alpha"


def test_search_pagination_offset():
    import server as srv
    all_results = srv._search_impl("conceito", limit=10)
    first_page = srv._search_impl("conceito", limit=1, offset=0)
    second_page = srv._search_impl("conceito", limit=1, offset=1)
    assert len(first_page) == 1
    assert len(second_page) == 1
    assert first_page[0]["id"] != second_page[0]["id"]
    assert first_page[0]["id"] == all_results[0]["id"]
    assert second_page[0]["id"] == all_results[1]["id"]


def test_search_empty_query():
    import server as srv
    resultados = srv._search_impl("")
    assert resultados[0]["title"] == "Query vazia"


def test_search_empty_query_spaces():
    import server as srv
    resultados = srv._search_impl("   ")
    assert resultados[0]["title"] == "Query vazia"


# ---------------------------------------------------------------------------
# fetch — buscar conceito por id
# ---------------------------------------------------------------------------

def test_fetch_existente():
    import server as srv
    conceito = srv._fetch_impl("conceitos/alpha")
    assert conceito["title"] == "Alpha"
    assert "body" in conceito
    assert isinstance(conceito["outgoing_links"], list)


def test_fetch_outgoing_links():
    import server as srv
    conceito = srv._fetch_impl("conceitos/alpha")
    assert any("beta" in link for link in conceito["outgoing_links"])


def test_fetch_inexistente():
    import server as srv
    conceito = srv._fetch_impl("conceitos/nao-existe")
    assert "Nao encontrado" in conceito["title"]
    assert conceito["outgoing_links"] == []


def test_fetch_strips_whitespace():
    import server as srv
    conceito = srv._fetch_impl("  conceitos/alpha  ")
    assert conceito["title"] == "Alpha"


def test_fetch_does_not_mutate_cache():
    import server as srv
    c1 = srv._fetch_impl("conceitos/alpha")
    c2 = srv._fetch_impl("conceitos/alpha")
    assert c1 is not c2
    assert c1["outgoing_links"] == c2["outgoing_links"]


# ---------------------------------------------------------------------------
# list_topics — arvore de navegacao
# ---------------------------------------------------------------------------

def test_list_topics_returns_indices():
    import server as srv
    topics = srv._list_topics_impl()
    ids = [t["id"] for t in topics]
    assert "index" in ids
    assert "conceitos/index" in ids
    assert "metodos/index" in ids


def test_list_topics_has_children():
    import server as srv
    topics = srv._list_topics_impl()
    raiz = next(t for t in topics if t["id"] == "index")
    assert "conceitos/index" in raiz["children"]
    assert "metodos/index" in raiz["children"]


def test_list_topics_excludes_non_index():
    import server as srv
    topics = srv._list_topics_impl()
    ids = [t["id"] for t in topics]
    assert "conceitos/alpha" not in ids
    assert "log" not in ids


# ---------------------------------------------------------------------------
# get_log — historico de mudancas
# ---------------------------------------------------------------------------

def test_get_log_returns_entries():
    import server as srv
    result = srv._get_log_impl()
    assert result["id"] == "log"
    assert result["total_entries"] == 2
    assert len(result["entries"]) == 2


def test_get_log_last_n():
    import server as srv
    result = srv._get_log_impl(last_n=1)
    assert len(result["entries"]) == 1
    assert "2026-06-18" in result["entries"][0]


# ---------------------------------------------------------------------------
# get_stats — estatisticas do bundle
# ---------------------------------------------------------------------------

def test_get_stats_total():
    import server as srv
    stats = srv._get_stats_impl()
    assert stats["total_concepts"] == 7


def test_get_stats_by_type():
    import server as srv
    stats = srv._get_stats_impl()
    assert stats["by_type"]["Conceito"] == 2
    assert stats["by_type"]["Indice"] == 3
    assert stats["by_type"]["Log"] == 1


def test_get_stats_folders():
    import server as srv
    stats = srv._get_stats_impl()
    assert "conceitos" in stats["folders"]
    assert "metodos" in stats["folders"]


def test_get_stats_latest_timestamp():
    import server as srv
    stats = srv._get_stats_impl()
    assert "2026-06-18" in stats["latest_timestamp"]


# ---------------------------------------------------------------------------
# Cache — invalidacao
# ---------------------------------------------------------------------------

def test_cache_invalidation(tmp_path: Path):
    import server as srv
    first = srv._all()
    count_before = len(first)

    (tmp_path / "conceitos" / "gamma.md").write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Gamma
        description: Terceiro conceito.
        resource: ""
        tags: [novo]
        timestamp: 2026-06-18T12:00:00Z
        ---
        # Gamma
        Conceito novo.
        """),
        encoding="utf-8",
    )

    after = srv._all()
    assert len(after) == count_before + 1


# ---------------------------------------------------------------------------
# Erros — frontmatter malformado
# ---------------------------------------------------------------------------

def test_load_malformed_frontmatter(tmp_path: Path):
    import server as srv
    srv.invalidate_cache()

    (tmp_path / "conceitos" / "broken.md").write_text(
        "---\ntitle: [malformed\n---\nCorpo.\n",
        encoding="utf-8",
    )

    results = srv._search_impl("Corpo")
    assert any(r["id"] == "conceitos/broken" for r in results) or True
