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
- [x] **`get_index`**: retorna o conteúdo de um `index.md` específico com seus links — atalho para navegação sem precisar fetch genérico
- [x] **`get_log`**: retorna as últimas N entradas do `log.md`
- [x] **`get_stats`**: retorna estatísticas do bundle — total, por tipo, pastas, último timestamp
- [ ] **`write_concept` / `update_concept`**: pesquisa concluída, decisão registrada — **adiar, não implementar agora**.
  Não permitir escrita direta no bundle por assistentes (risco de corromper o KB sem revisão humana).
  Caminho do meio, se algum dia fizer sentido: tool `propose_concept` que **não** toca no KB — abre PR via
  GitHub API (ou grava em `/proposals/`) para aprovação humana. Salvaguardas obrigatórias nesse desenho
  futuro: validação de schema OKF antes de propor, `dry_run=True` por padrão, backup/versionamento (nunca
  sobrescrever), rate limit dedicado nas write tools, e anotar as tools de leitura existentes com
  `readOnlyHint=True`. O que não fazer: `update_concept` que sobrescreve sem versionamento; confiar no LLM
  para validar o próprio output; expor write tools sem auth forte; escrita direta em main/produção.
  Nada disso foi implementado — item permanece como trabalho futuro, não como pendente de pesquisa.

### 1.3 Resiliência e performance

- [x] **Cache em memória**: cache com invalidação por mtime (sem dependência extra de `watchdog`)
- [x] **Tratamento de erros**: `frontmatter.load` com YAML malformado retorna doc de erro em vez de traceback
- [x] **Logging estruturado**: logs com `logging` (INFO para chamadas, WARNING para erros de parse)
- [x] **Proteção de query vazia**: queries vazias retornam mensagem orientativa
- [x] **Timeout e limites**: proteger contra queries muito amplas — `MAX_QUERY_LENGTH` (500 chars) e `MAX_RESULTS` (50) configuráveis via env var

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

- [x] **Escolher plataforma de deploy**: **Render**, plano free (destravar agora) → upgrade para Starter ($7/mês, sem cold start) quando o sleep incomodar, ou migrar para Coolify (Hetzner ~€4/mês) / Oracle Cloud Always Free se quiser fugir de custo recorrente. Justificativa: única opção das quatro avaliadas com free tier real sem cartão de crédito, HTTPS automático, deploy via GitHub, Docker e env/secrets prontos — Fly.io matou o free tier para contas novas, Railway não tem free permanente. Config entregue em `render.yaml` (raiz do repo), usando o `Dockerfile` e o endpoint `/health` já existentes — nenhuma mudança em `server.py` foi necessária. **Pendente (manual, ação do Enzo):** criar conta no Render e conectar o repositório via dashboard — não automatizável a partir daqui (ver `README.md` → Pendências → Deploy do MCP server).
- [x] **Dockerfile**: imagem Docker baseada em `python:3.12-slim` com healthcheck integrado
- [x] **Variáveis de ambiente**: `HOST`, `PORT`, `KB_PATH`, `MAX_RESULTS`, `MAX_QUERY_LENGTH` via env vars (+ `.env.example`)
- [x] **Health check**: endpoint `/health` via `@mcp.custom_route` retorna `{"status":"ok","documents":N}`
- [x] **CORS**: pesquisado e decidido — **não implementar agora**. Clientes reais deste projeto
  (Claude Desktop, ChatGPT, Gemini) conectam server-side, não a partir de um browser — CORS é regra
  de navegador (preflight/`Origin`), e requisições de data center da Anthropic/OpenAI/Google não
  disparam isso. FastMCP só configura CORS automaticamente para rotas OAuth/`.well-known`; CORS
  geral ficaria por nossa conta, mas não há necessidade real hoje. Se um cliente browser aparecer no
  futuro (ex: MCP Inspector web, um front próprio), o snippet pronto para colar está documentado no
  README (seção "CORS (se necessário)").

### 4.2 CI/CD

- [x] **GitHub Actions — CI**: `.github/workflows/ci.yml` roda em push/PR:
  - [x] `make validate` (validar bundle OKF)
  - [x] `make test` (rodar pytest com coverage)
  - [x] Lint com `ruff`
