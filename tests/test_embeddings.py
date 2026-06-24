"""Testes para busca semântica (embeddings.py + semantic_search no server)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


def _make_bundle(tmp_path: Path) -> Path:
    """Cria um bundle OKF de teste com conceitos variados."""
    kb = tmp_path / "kb"
    kb.mkdir()
    (kb / "conceitos").mkdir()
    (kb / "metodos").mkdir()

    docs = [
        (
            "conceitos/motor-eletrico.md",
            {
                "type": "Conceito",
                "title": "Motor Elétrico",
                "description": "Motor de corrente contínua usado para acionar o triturador.",
                "resource": "",
                "tags": ["motor", "elétrico", "acionamento"],
                "timestamp": "2026-06-17T12:00:00Z",
            },
            "# Motor Elétrico\n\nMotor DC brushless de 500W para acionamento do eixo principal.",
        ),
        (
            "conceitos/lâminas.md",
            {
                "type": "Conceito",
                "title": "Lâminas de Corte",
                "description": "Lâminas de aço para trituração de plástico.",
                "resource": "",
                "tags": ["lâmina", "corte", "aço"],
                "timestamp": "2026-06-17T12:00:00Z",
            },
            "# Lâminas de Corte\n\nLâminas fabricadas em aço SAE 1045 temperado.",
        ),
        (
            "metodos/duplo-rotor.md",
            {
                "type": "Conceito",
                "title": "Triturador de Duplo Rotor",
                "description": "Método de trituração com dois eixos contra-rotativos.",
                "resource": "",
                "tags": ["triturador", "duplo rotor", "método"],
                "timestamp": "2026-06-17T12:00:00Z",
            },
            "# Duplo Rotor\n\nDois eixos giram em sentidos opostos, puxando o material para baixo.",
        ),
        (
            "conceitos/sustentabilidade.md",
            {
                "type": "Conceito",
                "title": "Sustentabilidade e Reciclagem",
                "description": "Impacto ambiental positivo da reciclagem mecânica de plásticos.",
                "resource": "",
                "tags": ["sustentabilidade", "reciclagem", "meio ambiente"],
                "timestamp": "2026-06-17T12:00:00Z",
            },
            "# Sustentabilidade\n\nA reciclagem mecânica reduz a necessidade de plástico virgem.",
        ),
    ]

    for rel_path, meta, body in docs:
        import frontmatter as fm

        post = fm.Post(body, **meta)
        p = kb / rel_path
        p.write_text(fm.dumps(post), encoding="utf-8")

    return kb


@pytest.fixture
def semantic_index(tmp_path):
    """Cria um SemanticIndex sobre um bundle de teste."""
    kb = _make_bundle(tmp_path)
    chroma_dir = tmp_path / ".chroma"

    from embeddings import SemanticIndex

    idx = SemanticIndex(kb_root=kb, chroma_dir=chroma_dir)
    idx.build()
    return idx, kb, chroma_dir


class TestBuild:
    def test_build_indexes_all_docs(self, semantic_index):
        idx, kb, _ = semantic_index
        assert idx.count() == 4

    def test_build_is_idempotent(self, semantic_index):
        idx, kb, _ = semantic_index
        idx.build()
        assert idx.count() == 4


class TestQuery:
    def test_exact_term_finds_doc(self, semantic_index):
        idx, _, _ = semantic_index
        hits = idx.query("motor elétrico")
        assert len(hits) > 0
        assert hits[0]["title"] == "Motor Elétrico"

    def test_paraphrased_query(self, semantic_index):
        """Busca parafraseada deve encontrar conceito relevante."""
        idx, _, _ = semantic_index
        hits = idx.query("como funciona o sistema de acionamento")
        titles = [h["title"] for h in hits]
        assert "Motor Elétrico" in titles

    def test_semantic_proximity(self, semantic_index):
        """Termos do mesmo domínio devem ter score alto."""
        idx, _, _ = semantic_index
        hits = idx.query("reciclagem de plástico")
        titles = [h["title"] for h in hits]
        assert "Sustentabilidade e Reciclagem" in titles

    def test_results_have_score(self, semantic_index):
        idx, _, _ = semantic_index
        hits = idx.query("triturador")
        assert all("score" in h for h in hits)
        assert hits[0]["score"] > 0

    def test_results_ordered_by_score(self, semantic_index):
        idx, _, _ = semantic_index
        hits = idx.query("método de trituração")
        scores = [h["score"] for h in hits]
        assert scores == sorted(scores, reverse=True)

    def test_limit_respected(self, semantic_index):
        idx, _, _ = semantic_index
        hits = idx.query("triturador", n_results=2)
        assert len(hits) <= 2

    def test_empty_index_returns_empty(self, tmp_path):
        kb = tmp_path / "empty_kb"
        kb.mkdir()
        chroma_dir = tmp_path / ".chroma_empty"

        from embeddings import SemanticIndex

        idx = SemanticIndex(kb_root=kb, chroma_dir=chroma_dir)
        hits = idx.query("qualquer coisa")
        assert hits == []


class TestUpdate:
    def test_incremental_detects_new_doc(self, semantic_index):
        idx, kb, _ = semantic_index
        assert idx.count() == 4

        import frontmatter as fm

        new_doc = fm.Post(
            "# Peneira\n\nSepara partículas por tamanho.",
            type="Conceito",
            title="Peneira Vibratória",
            description="Equipamento para classificação granulométrica.",
            resource="",
            tags=["peneira", "classificação"],
            timestamp="2026-06-18T12:00:00Z",
        )
        (kb / "conceitos" / "peneira.md").write_text(
            fm.dumps(new_doc), encoding="utf-8"
        )

        added, updated, removed = idx.update()
        assert added == 1
        assert idx.count() == 5

    def test_incremental_detects_modification(self, semantic_index):
        idx, kb, _ = semantic_index

        path = kb / "conceitos" / "motor-eletrico.md"
        import frontmatter as fm

        post = fm.load(path)
        post.content = "# Motor Elétrico\n\nAtualizado: agora usa motor AC trifásico de 750W."
        path.write_text(fm.dumps(post), encoding="utf-8")

        added, updated, removed = idx.update()
        assert updated == 1
        assert idx.count() == 4

    def test_incremental_detects_deletion(self, semantic_index):
        idx, kb, _ = semantic_index
        (kb / "conceitos" / "sustentabilidade.md").unlink()

        added, updated, removed = idx.update()
        assert removed == 1
        assert idx.count() == 3


class TestServerIntegration:
    """Testa semantic_search via server.py (sem MCP transport)."""

    @pytest.fixture(autouse=True)
    def setup_server(self, tmp_path, monkeypatch):
        kb = _make_bundle(tmp_path)
        chroma_dir = tmp_path / ".chroma_srv"

        from embeddings import SemanticIndex

        idx = SemanticIndex(kb_root=kb, chroma_dir=chroma_dir)
        idx.build()

        import server as srv

        monkeypatch.setattr(srv, "KB", kb)
        monkeypatch.setattr(srv, "_semantic_index", idx)
        self.srv = srv
        yield

    def test_semantic_search_returns_results(self):
        results = self.srv._semantic_search_impl("motor de acionamento")
        assert len(results) > 0
        assert results[0]["score"] > 0

    def test_semantic_search_fallback_on_no_index(self, monkeypatch):
        monkeypatch.setattr(self.srv, "_semantic_index", None)
        results = self.srv._semantic_search_impl("motor")
        assert len(results) > 0
        assert results[0]["title"] != "Nada encontrado"

    def test_semantic_search_supplements_low_score(self):
        results = self.srv._semantic_search_impl("xyzzy gibberish nonsense")
        assert len(results) > 0
