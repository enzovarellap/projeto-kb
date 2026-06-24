# projeto-kb

Base de conhecimento compartilhada em formato OKF (Open Knowledge Format), exposta via MCP server para Claude, ChatGPT e Gemini.

## Arquitetura

```
Origem (Google Drive)  →  Bundle OKF (kb/)  →  MCP server (server.py)
                                                      ↓
                                          Claude / ChatGPT / Gemini
```

- **Bundle OKF:** pasta de markdown com YAML frontmatter. Versionado neste repo.
- **MCP server:** expõe 5 tools via `streamable-http` em `127.0.0.1:8000`:
  - `search(query, limit, offset)` — busca multi-termo com relevância e normalização de acentos
  - `fetch(id)` — conceito completo com outgoing_links resolvidos
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

## Estrutura

```
projeto-kb/
├── kb/                    # bundle OKF
│   ├── index.md           # índice raiz
│   ├── log.md             # histórico de mudanças
│   ├── conceitos/         # definições e glossário
│   └── playbooks/         # guias operacionais
├── server.py              # MCP server (search, semantic_search, fetch)
├── embeddings.py          # índice semântico (ChromaDB + embeddings)
├── ingest.py              # ingestão local
├── ingest_drive.py        # integração Google Drive
├── validate_okf.py        # validador OKF
├── tests/                 # testes pytest
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
O server hoje roda localmente em `127.0.0.1:8000`. Para expor na internet:
- **FastMCP Cloud:** `fastmcp deploy server.py` (requer conta).
- **Render / Railway:** criar serviço web apontando para `python server.py`.

### ChatGPT (OAuth / Developer Mode)
Para plugar o server no ChatGPT como "Custom GPT Action":
1. Criar um GPT no ChatGPT.
2. Adicionar uma Action apontando para a URL pública do server.
3. Configurar autenticação (API Key ou OAuth).

### Embeddings / Vector DB
Implementado na Fase 2. Rode `make index` para gerar os embeddings e use `semantic_search` via MCP.
