---
description: Importado de '2.5 Relatório Granulometria e Dimensionamento de Peneira.pdf'.
resource: drive://1JX5eHvCl73VF5qm-aKfeiSyISLgS8Qf9
tags: []
timestamp: '2026-07-16T02:44:17Z'
title: 2.5 Relatório Granulometria E Dimensionamento De Peneira
type: Conceito
---

Relatório: Granulometria e Dimensionamento da
Peneira
1. Introdução e Objetivo
Este documento consolida os parâmetros de engenharia necessários para o desenvolvimento do
Módulo de Trituração de Resíduos de Impressão 3D (PLA/PETG), com foco específico no
dimensionamento da peneira de classificação e na interface de alimentação com a extrusora. O objetivo
principal é fornecer à Gestão de Projeto e à equipe de Fabricação as justificativas técnicas baseadas na
literatura de processamento de polímeros (transporte de sólidos) para garantir que o material triturado flua
adequadamente, evite o travamento do sistema e assegure uma extrusão contínua.
2. A Importância da Interface Trituradora-Extrusora
O dimensionamento da peneira não deve ser guiado apenas pela capacidade de corte do triturador
de eixo único, mas primariamente pelas restrições físicas do maquinário subsequente (a extrusora). A
literatura técnica de transporte de sólidos em polímeros demonstra que o fluxo no funil de alimentação
(feed hopper) e na zona inicial da rosca é o estágio mais crítico do processo.
2.1. Escoamento no Funil e Riscos de Obstrução
Formação de Pontes (Bridging/Arching): Ocorre quando fragmentos muito irregulares ou com
alta coesão formam uma estrutura rígida no funil, suportando o peso do material acima e interrompendo a
descida para a rosca.
Efeito Tubo (Piping): Formação de um canal central de escoamento rápido, com o material nas
paredes do funil estagnado.
Risco de Pós Finais: Malhas muito restritivas mantêm o plástico por muito tempo na câmara de
corte, gerando micropartículas e pós (menores que 0,2 mm). Pós de polímeros são altamente coesivos e
são a principal causa de falhas de escoamento induzido pela gravidade.
2.2. Formação da Cama Sólida (Solid Bed)
Para que a extrusora funcione com pressão estável, o plástico reciclável precisa descer e se
compactar no canal da rosca, formando um bloco contínuo (plug flow). Fragmentos de formatos muito
variados, como lascas longas geradas sem peneira adequada, impedem essa compactação, resultando no
"Transporte de Arquimedes", caracterizado por canais de rosca vazios, perda de pressão e falhas na
extrusão do filamento.

3.  Especificação  de  Granulometria  e  Dimensionamento  da
Peneira
Com  base  nos  fundamentos  de  transporte  de  sólidos  induzido  por  arraste  (drag  induced
conveying), a especificação da granulometria de saída da trituradora deve simular o comportamento
mecânico de pellets virgens.

3.1. Granulometria Alvo
A literatura técnica define que a profundidade do filete na zona de alimentação da rosca deve ser
igual ou superior ao tamanho de um pellet típico de polímero, estabelecido entre 3 mm e 4 mm.
Fragmentos maiores que a profundidade da rosca não conseguirão entrar no canal, causando o engasgo do
sistema.

3.2. Parâmetros Construtivos da Peneira
Para obter a granulometria alvo sem sobrecarregar o motor e sem derreter o PLA por atrito
prolongado na câmara de corte, recomenda-se a seguinte especificação técnica para a chapa perfurada,
posicionada sob o rotor do eixo único:

| Parâmetro  | Especificação  |     | Justificativa Técnica  |     |     |
| ---------- | -------------- | --- | ---------------------- | --- | --- |
Recomendada
| Diâmetro do Furo (D)  | 5,0 mm  |     | Garante  | que  | o   |
| --------------------- | ------- | --- | -------- | ---- | --- |
fragmento resultante possua, em
média, de 3 a 4 mm (dimensão
de um pellet virgem).
| Arranjo dos Furos  | Triangular  | a  60°  | Otimiza                         | a             | tensão      |
| ------------------ | ----------- | ------- | ------------------------------- | ------------- | ----------- |
| (Staggered)        |             |         | mecânica suportada pela chapa,  |               |             |
|                    |             |         | permitindo                      | maior  vazão  | sem         |
|                    |             |         | perda  de                       | resistência   | estrutural  |
aos impactos.
| Área Aberta  | 35% a 45%  |     | Garante     | o  escoamento  |            |
| ------------ | ---------- | --- | ----------- | -------------- | ---------- |
|              |            |     | rápido      | do  material.  | Áreas      |
|              |            |     | abertas     | menores  que   | 30%        |
|              |            |     | causam      | retenção  do   | plástico,  |
|              |            |     | aumentando  | o  atrito,     | o  calor   |
|              |            |     | friccional  | e  causando    | o          |
derretimento do PLA na câmara
de corte.

