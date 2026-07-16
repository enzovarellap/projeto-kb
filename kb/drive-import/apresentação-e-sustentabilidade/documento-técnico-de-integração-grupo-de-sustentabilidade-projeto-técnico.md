---
description: Importado de 'Documento Técnico de Integração — Grupo de Sustentabilidade
  & Projeto Técnico.docx'.
resource: drive://1guii59kN3oH7-8qrXqcPjCgVB5qI1cprx3UCT5M6uJo
tags: []
timestamp: '2026-07-16T02:43:39Z'
title: Documento Técnico De Integração — Grupo De Sustentabilidade & Projeto Técnico
type: Conceito
---

**Documento Técnico de Integração — Grupo de Sustentabilidade & Projeto Técnico**
**Projeto:** Trituradora de Eixo Único para Resíduos de PLA e PETG

### **1. Objetivo**

Este documento apresenta a estimativa teórica do consumo de energia elétrica por quilograma de material processado (kWh/kg) e a taxa de redução de volume físico dos resíduos plásticos após o processo de moagem. Essas métricas são fundamentais para atestar a viabilidade ecológica, operacional e econômica do sistema de economia circular em ambiente laboratorial.

### **2. Eficiência Energética Teórica (Cálculo de Consumo)**

Para determinar o consumo do equipamento, partimos dos parâmetros de projeto consolidados pela equipe de Projeto Técnico (Rotor V2):

* **Torque Nominal Misto (T):** 105 Nm (faixa operacional de 90 a 120 Nm)
* **Rotação de Trabalho (N):** 40 RPM (faixa operacional de 30 a 50 RPM)

#### **Passo 2.1: Cálculo da Potência Mecânica Útil (P\_mec)**

A potência mecânica necessária diretamente no eixo do rotor para cisalhar os polímeros é dada pela relação:

$P\_{mec}=\frac{T⋅2π⋅N}{60}$

Substituindo os valores nominais adotados pelo grupo:

$P\_{mec}= \frac{105⋅2π⋅40}{60}≈ 440 W = 0,44 kW$

#### **Passo 2.2: Estimativa de Consumo da Rede Elétrica (P\_elétrica)**

Considerando que o conjunto motorredutor de corrente contínua/indução possui perdas por efeito Joule e atrito interno nas engrenagens de redução, adotamos um rendimento comercial estimado de $η = 70\% (0,70)$:

$P\_{elétrica}=\frac{P\_{mec}}{η}=\frac{0,44 kW}{0,70}≈0,63 kW$

#### **Passo 2.3: Consumo Específico por Massa (kWh/kg)**

Tomando como base de projeto a vazão média esperada de 4 kg/h (compatível com moinhos de bancada de mesma categoria):

$Consumo Específico = \frac{P\_{elétrica}}{Vazão}=\frac{0,63 kW}{4 kg/h}≈ 0,157 kWh/kg$

**Impacto de Sustentabilidade:** Considerando a tarifa média de energia elétrica industrial/comercial brasileira de R$ 0,80 por kWh, o custo energético para triturar um quilo de resíduo de impressão 3D é de aproximadamente R$ 0,13/kg, o que valida totalmente a viabilidade econômica frente ao valor do filamento reciclado (R$ 70 - R$ 110 /kg).

### **3. Redução Volumétrica dos Resíduos**

O processo de moagem altera drasticamente a densidade aparente do material (massa dividida pelo volume total ocupado, incluindo os espaços vazios).

* **Estado Inicial (Peças inteiras, suportes e falhas de impressão):** Apresentam alta porosidade e vazios estruturais.
  + *Densidade Aparente Estimada (D\_i):* $≈ 100 kg/m³$(alta variação volumétrica devido às geometrias irregulares).
* **Estado Final (*Flakes* triturados de 3 a 5 mm):** O material fragmentado se assenta de forma compacta.
  + *Densidade Aparente Estimada (D\_f):* $≈ 450 kg/m³$*.*

#### **Cálculo do Fator de Redução Volumétrica (F\_v):**

$F\_{v}=\frac{D\_{f}}{D\_{i}}=\frac{450}{100}=4,5$

**Conclusão:** O processo de trituração promove uma redução de aproximadamente 4,5 vezes no volume ocupado pelo resíduo plástico. Isso otimiza drasticamente o armazenamento no laboratório e facilita o fluxo contínuo de alimentação do funil da extrusora na etapa seguinte de reciclagem.

### **4. Justificativa Metodológica das Estimativas (Rendimento e Vazão)**

Como o projeto encontra-se em fase de modelagem computacional e detalhamento em CAD (antecedendo os testes empíricos de bancada), as variáveis de rendimento mecânico ($η$) e vazão mássica foram estabelecidas por meio de métodos de engenharia reversa e correlação com dados comerciais, garantindo segurança e confiabilidade aos cálculos preventivos:

#### **4.1. Definição do Rendimento do Motorredutor** ($η=70\%$)

O rendimento total do sistema de acionamento não é um valor absoluto calculado, mas sim uma característica intrínseca aos componentes físicos selecionados. Para esta estimativa, considerou-se:

* **Eficiência do Motor Elétrico:** Motores CC ou de indução de pequeno porte operam tipicamente com eficiência entre 80% e 90%.
* **Perdas por Transmissão e Redução:** O triturador exige reduções severas de velocidade para priorizar o torque elevado (redução por engrenagens ou rosca sem fim). Sistemas de redução mecânica compactos introduzem perdas por atrito viscoso e calor, reduzindo a eficiência do conjunto para a faixa de 65% a 75%.
* **Fator de Conservadorismo:** Adotar $η=0,70 (70\%)$ é uma prática padrão na engenharia mecânica para projetos preliminares. Isso garante uma margem de segurança segura, evitando subdimensionar a rede elétrica de alimentação do laboratório.

#### **4.2. Estabelecimento da Meta de Vazão (4kg/h)**

A capacidade de processamento (vazão) depende diretamente da geometria final da câmara de moagem, da taxa de alimentação do operador e do número de facas atuantes. Diante disso, a meta de 4kg/h foi balizada a partir de *benchmarking* técnico dos principais concorrentes de mercado na mesma categoria de potência (entre 300 W e 750 W):

* **Felfil Shredder+ (750 W):** Capacidade de processamento de até 4 kg/h.
* **Polystruder GR PRO (300 W):** Capacidade de processamento de até 5 kg/h (otimizado por algoritmo de alimentação controlada).

**Conclusão:** A meta de 4 kg/h estabelece um compromisso viável entre as dimensões compactas propostas para o nosso rotor (100 mm a 150 mm) e a taxa de consumo de resíduos esperada em um laboratório acadêmico de manufatura aditiva.