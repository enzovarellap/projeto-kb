---
description: Importado de 'MATRIZ DE TESTES E VALIDAÇÃO.docx'.
resource: drive://1cSYBR3ftaZN0To-EcveDevJek-Z4TrCX
tags: []
timestamp: '2026-07-16T02:43:49Z'
title: '**DIMENSIONAMENTO PRELIMINAR DO SISTEMA DE TRITURAÇÃO DE RESÍDUOS DE IMPRESSÃO
  3D**'
type: Conceito
---

# **DIMENSIONAMENTO PRELIMINAR DO SISTEMA DE TRITURAÇÃO DE RESÍDUOS DE IMPRESSÃO 3D**

**1. INTRODUÇÃO E ESCOPO DA VALIDAÇÃO**

**1.1 Contextualização e Justificativa dos Ensaios**

O processo de reciclagem de termoplásticos provenientes de manufatura aditiva (especialmente Ácido Polilático - PLA e Polietileno Tereftalato Glicol - PETG) impõe severas solicitações mecânicas e dinâmicas ao sistema de trituração.

Embora o dimensionamento preliminar forneça uma base analítica sólida através do cálculo estático de cisalhamento, a natureza caótica dos resíduos de impressão 3D — caracterizada por preenchimentos variados (*infills*), suportes e peças maciças rejeitadas — gera picos de carga mecânica e flutuações de torque que não são integralmente capturadas em modelos teóricos puros.

Dessa forma, a fase de testes e ensaios experimentais torna-se indispensável para mitigar riscos de falha estrutural, validar a viabilidade do conjunto motor-redutor selecionado e garantir a confiabilidade dos sistemas eletrônicos de proteção ativa.

**1.2 Objetivos do Programa de Testes**

O plano de ensaios estruturado neste documento tem como objetivos principais:

* **Validação Empírica de Torque:** Verificar se o torque disponível no conjunto motorredutor (entre 90 e 120 N/m) atende com margem de segurança o regime dinâmico de trituração do PLA e do PETG em condições reais de operação.
* **Calibração do Subsistema Eletrônico:** Mapear as curvas de corrente do motor por meio do sensor ACS712 para parametrizar logicamente o limiar de corte (*overcurrent*) no arduino.
* **Avaliação de Segurança:** Garantir a eficiência do tempo de resposta do sistema de interrupção imediata (Módulo Relé e Botão de Emergência) sob condições severas de carga.
* **Homogeneidade do Produto:** Avaliar a granulometria do material triturado resultante para assegurar sua compatibilidade com o processo subsequente de extrusão de novos filamentos.

**1.3 Limites do Sistema e Premissas de Projeto**

Para efeito de planejamento e execução dos testes de bancada, são adotadas as seguintes premissas e limites estabelecidos na memória de cálculo preliminar:

|  |  |  |
| --- | --- | --- |
| **Parâmetro Mecânico / Eletrônico** | **Valor de Referência (Teórico)** | **Aplicação no Ensaio** |
| **Seção Máxima de Corte** | 3 mm (espessura) × 10 mm (largura) | Geometria padrão dos corpos de prova iniciais |
| **Torque de Projeto Mínimo** | 84 N/m (PLA) / 72 N/m (PETG) | Limite inferior para validação de torque em operação |
| **Rotação do Eixo Principal** | 35 a 50 rpm | Faixa de velocidade síncrona a ser monitorada |
| **Tensão de Operação de Controle** | 5 Vcc (Barramento Arduino) | Tensão nominal para sensores, relé e displays |

**2. METODOLOGIA E PROTOCOLOS DE ENSAIO**

Este capítulo define as diretrizes práticas, o arranjo experimental e os procedimentos passo a passo para a execução dos testes em bancada.

**2.1 Arranjo Experimental e Instrumentação**

Para a execução dos ensaios, o protótipo do triturador deve ser instrumentado conforme a arquitetura de controle estabelecida. O diagrama de conexões deve garantir a aquisição de dados em tempo real e a segurança dos operadores.

* **Aquisição de Corrente:** O sensor de efeito Hall ACS712 deve ser intercalado em série com uma das fases de alimentação do motor elétrico. O sinal analógico de saída deve ser conectado a uma porta analógica do Arduino Uno (ex: A0).
* **Interface Visual:** O Display LCD 16x2 I2C deve ser configurado para exibir continuamente a corrente instantânea ***A*** e o status do sistema (Operacional / Sobrecarga / Emergência).
* **Corte de Potência:** O Módulo Relé de 5 V deve atuar diretamente sobre a contatora ou circuito de acionamento do motor elétrico.

**2. METODOLOGIA E PROTOCOLOS DE ENSAIO**

