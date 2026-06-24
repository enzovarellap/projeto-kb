# TODO — Implementação Completa do MCP projeto-kb

Status: `[x]` feito · `[ ]` pendente · `[🔍]` requer pesquisa antes de implementar

---

## Fase 0 — Já implementado (baseline)

- [x] Scaffolding do repositório e bundle OKF semente
- [x] Validador de conformidade OKF (`validate_okf.py`)
- [x] MCP server com tools `search` e `fetch` (`server.py`)
- [x] Pipeline de ingestão local (`ingest.py`) — PDF, DOCX, PPTX, CSV, TXT, MD
- [x] Empacotamento — `requirements.txt`, `Makefile`, `README.md`
- [x] Testes unitários — `test_server.py` + `test_validate.py` (6 testes)
- [x] Bundle de conteúdo do projeto Trituradora FDM (24 arquivos `.md`)

---

## Fase 1 — Robustez do MCP Server

### 1.1 Melhorias nas tools existentes

- [x] **Busca multi-termo**: `search` agora usa AND — "motor elétrico" exige ambos os termos
- [x] **Relevância / scoring**: resultados ordenados por score (título=8, tags=4, descrição=2, corpo=1)
- [x] **Paginação**: parâmetro `offset` adicionado ao `search`
- [x] **Busca tolerante a acentos**: normalização via `unicodedata` (stdlib) — "trituracao" encontra "trituração"
- [x] **Busca fuzzy / typos**: `rapidfuzz` integrado — "triturdora" encontra "trituradora" (threshold 80, penalidade 0.6x no score)

### 1.2 Novas tools MCP

- [x] **`list_topics`**: retorna a árvore de pastas/índices do bundle com filhos resolvidos
- [ ] **`get_index`**: retorna o conteúdo de um `index.md` específico com seus links — atalho para navegação sem precisar fetch genérico (coberto por `fetch` + `list_topics`, baixa prioridade)
- [x] **`get_log`**: retorna as últimas N entradas do `log.md`
- [x] **`get_stats`**: retorna estatísticas do bundle — total, por tipo, pastas, último timestamp
- [🔍] **`write_concept` / `update_concept`**: permitir que o assistente crie ou edite conceitos diretamente via MCP? (avaliar se faz sentido no fluxo do projeto — risco de corromper o bundle)

### 1.3 Resiliência e performance

- [x] **Cache em memória**: cache com invalidação por mtime (sem dependência extra de `watchdog`)
- [x] **Tratamento de erros**: `frontmatter.load` com YAML malformado retorna doc de erro em vez de traceback
- [x] **Logging estruturado**: logs com `logging` (INFO para chamadas, WARNING para erros de parse)
- [x] **Proteção de query vazia**: queries vazias retornam mensagem orientativa
- [ ] **Timeout e limites**: proteger contra queries muito amplas que retornam o bundle inteiro

---

## Fase 2 — Busca Semântica (Embeddings)

- [x] **Escolher vector DB local**: ChromaDB — zero-infra, API simples, persistência em arquivo (`.chroma/`), espaço cosine
- [x] **Escolher modelo de embeddings**: default ONNX `all-MiniLM-L6-v2` (embutido no ChromaDB, sem dependência externa); suporte a modelo multilingual (`paraphrase-multilingual-MiniLM-L12-v2`) via `--model` quando HuggingFace Hub estiver acessível
- [x] **Gerar embeddings do bundle**: `embeddings.py` com CLI (`make index` / `make index-update`) — `SemanticIndex.build()` para full reindex
- [x] **Tool `semantic_search(query)`**: nova tool MCP com score de similaridade (0-1), lazy-load do índice
- [x] **Reindexação incremental**: `SemanticIndex.update()` compara hash MD5 de cada arquivo — adiciona novos, atualiza modificados, remove deletados
- [x] **Fallback**: se índice indisponível, faz fallback para `search` (keyword); se top score < 0.25, suplementa com resultados keyword
- [x] **Testes**: 15 testes cobrindo build, query (exata, parafraseada, proximidade semântica), update incremental, integração com server, e fallback

---

## Fase 3 — Integração Google Drive

