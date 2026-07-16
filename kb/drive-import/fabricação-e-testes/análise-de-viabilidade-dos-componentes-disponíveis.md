---
description: Importado de 'Análise de Viabilidade dos Componentes Disponíveis.docx'.
resource: drive://12BZ3LjW7XeA_KLEqv_nPYhCHj4M7wOXx
tags: []
timestamp: '2026-07-16T02:43:49Z'
title: '**Comparativo de Viabilidade Real**'
type: Conceito
---

a alternativa mais viável para um projeto acadêmico de reciclagem de filamentos FDM é uma abordagem em duas etapas:

1. **Protótipo funcional inicial:** Triturador por Tesoura Rotativa (Método 06)
2. **Versão final:** Triturador de Duplo Rotor (Método 01)

## **Análise de Viabilidade dos Componentes Disponíveis**

### **Componentes que você já possui e podem ser aproveitados**

#### **Controle e Automação**

* Arduino Mega 2560
* Arduino Uno R3
* Arduino Nano
* Sensor de corrente ACS712 (detecção de sobrecarga)
* Sensor de vibração SW-420
* Display LCD 20x4
* Relés 2 e 4 canais
* ESP32 para monitoramento remoto

#### **Fontes**

* Fonte chaveada 12V 5A
* Fontes 9V

#### **Estrutura e Prototipagem**

* Protoboards
* Jumpers
* Raspberry Pi (opcional para monitoramento)

## **Componentes Críticos que NÃO constam no inventário**

### **Para qualquer triturador motorizado**

| **Item** | **Necessidade** | **Estimativa** |
| --- | --- | --- |
| Motor com redutor alto torque | Obrigatório | R$ 250 – 800 |
| Eixo de aço 25 mm | Obrigatório | R$ 80 – 150 |
| Mancais UCP/UCF | Obrigatório | R$ 80 – 200 |
| Facas ou discos em aço | Obrigatório | R$ 300 – 1000 |
| Estrutura metálica | Obrigatório | R$ 200 – 600 |
| Acoplamentos | Obrigatório | R$ 50 – 150 |
| Botão de emergência | Recomendado | R$ 30 – 80 |

Os motores disponíveis no laboratório (NEMA, 28BYJ-48, motores DC 6V) não possuem torque suficiente para triturar PLA ou PETG.

# **Comparativo de Viabilidade Real**

| **Método** | **Viabilidade** | **Observação** |
| --- | --- | --- |
| Manual (04) | ⭐⭐⭐⭐⭐ | Pode ser construído rapidamente |
| Tesoura Rotativa (06) | ⭐⭐⭐⭐ | Melhor custo-benefício |
| Eixo Único (02) | ⭐⭐⭐ | Exige mais usinagem |
| Duplo Rotor (01) | ⭐⭐⭐ | Melhor resultado final |
| Granulador (03) | ⭐⭐ | Risco elevado |
| Martelos (05) | ⭐ | Não recomendado |

# **Melhor Solução para a Disciplina**

## **Opção A – Baixo risco (Recomendada)**

### **Triturador por Tesoura Rotativa**

Vantagens:

* Apenas 1 eixo
* Menos peças usinadas
* Menor torque necessário
* Pode utilizar discos de serra adaptados
* Menor custo

### **Tempo estimado**

| **Etapa** | **Tempo** |
| --- | --- |
| Projeto CAD | 1 semana |
| Compra de materiais | 1 semana |
| Fabricação da estrutura | 1 semana |
| Montagem mecânica | 1 semana |
| Eletrônica e Arduino | 3 dias |
| Testes | 1 semana |

**Total:** 4–6 semanas

### **Custo estimado**

R$ 700 – 1.500

## **Opção B – Melhor resultado técnico**

### **Duplo Rotor**

Vantagens:

* Padrão Precious Plastic
* Granulometria controlada
* Maior produtividade
* Excelente para futura extrusora

### **Tempo estimado**

| **Etapa** | **Tempo** |
| --- | --- |
| Projeto mecânico | 2 semanas |
| Fabrar facas | 2–3 semanas |
| Fabricação dos eixos | 1 semana |
| Estrutura | 1 semana |
| Integração eletrônica | 1 semana |
| Testes | 1–2 semanas |

**Total:** 8–10 semanas

### **Custo estimado**

R$ 1.800 – 3.500

# **Arquitetura Eletrônica Recomendada**

Utilizando os componentes já disponíveis:

Arduino Mega

│

├── ACS712

│ └── Detecta sobrecorrente

│

├── Relé

│ └── Inverte motor em atolamento

│

├── LCD 20x4

│ └── Status do sistema

│

├── Sensor de Vibração

│ └── Monitora desbalanceamento

│

└── ESP32 (opcional)

└── Telemetria Wi-Fi

# **Estimativa de Esforço da Equipe**

Para uma equipe de 4 alunos:

| **Atividade** | **Horas** |
| --- | --- |
| Projeto mecânico | 20–30 h |
| Eletrônica | 10–15 h |
| Programação Arduino | 10 h |
| Montagem | 20 h |
| Testes | 15 h |

**Total aproximado:** 75–90 horas de trabalho.

# **Conclusão**

Para o cronograma acadêmico e considerando o material já disponível, eu recomendaria:

1. **Construir primeiro um Triturador por Tesoura Rotativa (Método 06)** para validar o conceito.
2. Utilizar o **Arduino Mega + ACS712 + Relé + LCD** para implementar monitoramento e proteção.
3. Caso haja tempo e recursos após a validação, evoluir para o **Duplo Rotor (Método 01)**, reaproveitando boa parte da eletrônica.

Essa estratégia reduz o risco do projeto em cerca de 50% e aumenta significativamente a chance de entregar um protótipo funcional dentro do prazo da disciplina.