"""Testes para autenticação por API key (ApiKeyMiddleware, Fase 4.3)."""

import sys
from pathlib import Path

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient

sys.path.insert(0, str(Path(__file__).parent.parent))

from server import ApiKeyMiddleware, _build_middleware, _load_valid_api_keys  # noqa: E402


async def _health(request):
    return JSONResponse({"status": "ok"})


async def _protected(request):
    return JSONResponse({"secret": "dados"})


def _make_app(valid_keys):
    routes = [
        Route("/health", _health),
        Route("/mcp", _protected),
    ]
    middleware = [Middleware(ApiKeyMiddleware, valid_keys=valid_keys)]
    return Starlette(routes=routes, middleware=middleware)


def test_load_valid_api_keys_ausente(monkeypatch):
    monkeypatch.delenv("MCP_API_KEYS", raising=False)
    assert _load_valid_api_keys() == set()


def test_load_valid_api_keys_vazia(monkeypatch):
    monkeypatch.setenv("MCP_API_KEYS", "")
    assert _load_valid_api_keys() == set()


def test_load_valid_api_keys_multiplas(monkeypatch):
    monkeypatch.setenv("MCP_API_KEYS", "chave-a, chave-b,chave-c ")
    assert _load_valid_api_keys() == {"chave-a", "chave-b", "chave-c"}


def test_build_middleware_vazio_quando_sem_env(monkeypatch):
    """Sem MCP_API_KEYS, nenhum middleware de auth deve ser adicionado (auth OFF por padrao)."""
    monkeypatch.delenv("MCP_API_KEYS", raising=False)
    assert _build_middleware() == []


def test_build_middleware_presente_quando_com_env(monkeypatch):
    monkeypatch.setenv("MCP_API_KEYS", "minha-chave")
    middleware = _build_middleware()
    assert len(middleware) == 1


def test_health_bypassa_auth_mesmo_sem_key():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_protected_sem_key_retorna_401():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/mcp")
    assert resp.status_code == 401
    assert resp.json() == {"error": "unauthorized"}


def test_protected_com_key_invalida_retorna_401():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/mcp", headers={"x-api-key": "chave-errada"})
    assert resp.status_code == 401


def test_protected_com_x_api_key_valida_passa():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/mcp", headers={"x-api-key": "chave-valida"})
    assert resp.status_code == 200
    assert resp.json() == {"secret": "dados"}


def test_protected_com_bearer_valida_passa():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/mcp", headers={"Authorization": "Bearer chave-valida"})
    assert resp.status_code == 200
    assert resp.json() == {"secret": "dados"}


def test_protected_com_bearer_case_insensitive():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/mcp", headers={"Authorization": "bearer chave-valida"})
    assert resp.status_code == 200


def test_protected_com_bearer_invalido_retorna_401():
    app = _make_app(valid_keys={"chave-valida"})
    client = TestClient(app)
    resp = client.get("/mcp", headers={"Authorization": "Bearer chave-errada"})
    assert resp.status_code == 401


def test_sem_middleware_quando_valid_keys_vazio_no_app_real(monkeypatch):
    """Reproduz o cenario 'auth desligada': _build_middleware() vazio não bloqueia nada
    porque nenhum ApiKeyMiddleware é adicionado à app."""
    monkeypatch.delenv("MCP_API_KEYS", raising=False)
    app = Starlette(routes=[Route("/mcp", _protected)], middleware=_build_middleware())
    client = TestClient(app)
    resp = client.get("/mcp")
    assert resp.status_code == 200