- [ ] **Criar projeto no Google Cloud Console** (ação manual do Enzo)
- [ ] **Habilitar Google Drive API** (ação manual do Enzo)
- [ ] **Gerar credenciais OAuth 2.0** e salvar como `credentials.json` (ação manual do Enzo)
- [x] **Implementar `ingest_drive.py`**: usando `google-api-python-client` + `google-auth-oauthlib`
  - [x] Autenticação OAuth 2.0 com fluxo de consent (+ cache de token em `token.json`)
  - [x] Listar arquivos de uma pasta do Drive por ID (paginação automática)
  - [x] Download de arquivos (PDF, DOCX, PPTX, Sheets → CSV, Google Docs → DOCX, Slides → PPTX)
  - [x] Chamar `ingest.py` existente para converter → OKF
  - [x] Idempotência: identificar arquivos já importados pelo `resource: drive://<id>`
  - [x] Atualizar `log.md` com registro da sincronização
- [x] **Sincronização incremental**: verificar `modifiedTime` do Drive via `.drive-sync.json` para reimportar apenas alterados
- [x] **Comando Make**: `make sync-drive FOLDER_ID=xxx [OUT=kb/subpasta] [TYPE=Tipo] [INCREMENTAL=1]`
- [x] **Testes**: 17 testes mockando a API do Drive — list, download, export, filter, sync state, idempotência, log
- [x] **Alternativa: Google Drive MCP nativo**: avaliado — existe MCP server de Google Drive disponível, mas a ingestão própria foi implementada para permitir uso standalone (CI/CD, scripts, sem depender de sessão MCP)

---

## Fase 4 — Deploy e Infraestrutura

### 4.1 Deploy do server para URL pública

- [🔍] **Escolher plataforma de deploy**: avaliar Render vs. Railway vs. Fly.io vs. FastMCP Cloud `[🔍 pesquisar custo (free tier), latência, facilidade, suporte a streamable-http]`
- [x] **Dockerfile**: imagem Docker criada (`Dockerfile` + `.dockerignore`)
- [x] **Variáveis de ambiente**: `HOST`, `PORT`, `KB_PATH`, `RATE_LIMIT_MAX`, `RATE_LIMIT_WINDOW` externalizados via `os.environ`
- [x] **Health check**: `healthcheck.py` — script standalone que testa o endpoint MCP via `initialize` (usado pelo Docker `HEALTHCHECK`)
- [🔍] **CORS**: verificar se FastMCP já lida com isso `[🔍 pesquisar — ver prompt de pesquisa abaixo]`

### 4.2 CI/CD

- [x] **GitHub Actions — CI**: `.github/workflows/ci.yml` com 4 jobs:
  - [x] `lint` — `ruff check` + `ruff format --check`
  - [x] `test` — `make validate` + `pytest`
  - [x] `validate-bundle` — valida OKF standalone
  - [x] `docker` — build + healthcheck da imagem Docker
- [ ] **GitHub Actions — CD**: deploy automático ao fazer push na branch principal `[depende da escolha da plataforma — Fase 4.1]`
- [x] **Pre-commit hooks**: `.pre-commit-config.yaml` com `ruff` (lint + format) e `validate_okf.py` (validação do bundle)
- [x] **Ruff config**: `ruff.toml` configurado para Python 3.11, E/F/W/I rules

### 4.3 Segurança

- [🔍] **Autenticação do MCP server**: `[🔍 pesquisar — ver prompt de pesquisa abaixo]`
- [x] **Rate limiting**: rate limiter in-memory implementado em `server.py` (60 req/min por caller, configurável via env vars)
- [ ] **HTTPS**: resolvido pela plataforma de deploy (Render/Railway/Fly.io proveem TLS automático)
- [x] **Secrets management**: todas as configs externalizadas via variáveis de ambiente
- [x] **`.env` + `.env.example`**: template `.env.example` criado com todas as variáveis documentadas

---

## Fase 5 — Integrações Multi-Assistente

### 5.1 Claude Desktop / Claude Code

- [ ] **Documentar configuração** para `claude_desktop_config.json` com URL pública (já tem template para localhost no README)
- [ ] **Testar end-to-end**: validar que `search` e `fetch` funcionam corretamente via Claude Desktop conectado ao server remoto

### 5.2 ChatGPT (Custom GPT Action)

- [🔍] **Pesquisar formato de Action do ChatGPT**: entender spec OpenAPI / JSON Schema que o ChatGPT espera `[🔍 pesquisar documentação atualizada de Custom GPT Actions]`
- [ ] **Gerar spec OpenAPI**: exportar ou criar manualmente a especificação OpenAPI do server para registrar como Action
- [ ] **Autenticação para ChatGPT**: configurar API key ou OAuth para que o GPT se autentique no server
- [ ] **Criar Custom GPT**: configurar no ChatGPT com instructions + Action apontando para URL pública
- [ ] **Testar end-to-end**: validar busca e navegação pelo ChatGPT

