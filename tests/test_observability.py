"""Testes para observabilidade (log_event, _log_tool_call — Fase 6.2)."""

import json
import logging
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import server as srv  # noqa: E402


def _parse_json_records(caplog):
    """Extrai e parseia como JSON cada linha de log emitida durante o teste."""
    parsed = []
    for record in caplog.records:
        try:
            parsed.append(json.loads(record.message))
        except (json.JSONDecodeError, TypeError):
            continue
    return parsed


class TestLogEvent:
    def test_emits_json_line_with_given_keys(self, caplog):
        with caplog.at_level(logging.INFO, logger="projeto-kb"):
            srv.log_event(tool="search", status="ok", latency_ms=1.23, query_len=5)

        events = _parse_json_records(caplog)
        assert len(events) == 1
        assert events[0]["tool"] == "search"
        assert events[0]["status"] == "ok"
        assert events[0]["latency_ms"] == 1.23
        assert events[0]["query_len"] == 5
        assert "ts" in events[0]

    def test_never_raises_on_unserializable_kwarg(self):
        class Unserializable:
            pass

        # default=str no json.dumps deve lidar com isso sem levantar exceção.
        srv.log_event(tool="x", weird=Unserializable())


class TestLogToolCallDecorator:
    def test_logs_ok_status_and_latency_on_success(self, caplog):
        @srv._log_tool_call("dummy_tool")
        def fn(x):
            return x * 2

        with caplog.at_level(logging.INFO, logger="projeto-kb"):
            result = fn(21)

        assert result == 42
        events = _parse_json_records(caplog)
        assert len(events) == 1
        assert events[0]["tool"] == "dummy_tool"
        assert events[0]["status"] == "ok"
        assert isinstance(events[0]["latency_ms"], (int, float))

    def test_logs_error_status_and_reraises_on_exception(self, caplog):
        @srv._log_tool_call("dummy_tool")
        def fn():
            raise ValueError("boom")

        with caplog.at_level(logging.INFO, logger="projeto-kb"), pytest.raises(ValueError):
            fn()

        events = _parse_json_records(caplog)
        assert len(events) == 1
        assert events[0]["tool"] == "dummy_tool"
        assert events[0]["status"] == "error"

    def test_metrics_callback_adds_fields_without_leaking_raw_content(self, caplog):
        @srv._log_tool_call("search_like", metrics=lambda query, limit=8: {
            "query_len": len(query), "limit": limit,
        })
        def fn(query, limit=8):
            return ["hit"]

        with caplog.at_level(logging.INFO, logger="projeto-kb"):
            fn("conteudo sensivel de busca", limit=3)

        events = _parse_json_records(caplog)
        assert events[0]["query_len"] == len("conteudo sensivel de busca")
        assert events[0]["limit"] == 3
        # A query bruta nunca deve aparecer no log estruturado.
        dumped = json.dumps(events[0])
        assert "conteudo sensivel" not in dumped

    def test_broken_metrics_callback_does_not_break_call(self, caplog):
        @srv._log_tool_call("dummy_tool", metrics=lambda *a, **kw: 1 / 0)
        def fn():
            return "ok-result"

        with caplog.at_level(logging.INFO, logger="projeto-kb"):
            result = fn()

        assert result == "ok-result"
        events = _parse_json_records(caplog)
        assert events[0]["status"] == "ok"

    def test_preserves_function_signature_for_fastmcp_introspection(self):
        @srv._log_tool_call("dummy_tool")
        def fn(query: str, limit: int = 8, offset: int = 0) -> list:
            return []

        assert fn.__name__ == "fn"
        assert fn.__wrapped__ is not None


class TestToolWrappersEmitEvents:
    """Confere que os wrappers @mcp.tool reais estao instrumentados (sem
    duplicar logging nos _impl, chamados internamente por outras tools)."""

    @pytest.fixture(autouse=True)
    def kb_de_teste(self, tmp_path: Path, monkeypatch):
        (tmp_path / "index.md").write_text(
            "---\n"
            "type: Indice\n"
            "title: KB Raiz\n"
            "description: raiz\n"
            'resource: ""\n'
            "tags: [indice]\n"
            "timestamp: 2026-06-17T12:00:00Z\n"
            "---\n"
            "# KB Raiz\n",
            encoding="utf-8",
        )
        monkeypatch.setattr(srv, "KB", tmp_path)
        srv.invalidate_cache()
        yield
        srv.invalidate_cache()

    def test_search_tool_emits_single_event(self, caplog):
        with caplog.at_level(logging.INFO, logger="projeto-kb"):
            srv.search("raiz")

        events = _parse_json_records(caplog)
        search_events = [e for e in events if e.get("tool") == "search"]
        assert len(search_events) == 1
        assert search_events[0]["status"] == "ok"
        assert "query_len" in search_events[0]

    def test_fetch_tool_emits_single_event(self, caplog):
        with caplog.at_level(logging.INFO, logger="projeto-kb"):
            srv.fetch("nao-existe")

        events = _parse_json_records(caplog)
        fetch_events = [e for e in events if e.get("tool") == "fetch"]
        assert len(fetch_events) == 1
        # fetch nao-encontrado retorna um dict "nao encontrado", nao levanta —
        # portanto o status permanece "ok" (a tool respondeu com sucesso).
        assert fetch_events[0]["status"] == "ok"
