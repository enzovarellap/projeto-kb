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
- [ ] **Dockerfile**: criar imagem Docker para o server
- [ ] **Variáveis de ambiente**: externalizar `HOST`, `PORT`, `KB_PATH` para configuração via env vars
- [ ] **Health check**: adicionar endpoint `/health` para monitoramento da plataforma
- [ ] **CORS**: configurar CORS se necessário para acesso de clientes web `[🔍 verificar se fastmcp já lida com isso]`

### 4.2 CI/CD

- [ ] **GitHub Actions — CI**: workflow que roda em cada push:
  - [ ] `make validate` (validar bundle OKF)
  - [ ] `make test` (rodar pytest)
  - [ ] Lint com `ruff` ou `flake8`
- [ ] **GitHub Actions — CD**: deploy automático ao fazer push na branch principal
- [ ] **Pre-commit hooks**: `ruff check`, `validate_okf.py` antes de cada commit `[🔍 avaliar usar pre-commit framework]`

### 4.3 Segurança

- [ ] **Autenticação do MCP server**: adicionar API key ou token Bearer para proteger o acesso `[🔍 pesquisar como FastMCP lida com autenticação — middleware? decorator?]`
- [ ] **Rate limiting**: limitar chamadas por minuto para evitar abuso
- [ ] **HTTPS**: garantir que o deploy use TLS (geralmente resolvido pela plataforma)
- [ ] **Secrets management**: credenciais do Drive e API keys em variáveis de ambiente, não no código
- [ ] **`.env` + `.env.example`**: template de variáveis de ambiente necessárias

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
- [ ] **Testes de integração**: subir o server real e testar via cliente MCP
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
| 13 | Pre-commit | Vale usar o framework `pre-commit` para hooks? |

---

## Ordem sugerida de execução

```
Fase 1 (robustez)     ████████░░  ← próxima — melhora o que já existe
Fase 2 (semântica)    ██████████  ✅ COMPLETA
Fase 4 (deploy + CI)  ██████░░░░  ← habilita fases 3 e 5
Fase 3 (Google Drive) ████░░░░░░  ← depende de ação humana (credentials)
Fase 5 (multi-AI)     ████░░░░░░  ← depende do deploy (fase 4)
Fase 6 (qualidade)    ███░░░░░░░  ← contínua, em paralelo
Fase 7 (conteúdo)     ███░░░░░░░  ← contínua, em paralelo
```