### 5.3 Gemini

- [🔍] **Pesquisar integração Gemini + MCP**: verificar se o Gemini já suporta MCP nativo ou se precisa de adaptador/proxy `[🔍 pesquisar status do suporte MCP no Gemini — mudou em 2026?]`
- [ ] **Implementar adaptador se necessário**: bridge REST/gRPC → MCP ou vice-versa
- [ ] **Testar end-to-end**: validar que o Gemini consegue consumir o knowledge base

---

## Fase 6 — Qualidade e Observabilidade

### 6.1 Testes

- [ ] **Aumentar cobertura**: adicionar testes para:
  - [ ] `ingest.py` — testar conversão de cada formato (PDF, DOCX, PPTX, CSV)
  - [ ] Frontmatter malformado / encoding inválido
  - [ ] Busca com caracteres especiais, strings vazias, queries muito longas
  - [ ] Concorrência — múltiplas chamadas simultâneas ao server
- [ ] **Testes de integração**: subir o server real e testar via cliente MCP (nota: `streamable-http` exige handshake `initialize` → `Mcp-Session-Id` antes de qualquer `tools/call`; ver seção "Testar via curl" no README)
- [ ] **Coverage report**: configurar `pytest-cov` e definir threshold mínimo (ex: 80%)

### 6.2 Observabilidade

- [ ] **Métricas**: instrumentar o server com contadores de chamadas, latência por tool, erros
- [🔍] **Escolher stack de observabilidade**: Prometheus + Grafana? Simples JSON log + Datadog? `[🔍 avaliar o que a plataforma de deploy oferece gratuitamente]`
- [ ] **Alertas**: notificar se o server cair ou se a taxa de erro subir

---

## Fase 7 — Conteúdo e Evolução do Bundle

- [ ] **Ampliar o bundle**: adicionar mais documentos do projeto (atas de reunião, decisões técnicas, referências bibliográficas)
- [ ] **Playbooks adicionais**: guias para manutenção do server, troubleshooting, onboarding de novo membro
- [ ] **Versionamento do bundle**: tags git para marcar versões estáveis do knowledge base (ex: `kb-v1.0`)
- [ ] **Backup**: estratégia de backup do bundle (git já versiona, mas considerar export periódico)
- [🔍] **Multi-idioma**: avaliar se faz sentido ter versões em inglês dos conceitos para assistentes que performam melhor em EN `[🔍 pesquisar se modelos como Claude/GPT lidam bem com KB inteiramente em PT-BR]`

---

## Resumo de itens que requerem pesquisa [🔍]

| # | Tema | Pergunta-chave |
|---|------|----------------|
| ~~1~~ | ~~Busca fuzzy~~ | ~~Resolvido: rapidfuzz>=3.0.0~~ |
| 2 | Write via MCP | Faz sentido permitir que assistentes escrevam no bundle? Quais riscos? |
| ~~3~~ | ~~Vector DB~~ | ~~Resolvido: ChromaDB — zero-infra, persistente, API simples~~ |
| ~~4~~ | ~~Embeddings PT-BR~~ | ~~Resolvido: default ONNX (all-MiniLM-L6-v2); multilingual via --model~~ |
| 5 | Google Drive MCP | Existe MCP server de Google Drive pronto para reusar? |
| 6 | Plataforma de deploy | Render vs Railway vs Fly.io — qual tem melhor free tier para MCP? |
| 7 | CORS no FastMCP | FastMCP já configura CORS automaticamente? |
| 8 | Auth no FastMCP | Como implementar autenticação no FastMCP? Middleware? |
| 9 | ChatGPT Actions | Qual o formato atual da spec OpenAPI para Custom GPT Actions? |
| 10 | Gemini + MCP | O Gemini já suporta MCP nativamente em 2026? |
| 11 | Observabilidade | O que a plataforma de deploy escolhida oferece de monitoring grátis? |
| 12 | Multi-idioma | Modelos atuais lidam bem com KB inteiramente em PT-BR? |
| ~~13~~ | ~~Pre-commit~~ | ~~Resolvido: `.pre-commit-config.yaml` com ruff + validate_okf~~ |

---

## Prompts de pesquisa para itens [🔍] pendentes

Use estes prompts no Claude para pesquisar os itens que requerem input humano:

### 🔍 #6 — Plataforma de deploy (Render vs Railway vs Fly.io)