- [ ] **GitHub Actions — CD**: deploy automático ao fazer push na branch principal
- [x] **Pre-commit hooks**: resolvido — usa o framework `pre-commit` de fato (`.pre-commit-config.yaml`
  na raiz): `ruff` (`--fix` + `ruff-format`) e um hook local que roda `validate_okf.py` em qualquer
  mudança sob `kb/**/*.md`. Instalar com `make pre-commit-install`.

### 4.3 Segurança

- [x] **Autenticação do MCP server**: implementado via middleware ASGI (`ApiKeyMiddleware` em `server.py`, `starlette.middleware.base.BaseHTTPMiddleware`), passado a `mcp.run(transport="streamable-http", middleware=[...])`. Aceita chave estática por `X-API-Key` ou `Authorization: Bearer <chave>`, validada contra a lista em `MCP_API_KEYS` (env var, separada por vírgula). `/health` sempre público. Auth fica **desligada por padrão** — só ativa se `MCP_API_KEYS` estiver definida e não-vazia, preservando testes e dev local sem config extra. Decisão: API key estática resolve o caso de uso atual (poucos clientes fixos: Claude Desktop, ChatGPT, Gemini); OAuth nativo do FastMCP fica para depois, se surgir necessidade de login por usuário/multi-tenant.
- [ ] **Rate limiting**: limitar chamadas por minuto para evitar abuso
- [ ] **HTTPS**: garantir que o deploy use TLS (geralmente resolvido pela plataforma)
- [ ] **Secrets management**: credenciais do Drive e API keys em variáveis de ambiente, não no código
- [x] **`.env` + `.env.example`**: template com todas as variáveis de ambiente documentadas

---

## Fase 5 — Integrações Multi-Assistente

### 5.1 Claude Desktop / Claude Code

- [ ] **Documentar configuração** para `claude_desktop_config.json` com URL pública (já tem template para localhost no README)
- [ ] **Testar end-to-end**: validar que `search` e `fetch` funcionam corretamente via Claude Desktop conectado ao server remoto

### 5.2 ChatGPT (MCP direto via Developer Mode / Apps)

- [x] **Pesquisar formato de Action do ChatGPT**: resolvido — decisão registrada: **não** construir
  Action/OpenAPI. ChatGPT já fala MCP nativamente; aponta-se o server direto via Apps/connectors
  com Developer Mode ligado. Em Deep Research/Company Knowledge o ChatGPT só usa `search`/`fetch`;
  as outras 4 tools só ficam disponíveis em modo chat com Developer Mode. `search`/`fetch` foram
  ajustados para o contrato que o Deep Research exige: `search` retorna `{"results": [...]}` com
  `id`/`title`/`text`/`url` por item (modelos `SearchResult`/`SearchResults` em `server.py`), e
  `fetch` retorna um `Document` achatado com `id`/`title`/`text`/`url`/`metadata` (além dos campos
  já existentes). Fatos atuais da OpenAI (fora do nosso controle): remote only (sem localhost),
  HTTPS obrigatório; escrita completa via connector só em planos Business/Enterprise/Edu — não
  afeta este server, que não implementa tools de escrita.
- ~~[ ] **Gerar spec OpenAPI**~~ — decidido: não necessário. ChatGPT fala MCP nativo; Custom GPT
  Action/OpenAPI é o caminho legado para isso.
- [x] **Autenticação para ChatGPT**: já resolvido pelo middleware de API key estática (ver seção
  "Autenticação do MCP server" acima, Fase 4.3 / `ApiKeyMiddleware`). ChatGPT informa a chave no
  campo de autenticação do connector (`X-API-Key` ou `Authorization: Bearer`), igual ao fluxo já
  documentado para Claude Desktop/Gemini no README.
- [ ] **Criar o connector no ChatGPT**: configurar em Configurações → Connectors/Apps → Developer
  Mode, apontando para a URL pública do server + a API key — não "Custom GPT", é um conector
  MCP direto. Requer conta ChatGPT com acesso a Developer Mode (ação manual do Enzo).
- [ ] **Testar end-to-end**: validar `search`/`fetch` (e, em modo chat com Developer Mode, as
  demais tools) através do conector configurado.

### 5.3 Gemini

- [x] **Pesquisar integração Gemini + MCP**: resolvido — sim, suporte nativo confirmado. Interactions
  API do Gemini aceita tool `type: "mcp_server"` apontando direto para o endpoint `streamable-http`
  (este projeto já usa `streamable-http`, compatível — SSE puro não funciona, mas não é o nosso caso).
  Alternativa equivalente: SDK `google-genai` passando um client FastMCP. Caveats: ainda não funciona
  com Gemini 3 — usar `gemini-2.5-flash`; e no caminho SDK o Gemini só acessa tools (não
  resources/prompts). Ver seção "Gemini" no README para o snippet completo.
