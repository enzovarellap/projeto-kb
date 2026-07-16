---
description: Importado de '2.1 - Dimensionamento do Rotor - Triturador de Eixo Único
  V2 - Dimensionamento do Rotor - Triturador de Eixo Único V2.pdf'.
resource: drive://1bBDsex7NFc1Etl8hSMxIoYKB0NPSFG1T
tags: []
timestamp: '2026-07-16T02:44:17Z'
title: 2.1   Dimensionamento Do Rotor   Triturador De Eixo Único V2   Dimensionamento
  Do Rotor   Triturador De Eixo Único V2
type: Conceito
---

| Relatório: |             | Dimensionamento |            |          |               | do  | Rotor |
| ---------- | ----------- | --------------- | ---------- | -------- | ------------- | --- | ----- |
| para       | Triturador  |                 | de         | Eixo     | Único         | V2  |       |
| Projeto:   | Trituradora | de Eixo         | Único para | Resíduos | de PLA e PETG |     |       |
Objetivo: Dimensionamento detalhado do rotor principal, justificação do material de usinagem,
definição da arquitetura de corte helicoidal e integração do sistema de controle.
| 1. Introdução |     | e   | Escopo | do  | Projeto |     |     |
| ------------- | --- | --- | ------ | --- | ------- | --- | --- |
Este documento consolida os parâmetros de engenharia referentes ao dimensionamento do
rotor principal para o desenvolvimento do Módulo de Trituração de resíduos de impressão 3D
(PLA e PETG). O objetivo é fornecer justificativas técnicas robustas para a construção de um
equipamento de bancada focado em ambientes acadêmicos e laboratoriais. A abordagem
interdisciplinar exigida na concepção de máquinas modernas, aliando mecânica de precisão a
sistemas de controle inteligente, vai ao encontro direto dos princípios de uma formação sólida
em Ciência e Tecnologia, garantindo não apenas o processamento do material, mas a coleta e
| análise            | de dados | operacionais | para otimização. |     |          |        |      |
| ------------------ | -------- | ------------ | ---------------- | --- | -------- | ------ | ---- |
| 2. Dimensionamento |          |              | Físico:          |     | Diâmetro | de 100 | mm a |
150 mm
A especificação do diâmetro externo do rotor na faixa de 100 mm a 150 mm atende
perfeitamente aos requisitos de um equipamento compacto, estabelecendo uma proporção
segura entre o tamanho da estrutura e a capacidade de engajamento da matéria-prima. Este
| diâmetro | otimizado | assegura: |     |     |     |     |     |
| -------- | --------- | --------- | --- | --- | --- | --- | --- |
● Relação Torque-Velocidade: Operando em baixas rotações (em torno de 30 a 50 RPM),
esse diâmetro preserva uma velocidade tangencial que minimiza a elevação térmica. O
controle estrito do calor friccional é indispensável para evitar a plastificação e o
derretimento crônico do PLA dentro da câmara de corte, considerando seu baixo ponto
| de  | transição | vítrea (cerca | de 60°C). |     |     |     |     |
| --- | --------- | ------------- | --------- | --- | --- | --- | --- |
● Geometria da "Mordida": O raio de 50 a 75 mm a partir do centro do eixo cria um
ângulo de ataque ideal para puxar blocos sólidos de plástico e peças irregulares para o
espaço de esmagamento. Se o diâmetro fosse menor, as lâminas deslizariam sobre
| peças | maiores | sem conseguir | agarrá-las. |     |     |     |     |
| ----- | ------- | ------------- | ----------- | --- | --- | --- | --- |