```
Preciso fazer deploy de um MCP server Python (usando FastMCP com transporte streamable-http)
que serve um knowledge base via endpoint HTTP em /mcp. O server é stateless (lê arquivos .md
do disco) e roda com `python server.py` escutando na porta 8000.

Compare as seguintes plataformas para deploy:
1. Render (free tier)
2. Railway (free tier / Hobby)
3. Fly.io (free tier)
4. FastMCP Cloud (se existir em 2026)

Para cada uma, avalie:
- Custo mensal (free tier vs. plano pago mínimo)
- Suporte a Docker (preciso rodar imagem customizada)
- Suporte a long-lived HTTP connections (streamable-http usa SSE)
- Latência típica para requests HTTP
- Facilidade de setup (CLI, GitHub integration)
- Limitações do free tier (sleep after inactivity? request limits?)
- Suporte a variáveis de ambiente / secrets
- TLS/HTTPS automático
- Custom domain

Qual plataforma você recomenda para um projeto acadêmico com uso moderado
(~100 requests/dia, 1-3 usuários simultâneos)?
```

### 🔍 #7 — CORS no FastMCP

```
Estou usando FastMCP (versão >=2.10.6) com transporte streamable-http em Python.
Meu server MCP será acessado de clientes web (Claude Desktop, Custom GPT, etc.)
que podem rodar em domínios diferentes.

1. O FastMCP já configura CORS automaticamente no transporte streamable-http?
2. Se não, como configuro CORS? Preciso usar um middleware ASGI (como CORSMiddleware
   do Starlette) ou existe uma opção nativa no FastMCP?
3. Quais origins devo permitir para que Claude Desktop e ChatGPT consigam acessar?
4. Mostre um exemplo de código para configurar CORS no server FastMCP.
```

### 🔍 #8 — Autenticação no FastMCP

```
Tenho um MCP server Python usando FastMCP (>=2.10.6) com transporte streamable-http.
Quero proteger o acesso com autenticação (API key ou Bearer token).

1. O FastMCP tem suporte nativo a autenticação? Se sim, como configurar?
2. Se não, qual a melhor forma de adicionar autenticação?
   - Middleware ASGI?
   - Decorator nas tools?
   - Proxy reverso (nginx/caddy)?
3. Como o Claude Desktop envia credenciais ao conectar em um MCP server remoto?
   O `claude_desktop_config.json` suporta headers customizados?
4. Como o ChatGPT envia credenciais ao chamar uma Action (OpenAPI)?
5. Mostre um exemplo de código para proteger o server com API key via header.
```

### 🔍 #9 — ChatGPT Custom GPT Actions

```
Quero expor meu MCP server como uma Custom GPT Action no ChatGPT.
O server tem estas tools:
- search(query, limit, offset) → busca por keyword
- semantic_search(query, limit) → busca semântica
- fetch(id) → retorna conceito completo
- list_topics() → árvore de navegação
- get_log(last_n) → histórico
- get_stats() → estatísticas

1. Qual o formato atual (2026) da spec OpenAPI que o ChatGPT espera para Actions?
2. Preciso de uma API REST separada ou posso apontar diretamente para o endpoint MCP?
3. Como configurar autenticação (API key) para a Action?
4. Existem limitações de rate limiting ou tamanho de resposta?
5. Gere um exemplo de spec OpenAPI para estas 6 tools.
```

### 🔍 #10 — Gemini + MCP

```
Quero conectar o Google Gemini ao meu MCP server (FastMCP, streamable-http).

1. O Gemini (API ou Google AI Studio) já suporta MCP nativamente em 2026?
2. Se não, quais são as alternativas?
   - Existe um proxy MCP → Gemini function calling?
   - Posso usar a API REST do Gemini com tool definitions mapeadas das MCP tools?
3. Se suporta, como configurar a conexão (URL, auth)?
4. Qual o formato que o Gemini espera para function declarations?
   É compatível com o JSON Schema do MCP?
```

---

## Ordem sugerida de execução

```
Fase 1 (robustez)     ████████░░  ← melhorias restantes: get_index, write_concept, timeout
Fase 2 (semântica)    ██████████  ✅ COMPLETA
Fase 4 (deploy + CI)  ████████░░  ← 80% feito — falta escolher plataforma + CD + auth + CORS
Fase 3 (Google Drive) ████░░░░░░  ← depende de ação humana (credentials)
Fase 5 (multi-AI)     ████░░░░░░  ← depende do deploy (fase 4)
Fase 6 (qualidade)    ███░░░░░░░  ← contínua, em paralelo
Fase 7 (conteúdo)     ███░░░░░░░  ← contínua, em paralelo
```