Este capítulo define as diretrizes práticas, o arranjo experimental e os procedimentos passo a passo para a execução dos testes em bancada.

**2.1 Arranjo Experimental e Instrumentação**

Para a execução dos ensaios, o protótipo do triturador deve ser instrumentado conforme a arquitetura de controle estabelecida. O diagrama de conexões deve garantir a aquisição de dados em tempo real e a segurança dos operadores.

* **Aquisição de Corrente:** O sensor de efeito Hall ACS712 deve ser intercalado em série com uma das fases de alimentação do motor elétrico. O sinal analógico de saída deve ser conectado a uma porta analógica do Arduino Uno (ex: A0).
* **Interface Visual:** O Display LCD 16x2 I2C deve ser configurado para exibir continuamente a corrente instantânea ***A*** e o status do sistema (Operacional / Sobrecarga / Emergência).
* **Corte de Potência:** O Módulo Relé de 5 V deve atuar diretamente sobre a contatora ou circuito de acionamento do motor elétrico.

**2.2 Protocolos Operacionais Específicos**

**Protocolo P-01: Mapeamento de Corrente em Vazio e Carga Nominal (Validação dos Testes T-01 e T-02)**

1. Certificar-se de que a câmara de trituração está completamente limpa e livre de resíduos.
2. Energizar o subsistema eletrônico (Fonte 5 V) e inicializar o Arduino Uno.
3. Acionar o motor elétrico e registrar a corrente de partida (surto) e a corrente em regime permanente em vazio ***Ivazio*** por 2 minutos.
4. Introduzir sequencialmente 10 corpos de prova padronizados de PLA com seção de 3x10mm.
5. Repetir o passo anterior utilizando corpos de prova de PETG com a mesma seção.
6. Registrar os picos de corrente gerados durante o cisalhamento de cada amostra através do monitor serial.

**Protocolo P-02: Calibração de Proteção contra Travamento (Validação do Teste T-05)**

1. Carregar no Arduino o código de monitoramento com uma rotina de interrupção por sobrecorrente.
2. Alimentar o funil com um bloco maciço de sacrifício (espessura > 10mm), projetado para exceder a força de cisalhamento limite (1050N) e travar o eixo principal.
3. Iniciar a operação do motor.
4. Monitorar a curva de elevação da corrente. O software deve ser ajustado para que, assim que a corrente ultrapasse o limiar estipulado **(Ilimiar)**, o pino do Arduino conectado ao relé mude para nível lógico baixo (LOW), desativando o motor.
5. Medir o tempo decorrido entre o travamento mecânico e a abertura do relé (critério de sucesso: < 500ms).

**Protocolo P-03: Ensaio de Fadiga Térmica e Regime Contínuo (Validação do Teste T-07)**

1. Posicionar um termopar ou termômetro infravermelho apontado para a parede interna da câmara de moagem, próximo às contra-facas fixas.
2. Ligar o sistema e alimentar o funil continuamente com resíduos caóticos de impressão 3D a uma taxa constante de alimentação (ex: 200g a cada 5 minutos).
3. A cada 10 minutos, registrar:
   * A temperatura da câmara de moagem (°C).
   * A temperatura na carcaça do motor elétrico (°C).
   * A corrente média de operação ***A.***
4. Encerrar o teste após 60 minutos ou imediatamente se a temperatura da câmara atingir 45°C.

**2.3 Coleta de Dados e Tratamento Estatístico**

Todas as leituras de corrente coletadas via monitor serial do Arduino devem ser exportadas para planilhas (em formato .csv) para posterior tratamento de dados. Devem ser calculados:

* A média aritmética dos picos de corrente para cada material (PLA e PETG).
* O desvio padrão para avaliar a estabilidade do torque do motor-redutor diante de diferentes geometrias de resíduos.

**3. RESULTADOS ESPERADOS E CRITÉRIOS DE ACEITAÇÃO**

A análise dos resultados obtidos nos ensaios permitirá correlacionar as equações matemáticas do dimensionamento preliminar com o comportamento físico e dinâmico do protótipo. Espera-se que o torque disponível no conjunto motor-redutor absorva com folga os picos de impacto gerados pelo corte dos polímeros. Para que o sistema seja considerado aprovado e apto para a operação segura, os dados coletados na bancada de testes devem atender estritamente aos seguintes critérios de aceitação:

**3.1 Desempenho Mecânico e Demandas de Torque**

Durante a trituração dos corpos de prova padronizados de 3x10mm, o torque real exigido não deve, em hipótese alguma, ultrapassar o limite estipulado com o fator de segurança FS=2, que é de 84 N/M para o PLA e 72 N/M para o PETG.