● Dimensionamento dos Mancais: Um rotor contido nesta faixa permite a utilização de
mancais flangeados de linhas comerciais padrão, reduzindo o custo total de montagem e
|     | facilitando | a manutenção |          | preventiva. |       |     |     |      |     |
| --- | ----------- | ------------ | -------- | ----------- | ----- | --- | --- | ---- | --- |
| 3.  | Seleção     | de           | Material |             | Base: | Aço | SAE | 4140 |     |
O processamento de polímeros tenazes como o PETG exige torques consideráveis
(frequentemente entre 90 Nm e 120 Nm em escala laboratorial). Por isso, a definição de um
eixo usinado em Aço SAE 4140 é um diferencial crítico para o projeto:
● Resistência Estrutural Elevada: O SAE 4140 é um aço baixa-liga de alta resistência e
temperabilidade. Ele proporciona uma tenacidade superior a aços carbono comuns
(como o SAE 1045), o que previne a deflexão (envergamento) do eixo e a torção sob
|     | cargas | extremas | de impacto | contínuo. |     |     |     |     |     |
| --- | ------ | -------- | ---------- | --------- | --- | --- | --- | --- | --- |
● Vida Útil Sob Fadiga: Ao trabalhar com trituração, o eixo está sujeito a ciclos repetitivos
de carga e alívio a cada corte. O tratamento térmico do aço 4140 assegura baixíssimo
índice de desgaste e falha por fadiga, garantindo que as facas mantenham o fio e a
integridade geométrica por muito mais tempo, evitando manutenções corretivas
excessivas.
| 4.  | Arranjo | do  | Mecanismo |     |     | de Corte: | Facas |     | em Espiral |
| --- | ------- | --- | --------- | --- | --- | --------- | ----- | --- | ---------- |
(Helicoidal)
O modelo de triturador adota o princípio de cisalhamento entre lâminas rotativas e facas de
estator. A distribuição dessas lâminas móveis deve, obrigatoriamente, seguir um arranjo em
| espiral. | Os ganhos |     | mecânicos | desta | arquitetura | incluem: |     |     |     |
| -------- | --------- | --- | --------- | ----- | ----------- | -------- | --- | --- | --- |
● Suavização do Perfil de Carga: A disposição defasada assegura que as lâminas entrem
em contato com o material de forma sequencial, reduzindo os picos de carga. Se todas
as facas cortassem ao mesmo tempo, o motor sofreria picos de corrente extremos,
|     | elevando | o risco | de queda | do  | disjuntor | ou queima | do estator. |     |     |
| --- | -------- | ------- | -------- | --- | --------- | --------- | ----------- | --- | --- |
● Prevenção de Travamentos (Jamming): O corte distribuído fraciona a energia
necessária, dificultando que um bloco plástico mais rígido pare o eixo. Além de preservar
o motor, isso prolonga significativamente a vida útil da caixa redutora planetária e das
|     | correias/correntes |     | de  | transmissão. |     |     |     |     |     |
| --- | ------------------ | --- | --- | ------------ | --- | --- | --- | --- | --- |
● Fluxo Granulométrico: A geometria helicoidal atua de forma similar a uma rosca
transportadora, empurrando gradualmente as partículas sobre a malha metálica inferior
(peneira de ~5 mm). Isso acelera a evasão de flocos no tamanho correto e minimiza a

|     | fricção    | prolongada | que geraria  | pós | ou aerossóis |     | plásticos. |          |     |
| --- | ---------- | ---------- | ------------ | --- | ------------ | --- | ---------- | -------- | --- |
| 5.  | Integração |            | de Automação |     |              | e   | Análise    | de Dados |     |
Para elevar o rigor tecnológico do protótipo e evitar falhas operacionais críticas, a gestão
inteligente do motorredutor é recomendada. O acompanhamento contínuo da operação
| fornecerá | indicadores |     | vitais sobre | o desempenho |     | da  | máquina: |     |     |
| --------- | ----------- | --- | ------------ | ------------ | --- | --- | -------- | --- | --- |
● Sensoriamento de Corrente: A instalação de módulos sensores permite detectar
imediatamente os picos anômalos de corrente quando o rotor encontra uma obstrução
maciça.
● Lógica de Reversão: Essa variação de corrente aciona automaticamente relés para
reverter a rotação do motor por alguns segundos, reposicionando o resíduo plástico
|     | antes | de retomar | o ciclo | de avanço. |     |     |     |     |     |
| --- | ----- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- |
● Construção de Indicadores: O registro desses eventos de travamento e consumo
elétrico permite construir indicadores de performance. Um programa simples em Python
iterando sobre esses dados, por exemplo, pode gerar alertas visuais sobre a eficiência
térmica ou alertar quando as lâminas começarem a perder o fio com base na exigência
|            | do motorredutor |     | ao longo       | do tempo.     |     |          |     |               |     |
| ---------- | --------------- | --- | -------------- | ------------- | --- | -------- | --- | ------------- | --- |
| 6.         | Síntese         |     | dos Parâmetros |               |     | Técnicos |     | Exigidos      |     |
| Componente |                 |     |                | Especificação |     |          |     | Justificativa | de  |
Engenharia
| Diâmetro |     | do Rotor |     | 100 mm | a 150 | mm  |     | Maximiza   | o ângulo de   |
| -------- | --- | -------- | --- | ------ | ----- | --- | --- | ---------- | ------------- |
|          |     |          |     |        |       |     |     | ataque e   | mantém a      |
|          |     |          |     |        |       |     |     | velocidade | periférica    |
|          |     |          |     |        |       |     |     | reduzida,  | controlando a |
temperatura.
Material Estrutural Aço SAE 4140 Temperado Suporta torques altíssimos
|     |     |     |     |     |     |     |     | e impactos  | cíclicos,   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- |
|     |     |     |     |     |     |     |     | oferecendo  | excepcional |
|     |     |     |     |     |     |     |     | resistência | à fadiga    |

| Componente |     | Especificação | Justificativa | de  |     |
| ---------- | --- | ------------- | ------------- | --- | --- |
Engenharia
mecânica.
| Padrão das | Lâminas | Arranjo Helicoidal | Evita sobrecarga      |              |     |
| ---------- | ------- | ------------------ | --------------------- | ------------ | --- |
|            |         |                    | simultânea,           | distribuindo | o   |
|            |         |                    | corte sequencialmente |              | e   |
|            |         |                    | reduzindo             | vibrações    |     |
excessivas.