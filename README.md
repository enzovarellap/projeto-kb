# projeto-kb

Base de conhecimento compartilhada em formato OKF (Open Knowledge Format), exposta via MCP server para Claude, ChatGPT e Gemini.

## Arquitetura

```
Origem (Google Drive)  →  Bundle OKF (kb/)  →  MCP server (server.py)
                                                      ↓
                                          Claude / ChatGPT / Gemini
```

- **Bundle OKF:** pasta de markdown com YAML frontmatter. Versionado neste repo.
- **MCP server:** expõe 7 tools somente-leitura (`readOnlyHint=True`) via `streamable-http`
  em `127.0.0.1:8000`. Fluxo recomendado (ver `instructions` do servidor e docstring de
  cada tool em `server.py` — é isso que a IA cliente lê para decidir qual chamar):
  1. Sem saber o que procurar → `list_topics()` (árvore completa) ou `get_index(id)` (detalhe
     de uma seção) para se orientar.
  2. Sabe os termos exatos → `search(query, limit, offset)` primeiro: busca multi-termo (AND)
     com relevância, normalização de acentos e fuzzy match para typos. Retorna
     `{"results": [...]}` com `id`, `type`, `title`, `description`, `text` (snippet) e
     `url` (`kb://<id>`) — contrato exigido pelo ChatGPT Deep Research (ver
     [ChatGPT](#chatgpt-mcp-direto-via-developer-mode--apps)).
  3. `search` não achou nada, ou a pergunta é conceitual/parafraseada → `semantic_search(query,
     limit)`: busca por similaridade vetorial (ChromaDB + embeddings), com fallback automático
     para `search` se o índice não estiver disponível.
  4. Sempre que tiver um `id` e for responder com conteúdo → `fetch(id)`: único tool que
     retorna o corpo completo do conceito, com `outgoing_links` resolvidos para continuar
     navegando o grafo; inclui também `text`, `url` e `metadata`, compatível com o `Document`
     do Deep Research.
  5. `get_log(last_n)` — histórico de mudanças do bundle (o que mudou recentemente).
  6. `get_stats()` — estatísticas agregadas: total, por tipo, pastas, último timestamp.
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

A busca semântica usa ChromaDB + embeddings (default: `all-MiniLM-L6-v2` via ONNX).

**Decisão registrada em `TODO.md` (Fase 7, "Multi-idioma"):** o KB deste projeto fica só em
PT-BR — não vale a pena traduzir os conceitos para inglês "por garantia" (Claude/GPT lidam
bem com KB em português, e embeddings modernos já são multilíngues). O risco real é outro:
o embedding *default* do ChromaDB (`all-MiniLM-L6-v2`) é English-centric e relativamente
fraco em PT-BR. O lever que realmente importa é trocar o **modelo de embedding**, não o
idioma do conteúdo. Modelo recomendado (mais forte em PT-BR que a opção antiga
`paraphrase-multilingual-MiniLM-L12-v2`, ainda suportada mas não é mais a recomendação):

```bash
python embeddings.py --model intfloat/multilingual-e5-large
```

Alternativa equivalente: `BGE-M3`. Ambos requerem acesso ao HuggingFace Hub (download do
modelo, alguns GB) e compute local razoável — **ação manual do Enzo**, não roda neste
ambiente de desenvolvimento (sem acesso à rede para baixar modelos).

Modelos da família e5 (como `intfloat/multilingual-e5-large`) rendem mais com prefixos
explícitos no texto — `"query: "` nas buscas e `"passage: "` nos documentos indexados.
`embeddings.py` já detecta automaticamente quando o modelo é da família e5 (prefixo
`intfloat/multilingual-e5`) e aplica esses prefixos sozinho; nenhuma configuração extra é
necessária além de passar `--model`.

**Importante:** ao trocar de modelo, sempre rode full reindex (`make index`, **não**
`make index-update`) — vetores gerados por modelos diferentes não são comparáveis entre
si, misturar os dois no mesmo índice corrompe a busca.

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
`mcp_server` — ver seção [Gemini](#gemini) abaixo para o exemplo completo.

## CORS (se necessário)

Decisão registrada em `TODO.md` (Fase 4.1): **não configurar CORS agora**. Os clientes
reais deste projeto — Claude Desktop, ChatGPT, Gemini — conectam ao server **server-side**
(a partir de um data center, não de um browser), e CORS é uma regra imposta por browsers
(preflight `OPTIONS` + header `Origin`); essas requisições nunca disparam isso. O FastMCP só
configura CORS automaticamente para rotas OAuth/`.well-known` — CORS geral fica por conta de
quem hospeda, mas não há necessidade real enquanto nenhum cliente roda num browser.

Se um dia isso mudar (ex: usar o MCP Inspector via web, ou construir um front-end próprio
que fala com o server diretamente do browser do usuário), o snippet abaixo é a referência
pronta para colar em `server.py` — **não está ativo, é só documentação**:

```python
from starlette.middleware.cors import CORSMiddleware

app = mcp.http_app()
app = CORSMiddleware(
    app,
    allow_origins=["https://seu-front.exemplo.com"],
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-API-Key", "Mcp-Session-Id"],
    expose_headers=["Mcp-Session-Id"],
)
```

**O que não fazer:** não usar `allow_origins=["*"]` junto com `allow_credentials=True`
(browsers rejeitam essa combinação); não empilhar dois middlewares CORS; não esquecer
`expose_headers=["Mcp-Session-Id"]` — sem isso o browser recebe a resposta mas não
consegue ler o header de sessão do MCP via JS.

## Gemini

Decisão registrada em `TODO.md` (Fase 5.3): sim, o Gemini já suporta MCP nativamente — não é
preciso nenhum adaptador/bridge. Duas formas de conectar:

1. **Interactions API**, apontando direto para o endpoint `streamable-http` do server (é o
   transporte que este projeto já usa — SSE puro *não* funciona com MCP remoto no Gemini):

   ```python
   from google import genai

   client = genai.Client()
   r = client.interactions.create(
       model="gemini-2.5-flash",
       input="Busque conceitos sobre X no meu KB e resuma.",
       tools=[{
           "type": "mcp_server",
           "name": "projeto_kb",
           "url": "https://projeto-kb.onrender.com/mcp/",
           "headers": {"x-api-key": "SUA_CHAVE"},
       }],
   )
   ```

2. **Alternativa via SDK:** `google-genai` também aceita passar um client FastMCP
   diretamente — mas nesse caminho o Gemini só enxerga *tools*, não resources/prompts.

**Caveats importantes:**
- **Modelo:** ainda não funciona com Gemini 3 — use `gemini-2.5-flash`.
- **Nome do tool sem hífen:** o campo `name` acima (`"projeto_kb"`) é o *rótulo que o
  Gemini usa para essa tool na própria requisição do cliente* — não precisa (e não deve)
  ter hífen, então usamos snake_case (`projeto_kb`). Isso é independente do nome interno
  registrado no server (`FastMCP(name="projeto-kb", ...)` em `server.py`, com hífen) —
  são dois namespaces diferentes, um do lado do chamador e outro do lado do server; o
  Gemini não valida um contra o outro. (Não encontramos documentação da Google explícita
  o bastante para garantir isso com 100% de certeza — se o snippet acima falhar por causa
  do nome, tente alinhar os dois como `projeto_kb` também no server como teste rápido.)
- Requer o server publicamente acessível via HTTPS (ver [Deploy](#deploy-render)) e uma
  API key configurada (ver [Autenticação](#autenticação) acima).

**Passo manual pendente (Enzo):** testar end-to-end de verdade com uma conta/API key do
Gemini, depois que o server estiver deployado — isso não é automatizável a partir daqui
(ver [Pendências](#pendências--bloqueio-humano)).

## Observabilidade

Decisão registrada no TODO.md (Fase 6.2): **logs JSON estruturados sempre ligados** +
**tracing OpenTelemetry opt-in via Logfire**. Prometheus + Grafana foi avaliado e
descartado — é trabalho de infra que não se paga no volume deste projeto (~100 req/dia).

### Logs estruturados (sempre ativos)

Cada chamada a uma tool MCP (`search`, `semantic_search`, `fetch`, `list_topics`,
`get_log`, `get_stats`, `get_index`) emite uma linha JSON via o `log_event()`/
`_log_tool_call` de `server.py`, com `tool`, `status` (`ok`/`error`), `latency_ms` e
metadados baratos e não-sensíveis (ex: `query_len`, `limit`, `id_len` — nunca a query
ou o conteúdo bruto de um documento, e nunca a API key). Uma falha ao logar nunca
derruba a chamada da tool (best-effort, `try/except` silencioso).

Como o server já usa `logging.basicConfig` para stdout, esses logs aparecem e ficam
pesquisáveis diretamente no dashboard de logs do Render — suficiente para começar,
sem infra adicional.

### Tracing com Logfire (opcional)

O FastMCP já emite spans OpenTelemetry automaticamente para tool/resource/prompt
(no-op sem um SDK configurado). Para tracing de verdade com ~zero esforço, ligue o
[Logfire](https://logfire.pydantic.dev/) (Pydantic, free tier generoso, mesmo
ecossistema que sustenta o FastMCP):

```bash
pip install logfire   # não é dependência obrigatória — ver nota abaixo
export LOGFIRE_TOKEN=seu-token-aqui
```

Com `LOGFIRE_TOKEN` definida e o pacote instalado, `server.py` chama
`logfire.configure(service_name="projeto-kb")` na inicialização e os spans nativos do
FastMCP passam a fluir para o Logfire automaticamente — nenhuma instrumentação manual
adicional é necessária. Sem o pacote instalado ou sem a variável definida, o import é
best-effort (`try/except ImportError`) e o server roda normalmente, só com os logs
JSON.

**Nota sobre a dependência:** `logfire` não está em `requirements.txt` porque seus
requisitos transitivos de OpenTelemetry conflitam de versão com os que o `chromadb`
já fixa neste projeto (`opentelemetry-sdk`/`opentelemetry-proto`/
`opentelemetry-exporter-otlp-proto-*`). Instalar `logfire` à parte funciona (o
conflito é só um aviso do `pip check`, não quebra nada em teste), mas para não
arriscar esse atrito em toda instalação padrão, ele fica como instalação manual
opcional, guardada por `try/except` no código.

### Alertas

Ainda não configurados neste repositório — mas com logs estruturados e tracing no ar,
já é possível ligar alerting nativo do Render (nível de serviço/uptime) ou do Logfire
(taxa de erro, latência) assim que houver uma conta configurada em produção.

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

Todo o código, configuração e decisões de arquitetura deste projeto estão prontos (ver
`TODO.md` para o detalhamento fase a fase). O que resta são ações que só o Enzo pode
fazer — criação de contas, autorização OAuth, testes com credenciais reais. Nada abaixo
requer mais código.

### 1. Google Drive — autorizar e sincronizar
`ingest_drive.py` já está implementado e testado (mocks). Para ativar de verdade:
1. Criar projeto no Google Cloud Console e habilitar a Drive API.
2. Gerar credenciais OAuth 2.0 e salvar como `credentials.json` na raiz do repo.
3. Rodar `make sync-drive FOLDER_ID=<id>` — um browser abre para autorizar (token
   fica salvo em `token.json` para as próximas execuções).

### 2. Deploy do MCP server (Render) — criar conta e conectar o repo
Decisão registrada em `TODO.md` (Fase 4.1): **Render**, plano free, via `render.yaml`
já pronto na raiz (ver [Deploy (Render)](#deploy-render) acima).
1. Criar conta no [Render](https://render.com) (sem cartão de crédito no free tier).
2. "New +" → "Blueprint" → conectar o repositório GitHub `projeto-kb`. O Render lê
   `render.yaml` e cria o serviço sozinho.
3. Setar o secret `MCP_API_KEYS` na tela de Environment do serviço (o `render.yaml`
   já declara a variável com `sync: false`, então o Render pede o valor na hora).
4. Disparar o primeiro deploy (automático após o blueprint ser aplicado).

**Cold start (plano free):** o serviço dorme após 15 min de inatividade; a primeira
chamada depois disso acorda o dyno em ~30-50s, o que pode estourar timeout de cliente
MCP — teste isso antes de depender do free tier para algo user-facing. Se incomodar,
trocar `plan: free` por `plan: starter` ($7/mês, sem sleep) em `render.yaml`, ou migrar
para Coolify/Oracle Cloud Always Free. Não vale tentar "keep-alive" com pinger externo
— é gambiarra frágil e contra os termos de uso do Render.

### 3. ChatGPT — criar o connector e testar
Decisão registrada em `TODO.md` (Fase 5.2): nenhum Custom GPT Action/OpenAPI —
ChatGPT já fala MCP nativamente, e `search`/`fetch` já seguem o contrato do Deep
Research (ver `SearchResult`/`SearchResults`/`Document` em `server.py`). Falta só:
1. Configurações → Connectors/Apps → **Developer Mode** → adicionar servidor MCP
   apontando para a URL pública do server (pós-deploy) + a `MCP_API_KEYS`, igual ao
   Claude Desktop acima. Requer conta ChatGPT com acesso a Developer Mode.
2. Testar `search`/`fetch` end-to-end (e, em modo chat com Developer Mode ligado, as
   demais tools: `semantic_search`, `list_topics`, `get_log`, `get_stats`).

### 4. Gemini — testar end-to-end
Decisão registrada em `TODO.md` (Fase 5.3): suporte nativo confirmado, sem adaptador
(ver [Gemini](#gemini) acima para o snippet). Falta só rodar de fato: precisa do
server deployado (item 2) e de uma conta/API key do Gemini — depois disso é só
executar o snippet com `model="gemini-2.5-flash"` e conferir que `search`/`fetch`
respondem.

### 5. Claude Desktop remoto — documentar e testar
O template de config local já existe (ver [Subir o MCP server](#subir-o-mcp-server)
acima); falta documentar a variante apontando para a URL pública (pós-deploy, mesmo
formato do bloco JSON em [Configuração por cliente](#configuração-por-cliente)) e
confirmar que `search`/`fetch` funcionam de ponta a ponta contra o server remoto.

### 6. Embeddings — reindexar com o modelo multilingual recomendado
Decisão registrada em `TODO.md` (Fase 7, "Multi-idioma"): o KB fica em PT-BR; o que
precisa trocar é o modelo de embedding, não o idioma do conteúdo. `embeddings.py` já
suporta `--model intfloat/multilingual-e5-large` (com prefixos `query:`/`passage:`
aplicados automaticamente). Rodar localmente (requer download do HuggingFace Hub, não
disponível no ambiente de desenvolvimento usado para preparar este repo):

```bash
python embeddings.py --model intfloat/multilingual-e5-large   # full reindex, não --update
```