Parâmetro Especificação Justificativa Técnica
Recomendada
Espessura da Chapa 3,0 mm a 4,0 mm A espessura não deve
ultrapassar o diâmetro do furo
para evitar o "efeito túnel"
(entupimento crônico). Utilizar
aço carbono (ex: SAE 1020) ou
inox.
4. Benchmarking e Estado da Técnica (Análise de Similares)
A especificação de 5 mm para a peneira é amplamente validada por soluções comerciais e de
código aberto utilizadas mundialmente na reciclagem de polímeros em escala laboratorial e desktop:
● Precious Plastic (V4 Pro): O projeto de inovação aberta de referência global utiliza em seu
"Shredder Pro" uma peneira de chapa perfurada curva com furos redondos de 5 mm, otimizada
pela comunidade para alimentação direta de extrusoras e injetoras compactas.
● Felfil Shredder+ e Polystruder GR PRO: Fabricantes comerciais consolidados de equipamentos
de reciclagem acadêmica atestam em seus catálogos técnicos uma granulometria de saída nominal
de até 5 mm, comprovando a viabilidade industrial desta dimensão para o mercado de filamentos.
5. Sustentabilidade e Controle de Microplásticos
O design da peneira possui impacto direto na mitigação de resíduos finos e aerossóis no ambiente.
Uma chapa com área aberta otimizada (aproximadamente 40%) garante o escoamento rápido do material
triturado, minimizando o tempo de residência. Malhas excessivamente restritivas mantêm o plástico em
constante atrito na câmara de corte, fragmentando-o repetidas vezes até gerar pó e microplásticos. A
contenção e redução desses finos são cruciais por dois motivos centrais:
● Prevenção de Obstruções (Bridging): Pós de polímeros (partículas com diâmetro inferior a 0,2
mm) exibem altíssima coesividade mecânica, promovendo o colapso do escoamento por gravidade
no funil da extrusora.
● Segurança Ocupacional e Ambiental: A dispersão de microplásticos suspensos no ar representa
um risco respiratório severo em ambientes acadêmicos e makerspaces com baixa circulação de ar,
contrariando as diretrizes de ecodesign do projeto.
6. Metodologia de Validação Prática
Para comprovar a eficácia do protótipo mecânico em relação à granulometria estipulada, a
validação do produto deverá seguir os preceitos metodológicos da norma internacional ASTM D1921
(Standard Test Methods for Particle Size of Plastic Materials). O ensaio físico recomendado é composto
pelas seguintes etapas:
1. Trituração de um lote amostral de resíduos heterogêneos de impressão 3D (PLA e PETG).
2. Passagem do material processado por um conjunto de peneiras de teste (malhas granulométricas de

laboratório) sobrepostas sob vibração controlada.
3. Análise gravimétrica para levantamento da curva de distribuição do tamanho de partículas (massa
retida por malha), atestando a predominância estatística da fração compreendida entre 3 mm e 5
mm.
7. Estratégia de Operação: Alimentação Dosada vs. Funil
Cheio
A interação entre a saída da trituradora e a entrada da extrusora ditará a qualidade do filamento
reciclado.
● Alimentação por Funil Cheio (Flood Feeding): Prática comum onde o funil é preenchido até o
topo. O peso da coluna gera altas pressões na base. Risco alto de aglomeração prematura de flocos
recicláveis devido ao calor de atrito gerado contra o barril (o que destrói o mecanismo de
transporte sólido).
● Alimentação Dosada (Starve Feeding): O material é fornecido em uma taxa controlada.
Recomendação estrita para este projeto. O triturador (ou uma válvula rotativa abaixo dele) deve
atuar limitando a vazão de entrada na extrusora. Isso reduz a pressão na zona inicial da rosca,
previne o derretimento precoce e promove o derretimento de sólidos dispersos (DSM), melhorando
severamente a homogeneidade da mistura térmica e a qualidade do filamento impresso.
8. Conclusões e Recomendações para as Equipes
1. Equipe de Pesquisa e Projeto Técnico: Modelar a malha da peneira no CAD com furos de 5 mm
e buscar fornecedores de chapas perfuradas comerciais que atendam à área aberta próxima de 40%,
evitando custos altos de usinagem customizada.
2. Equipe de Gestão e Desenvolvimento: Alinhar imediatamente com o grupo responsável pela
Extrusora para confirmar que a profundidade do filete da rosca deles suporta partículas de 4 mm de
diâmetro. Caso a rosca seja menor, toda a especificação da malha precisará ser recalculada.
3. Equipe de Sustentabilidade e Apresentações: Utilizar este documento para justificar o rigor
técnico do projeto durante as defesas, provando que o controle de fluxo, a mitigação de
microplásticos e a prevenção de falhas de extrusão ditaram o dimensionamento mecânico.
9. Referências Bibliográficas
ASTM INTERNATIONAL. ASTM D1921-18: Standard Test Methods for Particle Size (Sieve
Analysis) of Plastic Materials. West Conshohocken, PA: ASTM International, 2018.
FELFIL. Felfil Shredder - Technical Datasheet. Turim, Itália. Disponível no site oficial do
fabricante (felfil.com).
GILES, Harold F.; WAGNER, John R.; MOUNT, Eldridge M. Extrusion: The Definitive
Processing Guide and Handbook. William Andrew, 2004.
LA MANTIA, Francesco. Handbook of Plastics Recycling. iSmithers Rapra Publishing, 2002.
PRECIOUS PLASTIC. Precious Plastic V4: Shredder Pro Technical Drawings & BOM.
2020. Disponível no repositório do projeto.
RAUWENDAAL, Chris. Polymer Extrusion. 5. ed. Hanser Publications, 2014. p. 258-304.