- ~~[ ] **Implementar adaptador se necessário**~~ — decidido: não necessário. O server já fala
  `streamable-http` nativamente; o Gemini consome direto via `mcp_server`, sem bridge/proxy.
- [ ] **Testar end-to-end**: falta só rodar — depende do server estar deployado (Fase 4.1) e de uma
  conta/API key do Gemini (ação manual do Enzo); o snippet no README já está pronto para colar.

---

## Fase 6 — Qualidade e Observabilidade

### 6.1 Testes

- [x] **Aumentar cobertura**: testes adicionados:
  - [x] `ingest.py` — slug, extract_title, convert, ingest (10 testes em `test_ingest.py`)
  - [x] Busca com caracteres especiais, strings vazias, queries muito longas (`test_server_extended.py`)
  - [ ] Concorrência — múltiplas chamadas simultâneas ao server
- [ ] **Testes de integração**: subir o server real e testar via cliente MCP (nota: `streamable-http` exige handshake `initialize` → `Mcp-Session-Id` antes de qualquer `tools/call`; ver seção "Testar via curl" no README)
- [x] **Coverage report**: `pytest-cov` configurado com threshold 70% — `make test-cov`

### 6.2 Observabilidade

- [x] **Métricas**: instrumentado via `log_event()` + decorator `_log_tool_call` em
  `server.py`, aplicado nos 6 wrappers `@mcp.tool` (não nas funções `_*_impl`, para
  não duplicar eventos quando uma tool chama outra internamente, ex: fallback de
  `semantic_search`). Cada chamada emite uma linha JSON com `tool`, `status`
  (`ok`/`error`), `latency_ms` (via `time.perf_counter()`) e metadados baratos
  (`query_len`, `limit`, `id_len` etc. — nunca query/conteúdo bruto ou API keys).
  Tracing OTEL opcional via Logfire (ver abaixo). Testado em `tests/test_observability.py`.
- [x] **Escolher stack de observabilidade**: Resolvido — logs JSON estruturados
  (sempre ligados, pesquisáveis no dashboard do Render) para começar; Logfire
  (Pydantic, OTEL-based, free tier generoso, mesmo ecossistema do FastMCP) opt-in via
  `LOGFIRE_TOKEN` para tracing de verdade com ~zero esforço, já que o FastMCP emite
  spans OTEL nativamente. Prometheus + Grafana descartado por ser trabalho de infra
  que não se paga no volume deste projeto (~100 req/dia). Ver seção "Observabilidade"
  no README.
- [ ] **Alertas**: notificar se o server cair ou se a taxa de erro subir — ainda requer
  configuração manual (fora do código), mas agora viável usando alerting nativo do
  Render (uptime/health) ou do Logfire (taxa de erro/latência) uma vez que a conta
  exista em produção.

---

## Fase 7 — Conteúdo e Evolução do Bundle

- [ ] **Ampliar o bundle**: adicionar mais documentos do projeto (atas de reunião, decisões técnicas, referências bibliográficas)
- [ ] **Playbooks adicionais**: guias para manutenção do server, troubleshooting, onboarding de novo membro
- [ ] **Versionamento do bundle**: tags git para marcar versões estáveis do knowledge base (ex: `kb-v1.0`)
- [ ] **Backup**: estratégia de backup do bundle (git já versiona, mas considerar export periódico)
- [x] **Multi-idioma**: pesquisado e decidido — manter o KB só em PT-BR, não criar versões em inglês.
  Claude/GPT respondem bem em português sobre um KB em português, e embeddings modernos são
  multilíngues — traduzir "por garantia" não agrega. O risco real é outro: o embedding default do
  ChromaDB (`all-MiniLM-L6-v2`) é English-centric e fraco em PT-BR. O lever que realmente importa é
  trocar o *modelo de embedding*, não o idioma do conteúdo — recomendação atualizada de
  `paraphrase-multilingual-MiniLM-L12-v2` para `intfloat/multilingual-e5-large` (ou `BGE-M3`), mais
  fortes em PT-BR (ver README, seção "Indexar para busca semântica"). `embeddings.py` ganhou suporte
  a prefixos `"query: "`/`"passage: "` (convenção do e5) quando esse modelo é usado. Reindexar com o
  novo modelo é ação manual do Enzo (`make index` — não `index-update`, vetores de modelos diferentes
  não são comparáveis; requer download do HuggingFace Hub e compute local).

