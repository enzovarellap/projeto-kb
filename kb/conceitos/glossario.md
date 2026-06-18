---
type: Glossário
title: Glossário
description: Termos e definições usados em toda a base de conhecimento.
resource: ""
tags: [glossário, definições, vocabulário]
timestamp: 2026-06-17T12:00:00Z
---

# Glossário

Definições dos termos usados nesta KB. Para contexto geral do projeto, veja [Visão Geral](visao-geral.md).

## Termos

**OKF (Open Knowledge Format)**
: Convenção de arquivos markdown com YAML frontmatter. Campos obrigatórios: `type`, `title`, `description`, `resource`, `tags`, `timestamp`.

**Bundle OKF**
: Conjunto de arquivos `.md` conformantes com o OKF, organizados em pastas com `index.md` em cada nível.

**Conceito**
: Unidade atômica de conhecimento na KB. Identificado pelo caminho relativo sem `.md` (ex.: `conceitos/visao-geral`).

**MCP (Model Context Protocol)**
: Protocolo aberto para expor ferramentas e contexto a IAs. O server deste projeto expõe as tools `search` e `fetch`.

**`search`**
: Tool MCP que localiza conceitos por palavra-chave em título, descrição, tags e corpo. Retorna `{id, type, title, description}`.

**`fetch`**
: Tool MCP que retorna o conceito completo pelo `id`, incluindo `outgoing_links` — lista de ids dos conceitos referenciados no corpo.

**`outgoing_links`**
: Links de saída de um conceito para outros conceitos da KB. Permitem à IA navegar o grafo de conhecimento.

**Ingestão**
: Processo de converter arquivos externos (PDF, DOCX, etc.) em conceitos OKF via `ingest.py`. Deve ser idempotente.

**Idempotência**
: Propriedade de uma operação que, ao ser executada múltiplas vezes com os mesmos inputs, produz sempre o mesmo resultado sem efeitos colaterais acumulados.
