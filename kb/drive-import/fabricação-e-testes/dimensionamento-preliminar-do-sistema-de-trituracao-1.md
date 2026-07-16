---
description: Importado de 'DIMENSIONAMENTO PRELIMINAR DO SISTEMA DE TRITURACAO (1).docx'.
resource: drive://15fmPRSLUhze7mQjWotmOi8IbuiKNUGu2
tags: []
timestamp: '2026-07-16T02:43:49Z'
title: '**DIMENSIONAMENTO PRELIMINAR DO SISTEMA DE TRITURAÇÃO DE RESÍDUOS DE IMPRESSÃO
  3D**'
type: Conceito
---

# **DIMENSIONAMENTO PRELIMINAR DO SISTEMA DE TRITURAÇÃO DE RESÍDUOS DE IMPRESSÃO 3D**

## **Descrição do Sistema**

O sistema de reciclagem de resíduos provenientes de manufatura aditiva foi projetado para promover a reutilização de materiais termoplásticos, especialmente PLA (Ácido Polilático) e PETG (Polietileno Tereftalato Glicol), amplamente utilizados em impressoras 3D. Conforme apresentado por Cytrynbaum (2022), a etapa de trituração possui papel fundamental na preparação da matéria-prima para o processo posterior de extrusão e fabricação de novos filamentos.

O equipamento proposto é constituído por um triturador de eixo único acionado por motor elétrico com redução mecânica de velocidade, associado a um sistema eletrônico de monitoramento e controle baseado em microcontrolador Arduino.

## **Componentes do Sistema**

### **Subsistema Mecânico**

O conjunto mecânico é composto pelos seguintes elementos:

* Funil de alimentação;
* Eixo principal de trituração;
* Facas móveis;
* Contra-facas fixas;
* Mancais de apoio;
* Redutor de velocidade;
* Motor elétrico;
* Estrutura metálica de sustentação;
* Caixa coletora para armazenamento do material triturado.

### **Subsistema Eletrônico**

O sistema eletrônico é responsável pelo monitoramento operacional e proteção do equipamento, sendo constituído pelos seguintes componentes:

| **Componente** | **Função** |
| --- | --- |
| Arduino Uno | Controle e processamento dos sinais |
| ACS712 | Medição da corrente elétrica do motor |
| Módulo Relé 5 V | Acionamento do motor |
| Display LCD 16x2 I2C | Exibição de informações operacionais |
| Fonte 5 V | Alimentação dos circuitos eletrônicos |
| Botão de Emergência | Interrupção imediata da operação |
| LEDs Indicadores | Sinalização do estado do sistema |

## **Arquitetura de Controle**

O sistema de monitoramento foi desenvolvido utilizando um microcontrolador Arduino Uno. O sensor ACS712 realiza a medição da corrente consumida pelo motor, permitindo identificar condições de sobrecarga ou travamento do triturador. As informações são apresentadas em um display LCD, enquanto o acionamento do motor é realizado por intermédio de um módulo relé.

O fluxo operacional do sistema pode ser representado conforme descrito a seguir:

Motor Elétrico → Triturador → Material Triturado

Motor Elétrico → Sensor ACS712 → Arduino Uno → LCD

Arduino Uno → Relé → Acionamento do Motor

Arduino Uno → Sistema de Segurança

![](data:image/png;base64...)

## **Levantamento das Propriedades Mecânicas dos Materiais**

Para o dimensionamento preliminar do triturador foram consideradas propriedades mecânicas típicas dos polímeros utilizados em impressão 3D.

### **PLA**

| **Propriedade** | **Valor Médio** |
| --- | --- |
| Resistência à Tração | 50 a 65 MPa |
| Resistência ao Cisalhamento | 30 a 40 MPa |
| Densidade | 1,24 g/cm³ |

Para os cálculos foi adotada resistência ao cisalhamento de:

τPLA = 35 MPa

### **PETG**

| **Propriedade** | **Valor Médio** |
| --- | --- |
| Resistência à Tração | 45 a 55 MPa |
| Resistência ao Cisalhamento | 25 a 35 MPa |
| Densidade | 1,27 g/cm³ |

Para os cálculos foi adotada resistência ao cisalhamento de:

τPETG = 30 MPa

## **Cálculo da Força de Cisalhamento**

Considerou-se uma seção típica de material submetida ao corte pelas facas do triturador.

Espessura do material:

e = 3 mm

Largura da região de corte:

b = 10 mm

A área submetida ao cisalhamento é determinada por:

A = e × b

A = 3 × 10

A = 30 mm²

Convertendo para o Sistema Internacional:

A = 3 × 10⁻⁵ m²

A força de cisalhamento pode ser calculada pela Equação:

F = τ × A

### **Força de Cisalhamento para PLA**

FPLA = 35 × 10⁶ × 3 × 10⁻⁵

FPLA = 1050 N

### **Força de Cisalhamento para PETG**

FPETG = 30 × 10⁶ × 3 × 10⁻⁵

FPETG = 900 N

## **Cálculo do Torque Motriz**

Para o cálculo do torque foi considerado um raio efetivo de atuação da faca igual a:

r = 40 mm = 0,04 m

O torque é determinado por:

T = F × r

### **Torque para PLA**

TPLA = 1050 × 0,04

TPLA = 42 N·m

### **Torque para PETG**

TPETG = 900 × 0,04

TPETG = 36 N·m

## **Fator de Segurança**

Devido às cargas dinâmicas e aos impactos característicos do processo de trituração, foi adotado fator de segurança igual a 2.

FS = 2

Assim, obtém-se:

### **Torque de Projeto para PLA**

Tproj = 42 × 2

Tproj = 84 N·m

### **Torque de Projeto para PETG**

Tproj = 36 × 2

Tproj = 72 N·m

## **Seleção do Conjunto Motor-Redutor**

Com base nos resultados obtidos, recomenda-se a utilização de um conjunto motor-redutor capaz de fornecer torque superior a 84 N·m.

As especificações preliminares são:

* Motor elétrico de 1 CV (746 W);
* Rotação nominal de 1750 rpm;
* Redutor de velocidade com relação de transmissão entre 1:40 e 1:50;
* Velocidade de saída entre 35 e 50 rpm;
* Torque disponível entre 90 e 120 N·m.

Essas características fornecem margem operacional suficiente para o processamento de resíduos de PLA e PETG provenientes de suportes, peças rejeitadas e falhas de impressão, garantindo desempenho adequado e segurança durante a operação.

![](data:image/png;base64...)

## **Referência Bibliográfica**

CYTRYNBAUM, Natan. Sistema de reciclagem de resíduos provenientes de manufatura aditiva visando produção de filamentos destinados à impressão 3D. Trabalho de Conclusão de Curso. Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ), Rio de Janeiro, 2022.

https://repositorio.utfpr.edu.br/jspui/bitstream/1/32149/1/projetotrituradorpolimerosutfpr.pdf

Imagens

![](data:image/png;base64...)

![](data:image/png;base64...)

![](data:image/png;base64...)