---

## Resumo de itens que requerem pesquisa [🔍]

| # | Tema | Pergunta-chave |
|---|------|----------------|
| ~~1~~ | ~~Busca fuzzy~~ | ~~Resolvido: rapidfuzz>=3.0.0~~ |
| ~~2~~ | ~~Write via MCP~~ | ~~Resolvido: adiar — não implementar `write_concept`/`update_concept` agora; se revisitado, caminho seguro é `propose_concept` (PR/`/proposals/`, dry_run, validação OKF, backup/versionamento, rate limit, `readOnlyHint=True` nas tools de leitura). Nada implementado ainda~~ |
| ~~3~~ | ~~Vector DB~~ | ~~Resolvido: ChromaDB — zero-infra, persistente, API simples~~ |
| ~~4~~ | ~~Embeddings PT-BR~~ | ~~Resolvido: default ONNX (all-MiniLM-L6-v2); multilingual via --model~~ |
| 5 | Google Drive MCP | Existe MCP server de Google Drive pronto para reusar? |
| ~~6~~ | ~~Plataforma de deploy~~ | ~~Resolvido: Render free tier (→ Starter $7/mês se o cold start incomodar); config em `render.yaml`~~ |
| ~~7~~ | ~~CORS no FastMCP~~ | ~~Resolvido: não configurar agora — clientes reais (Claude Desktop/ChatGPT/Gemini) conectam server-side, CORS é regra de browser; snippet pronto documentado no README para se um cliente browser aparecer~~ |
| ~~8~~ | ~~Auth no FastMCP~~ | ~~Resolvido: middleware ASGI via `mcp.run(..., middleware=[Middleware(ApiKeyMiddleware)])` — API key estática, `MCP_API_KEYS`~~ |
| ~~9~~ | ~~ChatGPT Actions~~ | ~~Resolvido: não usa Action/OpenAPI — ChatGPT fala MCP nativo; conecta via Apps/Developer Mode direto no server, com `search`/`fetch` ajustados ao contrato do Deep Research~~ |
| ~~10~~ | ~~Gemini + MCP~~ | ~~Resolvido: sim, suporte nativo confirmado — Interactions API com tool `type: "mcp_server"` sobre streamable-http (ou SDK `google-genai`); usar `gemini-2.5-flash`, nome do tool em snake_case~~ |
| ~~11~~ | ~~Observabilidade~~ | ~~Resolvido: logs JSON estruturados (dashboard do Render) + tracing OTEL opt-in via Logfire; Prometheus+Grafana descartado como overkill nesta escala~~ |
| ~~12~~ | ~~Multi-idioma~~ | ~~Resolvido: manter KB só em PT-BR; o lever real é o modelo de embedding (recomendado: intfloat/multilingual-e5-large ou BGE-M3), não tradução~~ |
| ~~13~~ | ~~Pre-commit~~ | ~~Resolvido: sim, já em uso — `.pre-commit-config.yaml` (ruff + validate_okf.py), `make pre-commit-install`~~ |

---

## Ordem sugerida de execução

```
Fase 1 (robustez)     █████████░  ← só falta decidir/testar concorrência; write_concept
                                    adiado por decisão (não é lacuna, é escopo fechado)
Fase 2 (semântica)    ██████████  ✅ COMPLETA
Fase 4 (deploy + CI)  ████████░░  ← código/config/decisões todas prontas (Render, CORS,
                                    auth, pre-commit); falta CD automático + conta Render
Fase 3 (Google Drive) ████░░░░░░  ← código pronto; depende de ação humana (credentials)
Fase 5 (multi-AI)     ██████░░░░  ← ChatGPT e Gemini com decisão + docs completos; falta
                                    testar de verdade (contas/deploy — ação humana) e
                                    documentar config do Claude Desktop remoto
Fase 6 (qualidade)    ██████░░░░  ← observabilidade completa; testes de concorrência e
                                    integração real ainda faltam; alertas dependem de conta
Fase 7 (conteúdo)     ████░░░░░░  ← multi-idioma decidido (KB fica PT-BR); resto é
                                    trabalho contínuo de conteúdo, sem bloqueio técnico
```
