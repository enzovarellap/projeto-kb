---
type: Conceito
title: Visão Geral
description: O que é este projeto, seus objetivos e a arquitetura de três camadas da KB.
resource: ""
tags: [contexto, escopo, arquitetura]
timestamp: 2026-06-17T12:00:00Z
---

# Visão Geral

Este projeto monta uma **fonte única de contexto** consumida por múltiplas IAs
(Claude, ChatGPT, Gemini), cada uma na interface preferida de cada pessoa.

## Objetivos

- Eliminar fragmentação de conhecimento espalhado em múltiplos documentos.
- Permitir que qualquer IA acesse o contexto via um protocolo padrão (MCP).
- Manter o conteúdo versionado e auditável em formato aberto (OKF).

## Arquitetura

A KB tem três camadas:

| Camada | O que é | Responsável |
|--------|---------|-------------|
| **Origem** | Documentos no Google Drive (read-only, legado) | Humano |
| **Canônica** | Bundle OKF — pasta de markdown com frontmatter | Este repositório |
| **Transporte** | MCP server `search`/`fetch` plugável em IAs | `server.py` |

## Princípios de design

- **Navegação-primeiro, sem embeddings:** retrieval por palavra-chave + grafo de links. Vetores são fase futura.
- **Idempotência:** reprocessar os mesmos arquivos não duplica conceitos.
- **Conteúdo em PT-BR.**

Para os termos usados aqui, veja o [glossário](glossario.md).
Para adicionar novos documentos, veja o [playbook de ingestão](../playbooks/como-adicionar-doc.md).
