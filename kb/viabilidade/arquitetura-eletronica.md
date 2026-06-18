---
type: Conceito
title: Arquitetura eletrônica recomendada
description: Topologia de controle reaproveitando os componentes já disponíveis.
resource: drive://SDE 2026.2/Analise de Viabilidade dos Componentes Disponiveis.docx
tags: [viabilidade, eletronica, arduino]
timestamp: 2026-06-17T12:00:00Z
---

# Arquitetura eletrônica recomendada

Reaproveitando o que o grupo já tem:

- **Arduino Mega** — controlador central
- **ACS712** — detecta sobrecorrente (atolamento)
- **Relé** — inverte o motor em atolamento
- **LCD 20x4** — status do sistema
- **Sensor de vibração** — monitora desbalanceamento
- **ESP32 (opcional)** — telemetria Wi-Fi

Esta eletrônica é reaproveitável entre o protótipo e o produto final, qualquer que seja o
[método escolhido](/projeto/decisao-metodo.md).