* **Consumo de Corrente:** Traduzindo isso para a parte elétrica, a corrente lida pelo sensor ACS712 durante o corte nominal deve se manter próxima à corrente de trabalho do motor de 1 CV, sem atingir a corrente de pico de travamento.
* **Estabilidade de Rotação:** O redutor mecânico deve manter a velocidade do eixo principal de trituração estavelmente dentro da faixa de35 a 50 RPM. Ruídos excessivos, vibrações fora do comum na estrutura metálica de sustentação ou quedas drásticas de rotação serão critérios para reprovação mecânica imediata.

**3.2 Confiabilidade do Sistema de Proteção Eletrônica**

O subsistema eletrônico baseado no Arduino Uno deve atuar como uma mente ágil para proteger o hardware mecânico. Espera-se que a calibração do sensor ACS712 seja precisa o suficiente para diferenciar um pequeno esforço momentâneo de um travamento real do eixo.

* **Tempo de Desarme (Sobrecarga):** No teste de travamento forçado, o comando de corte enviado ao Módulo Relé de 5V deve interromper a alimentação do motor em no máximo 500 ms. Qualquer atraso superior a esse tempo coloca em risco os enrolamentos do motor e a integridade das facas.
* **Eficácia da Parada de Emergência:** Ao pressionar o Botão de Emergência, o display LCD deve atualizar instantaneamente seu status e o motor deve parar de girar quase imediatamente, garantindo que o operador esteja seguro contra acidentes na zona de alimentação.

**3.3 Qualidade do Material Processado (Output)**

Como o objetivo final do triturador é alimentar uma extrusora para fabricar novos filamentos, a geometria do material que cai na caixa coletora é um critério de sucesso crucial.

* **Granulometria:** Espera-se obter *flakes* (pedacinhos) relativamente homogêneos. O critério de aceitação define que, após o peneiramento, pelo menos 80% do lote testado deve apresentar dimensões entre 2 mm e 5 mm. Grãos maiores do que isso indicam que a folga entre as facas móveis e contra-facas fixas está muito grande, exigindo ajuste mecânico no eixo.

**4. CRONOGRAMA E GESTÃO DOS ENSAIOS**

Para garantir a segurança dos membros da equipe de testes e a integridade dos equipamentos, a execução dos ensaios seguirá uma ordem cronológica rigorosa de complexidade ascendente. Nenhum teste com carga real de material será realizado antes que os sistemas de segurança eletrônica estejam completamente validados e operacionais.

**4.1 Fases de Execução do Cronograma**

O plano de testes será dividido em três fases lógicas sequenciais, distribuídas ao longo das semanas de desenvolvimento do protótipo:

* **Fase 1: Homologação em Vazio e Segurança (Semana 1):** Esta fase compreende o teste de corrente em vazio e o de funcionamento do botão de emergência. O objetivo é garantir que o motor gire livremente e que o módulo relé corte a potência de forma imediata.
* **Fase 2: Calibração Eletrônica e Sobrecarga (Semana 2):** Focada na simulação de travamento do eixo. Aqui, a equipe irá calibrar o sensor ACS712 e programar o Arduino Uno para desarmar o sistema antes que o motor atinja sua corrente crítica de curto-circuito.
* **Fase 3: Ensaios de Carga, Granulometria e Regime Contínuo (Semana 3):** Com a segurança eletrônica validada, serão realizados os testes processando amostras reais de PLA e PETG para avaliar o torque, o desgaste inicial das facas e o aquecimento da câmara.

**4.2 Matriz de Responsabilidades da Equipe**

A operação dos testes exige a divisão clara de funções na bancada para evitar acidentes e garantir a confiabilidade dos dados coletados. As funções serão distribuídas da seguinte forma:

* **Operador de Alimentação:** Responsável por introduzir os corpos de prova e resíduos de impressão 3D no funil de forma controlada, vestindo todos os EPIs necessários, como óculos de proteção, luvas e protetor auricular.
* **Monitor de Instrumentação:** Responsável por acompanhar o monitor serial do Arduino, registrar os picos de corrente lidos pelo ACS712 e aferir as temperaturas da carcaça do motor e dos mancais com o termômetro infravermelho.
* **Fiscal de Segurança:** Membro posicionado estrategicamente com controle exclusivo sobre o Botão de Emergência, encarregado de interromper o ensaio imediatamente ao menor sinal de fumaça, travamento sem desarme automático ou vibração estrutural excessiva.

**4.3 Liberação do Equipamento (Sign-off)**

Após a conclusão de todas as fases e o preenchimento dos relatórios de ensaio, o triturador só será considerado "Homologado" se apresentar 100% de sucesso nos critérios de aceitação eletrônica e mecânica. Caso ocorra alguma falha, os testes serão suspensos e o protótipo retornará para as equipes de projeto mecânico ou de software para as devidas correções.