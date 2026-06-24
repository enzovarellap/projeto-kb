"""Testes para validate_okf.py."""

import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from validate_okf import validate


@pytest.fixture
def bundle_valido(tmp_path: Path) -> Path:
    """Cria um bundle OKF mínimo e válido."""
    (tmp_path / "conceitos").mkdir()

    (tmp_path / "index.md").write_text(
        textwrap.dedent("""\
        ---
        type: Índice
        title: Índice Raiz
        description: Índice de teste.
        resource: ""
        tags: []
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Índice
        - [Conceito A](conceitos/a.md)
        """),
        encoding="utf-8",
    )
    (tmp_path / "conceitos" / "a.md").write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Conceito A
        description: Primeiro conceito de teste.
        resource: ""
        tags: [teste]
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Conceito A
        Texto do conceito A.
        """),
        encoding="utf-8",
    )
    return tmp_path


def test_bundle_valido_passa(bundle_valido: Path) -> None:
    erros = validate(bundle_valido)
    assert erros == [], f"Erros inesperados: {erros}"


def test_type_ausente_reprova(bundle_valido: Path) -> None:
    alvo = bundle_valido / "conceitos" / "a.md"
    alvo.write_text(
        textwrap.dedent("""\
        ---
        title: Conceito sem type
        description: Vai falhar.
        resource: ""
        tags: []
        timestamp: 2026-06-17T12:00:00Z
        ---
        # Sem type
        """),
        encoding="utf-8",
    )
    erros = validate(bundle_valido)
    assert any("type" in e for e in erros), f"Esperava erro de 'type', mas erros foram: {erros}"


def test_link_quebrado_reprova(bundle_valido: Path) -> None:
    index = bundle_valido / "index.md"
    conteudo = index.read_text(encoding="utf-8")
    conteudo = conteudo.replace(
        "- [Conceito A](conceitos/a.md)",
        "- [Conceito A](conceitos/a.md)\n- [Inexistente](conceitos/nao-existe.md)",
    )
    index.write_text(conteudo, encoding="utf-8")
    erros = validate(bundle_valido)
    assert any("nao-existe" in e for e in erros), (
        f"Esperava erro de link quebrado, mas erros foram: {erros}"
    )


def test_timestamp_invalido_reprova(bundle_valido: Path) -> None:
    alvo = bundle_valido / "conceitos" / "a.md"
    alvo.write_text(
        textwrap.dedent("""\
        ---
        type: Conceito
        title: Timestamp ruim
        description: Vai falhar no timestamp.
        resource: ""
        tags: []
        timestamp: 17/06/2026
        ---
        # Timestamp inválido
        """),
        encoding="utf-8",
    )
    erros = validate(bundle_valido)
    assert any("timestamp" in e.lower() for e in erros), (
        f"Esperava erro de timestamp, mas erros foram: {erros}"
    )
