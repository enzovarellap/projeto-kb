---
type: Playbook
title: Como Adicionar Documentos à KB
description: Passo a passo para converter arquivos externos em conceitos OKF usando ingest.py.
resource: ""
tags: [ingestão, fluxo, onboarding]
timestamp: 2026-06-17T12:00:00Z
---

# Como Adicionar Documentos à KB

Este playbook descreve como converter arquivos externos em conceitos OKF.
Para entender a estrutura do projeto, veja [Visão Geral](../conceitos/visao-geral.md).
Para os termos usados aqui, veja o [Glossário](../conceitos/glossario.md).

## Pré-requisitos

- Python 3.11+ instalado.
- Dependências instaladas: `make install`.
- Arquivos a ingerir baixados localmente (PDF, DOCX, MD, TXT, PPTX, CSV).

## Passo a passo

### 1. Coloque os arquivos numa pasta

```bash
mkdir exemplos/meu-lote
cp meu-documento.pdf exemplos/meu-lote/
```

### 2. Execute a ingestão

```bash
make ingest SRC=exemplos/meu-lote OUT=kb/importados
# ou diretamente:
python ingest.py --src exemplos/meu-lote --out kb/importados --type Conceito
```

O script:
- Converte cada arquivo para markdown com **markitdown**.
- Gera um conceito OKF com frontmatter completo.
- Preenche `resource` com o caminho do arquivo de origem.
- Atualiza `kb/importados/index.md` automaticamente.
- É **idempotente**: rodar de novo atualiza, não duplica.

### 3. Valide o resultado

```bash
make validate
```

Qualquer problema de conformidade com o OKF é listado com mensagem clara.

### 4. Rode os testes

```bash
make test
```

### 5. Commit

```bash
git add kb/
git commit -m "ingest: adiciona lote meu-lote"
```

## Pendências humanas (🛑)

- **Google Drive:** a ingestão hoje opera sobre pasta local. Autenticação com Drive API requer credenciais do Enzo — documentado como extensão futura.
- **Deploy do MCP server:** requer conta no FastMCP Cloud / Render — a ser feito pelo Enzo.
