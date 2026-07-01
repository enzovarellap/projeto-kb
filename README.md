# projeto-kb

Base de conhecimento compartilhada em formato OKF (Open Knowledge Format), exposta via MCP server para Claude, ChatGPT e Gemini.

## Arquitetura

```
Origem (Google Drive)  →  Bundle OKF (kb/)  →  MCP server (server.py)
                                                      ↓
                                          Claude / ChatGPT / Gemini
```

- **Bundle OKF:** pasta de markdown com YAML frontmatter. Versionado neste repo.
- **MCP server:** expõe 6 tools via `streamable-http` em `127.0.0.1:8000`:
  - `search(query, limit, offset)` — busca multi-termo com relevância e normalização de acentos.
    Retorna `{"results": [...]}` com `id`, `type`, `title`, `description`, e os campos
    `text` (snippet) e `url` (`kb://<id>`) exigidos pelo contrato de busca do ChatGPT
    Deep Research (ver [ChatGPT](#chatgpt-mcp-direto-via-developer-mode--apps))
  - `semantic_search(query, limit)` — busca por similaridade vetorial (ChromaDB + embeddings)
  - `fetch(id)` — conceito completo com outgoing_links resolvidos; inclui também `text`
    (mesmo conteúdo de `body`), `url` (`kb://<id>`) e `metadata`
    (type/tags/timestamp/resource), compatível com o `Document` do Deep Research
  - `list_topics()` — árvore de navegação (índices + filhos)
  - `get_log(last_n)` — histórico de mudanças do bundle
  - `get_stats()` — estatísticas: total, por tipo, pastas, último timestamp
- **Ingestão:** `ingest.py` converte arquivos locais (PDF, DOCX, etc.) em conceitos OKF.

## Instalação

```bash
# Python 3.11+
pip install -r requirements.txt
# ou via make:
make install
```

## Uso

### Validar o bundle

```bash
make validate
# ou: python validate_okf.py
```

### Subir o MCP server

```bash
make serve
# ou: python server.py
# Acesse: http://127.0.0.1:8000/mcp
```

### Testar via curl

O transporte `streamable-http` exige um handshake de inicialização antes de chamar qualquer tool. O header `Accept` deve incluir `application/json` e `text/event-stream`.

**1. Inicializar sessão** (obter `Mcp-Session-Id`):

```bash
curl -v http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc":"2.0","id":1,"method":"initialize",
    "params":{
      "protocolVersion":"2025-03-26",
      "capabilities":{},
      "clientInfo":{"name":"test-client","version":"1.0"}
    }
  }'
```

Copie o valor de `mcp-session-id` do header de resposta (ex: `8dd8c7d9...`).

**2. Chamar tools** (usando o session ID):

```bash
SID="<mcp-session-id>"

# Listar tools disponíveis
curl -s http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'

# Buscar conceitos
curl -s http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"search","arguments":{"query":"trituracao"}}}'

# Buscar conceito por id
curl -s http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"fetch","arguments":{"id":"metodos/01-duplo-rotor"}}}'

# Árvore de navegação
curl -s http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"list_topics","arguments":{}}}'

# Estatísticas do bundle
curl -s http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":6,"method":"tools/call","params":{"name":"get_stats","arguments":{}}}'

# Histórico de mudanças
curl -s http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":7,"method":"tools/call","params":{"name":"get_log","arguments":{"last_n":5}}}'
```

Adicione ao Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "projeto-kb": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

### Ingerir arquivos locais

```bash
make ingest SRC=exemplos/meu-lote OUT=kb/importados
# ou com tipo personalizado:
python ingest.py --src exemplos/meu-lote --out kb/importados --type Playbook
```

### Indexar para busca semântica

```bash
make index          # full reindex (recria do zero)
make index-update   # incremental (apenas novos/modificados)
```

A busca semântica usa ChromaDB + embeddings (default: `all-MiniLM-L6-v2` via ONNX). Para usar um modelo multilingual melhor para PT-BR (requer acesso ao HuggingFace Hub):

```bash
python embeddings.py --model paraphrase-multilingual-MiniLM-L12-v2
```

### Sincronizar com Google Drive

```bash
# Sincronização completa
make sync-drive FOLDER_ID=<id-da-pasta-no-drive>

# Com subpasta personalizada
make sync-drive FOLDER_ID=<id> OUT=kb/documentos-drive

# Sincronização incremental (apenas arquivos novos/modificados)
make sync-drive FOLDER_ID=<id> INCREMENTAL=1

# Via CLI direto
python ingest_drive.py --folder-id <id> --out kb/drive-import --incremental
```

**Pré-requisitos:**
1. Criar projeto no Google Cloud Console e habilitar a Google Drive API
2. Gerar credenciais OAuth 2.0 e salvar como `credentials.json` na raiz do projeto
3. Na primeira execução, um browser abrirá para autorizar o acesso (token salvo em `token.json`)

**Formatos suportados:**
- Download direto: PDF, DOCX, PPTX, CSV, TXT, MD
- Exportação automática: Google Sheets → CSV, Google Docs → DOCX, Google Slides → PPTX

### Rodar os testes

```bash
make test
# ou: python3 -m pytest tests/ -v
```

### Docker

```bash
# Build da imagem
make docker

# Rodar com variáveis de ambiente
make docker-run
# ou: docker run -p 8000:8000 -e HOST=0.0.0.0 -e PORT=8000 projeto-kb
```

### Deploy (Render)

O repositório inclui `render.yaml` (Blueprint spec do Render) na raiz, pronto para uso:

```yaml
services:
  - type: web
    name: projeto-kb
    runtime: docker        # usa o Dockerfile já existente
    plan: free              # trocar por "starter" p/ eliminar cold start
    healthCheckPath: /health
    autoDeploy: true        # redeploy automático a cada push
    envVars:
      - key: MCP_API_KEYS
        sync: false          # secret, setado manualmente no dashboard
      # HOST, KB_PATH, MAX_RESULTS, MAX_QUERY_LENGTH, RATE_LIMIT_MAX,
      # RATE_LIMIT_WINDOW também são declaradas com defaults sensatos.
```

Ele usa o `Dockerfile` já existente (nenhuma mudança de código foi necessária: `server.py`
já lê `HOST`/`PORT` de env vars e o Render injeta `PORT` automaticamente em serviços web
docker) e aponta `healthCheckPath` para o endpoint `/health` que já existe no server.

Para usar, depois de ter acesso a uma conta Render: dashboard → "New +" → "Blueprint" →
conectar este repositório. O Render lê `render.yaml` e cria o serviço sozinho; só falta
setar o secret `MCP_API_KEYS` na tela de Environment. Detalhes do que ainda é manual e
do trade-off do plano free (cold start) estão em
[Pendências → Deploy do MCP server](#deploy-do-mcp-server).

### Lint e formatação

```bash
make lint       # ruff check
make format     # ruff format

# Instalar pre-commit hooks (roda lint + validate antes de cada commit)
make pre-commit-install
```

## Variáveis de ambiente

| Variável | Default | Descrição |
|----------|---------|-----------|
| `HOST` | `127.0.0.1` | Endereço de bind do server |
| `PORT` | `8000` | Porta do server |
| `KB_PATH` | `./kb` | Caminho para o bundle OKF |
| `RATE_LIMIT_MAX` | `60` | Máximo de requests por janela |
| `RATE_LIMIT_WINDOW` | `60` | Janela de rate limiting (segundos) |
| `MCP_API_KEYS` | *(vazio)* | Lista de API keys válidas, separadas por vírgula. Vazio/ausente = autenticação desligada |

Copie `.env.example` para `.env` e ajuste os valores.

## Autenticação

O server suporta autenticação por API key estática via header, implementada como
middleware ASGI (`ApiKeyMiddleware` em `server.py`). **Fica desligada por padrão** —
só é ativada quando a variável `MCP_API_KEYS` está definida e não-vazia, o que mantém
dev local e os testes funcionando sem nenhuma configuração extra.

### Ativando

```bash
# .env ou variável de ambiente do serviço de deploy
MCP_API_KEYS=chave-secreta-um,chave-secreta-dois
```

Com isso, toda rota (exceto `/health`, sempre público para healthcheck da plataforma
de deploy) passa a exigir uma das chaves acima, enviada em um dos dois formatos:

- Header `X-API-Key: <chave>`
- Header `Authorization: Bearer <chave>`

Requisições sem chave válida recebem `401 {"error": "unauthorized"}`. O handshake MCP
(`initialize`, `tools/list`, `tools/call`, etc.) funciona normalmente para requisições
autenticadas — a autenticação não interfere no protocolo, só barra quem não tem chave.

**Não faça:** não hardcode a key no repositório, não passe a key por query param, e não
confie apenas em rate limiting como proteção de acesso.

### Configuração por cliente

**Claude Desktop** (`claude_desktop_config.json`, servers tipo `http` suportam `headers`):

```json
{
  "mcpServers": {
    "projeto-kb": {
      "type": "http",
      "url": "https://projeto-kb.onrender.com/mcp/",
      "headers": { "x-api-key": "SUA_CHAVE" }
    }
  }
}
```

**ChatGPT:** ao adicionar o connector/app, informe a chave no campo de autenticação
(token). Via API (Responses), passe o header no tool `mcp`.

**Gemini:** informe `headers: {"x-api-key": "..."}` diretamente na definição do tool
`mcp_server`.

## Estrutura

```
projeto-kb/
├── kb/                        # bundle OKF
│   ├── index.md               # índice raiz
│   ├── log.md                 # histórico de mudanças
│   ├── conceitos/             # definições e glossário
│   └── playbooks/             # guias operacionais
├── server.py                  # MCP server (search, semantic_search, fetch)
├── embeddings.py              # índice semântico (ChromaDB + embeddings)
├── ingest.py                  # ingestão local
├── ingest_drive.py            # integração Google Drive
├── validate_okf.py            # validador OKF
├── healthcheck.py             # health check para Docker/plataformas
├── tests/                     # testes pytest
├── Dockerfile                 # imagem Docker
├── .github/workflows/ci.yml   # GitHub Actions CI
├── .pre-commit-config.yaml    # pre-commit hooks (ruff + validate)
├── ruff.toml                  # config do linter
├── .env.example               # template de variáveis de ambiente
├── requirements.txt
└── Makefile
```

## Formato OKF

Todo arquivo `.md` em `kb/` deve ter este frontmatter:

```yaml
---
type: Conceito          # obrigatório
title: Meu Conceito
description: Uma linha.
resource: drive://<id>  # "" se nativo
tags: [tag1, tag2]
timestamp: 2026-06-17T12:00:00Z
---
```

## Pendências (🛑 bloqueio humano)

As etapas abaixo requerem ação do Enzo:

### Google Drive
`ingest_drive.py` está implementado. Para ativar:
1. Criar projeto no Google Cloud Console.
2. Habilitar a Drive API.
3. Gerar credenciais OAuth 2.0 e salvar como `credentials.json` na raiz.
4. Executar `make sync-drive FOLDER_ID=<id>` — o browser abrirá para autorizar.

### Deploy do MCP server
Decisão registrada em `TODO.md` (Fase 4.1): **Render**, plano free, via `render.yaml`
(veja a seção [Deploy (Render)](#deploy-render) abaixo). É a única das opções avaliadas
(Render, Railway, Fly.io, FastMCP Cloud) com free tier real sem cartão de crédito,
HTTPS automático, deploy via GitHub e suporte a Docker + streamable-http.

O que falta é só a parte que exige conta/dashboard (não automatizável a partir daqui):
1. Criar conta no [Render](https://render.com) (sem cartão de crédito no free tier).
2. "New +" → "Blueprint" → conectar o repositório GitHub `projeto-kb`. O Render lê
   `render.yaml` da raiz e cria o serviço web automaticamente.
3. No dashboard do serviço, em Environment, setar o secret `MCP_API_KEYS` (o
   `render.yaml` já declara a chave com `sync: false`, então o Render vai pedir o
   valor na hora de criar o serviço).
4. Disparar o primeiro deploy (automático após o blueprint ser aplicado).

**Cold start (plano free):** o serviço dorme após 15 min de inatividade; a primeira
chamada depois disso acorda o dyno em ~30-50s, o que pode estourar timeout de cliente
MCP. Teste esse comportamento antes de depender do free tier para algo user-facing.
Se incomodar, dois caminhos:
- Upgrade para o plano **Starter** ($7/mês, sem sleep) — só trocar `plan: free` por
  `plan: starter` em `render.yaml`.
- Migrar para **Coolify** num VPS barato (Hetzner ~€4/mês) ou **Oracle Cloud Always
  Free** (VM ARM always-on, 100% grátis) se quiser fugir de custo recorrente.

Não vale a pena tentar "keep-alive" com pinger externo para evitar o sleep — é
gambiarra frágil e contra os termos de uso do Render.

### ChatGPT (MCP direto via Developer Mode / Apps)
Decisão registrada em `TODO.md` (Fase 5.2): **não** construir um Custom GPT Action /
spec OpenAPI separado. ChatGPT já fala MCP nativamente — o server deste repo é
apontado direto via **Apps/connectors com Developer Mode** ligado, sem duplicar
lógica numa API REST paralela.

- As tools `search(query, ...)` e `fetch(id)` já seguem o contrato exigido pelo
  ChatGPT Deep Research: `search` retorna `{"results": [...]}` (cada item com
  `id`, `title`, `text` — snippet — e `url` no formato `kb://<id>`) e `fetch`
  retorna um `Document` achatado com `id`, `title`, `text` (conteúdo completo,
  mesmo valor de `body`), `url` e `metadata` (type/tags/timestamp/resource). Ver
  `SearchResult`/`SearchResults`/`Document` em `server.py`.
- Em **Deep Research / Company Knowledge**, o ChatGPT só chama `search` e
  `fetch` — as outras 4 tools (`semantic_search`, `list_topics`, `get_log`,
  `get_stats`) só ficam disponíveis em modo chat normal com Developer Mode
  ligado (conector completo).
- **Gating por plano (fato atual da OpenAI, fora do nosso controle):** o server
  precisa estar em HTTPS público (sem localhost); acesso de escrita completo via
  connector só é liberado em planos Business/Enterprise/Edu — Plus/Pro ficam
  limitados a leitura (`search`/`fetch`). Isso não afeta este server porque
  nenhuma tool de escrita foi implementada aqui (decisão separada, ver `TODO.md`).
- **Passo manual pendente (Enzo):** criar o connector de fato no ChatGPT
  (Configurações → Connectors/Apps → Developer Mode → adicionar servidor MCP
  apontando para a URL pública + `MCP_API_KEYS`, igual ao Claude Desktop acima)
  e testar `search`/`fetch` end-to-end — isso exige uma conta ChatGPT com acesso
  a Developer Mode e não é automatizável a partir daqui.

### Embeddings / Vector DB
Implementado na Fase 2. Rode `make index` para gerar os embeddings e use `semantic_search` via MCP.
