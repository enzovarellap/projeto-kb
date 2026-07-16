---
description: Importado de 'content.pdf'.
resource: drive://15I4YYjDBiQp8HmFaF3RrTcc6fvOxpjbN
tags: []
timestamp: '2026-07-16T02:43:49Z'
title: Content
type: Conceito
---

Projeto de um triturador para reciclagem de PLA e
ABS resultantes de impressões por Fused Filament
Fabrication
PEDRO PIRES BRAGUÊS
(Licenciado em Engenharia Mecânica)
Trabalho de Projeto para obtenção do grau de Mestre em Engenharia Mecânica, na Área de
Especialização de Manutenção e Produção
Orientadores:
Doutor André Rui Dantas Carvalho
Doutor Ivan Rodolfo Garcia Pereira de Galvão
Júri:
Presidente: Doutora Maria Amélia Ramos Loja
Vogais:
Doutor Bruno Alexandre Rodrigues Simões Soares
Doutor André Rui Dantas Carvalho
Novembro, 2024

Projeto de um triturador para reciclagem de PLA e
ABS resultantes de impressões por Fused Filament
Fabrication
PEDRO PIRES BRAGUÊS
(Licenciado em Engenharia Mecânica)
Trabalho de Projeto para obtenção do grau de Mestre em Engenharia Mecânica, na Área de
Especialização de Manutenção e Produção
Orientadores:
Doutor André Rui Dantas Carvalho, ISEL/IPL
Doutor Ivan Rodolfo Garcia Pereira de Galvão, ISEL/IPL
Júri:
Presidente: Doutora Maria Amélia Ramos Loja, ISEL/IPL
Vogais:
Doutor Bruno Alexandre Rodrigues Simões Soares, FCT/UNL
Doutor André Rui Dantas Carvalho, ISEL/IPL
Novembro, 2024

Agradecimentos
Gostaria de agradecer primeiramente a ambos os meus orientadores por toda a ajuda
e diretrizes que me deram ao longo do percurso de elaboração deste projeto, estando
sempre disponíveis para me ajudar. Ao professor André Carvalho pela sugestão do tema
e por confiar em mim para abordar o mesmo. E ao professor Ivan Galvão pelo apoio e
disponibilidade para a realização de ensaios mecânicos pertinentes para o projeto, no
laboratório onde faz investigação.
Aos meus pais e ao meu irmão, pelo apoio constante, pela confiança na minha pessoa
e por serem exemplos de sucesso que eu pretendo seguir.
À minha instituição, o ISEL, que é um excelente local de aprendizagem, que muito me
ensinou e me preparou para a indústria.
Por último, e não menos importante, aos meus amigos mais próximos, que sempre me
acompanharam neste percurso onde foram, e continuam a ser, essenciais para o meu
sucesso e felicidade.
Um grande obrigado a todos!
i

Declaração de integridade
Declaro que este trabalho de projeto é o resultado da minha investigação pessoal e
independente. O seu conteúdo é original e todas as fontes listadas nas referências
bibliográficas foram consultadas e estão devidamente mencionadas no texto. Mais
declaro que todas as referências científicas e técnicas relevantes para o
desenvolvimento do trabalho estão devidamente citadas e constam das referências
bibliográficas.
O autor
Lisboa, 22 de setembro de 2024
iii

Projeto de um triturador para reciclagem de PLA e
ABS resultantes de impressões por Fused Filament
Fabrication
Resumo
O cenário tecnológico contemporâneo tem sido marcado por um crescimento
exponencial no uso de tecnologias de impressão 3D, em particular, a popularidade dos
polímeros PLA e ABS que têm aumentado consideravelmente. No entanto, esse
aumento na produção e utilização de peças impressas traz consigo o desafio substancial
da gestão dos resíduos resultantes de defeitos de impressão, rejeições e produtos
indesejáveis. O descarte inadequado desses resíduos origina uma carga ambiental
significativa, dada a natureza não biodegradável de certos polímeros. Assim, é
necessário explorar soluções sustentáveis e eficazes para lidar com essa questão,
minimizando o impacto ambiental e promovendo a reutilização desses materiais.
Este estudo tem como objetivo abordar esse desafio ao propor o projeto de um triturador
especializado e otimizado para a reciclagem eficaz de resíduos de PLA e ABS
resultantes de impressões por fused filament fabrication. O triturador proposto terá a
finalidade de transformar esses resíduos em matéria-prima reutilizável, como
filamentos, que podem ser reintroduzidos no ciclo de produção de impressão 3D.
O projeto do triturador consiste no dimensionamento e/ou seleção de todos os
componentes constituintes do mesmo, para que este cumpra eficientemente o seu
propósito. Para tal recorrer-se-á a equipamentos de processamento de granulado para
ser possível definir certas características de projeto, nomeadamente extrusoras de
termoplásticos.
Palavras-chave: Fabrico Aditivo, Polímeros, Trituração, Granulado, Análise Estrutural
v

Design of a shredder for recycling PLA and ABS
resulting from Fused Filament Fabrication 3D prints
Abstract
The contemporary technological landscape has been marked by exponential growth in
the use of 3D printing technologies, in particular the popularity of PLA and ABS polymers
has increased considerably. However, this increase in the production and use of 3D
printed parts brings with it the substantial challenge of managing waste resulting from
printing defects, rejects and unwanted products. Improper disposal of this waste creates
a significant environmental burden, given the non-biodegradable nature of certain
polymers. It is therefore necessary to explore sustainable and effective solutions to deal
with this issue, minimizing the environmental impact and promoting the reuse of these
materials.
This study aims to address this challenge by proposing the design of a specialized and
optimized shredder for the effective recycling of PLA and ABS waste resulting from fused
filament fabrication 3D prints. The proposed shredder aims to transform this waste into
reusable raw materials, such as filaments, which can be reintroduced into the 3D printing
production cycle.
The design of the shredder consists of dimensioning and/or selecting all of its
components so that it fulfills its purpose efficiently. To do this, granulate processing
equipment, like thermoplastic extruders, will be used to define certain design
characteristics.
Keywords: Additive Manufacturing, Polymers, Shredding, Granulate, Structural Analysis
vii

Lista de Símbolos e de siglas
Alfabeto romano
A Área de corte
b Comprimento do lado do pentágono
d Distância da extremidade da lâmina ao centro do veio
D Diâmetro do veio
F Força de corte
𝑘 Pressão específica de corte
𝑠
𝑛 Velocidade de rotação
𝑃 Potência mínima
𝑚𝑖𝑛
T Binário
t Espessura do polímero
w Espessura das lâminas de corte
Alfabeto grego
𝜏(𝑏𝑟) Resistência ao corte do PLA (PLA’s Breaking Strength)
𝑃𝐿𝐴
𝜎 Tensão de rotura (Ultimate Tensile Strength)
𝑢
𝜎 Tensão de cedência (Yield Strength)
𝑐𝑒𝑑
𝜏 Tensão de corte admissível
𝑎𝑑𝑚
𝜏 Tensão de rotura ao corte
𝑢
𝜏 Tensão de cedência ao corte
𝑐𝑒𝑑
𝜀 Quantidade relativa de penetração da lâmina no material
0𝑡
𝜑 Ângulo de inclinação da lâmina no início do corte
Acrónimos
3D Tridimensional
ABS Acrilonitrilo butadieno estireno
CAD Desenho assistido por computador (Computer Aided Design)
CS Coeficiente de Segurança
DIY Do it yourself
FA Fabrico aditivo

FFF Fabrico por filamentos fundidos (Fused Filament Fabrication)
FDM Modelação por fusão e deposição (Fused Deposition Modeling)
G-CODE Código G (Geometric Code)
HV Dureza Vickers (Vickers Hardness)
PLA Bipolímero ácido poliáctico
PP Polipropileno
PVC Policloreto de vinila
SLA Estereolitografia (Stereolithography)
SLS Sinterização Seletiva a Laser (Selective Laser Sintering)
STL Stereolithography file format

Índice
1 INTRODUÇÃO ................................................................................................................................ 1
1.1 MOTIVAÇÃO E OBJETIVOS .................................................................................................................. 1
1.2 ESTRUTURA .................................................................................................................................... 2
2 REVISÃO DA LITERATURA .............................................................................................................. 3
2.1 FABRICO ADITIVO ............................................................................................................................. 3
2.2 PLA E ABS ..................................................................................................................................... 8
2.3 RECICLAGEM MECÂNICA ................................................................................................................. 10
2.4 EQUIPAMENTOS EXISTENTES ............................................................................................................. 13
2.4.1 Estudo de mercado ............................................................................................................... 13
2.4.2 Estudo científico .................................................................................................................... 16
3 DIMENSIONAMENTO E SELEÇÃO DE MATERIAIS .......................................................................... 19
3.1 1º ESTÁGIO DE TRITURAÇÃO ............................................................................................................ 19
3.1.1 Determinação de Propriedades Mecânicas .......................................................................... 19
3.1.2 Lâminas ................................................................................................................................. 22
3.1.3 Veio ....................................................................................................................................... 23
3.1.4 Estrutura, elementos de ligação e componentes auxiliares ................................................. 26
3.1.5 Motor, acoplamento, rolamentos e elementos de transmissão ........................................... 29
3.2 2º ESTÁGIO DE TRITURAÇÃO ............................................................................................................ 30
3.2.1 Navalhas ............................................................................................................................... 30
3.2.2 Configuração ........................................................................................................................ 32
3.2.3 Estrutura, elementos de ligação e componentes auxiliares ................................................. 34
3.2.4 Motor, acoplamento, rolamento e elementos de transmissão ............................................ 35
4 MODELAÇÃO DE ELEMENTOS FINITOS ......................................................................................... 37
4.1 LÂMINAS E VEIO DO 1º ESTÁGIO ........................................................................................................ 37
4.2 NAVALHAS E VEIO DO 2º ESTÁGIO...................................................................................................... 42
4.3 ESTRUTURA .................................................................................................................................. 45
5 CONCLUSÕES E TRABALHO FUTURO ............................................................................................ 48
5.1 CONCLUSÕES ................................................................................................................................ 48
5.2 TRABALHO FUTURO ........................................................................................................................ 49
REFERÊNCIAS BIBLIOGRÁFICAS ............................................................................................................ 50

Índice de figuras
FIGURA 2.1 – EXEMPLIFICAÇÃO DA TECNOLOGIA FDM/FFF (3D PRINTING TECHNOLOGY COMPARISON: FDM VS. SLA VS.
SLS | FORMLABS)..................................................................................................................................... 5
FIGURA 2.2 – EXEMPLO DE UMA ARMAÇÃO DE ÓCULOS DE SKI IMPRESSA POR FDM (FORMLABS FORM 3 DESKTOP SLA 3D
PRINTER) ................................................................................................................................................. 5
FIGURA 2.3 – EXEMPLIFICAÇÃO DA TECNOLOGIA SLA (3D PRINTING TECHNOLOGY COMPARISON: FDM VS. SLA VS. SLS |
FORMLABS) ............................................................................................................................................. 6
FIGURA 2.4 – EXEMPLO DE UMA ARMAÇÃO DE ÓCULOS DE SKI IMPRESSA POR SLA (FORMLABS FORM 3 DESKTOP SLA 3D
PRINTER) ................................................................................................................................................. 6
FIGURA 2.5 – EXEMPLIFICAÇÃO DA TECNOLOGIA SLS (3D PRINTING TECHNOLOGY COMPARISON: FDM VS. SLA VS. SLS |
FORMLABS) ............................................................................................................................................. 7
FIGURA 2.6 – EXEMPLO DE UMA ARMAÇÃO DE ÓCULOS DE SKI IMPRESSA POR SLS (FORMLABS FUSE 1 BENCHTOP SLS 3D
PRINTER) ................................................................................................................................................. 7
FIGURA 2.7 – TRITURADOR DO TIPO I (HILL, 1986)............................................................................................... 11
FIGURA 2.8 – TRITURADOR DO TIPO II (HILL, 1986).............................................................................................. 12
FIGURA 2.9 – TRITURADOR DO TIPO III (HILL, 1986)............................................................................................. 13
FIGURA 2.10 – DIY CHEN – STAINLESS STEEL MINI PLASTIC SHREDDER (STAINLESS STEEL MINI PLASTIC SHREDDER WITH
NRV050 REDUCER (HARDENING BLADE) – DIY CHEN) ................................................................................. 14
FIGURA 2.11 – ACTION BOX – SHREDII 5.0 (SHREDIITM 5.0 | MECHANICAL KIT | ACTION BOX) ........................... 15
FIGURA 2.12 – 3DEVO – GP20 HYBRID (GP20 PLASTIC SHREDDER HYBRID | 3DEVO) ................................................ 16
FIGURA 2.13 – LÂMINA DE TRITURAÇÃO COM 2 DENTES (MUTHIAH ET AL., 2022) ...................................................... 17
FIGURA 2.14 – LÂMINA DE TRITURAÇÃO COM 5 DENTES ......................................................................................... 18
FIGURA 3.1 – MICROGRAFIA DE UMA IDENTAÇÃO REALIZADA NUMA PEÇA EM PLA DE COR PRETO .................................. 20
FIGURA 3.2 – MODELO DA LÂMINA .................................................................................................................... 22
FIGURA 3.3 – CONFIGURAÇÃO INICIAL DE 33 LÂMINAS A ATUAR SIMULTANEAMENTE ................................................... 24
FIGURA 3.4 – CONFIGURAÇÃO FINAL DO 1º ESTÁGIO DE TRITURAÇÃO COM 5 LÂMINAS A ATUAR SIMULTANEAMENTE.......... 25
FIGURA 3.5 – MODELO CAD DO VEIO ................................................................................................................. 26
FIGURA 3.6 – ESTRUTURA DE SUPORTE DO 1º ESTÁGIO DE TRITURAÇÃO ..................................................................... 27
FIGURA 3.7 – TREMONHA DO 1º ESTÁGIO ............................................................................................................ 28
FIGURA 3.8 – MODELO FINAL DO 1º ESTÁGIO DE TRITURAÇÃO ................................................................................. 29
FIGURA 3.9 – MODELO CAD DO ACOPLAMENTO .................................................................................................. 30
FIGURA 3.10 – MODELO DA NAVALHA ................................................................................................................ 31
FIGURA 3.11 – CONFIGURAÇÃO DO CORTE DO 2º ESTÁGIO ...................................................................................... 31
FIGURA 3.12 – EVOLUÇÃO DA PRESSÃO ESPECIFICA DE CORTE COM A PROFUNDIDADE DE CORTE (KERESZTES ET AL., 2011). 32
FIGURA 3.13 – CONJUNTO DO VEIO, NAVALHAS E BATENTES, DO 2º ESTÁGIO .............................................................. 33
FIGURA 3.14 – CONFIGURAÇÃO DO 2º ESTÁGIO, COM 3 NAVALHAS ROTATIVAS ........................................................... 33
FIGURA 3.15 – ESTRUTURA DE SUPORTE DO 2º ESTÁGIO DE TRITURAÇÃO ................................................................... 34
i

FIGURA 3.16 – TREMONHA DO 2º ESTÁGIO .......................................................................................................... 35
FIGURA 3.17 – MODELO FINAL DO 2º ESTÁGIO DE TRITURAÇÃO ............................................................................... 35
FIGURA 4.1 – MODELO DE ELEMENTOS FINITOS DO 1º ESTÁGIO ............................................................................... 37
FIGURA 4.2 – RESULTADOS DA ANÁLISE POR ELEMENTOS FINITOS ÀS LÂMINAS ............................................................ 38
FIGURA 4.3 – À ESQUERDA: MODELO DE SIMULAÇÃO DO 1º ESTÁGIO COM MALHA DE 10 MM. À DIREITA: MODELO DE
SIMULAÇÃO DO 1º ESTÁGIO COM MALHA FINAL REFINADA DE 0,5 MM............................................................... 38
FIGURA 4.4 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON-MISES CONFORME A DIMENSÃO DA MALHA, PARA O MODELO
INICIAL DO VEIO DO 1º ESTÁGIO ................................................................................................................. 39
FIGURA 4.5 – MODELO OTIMIZADO POR ELEMENTOS FINITOS DO 1º ESTÁGIO ............................................................. 40
FIGURA 4.6 – À ESQUERDA: MODELO OTIMIZADO DE SIMULAÇÃO DO 1º ESTÁGIO COM MALHA DE 10 MM. À DIREITA:
MODELO OTIMIZADO DE SIMULAÇÃO DO 1º ESTÁGIO COM MALHA FINAL REFINADA DE 0,5 MM. ............................. 40
FIGURA 4.7 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON MISES CONFORME A DIMENSÃO DA MALHA, PARA O MODELO
OTIMIZADO DO VEIO DO 1º ESTÁGIO ........................................................................................................... 41
FIGURA 4.8 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON MISES CONFORME A DIMENSÃO DA MALHA, PARA O MODELO
OTIMIZADO DO VEIO DO 1º ESTÁGIO, UTILIZANDO A FERRAMENTA PROBE ........................................................... 42
FIGURA 4.9 – MODELO DE ELEMENTOS FINITOS DO 2º ESTÁGIO ............................................................................... 43
FIGURA 4.10 – RESULTADOS DA ANÁLISE POR ELEMENTOS FINITOS ÀS NAVALHAS ........................................................ 43
FIGURA 4.11 – À ESQUERDA: MODELO DE SIMULAÇÃO DO 2º ESTÁGIO COM MALHA DE 10 MM. À DIREITA: MODELO DE
SIMULAÇÃO DO 2º ESTÁGIO COM MALHA FINAL REFINADA DE 0,5 MM............................................................... 44
FIGURA 4.12 - EVOLUÇÃO DOS VALORES DE TENSÃO DE VON MISES CONFORME A DIMENSÃO DA MALHA, PARA O VEIO DO 2º
ESTÁGIO, UTILIZANDO A FERRAMENTA PROBE ............................................................................................... 45
FIGURA 4.13 – CARGAS APLICADAS NO MODELO DE ANÁLISE DA ESTRUTURA .............................................................. 46
FIGURA 4.14 – CONSTRANGIMENTOS APLICADOS NO MODELO DE ANÁLISE DA ESTRUTURA ............................................ 46
FIGURA 4.15 – RESULTADOS DA ANÁLISE POR ELEMENTOS FINITOS À ESTRUTURA ........................................................ 47
ii

Índice de tabelas
TABELA 2.1 – PROPRIEDADES DO PLA E ABS (KOLYUDA, 2021) (KUMAR PATRO ET AL., 2023) (DURGA RAJESH ET AL.,
2023) .................................................................................................................................................... 9
TABELA 3.1 – VALORES EXPERIMENTAIS MÁXIMOS DE DUREZA PARA CADA PEÇA .......................................................... 20
TABELA 3.2 – PROPRIEDADES MECÂNICAS DO PLA E ABS ....................................................................................... 22
TABELA 3.3 – COMPONENTES NORMALIZADOS UTILIZADOS NO 1º ESTÁGIO ................................................................ 27
TABELA 3.4 – COMPONENTES NORMALIZADOS UTILIZADOS NO 2º ESTÁGIO ................................................................ 34
TABELA 4.1 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON MISES CONFORME A DIMENSÃO DA MALHA, PARA O MODELO
INICIAL DO VEIO DO 1º ESTÁGIO ................................................................................................................. 39
TABELA 4.2 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON MISES CONFORME A DIMENSÃO DA MALHA, PARA O MODELO
OTIMIZADO DO VEIO DO 1º ESTÁGIO ........................................................................................................... 41
TABELA 4.3 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON MISES CONFORME A DIMENSÃO DA MALHA, PARA O MODELO
OTIMIZADO DO VEIO DO 1º ESTÁGIO, UTILIZANDO A FERRAMENTA PROBE ........................................................... 42
TABELA 4.4 – EVOLUÇÃO DOS VALORES DE TENSÃO DE VON-MISES CONFORME A DIMENSÃO DA MALHA, PARA O VEIO DO 2º
ESTÁGIO, UTILIZANDO A FERRAMENTA PROBE ............................................................................................... 44
iii

1 Introdução
O primeiro capítulo consiste na introdução, sendo esta composta pela motivação e
objetivos e a estrutura do presente trabalho.
1.1 Motivação e Objetivos
Embora as vantagens do fabrico aditivo sejam inúmeras, a impressão 3D possui
também as suas limitações e desafios. Entre estes, destacam-se o tratamento dos
resíduos resultantes de defeitos de impressão, rejeições e produtos indesejáveis. Para
contornar este problema, têm sido desenvolvidos vários equipamentos e estações de
reciclagem para tratamento destes mesmos resíduos, nomeadamente trituradoras. No
entanto, estes equipamentos possuem algumas limitações, sendo estas ultrapassadas
com o desenvolvimento do triturador em questão.
O objetivo deste trabalho final de mestrado consiste em projetar um equipamento capaz
de triturar eficazmente os materiais PLA e ABS. Esta trituradora terá de ser capaz de
triturar todos os pedaços de material, de reduzi-los a granulados de pequenas
dimensões para poderem, posteriormente, ser processados e convertidos em filamento
contínuo, por outro equipamento. É importante que durante o processo de trituração, o
material seja de facto triturado através de um corte limpo, sem atingir temperaturas
próximas à temperatura de fusão do mesmo.
A trituradora necessita de cumprir o seu propósito, com eficiência, mantendo a sua
estabilidade estrutural. Para tal, durante o processo de dimensionamento da mesma,
realizado através de software CAD, utilizam-se ferramentas de análise estrutural para
garantir este mesmo aspeto.
1

1.2 Estrutura
Este trabalho de projeto encontra-se organizado em cinco capítulos principais, além das
seções de referências bibliográficas e anexos.
No primeiro capítulo, a introdução, são apresentados a motivação para a realização do
trabalho e os objetivos principais. Também é discutida a importância do tema, bem como
o contexto em que se insere.
No segundo capítulo procede-se à revisão da literatura existente sobre os principais
tópicos explorados ao longo do trabalho. Nesse capítulo, abordam-se os conceitos
relacionados ao fabrico aditivo, características dos polímeros PLA e ABS, métodos de
reciclagem mecânica e uma análise dos equipamentos atualmente disponíveis no
mercado.
No terceiro capítulo, detalha-se o processo de dimensionamento e seleção dos materiais
e componentes necessários para o desenvolvimento do triturador. São abordadas as
características mecânicas das lâminas e veios, bem como a estrutura e os componentes
auxiliares, incluindo motores e sistemas de transmissão.
O quarto capítulo apresenta os modelos de elementos finitos que foram utilizados para
analisar as tensões e deformações nos componentes principais do triturador. São
discutidos os resultados das simulações realizadas com o módulo SIMULATION do
software SOLIDWORKS.
Por fim, no quinto capítulo, resumem-se as principais conclusões do trabalho realizado,
além de se proporem guias para futuras pesquisas e melhorias no projeto do triturador.
2

2 Revisão da Literatura
Este capítulo encontra-se dividido em 4 subcapítulos, cada um sobre um tema em
específico relacionado com o projeto em questão, que têm como objetivo contextualizar
o tema.
2.1 Fabrico Aditivo
O Fabrico Aditivo (FA) consiste na produção de objetos físicos a partir de um modelo
digital, através da adição contínua de camadas de um determinado material, por uma
impressora 3D, até à formação de um produto final. O conceito de adição de camadas
é transversal a todas as impressoras 3D, mas a tecnologia utilizada para depositar
camadas difere consoante o material utilizado e o tipo de FA. Os tipos mais comuns de
FA são FFF, SLS e SLA (Kolyuda, 2021).
Os processos de FA são constituídos maioritariamente por 3 etapas. A etapa inicial
consiste no desenvolvimento do modelo 3D, onde é desenvolvido o projeto
tridimensional num software de CAD, sendo definido o design e as dimensões da peça
a fabricar.
A segunda etapa consiste no slicing, ou corte em camadas. Nesta etapa o modelo 3D é
dividido em camadas/fatias. Para tal ser possível, o modelo 3D deve ser exportado, do
software CAD, para ser processado no devido software de slicing. Após definidos os
parâmetros no slicer, é gerado um arquivo em formato G-code.
A terceira e última etapa, consiste efetivamente no processo de fabrico aditivo. Nesta
etapa, o arquivo G-code é enviado para a impressora 3D, que faz a leitura das
coordenadas e a deposição do material em camadas, até se completar o fabrico da
peça. Este processo pode ter uma duração de poucos minutos ou alguns dias,
dependendo das variáveis do projeto.
Esta tecnologia, como qualquer outra, possui as suas vantagens e desvantagens,
podendo algumas ser enumeradas (Costabile et al., 2017).
Vantagens:
• Desenvolvimento mais flexível;
• Liberdade de conceção e construção;
• Redução dos processos de montagem;
• Eliminação de ferramentas de produção;
• Redução de peças sobresselentes em stock;
• Redução de complexidade no negócio devido à redução de peças para gerir;
3

• Redução do tempo de colocação dos produtos no mercado;
• Implementação mais rápida de alterações.
Desvantagens:
• Necessidade recorrente de operações de acabamento;
• Tempo de fabrico muito dependente das dimensões da peça, podendo ter a
duração de dias;
• Ineficiência para elevados volumes de produção.
Existem 3 principais tipos de tecnologias de fabrico aditivo de polímeros, sendo estes a
Modelação por Fusão e Deposição (FDM, do inglês Fused Deposition Modeling/FFF, do
inglês Fused Filament Fabrication), a Estereolitografia (SLA) e a Sinterização Seletiva a
Laser (SLS) (Kanishka & Acherjee, 2023). De seguida serão abordadas estas 3
tecnologias e feita uma comparação visual, através de imagens, de uma mesma peça
produzida pelas diversas tecnologias, ilustrado nas Figuras 2.1 a 2.6.
• FDM/FFF - A modelação por fusão e deposição (FDM), também conhecida como
fabrico de filamento fundido (FFF), é a forma mais utilizada de impressão 3D ao
nível do consumidor, impulsionada pelo aparecimento de impressoras 3D para
amadores. As impressoras 3D FDM fabricam peças através da fusão e extrusão
de filamento termoplástico, que é depositado, camada a camada, por um bocal
na área de construção. O FDM funciona com uma gama de termoplásticos
padrão, como o ABS, o PLA e as suas várias misturas. A técnica é adequada
para modelos básicos de proof of concept, bem como para a prototipagem rápida
e de baixo custo de peças simples, tais como peças que normalmente seriam
maquinadas. As peças FFF tendem a ter linhas de camadas visíveis e podem
apresentar imprecisões em torno de características complexas. A tecnologia FFF
possui a menor resolução e precisão quando comparada com a SLA ou SLS e
não é a melhor opção para imprimir peças com características detalhadas. Os
acabamentos de maior qualidade podem ser obtidos através de processos de
polimento químico e mecânico. As impressoras 3D FDM industriais utilizam
suportes solúveis para mitigar alguns destes problemas e oferecem uma gama
mais alargada de termoplásticos de engenharia, mas também têm um preço
elevado (3D Printing Technology Comparison: FDM vs. SLA vs. SLS | Formlabs).
4

Figura 2.1 – Exemplificação da tecnologia FDM/FFF (3D Printing Technology Comparison:
FDM vs. SLA vs. SLS | Formlabs)
Figura 2.2 – Exemplo de uma armação de óculos de ski impressa por FDM (Formlabs Form 3
desktop SLA 3D printer)
• SLA - A estereolitografia foi a primeira tecnologia de impressão 3D desenvolvida.
Inventada na década de 1980, continua a ser uma das tecnologias mais
populares entre os profissionais. As impressoras 3D de resina SLA utilizam um
laser para curar a resina líquida e transformá-la em polímero endurecido, num
processo designado por fotopolimerização. As peças produzidas em SLA têm a
maior resolução e precisão, os detalhes mais nítidos e o acabamento de
superfície mais suave de todas as tecnologias de impressão 3D em polímero,
mas a principal vantagem da SLA reside na sua versatilidade. Os fabricantes de
materiais criaram formulações inovadoras de resina de fotopolímero SLA com
uma vasta gama de propriedades óticas, mecânicas e térmicas para
corresponder às dos termoplásticos padrão. As peças produzidas por SLA
possuem arestas vivas, um acabamento superficial suave e linhas de camada
mínimas visíveis. A tecnologia SLA é uma ótima opção para protótipos altamente
5

detalhados que requerem tolerâncias apertadas e superfícies lisas, tais como
moldes, padrões e peças funcionais. Esta tecnologia é amplamente utilizada
numa série de indústrias, desde a medicina dentária, à joalharia, fabrico de
modelos e até educação (3D Printing Technology Comparison: FDM vs. SLA vs.
SLS | Formlabs).
Figura 2.3 – Exemplificação da tecnologia SLA (3D Printing Technology Comparison: FDM vs.
SLA vs. SLS | Formlabs)
Figura 2.4 – Exemplo de uma armação de óculos de ski impressa por SLA (Formlabs Form 3
desktop SLA 3D printer)
• SLS - A sinterização seletiva a laser é a tecnologia de fabrico aditivo mais comum
para aplicações industriais, em que engenheiros e fabricantes de diferentes
indústrias confiam pela sua capacidade de produzir peças fortes e funcionais. As
impressoras 3D SLS utilizam um laser de alta potência para fundir pequenas
partículas de pó de polímero. O pó não fundido suporta a peça durante a
impressão e elimina a necessidade de estruturas de suporte dedicadas. Isto
torna a tecnologia SLS ideal para geometrias complexas, incluindo
6

características interiores, cortes inferiores e paredes finas. As peças produzidas
através da impressão SLS têm excelentes características mecânicas, com uma
resistência semelhante à das peças moldadas por injeção. Estas peças possuem
um acabamento superficial ligeiramente rugoso, mas quase sem linhas de
camada visíveis. O material mais comum para a sinterização seletiva a laser é a
poliamida [nylon], um material termoplástico de engenharia popular com
excelentes propriedades mecânicas. A poliamida é leve, flexível e resistente,
tanto estruturalmente e contra impactos, como contra produtos químicos, calor,
luz, raios UV e sujidade. A combinação de baixo custo por peça, alta
produtividade e inexistência de estruturas de suporte fazem da SLS uma escolha
popular entre os engenheiros para prototipagem funcional e uma alternativa
económica à moldagem por injeção para fabrico de séries limitadas ou de pontes
(3D Printing Technology Comparison: FDM vs. SLA vs. SLS | Formlabs).
Figura 2.5 – Exemplificação da tecnologia SLS (3D Printing Technology Comparison: FDM vs.
SLA vs. SLS | Formlabs)
Figura 2.6 – Exemplo de uma armação de óculos de ski impressa por SLS (Formlabs Fuse 1
benchtop SLS 3D printer)
7

2.2 PLA e ABS
Devido às grandes vantagens dos materiais poliméricos no fabrico aditivo,
nomeadamente, através da tecnologia FFF, o PLA e o ABS têm vindo a evoluir como
talvez os materiais mais utilizados na impressão 3D (Rodríguez-Reyna et al., 2022).
Tendo a tecnologia do fabrico aditivo um impacto significativo em diferentes aplicações
industriais, estes têm vindo a registar um enorme desenvolvimento e presença na
indústria nos últimos anos (Agrawal et al., 2023).
Dependendo do modo como estão ligados química e estruturalmente, os materiais
poliméricos podem ser divididos em duas classes, os termoplásticos e os
termoendurecíveis. No caso do PLA e ABS, tratam-se de polímeros termoplásticos, que
são caracterizados por necessitarem de calor para serem enformados e, após o
arrefecimento, manterem a forma que adquiriram durante a enformação. Estes materiais
podem ser várias vezes reaquecidos e reenformados em novas formas, sem que ocorra
alteração significativa das suas propriedades. A deformação dos materiais caracteriza-
se como elástica ou plástica. Nos polímeros termoplásticos, abaixo da temperatura de
transição vítrea, estes deformam-se elasticamente, enquanto acima da temperatura de
transição vítrea, eles sofrem essencialmente uma deformação plástica. Devido à sua
leveza, fácil processamento e resistência à corrosão, são usados em grandes
quantidades em componentes da indústria automóvel, aeroespacial e bens de consumo
(William F. Smith, 1998).
O PLA (bipolímero ácido polilático) é um termoplástico derivado de fontes renováveis,
sendo este biodegradável nas condições corretas. Este material é um dos bioplásticos
mais populares e é perfeito para uma variedade de aplicações, desde copos de plástico
a implantes médicos.
Em comparação com outros materiais utilizados na impressão 3D, o PLA é bastante
económico, oferecendo uma boa relação qualidade/preço, obtendo-se componentes de
alta qualidade com acabamentos superficiais relativamente suaves. O PLA é fácil de
imprimir, devido à sua temperatura de impressão mais baixa, e possui uma rigidez mais
elevada quando comparado a outros materiais poliméricos como o ABS e poliamida,
porém, este não resiste bem a temperaturas elevadas, produtos químicos e tensões
elevadas.
O ABS (acrilonitrilo butadieno estireno) é um material comum na impressão 3D e
bastante popular no processo de moldagem por injeção. As aplicações do ABS na
indústria variam desde brinquedos (LEGO), caixas para eletrónica, peças para
automóveis, eletrodomésticos, entre outros.
8

O ABS possui certas propriedades mecânicas superiores às do PLA, como a resistência
mecânica, sendo ao mesmo tempo mais leve. No entanto, as desvantagens que este
possui, tratam-se da dificuldade em ser impresso e requerer frequentemente
temperaturas mais elevadas para uma impressão eficaz. Este possui uma condutividade
térmica superior ao PLA, no entanto, não é de todo conhecido pela sua elevada
resistência térmica.
Tanto o PLA como o ABS possuem resistências à tração semelhantes, o que os torna
sólidas opções para muitas aplicações de prototipagem. Na indústria, é frequentemente
preferido o ABS devido à sua superior ductilidade, em relação ao PLA. O ABS tem uma
maior resistência à flexão e um melhor alongamento antes da rutura comparativamente
ao PLA, este, por outro lado, é mais popular para prototipagem rápida quando se dá
mais importância à forma do que à função da peça.
Para finalizar, o PLA trata-se de uma boa opção para o fabrico de peças personalizadas
domesticamente que não estejam sujeitas a elevadas cargas (ou radiação UV e
temperaturas elevadas), como maquetes ou peças decorativas. O ABS é mais
adequado para aplicações industriais e componentes funcionais, visto possuir uma
melhor resistência a cargas físicas do que o PLA (3D Printing with PLA vs. ABS: What’s
the Difference? | Hubs) (Oliveira, 2018) (Kumar Patro et al., 2023).
Para se poder visualizar de uma forma mais concisa algumas das propriedades do PLA
e ABS, elaborou-se a Tabela 2.1.
Tabela 2.1 – Propriedades do PLA e ABS (Kolyuda, 2021) (Kumar Patro et al., 2023) (Durga
Rajesh et al., 2023)
Propriedade PLA ABS Unidades
Módulo de Elasticidade (E) 1,9 0,9 GPa
Massa Volúmica (ρ) 1250 1040 kg/m^3
Temperatura de Transição
52 108 ºC
Vítrea
9

2.3 Reciclagem Mecânica
Segundo Valavanidis (2022), a reciclagem mecânica refere-se ao processamento de
resíduos de plástico em matérias-primas ou produtos secundários, sem alterar
significativamente a estrutura química do material. Na generalidade, todos os tipos de
materiais termoplásticos são passíveis de serem reciclados mecanicamente com pouco,
ou nenhum impacto na qualidade dos mesmos. Esta trata-se, na generalidade, da
abordagem mais económica de reciclagem de materiais termoplásticos (Valavanidis,
2022).
A reciclagem mecânica de polímeros é constituída por diferentes fases – em particular:
(1) Separação: onde os resíduos são divididos e reagrupados consoante o seu material;
(2) Trituração: onde estes são moídos e triturados em pedaços de menores dimensões
ou grânulos; (3) Lavagem: normalmente com água, que tem a finalidade de remover
eventuais contaminantes; (4) Secagem: onde são removidas as partículas de humidade;
(5) Extrusão: etapa final onde o material é fundido, compactado e extrudido (Oliveira,
2018).
Relativamente à fase de trituração, esta é habitualmente realizada em trituradores, ou
shredders em inglês. Um triturador trata-se de um equipamento cujo objetivo é reduzir
o tamanho de um certo material a uma desejada dimensão. Embora um triturador seja
comumente conhecido como um “equipamento utilizado para triturar documentos como
medida de privacidade”, isto refere-se a trituradores de documentos em papel, podendo
as máquinas de trituração ser de várias formas e feitios, dependendo do material que
se encontra a ser triturado. Existem máquinas de trituração concebidas para lidar com
a trituração de materiais numa vasta gama de utilizações de reciclagem, incluindo a
reciclagem de plástico, a reciclagem de sucata metálica, resíduos eletrónicos,
reciclagem de madeira e trituração ou reciclagem de pneus (Shredding Machines:
Types, Applications, Advantages, and Standards).
De acordo com Oliveira (2018), o funcionamento de um triturador resulta da combinação
de 3 ações:
• Ação de corte: é o mecanismo de corte em si. A sua eficiência depende de quão
afiadas estão as lâminas e da tolerância entre duas consecutivas, como se de
uma tesoura se tratasse;
• Ação de rasgo: deve ser tida em conta a ação de puxar o material e capacidade
de o separar, abrindo um rasgo inicial. Esta ação é particularmente verificada
com plásticos e borrachas;
10

• Ação de fratura: É comum haver fratura quando as lâminas não estão
devidamente afiadas ou existe demasiada folga entre as mesmas. Deste modo,
deve-se ter especial cuidado com este facto pelo perigo de projetar pequenas
partes para fora do equipamento (Oliveira, 2018).
Segundo Hill (1986), existem 3 tipos diferentes de trituradores, os de Tipo I, Tipo II e
Tipo III.
Os de Tipo I; são trituradores cuja aplicação se trata de desfazer materiais não ferrosos
como cabos isolantes e de os preparar para outro processo de reciclagem. Neste tipo,
o material é bastante homogéneo na sua composição, mas a sua distribuição pode
variar, ou seja, tanto podem existir amontoados de material agregado como fios
dispersos. O design resultante incorpora dois veios com lâminas removíveis, para
conveniente substituição, com sentidos de rotação opostos que nunca se cruzam entre
si e, no centro, um conjunto de lâminas fixas que realizam efetivamente a trituração do
material, como é possível observar na Figura 2.7. Os dois eixos são acionados de forma
independente e conseguem, caso exista alguma obstrução ou massa de maiores
dimensões, ser revertidos. Deste modo, a quantidade de material colocada no triturador
não tem influência na eficácia do mesmo e do produto final produzido. Neste tipo de
trituradores, é necessário recorrer a uma preparação do material, dividindo-o em
pedaços mais pequenos, sendo que o comprimento ideal é entre 15-60 mm, assumindo
que as lâminas possuem um toleranciamento justo. Este design torna-se pouco prático
para materiais como resíduos sólidos urbanos, pneus e outros resíduos volumosos.
Figura 2.7 – Triturador do Tipo I (Hill, 1986)
Os de Tipo II, como se observa na Figura 2.8, tratam-se dos trituradores de uso mais
comum cujas aplicações variam desde a trituração de lixo municipal, resíduos
volumosos ou de grandes dimensões como mobília doméstica, resíduos provenientes
da construção civil e de processos de fabrico, ou outros objetos que necessitem de
redução de tamanho. Neste tipo de trituradores, é necessário ter em especial atenção a
quantidade de material a ser triturado pois, para o seu funcionamento ser eficaz, a zona
11

de corte não deve possuir material em excesso. Este tipo de equipamento é constituído
por dois veios com sentidos de rotação opostos e diversas lâminas que interferem com
as do veio oposto. Dada a vasta gama de aplicações e flexibilidade que estes
trituradores possuem, características como as dimensões da câmara de corte, número
e dimensões das lâminas, potência e velocidade de rotação das lâminas variem
bastante. No entanto, um aspeto comum a todos os modelos de trituradores deste tipo
é a utilização de diferentes valores de binário e velocidade de rotação em cada veio. O
seu baixo custo de manutenção, consumo de energia reduzido e a redução dos riscos
de projeção de resíduos sólidos, durante o processamento, tornam-no bastante atrativo
quando comparado com outros métodos de reciclagem de materiais. Neste tipo de
trituradores, o material é puxado para o centro da zona de corte e rasgado em vez de
cortado, sendo a ação de rasgo o mecanismo de trituração predominante.
Figura 2.8 – Triturador do Tipo II (Hill, 1986)
Tal como os de Tipo I, o terceiro tipo foi projetado com o objetivo de preparar o material
triturado a ser queimado, necessitando este de ser expelido uniformemente no formato
de longas tiras de borracha. Sendo a matéria-prima volumosa, flexível e elástica, torna-
se difícil de se manter no centro das lâminas de corte (como no Tipo II), por conseguinte,
este Tipo III incorpora semelhanças existentes nos trituradores do Tipo I e II. Como se
pode observar na Figura 2.9, a introdução de novos componentes em formato de estrela
auxiliam a deslocação do material para o centro de corte, no entanto, aumentam a
complexidade do design e a dificuldade de manutenção do triturador (Hill, 1986).
12

Figura 2.9 – Triturador do Tipo III (Hill, 1986)
2.4 Equipamentos existentes
Um triturador trata-se de um equipamento muito comum em diversas indústrias,
concebido para triturar objetos ou materiais como papel, metais ou plásticos. As
características estruturais de um triturador variam consoante as suas funções e, mesmo
dentro da mesma indústria, as características de um triturador podem variar. Na
indústria dos plásticos, por exemplo, é possível encontrar trituradores com um eixo de
lâminas rotativas combinadas com um conjunto de lâminas fixas, ou trituradores com
duas filas de lâminas móveis. Em ambas as configurações, a construção de um
triturador implica a rotação das lâminas. A rotação das mesmas pode ser assegurada
por um veio, que é um elemento rotativo geralmente de secção transversal circular
(sólida ou oca), que é utilizada para transmitir potência e movimento angular em
equipamentos mecânicos. No geral, os veios não possuem um diâmetro uniforme, mas
são escalonados para fornecer locais para a localização das engrenagens, polias e
rolamentos, que atuam como fatores de concentração de tensões (Vicente et al., 2019).
2.4.1 Estudo de mercado
Este subcapítulo baseia-se na pesquisa comercial de trituradores existentes no mercado
de modo a se ter uma perceção inicial da configuração dos trituradores.
No âmbito dos trituradores de materiais poliméricos de pequenas dimensões, foi-se ao
encontro, principalmente, de 3 equipamentos vendidos no mercado. Iniciando-se pelo
Stainless steel mini plastic shredder, do fabricante DIY Chen, observado na Figura 2.10.
Este equipamento foi inicialmente desenvolvido numa perspetiva DIY [do it yourself], e
posteriormente comercializado. O âmbito deste triturador é a trituração de vários
materiais poliméricos, como o PLA, ABS, PVC, entre outros. A sua configuração é de 2
veios motores, com 9 lâminas por veio, obtendo-se dimensões da câmara de trituração
13

de 94,7 mm de comprimento por 98 mm de largura. Possui alimentação externa de
apenas um motor elétrico, com potência de 350 W, propulsionando os dois veios através
de um sistema de engrenagens. Sendo um equipamento simples, possui uma massa de
8,5 kg e tem um custo comercial de 342€ (Stainless Steel Mini Plastic Shredder with
NRV050 Reducer(Hardening Blade) – DIY Chen).
Figura 2.10 – DIY Chen – Stainless steel mini plastic shredder (Stainless Steel Mini Plastic
Shredder with NRV050 Reducer (Hardening Blade) – DIY Chen)
Identificou-se também o SHREDII 5.0, do fabricante Action BOX, demonstrado na Figura
2.11. É um equipamento ligeiramente mais complexo que o anterior, tendo alimentação
proveniente de dois motores elétricos com 746 W cada, sendo os dois veios alimentados
de forma independente. Similarmente ao equipamento anterior, este possui dois veios
motores, com 15 lâminas de trituração por veio e dimensões da câmara de trituração de
140 mm de comprimento por 160 mm de largura. Este triturador foi alvo de reprojeto,
sendo que se trata de uma segunda versão do SHREDII. Inicialmente foi projetado com
um menor número de lâminas de 5 mm de espessura, concluindo-se, posteriormente,
que se se reduzisse a espessura das lâminas e se aumentasse o número das mesmas,
obter-se-ia um granulado de dimensões mais satisfatórias, ou seja de menores
dimensões. Deste modo, esta segunda versão do equipamento possui as 15 lâminas
referidas anteriormente, cada uma com 3 mm de espessura. Este equipamento é
ligeiramente mais complexo, possuindo até uma proteção para o utilizador ao triturar
PLA, ABS e PVC, sendo o seu custo 510€ (SHREDIITM 5.0 | Mechanical Kit | Action
BOX).
14

Figura 2.11 – Action BOX – SHREDII 5.0 (SHREDIITM 5.0 | Mechanical Kit | Action BOX)
Por fim, identificou-se o triturador de configuração híbrida GP20 Hybrid, como demontra
a Figura 2.12, fabricado pela 3devo. Sendo híbrido, este possui dois estágios que podem
ser utilizados de forma independente, dependendo do granulado que se deseja obter.
O material é inserido por um funil de alimentação que possui um tapete rolante, que tem
como objetivo alimentar o material ao primeiro estágio, com uma cadência constante,
de modo a evitar sobrealimentação. Este primeiro estágio é semelhante aos
mencionados anteriormente, sendo constituído por dois veios motores cada um com 7
lâminas rotativas. É alimentado através de um motor elétrico de 1200W (240V) ou
1500W (120V).
O segundo estágio é constituido por um granulador de elevada velocidade de rotação
que possui 3 lâminas rotativas e um filtro, sendo que o granulado extraído do
equipamento possui dimensões máximas de 3,5 mm. A alimentação energética do
segundo estágio é identica à do primeiro, totalizando o equipameto, em termos de
alimentação externa, de 2 motores elétricos.
Devido à sua elevada complexidade e requinte, este é capaz de triturar PLA, ABS, PVC
e PP, sendo que a sua massa é de 125 kg e possui um custo de 13 000 € (GP20 Plastic
Shredder Hybrid | 3devo).
15

Figura 2.12 – 3devo – GP20 Hybrid (GP20 Plastic Shredder Hybrid | 3devo)
É de salientar que, podendo os trituradores de polímeros, ser equipamentos de
pequenas dimensões, estes podem ser construídos com alguma facilidade,
encontrando-se pela internet, uma vasta diversidade de trituradores “DIY – do it
yourself”.
2.4.2 Estudo científico
Uma vez feita uma análise de mercado, de cariz técnico, torna-se particularmente
relevante complementar a abordagem com uma análise da literatura científica. Deste
modo, neste subcapítulo é aprofundado o estudo numa perspetiva do tipo de lâminas
existentes nos equipamentos, bem como realizadas pesquisas de métodos analíticos
para determinação de esforços aplicados às lâminas.
Encontrou-se, essencialmente, na literatura, dois tipos diferentes de configurações de
lâminas e, associado a estes, duas formas analíticas de determinação de esforços nas
mesmas, ou seja, da força de corte aplicada às lâminas, proveniente da trituração dos
materiais.
As duas configurações de lâminas mais comuns são as lâminas com 2 dentes, e as
lâminas com 3 ou mais dentes. Nas Figuras 2.13 e 2.14, é possível observar as duas
configurações, uma lâmina com 2 dentes e uma lâmina com 5 dentes.
16

Figura 2.13 – Lâmina de trituração com 2 dentes (Muthiah et al., 2022)
De acordo com Oliveira (2018) e Muthiah et al. (2022), a força de corte aplicada às
lâminas (𝐹) de 2 dentes, proveniente da trituração, pode ser calculada através da
expressão presente na equação 2.1 (Oliveira, 2018) (Muthiah et al., 2022).
𝑡2
𝐹 = 𝜏 𝜀 (2.1)
𝑢 0𝑡2 tg (𝜑)
Onde 𝜏 é a tensão de rotura ao corte, 𝜀 a quantidade relativa de penetração da lâmina
𝑢 0𝑡
no material, 𝑡 a espessura do material a triturar e 𝜑 o ângulo de inclinação da lâmina no
início do corte.
Para as lâminas de 3 ou mais dentes, a metodologia de cálculo é diferente, sendo que
Nasr e Yehia (2019) e Sedani e Sudarshan (2022) calculam a força de corte (𝐹) aplicada
às lâminas de 3 ou mais dentes, de acordo com as equações 2, 3 e 4 (Nasr & Yehia,
2019) (Sedani & Sudarshan, 2022).
𝜏(𝑏𝑟)=𝐶𝑆 𝜏 (2.2)
𝑢
𝐴 = 𝑤 𝑡 (2.3)
𝐹 = 𝜏(𝑏𝑟) 𝐴 (2.4)
Onde 𝜏(𝑏𝑟) corresponde à resistência ao corte do material, que pode ser aproximada à
tensão de rotura ao corte do mesmo, impondo um coeficiente de segurança (𝐶𝑆) e 𝐴, a
17

área de corte, calculada através da espessura da lâmina de corte (𝑤) e da espessura
de material a triturar (𝑡).
Figura 2.14 – Lâmina de trituração com 5 dentes
18

3 Dimensionamento e Seleção de Materiais
O terceiro capítulo trata-se do projeto mecânico do equipamento em questão e encontra-
se dividido por estágios de trituração. Neste, são inicialmente determinadas as
propriedades mecânicas dos materiais a triturar pelo equipamento, de modo a se
possuírem valores concretos para os cálculos e dimensionamento. Serão também
apresentados todos os componentes do equipamento, bem como a montagem, em
CAD, do mesmo.
3.1 1º Estágio de Trituração
Inicia-se o capítulo de dimensionamento e seleção de materiais pelo 1º estágio de
trituração.
3.1.1 Determinação de Propriedades Mecânicas
A fase inicial do projeto do triturador começou pelo dimensionamento das lâminas de
corte, sendo estas o componente que maior interação tem com o material a triturar.
Deste modo, e para se poder dar início ao dimensionamento das mesmas, considerou-
se essencial determinar a dureza dos materiais a triturar. Sendo que o polímero
impresso em 3D se trata de um material cujas propriedades mecânicas podem variar
consoante a cor do filamento e o enchimento da peça, considerou-se pertinente realizar
ensaios de dureza Vickers a diversas peças impressas, com o objetivo de se obter um
valor de dureza empírico. Foram impressas 3 peças em PLA nas cores branco, vermelho
e preto, todas com 100% de enchimento, de modo a se obterem peças com
propriedades mecânicas superiores e se projetar o equipamento para a situação mais
exigente.
19

Para tal ser possível, foram realizados ensaios de macrodureza Vickers, num durómetro
laboratorial, com uma carga de 3 kgf e tempo de indentação de 10 segundos. Foram
realizadas 3 indentações numa mesma linha reta, sendo estas localizadas no centro, a
três quartos e na extremidade da peça. Obtendo-se as indentações necessárias nas
peças, estas foram observadas a microscópio, como ilustra a Figura 3.1. Com auxílio de
software, foi possível medir o comprimento médio entre as diagonais do losango
marcado nas peças e, através da equação 3.1, determinar o valor da dureza Vickers.
Sendo que F corresponde à carga aplicada e Dmédio ao comprimento médio das
diagonais do losango, como demonstrado na equação 3.2 (Durga Rajesh et al., 2023).
Figura 3.1 – Micrografia de uma identação realizada numa peça em PLA de cor preto
1,854𝐹
𝐻𝑉 = (3.1)
(𝐷𝑚é𝑑𝑖𝑜)2
𝐷 +𝐷
𝐷𝑚é𝑑𝑖𝑜 = 1 2 (3.2)
2
A Tabela 3.1 demonstra a gama de valores de dureza obtida experimentalmente, para
as peças de diferentes pigmentos.
Tabela 3.1 – Valores experimentais máximos de dureza para cada peça
Cor do filamento Gama de valores de dureza [HV3]
Branco 14,5 – 15,2
Preto 17,6 – 17,8
Vermelho 15,6 – 17,1
20

Tendo-se dado o procedimento por finalizado, observa-se que os valores de dureza
Vickers variam entre 14,5 HV (PLA branco) a 17,8 HV (PLA preto), sendo que para o
PLA vermelho os valores são intermédios. Observa-se uma ligeira variação de valores
para medições na mesma peça pois, como referido anteriormente, foram realizadas
várias medições em zonas distintas da peça, e, sendo estas heterógenas, devido à sua
natureza, obtêm-se propriedades ligeiramente diferentes consoante a localização de
medição.
É possível concluir que as peças produzidas em filamento PLA preto apresentam uma
dureza ligeiramente superior às restantes cores analisadas, deste modo, utilizou-se o
valor 18 HV ou 176,5 MPa como valor de referência da dureza do material PLA.
Realizando uma breve pesquisa bibliográfica relativamente à dureza deste mesmo
material, verifica-se que Durga Rajesh et al., (2023) obteve um valor de dureza média,
experimental, de 15,3 HV e Beltrán et al., (2021) um valor de 135 MPa, que corresponde
a 13,77 HV. Esta pesquisa corrobora os valores obtidos laboratorialmente, sendo que
estes pouco divergem dos valores obtidos pelos autores mencionados, podendo esta
variação estar relacionada à qualidade de impressão, ou mesmo do filamento (Durga
Rajesh et al., 2023) (Beltrán et al., 2021).
O mesmo procedimento foi realizado para o ABS, no entanto, apenas para peças de
filamento branco, obtendo-se valores de dureza Vickers entre 5,3 HV e 6,7 HV,
utilizando-se como valor de referência para a dureza do ABS, 7 HV. Comparando estes
valores com a literatura, observa-se que Durga Rajesh et al., (2023) obtém um valor de
dureza média de 12,7 HV e Saviello et al., (2018) um valor de 10,2 HV, sendo que estes
diferem bastante dos obtidos experimentalmente. Porém, como o PLA apresenta uma
maior dureza, o equipamento é dimensionado para o mesmo material, não sendo
preocupante o desvio de dureza detetado no ABS (Beltrán et al., 2021) (Saviello et al.,
2018).
Através dos valores de dureza obtidos experimentalmente, foi possível estimar os
valores de tensão de rotura (𝜎 ) de ambos os materiais, através da equação 3.3. É de
𝑢
notar que o valor de dureza (HV) vem expresso em MPa (Zhang et al., 2011).
𝐻𝑉
𝜎 = (3.3)
𝑢 3
Realizando o cálculo, obtêm-se valores de tensão de rotura (𝜎 ) de 58,8 MPa e 22,9
𝑢
MPa para PLA e ABS, respetivamente.
21

Na Tabela 3.2, é possível observar, de uma forma concisa, as propriedades mecânicas
relevantes do PLA e do ABS.
Tabela 3.2 – Propriedades mecânicas do PLA e ABS
Propriedade PLA ABS Unidades
Tensão de Rotura (𝜎 ) 58,8 22.9 MPa
𝑢
Dureza Vickers (HV3) 14,5 – 17,8 5,3 – 6,7 -
3.1.2 Lâminas
As lâminas desempenham o papel principal no triturador, sendo que necessitam de estar
corretamente toleranciadas, afiadas e dimensionadas para se efetuar o processo de
trituração com eficácia.
Relativamente à sua geometria, optou-se por uma configuração de 5 dentes, de modo
a se obter um bom escoamento do material e consequentemente evitar o encravamento
do mesmo. Optou-se, também, por uma espessura reduzida de modo a aumentar o
número de lâminas a utilizar no equipamento, o que originará numa redução das
dimensões do granulado produzido. Assim sendo, elaborou-se o modelo observado na
Figura 3.2.
Figura 3.2 – Modelo da lâmina
De modo a se proceder à caracterização e dimensionamento das mesmas, foi
necessário identificar quais os esforços aplicados nas lâminas, durante o processo de
trituração do polímero. Para tal, seguiu-se o processo de cálculo relativo a lâminas de 3
ou mais dentes, enunciado no subcapítulo 2.4.2.
Deste modo, deu-se início à elaboração do procedimento de cálculo para o PLA.
Assumiu-se um coeficiente de segurança (CS) de 1,5, tensão de rotura do material (𝜎 )
𝑢
22

de 58,8 MPa, largura da lâmina (w) 3 mm e espessura do material a triturar (t) 10 mm,
de modo a se projetar as lâminas para uma situação exigente. Relativamente à tensão
de rotura ao corte do material (𝜏 ), considerou-se como sendo 60% da tensão de rotura
𝑟𝑜𝑡
do mesmo.
𝜏(𝑏𝑟) = 0,6 𝐶𝑆 𝜎 (3.4)
𝑃𝐿𝐴 𝑢
𝐹 = 𝜏(𝑏𝑟) 𝐴 (3.5)
𝑃𝐿𝐴
Através da equação 3.4, obteve-se uma resistência ao corte do PLA (𝜏(𝑏𝑟) ) de 52,92
𝑃𝐿𝐴
MPa. Calculando-se uma a área de corte de 30 𝑚𝑚2, através da largura da lâmina (w)
e espessura do material a triturar (t) e utilizando a equação 3.5, foi possível obter uma
força de corte (F) de 1587,6 N. Esta trata-se da força aplicada a cada lâmina, durante o
processo de trituração do polímero.
Relativamente ao material constituinte das mesmas, optou-se por um aço inox AISI
310S, fornecido em formato de chapa calibrada. Selecionou-se o mesmo devido às suas
propriedades inoxidáveis e mecânicas, possuindo uma tensão de cedência 𝜎 =
𝑐𝑒𝑑
300 𝑀𝑃𝑎, tensão de rotura 𝜎 = 650 𝑀𝑃𝑎 e dureza = 200 HV (AISI 310S (S31008)
𝑢
Stainless Steel: MakeItFrom.Com).
Outro motivo para a seleção deste aço foi o seu estado de fornecimento. Este é
fornecido, pela empresa Ramada Aços, segundo a norma EN 10051, no formato de
chapa calibrada com o toleranciamento dimensional de espessura de 3±0,22 mm, para
chapas de largura até 1200 mm. Desta forma é possível controlar a espessura real das
lâminas, impedindo que as mesmas possuam uma espessura superior à projetada e
que, durante o funcionamento do equipamento, existam colisões entre as mesmas e as
lâminas fixas (Tolerances to EN 10051 for Continuously Rolled Hot Rolled Plate Sheet
and Strip – British Stainless Steel Association).
3.1.3 Veio
Para o dimensionamento do veio, optou-se por uma abordagem de análise de esforços
de corte sobre o mesmo, sendo estes aplicados, inicialmente, às lâminas. Para tal foi
necessário, assumir uma configuração inicial de lâminas e veios de modo a se obter os
esforços aplicados sobre o mesmo. Assim, considerou-se que cada veio possuía 33
lâminas de 3 mm de espessura cada, como ilustra a Figura 3.3.
23

Figura 3.3 – Configuração inicial de 33 lâminas a atuar simultaneamente
Para se obter o diâmetro do veio, utilizou-se o seguinte procedimento de cálculo.
Calculou-se, através da equação 3.6, o binário aplicado ao veio (T), multiplicando a força
de corte por lâmina (F), calculada anteriormente (1587,6 N) pela distância da
extremidade da lâmina ao cento do veio (d) de 0,06 m e, multiplicando pelo número de
lâminas (33), obteve-se um binário total aplicado ao veio (𝑇 ) de 3143,5 Nm.
33 𝑙â𝑚𝑖𝑛𝑎𝑠
𝑇 = 𝐹 𝑑 (3.6)
𝑇 = 33 𝑇 (3.7)
33 𝑙â𝑚𝑖𝑛𝑎𝑠
Antes de se prosseguir, foi necessário selecionar o material do veio. Optou-se por um
aço de baixo carbono 𝐴𝐼𝑆𝐼 1010 com valor de tensão de cedência 𝜎 = 190 𝑀𝑃𝑎 e
𝑐𝑒𝑑
tensão de rotura 𝜎 = 350 𝑀𝑃𝑎 (SAE-AISI 1010 (S10C, G10100) Carbon Steel:
𝑢
MakeItFrom.Com).
De seguida, através da equação 3.8, calculou-se o valor de tensão de cedência ao corte
(𝜏 ), aproximando este valor a 60% da tensão de cedência (𝜎 ) do material, obtendo-
𝑐𝑒𝑑 𝑐𝑒𝑑
se assim um valor de 114 MPa.
𝜏 = 0,6 𝜎 (3.8)
𝑐𝑒𝑑 𝑐𝑒𝑑
Projetou-se o veio para a cedência ao corte, impondo um coeficiente de segurança (CS)
de 1,5. Obtendo-se assim, através da equação 3.9, uma tensão de corte admissível
(𝜏 ) de 76 MPa.
𝑎𝑑𝑚
24

𝜏
𝑐𝑒𝑑
𝜏 = (3.9)
𝑎𝑑𝑚 𝐶𝑆
𝑇
33 𝑙â𝑚𝑖𝑛𝑎𝑠
𝜏 =
𝑚á𝑥 3 (3.10)
0,217 𝑏 𝐷2
2
Sendo o comprimento de um lado do pentágono (b) 23.09 mm, assumindo que o valor
de tensão de corte máxima (𝜏 ) corresponde à tensão de corte admissível (𝜏 ), e
𝑚á𝑥 𝑎𝑑𝑚
com o valor de binário total máximo aplicado ao veio (𝑇 ), foi possível, através
33 𝑙â𝑚𝑖𝑛𝑎𝑠
da equação 3.10, obter diâmetro necessário do veio (D) para que este suportasse as
cargas de trituração, obtendo-se um valor de 74,2 mm.
Conclui-se que o valor obtido é bastante elevado e seria irrealista utilizar um veio com
74,2 mm de diâmetro no equipamento em questão. Para tal, optou-se por reconfigurar
o triturador, alterando o número de lâminas a atuar em simultâneo, de modo a se reduzir
o esfoço aplicado ao veio.
Deste modo, desenvolveu-se a configuração da Figura 3.4, onde se reduziu o número
de lâminas a atuar em simultâneo para 5, desfasando-as umas das outras de modo a
se obter uma trituração mais uniforme. Aumentou-se, também, a espessura das
mesmas para 4 mm e considerou-se que o material a triturar possui, 5 mm de espessura,
obtendo-se assim uma nova área de corte de 20 𝑚𝑚2.
Figura 3.4 – Configuração final do 1º estágio de trituração com 5 lâminas a atuar
simultaneamente
25

Deste modo, mantendo-se o valor da resistência ao corte do PLA (𝜏(𝑏𝑟) ) de 52,92
𝑃𝐿𝐴
MPa foi possível recalcular, através da mesma Equação 3.5, uma nova força de corte
de 1058,4 N.
Realizando novamente o procedimento de cálculo das equações 3.7 e 3.10, no entanto,
para 5 lâminas em vez de 33, obteve-se um seguinte binário total aplicado ao veio
(𝑇 ) de 317,5 Nm e um diâmetro mínimo do veio (D) de 23,6 mm. Sendo assim,
5 𝑙â𝑚𝑖𝑛𝑎𝑠
optou-se por um diâmetro, da zona mais estreita, de 26 mm, de modo a se garantir uma
segurança superior, como ilustra a Figura 3.5.
Figura 3.5 – Modelo CAD do veio
3.1.4 Estrutura, elementos de ligação e componentes auxiliares
De modo a sustentar o triturador bem como o motor elétrico e os elementos
transmissores, foi necessário desenvolver uma estrutura resistente. Para tal, optou-se
por criar uma estrutura à base de calhas e elementos de união Bosch pré-fabricados.
Para fortalecer a segurança durante o funcionamento do equipamento, projetaram-se 5
chapas em acrílico que encaixam nas calhas e impedem a aproximação do utilizador
aos componentes móveis. Para a montagem do triturador, motor e placa de acrílico
superior à estrutura, optou-se por parafusos e porcas normalizados. A Figura 3.6 ilustra
o modelo CAD desenvolvido, utilizando-se os componentes sintetizados na Tabela 3.3.
26

Figura 3.6 – Estrutura de suporte do 1º estágio de trituração
Tabela 3.3 – Componentes normalizados utilizados no 1º estágio
| Quantidade  | Componente               | Dimensões [mm]   |
| ----------- | ------------------------ | ---------------- |
| 4           | Calha Bosch              | 80 x 80 x 460    |
| 2           | Calha Bosch              | 80 x 80 x 1082   |
| 2           | Calha Bosch              | 80 x 80 x 357    |
| 1           | Calha Bosch              | 40 x 40 x 357    |
| 1           | Chapa metálica           | 1076 x 511 x 3   |
| 2           | Placa acrílico maior     | 1106 x 288 x 10  |
| 2           | Placa acrílico menor     | 381 x 288 x 10   |
| 1           | Placa acrílico superior  | 1212 x 487 x 10  |
| 8           | Suporte de canto         | 80 x 80          |
| 4           | ISO 7045                 | M10 x 20         |
| 6           | ISO 7045                 | M6 x 10          |
| 6           | ISO 4016                 | M12 x 55         |
| 2           | ISO 4034                 | M12              |
| 4           | ISO 4016                 | M16 x 65         |
| 4           | ISO 4034                 | M16              |
| 8           | ISO 4016                 | M6 x 30          |
| 16          | ISO 10642                | M5 x 12          |

27

Para ser possível assegurar a correta alimentação e extração do material no triturador,
optou-se por desenvolver um funil de alimentação e uma tremonha por onde irá escoar
o material. O funil situa-se antes do 1º estágio de trituração e tem como objetivo orientar
o material a triturar para a câmara de trituração, possuindo paredes em acrílico, para
ser possível observar o funcionamento do triturador.
A tremonha encontra-se após o 1º estágio de trituração e impede que granulado com
dimensões indesejáveis, ou seja, com dimensão máxima superior a 5 mm, seja admitido
para o segundo estágio de trituração. Esta serve também para guiar o material triturado
para o 2º estágio de trituração. Na figura 3.7, é possível observar a geometria do mesmo,
identificando-se a zona, na lateral, por onde o granulado que não passa pela tremonha,
escoa. Este é, posteriormente, recolhido e admitido novamente no funil de alimentação
para ser novamente triturado.
Figura 3.7 – Tremonha do 1º estágio
Por fim, na figura 3.8, consegue-se observar o modelo final do 1º estágio de trituração,
desde os elementos projetados anteriormente, aos elementos normalizados
selecionados.
28

Figura 3.8 – Modelo final do 1º estágio de trituração
3.1.5 Motor, acoplamento, rolamentos e elementos de transmissão
A seleção do motor foi feita com base no binário total aplicado ao veio, proveniente da
força de corte do polímero, nas várias lâminas. Como não se quer que o material seja
projetado, mas sim triturado lentamente de modo a escoar e se obter um granulado de
boas dimensões, optou-se por utilizar uma velocidade de rotação reduzida. Deste modo,
definiu-se uma velocidade de rotação ao primeiro veio (𝑛) de 40 rpm.
𝜋
𝑃 = 𝑇 (𝑛 )𝜂 (3.11)
𝑚𝑖𝑛 5 𝑙â𝑚𝑖𝑛𝑎𝑠 30 𝑒𝑛𝑔
Através da equação 3.11, conhecendo-se o valor do binário máximo aplicado, e com
uma eficiência de engrenagens helicoidais de 95% (𝜂 = 1.05), obteve-se um valor de
𝑒𝑛𝑔
potência mínima de trituração (𝑃 ) de 1,4kW.
𝑚𝑖𝑛
Face às opções do mercado, optou-se por um moto-redutor com 1,5 kW de potência,
360 Nm de binário e velocidade de saída de 40 rpm.
De modo a transmitir a potência do motor para o triturador, optou-se por um
acoplamento de garras elástico, com corpo em alumínio, cujo modelo 3D está presente
na Figura 3.9.
29

Figura 3.9 – Modelo CAD do acoplamento
Para se obterem velocidades de rotação diferentes em ambos os veios do triturador, foi
necessário impor uma relação de transmissão entre as duas engrenagens que
transmitem a potência do motor. Deste modo, optou-se pelas engrenagens helicoidais
KHG2-45RJ25 e KHG2-60RJ25 para se obter uma relação de transmissão de 1,33,
tendo os veios velocidades de rotação de 40 rpm e 30 rpm, respetivamente.
Por fim, para suportar os veios e permitir a eficiente rotação dos mesmos, selecionaram-
se 4 rolamentos de esferas SKF 306, devido às suas dimensões.
3.2 2º Estágio de Trituração
De forma a se obter um granulado final com as dimensões desejadas, após o mesmo
ser triturado pelas lâminas rotativas, passa pela tremonha do 1º estágio e segue para o
2º estágio de trituração onde, através de uma geometria de corte mais refinada, uma
velocidade de rotação elevada e várias passagens, se irá obter um granulado de
menores dimensões.
3.2.1 Navalhas
De forma semelhante ao 1º estágio, iniciou-se o projeto deste estágio pela configuração
do corte, originado pelas navalhas. Para tal, optou-se pela configuração exemplificada
na Figura 3.10. Esta trata-se de uma navalha com ângulo de corte de 40º e que efetua
o corte, aprisionando o material entre a sua aresta e a rede metálica, como se verifica
na Figura 3.11.
30

Figura 3.10 – Modelo da navalha
Figura 3.11 – Configuração do corte do 2º estágio
De modo a ser possível caracterizar a força de corte gerada durante o processo de corte
polímero, utilizou-se a expressão da equação 3.12 (Keresztes et al., 2011).
𝐹 = 𝑘 𝐴 (3.12)
𝑠
Para se obter a área de corte (A), multiplicou-se a largura total da lâmina, de 160 mm,
pela profundidade de corte e considerou-se que apenas 10% da lâmina se encontra a
triturar o material, em cada passagem. Sendo que apenas são admitidos, no 2º estágio,
granulados de dimensões máximas de 5 mm, e que o corte se obtém quando a lâmina
raspa no polímero, que se encontra aprisionado pela rede metálica, estimou-se que a
profundidade de corte seria cerca de metade da dimensão máxima do granulado, ou
seja, 2,5 mm.
Relativamente ao valor da pressão especifica de corte (𝑘 ), observa-se, através do
𝑠
gráfico da Figura 3.12 que a mesma decresce com a diminuição da profundidade de
31

corte. Para uma profundidade de corte de 2,5 mm, estimou-se que a pressão especifica
de corte seria cerca de 25 MPa (Keresztes et al., 2011).
Desta forma obteve-se um valor de força de corte (F) aplicado às lâminas, de 1000 N.
Figura 3.12 – Evolução da pressão especifica de corte com a profundidade de corte (Keresztes
et al., 2011).
Relativamente ao material constituinte das mesmas, optou-se pelo mesmo das lâminas
do 1º estágio, o aço inox AISI 310S, fornecido em formato de chapa calibrada.
3.2.2 Configuração
De forma a transmitir a potência do motor e se realizar a trituração do material
eficazmente, desenvolveu-se a configuração da Figura 3.13. Esta conta com um veio
rotativo com geometria de secção circular variável e duas zonas de secção hexagonal
onde se aparafusam as navalhas de corte. De modo a providenciar uma segurança
extra, durante o processo de corte, desenvolveram-se dois batentes hexagonais, de
dimensão ligeiramente superior ao veio, que aparafusam às laterais e constrangem as
navalhas, impedindo-as de se moverem.
32

Figura 3.13 – Conjunto do veio, navalhas e batentes, do 2º estágio
De modo a garantir a sua estabilidade e correto funcionamento, o veio encontra-se
suportado à estrutura exterior por um rolamento de esferas e é na sua extremidade
esquerda onde estará unido o acoplamento que transmite a potência do motor.
Para se ter a certeza de que o granulado final possui as dimensões desejadas de, no
máximo, 3,5 mm, configurou-se o equipamento para que durante a trituração, as
navalhas de corte aprisionem o granulado entre a rede metálica, onde o material será
forçado a passar pelos furos da mesma ou será novamente triturado, até o desejado
acontecer. Na Figura 3.14, é possível observar a configuração desenvolvida onde se
pode ter a perceção do funcionamento da mesma.
Figura 3.14 – Configuração do 2º estágio, com 3 navalhas rotativas
33

3.2.3  Estrutura, elementos de ligação e componentes auxiliares
Relativamente à estrutura que sustenta o 2º estágio de trituração, optou-se, para
otimização de projeto, por utilizar uma estrutura semelhante à do 1º estágio, fazendo
apenas pequenas alterações ao nível da posição dos furos de retenção do triturador e
do motor elétrico, bem como nas placas laterais de acrílico, para impedir a aproximação
do utilizador aos componentes móveis. Estas alterações são visíveis na Figura 3.15.

Figura 3.15 – Estrutura de suporte do 2º estágio de trituração
Semelhantemente ao 1º estágio, para montagem do triturador e motor à estrutura,
optou-se por parafusos e porcas normalizados, como ilustra a Tabela 3.4.
Tabela 3.4 – Componentes normalizados utilizados no 2º estágio
| Quantidade  |     | Componente            | Dimensões [mm]   |                 |
| ----------- | --- | --------------------- | ---------------- | --------------- |
|             | 4   | Calha Bosch           |                  | 80 x 80 x 460   |
|             | 2   | Calha Bosch           |                  | 80 x 80 x 1082  |
|             | 2   | Calha Bosch           |                  | 80 x 80 x 357   |
|             | 1   | Calha Bosch           |                  | 40 x 40 x 357   |
|             | 1   | Chapa metálica        |                  | 1076 x 511 x 3  |
|             | 2   | Placa acrílico maior  | 1106 x 395 x 10  |                 |
|             | 2   | Placa acrílico menor  |                  | 381 x 400 x 10  |
|             | 8   | Suporte de canto      |                  | 80 x 80         |
|             | 10  | ISO 4016              |                  | M12 x 55        |
|             | 10  | ISO 4034              |                  | M12             |
|             | 8   | ISO 4016              |                  | M6 x 45         |
|             | 6   | ISO 7045              |                  | M10 x 20        |
34

De forma a se obter a correta extração do granulado, para este poder ser recolhido,
desenvolveu-se, de forma semelhante ao 1º estágio, uma tremonha, ilustrado na Figura
3.16. Este encontra-se na secção final do triturador e, através das 2 orelhas, é retido à
chapa metálica por 2 parafusos e porcas.
Figura 3.16 – Tremonha do 2º estágio
Por fim, na Figura 3.17, é possível observar o modelo final do 2º estágio de trituração,
desde os elementos projetados, aos elementos normalizados selecionados.
Figura 3.17 – Modelo final do 2º estágio de trituração
3.2.4 Motor, acoplamento, rolamento e elementos de transmissão
A seleção do motor que alimenta o triturador do 2º estágio foi feita com base no binário
produzido na trituração e na velocidade de rotação do veio. Ao contrário do 1º estágio,
neste deseja-se que a velocidade de rotação seja elevada de modo que a trituração se
dê tanto pelo corte do material, bem como pelo impacto das navalhas no mesmo. Ao
selecionar uma velocidade de rotação elevada, caso o material não fique triturado na
primeira passagem, rapidamente volta a ser triturado e assim possui-se uma elevada
cadência de trituração. Deste modo, optou-se por uma velocidade de rotação (𝑛) de 200
35

rpm. Para se calcular o binário, multiplicou-se a força de corte (F = 1000 N), calculada
em 3.2.1, pela distância entre a extremidade das lâminas ao centro do veio, sendo esta
77,87 mm. Obtendo-se assim um valor de binário produzido pela trituração de 77,87
Nm.
𝜋
𝑃 =𝑇 𝑛 (3.13)
𝑚𝑖𝑛 30
Através da equação 3.13, foi possível obter um valor de potência mínima (𝑃 ) que o
𝑚𝑖𝑛
motor necessita de ter, de 1,63 kW. Face às opções do mercado, optou-se por um moto-
redutor com 2,2 kW de potência, 106 Nm de binário e velocidade de saída de 193 rpm.
Optando-se por este motor, não é possível garantir a velocidade de rotação de 200 rpm,
no entanto, sendo a diferença bastante ligeira, não haverá impacto no funcionamento
do equipamento.
Para transmitir a potência do motor para o triturador, utilizou-se o um acoplamento de
garras elástico semelhante ao do 1º estágio, apenas com diâmetros para entrada de
veios diferentes.
Relativamente ao rolamento utilizado para sustentar o veio, optou-se por um rolamento
de esferas SKF 62208-2RS1, devido às suas dimensões.
36

4 Modelação de Elementos Finitos
De modo a se projetar um equipamento estruturalmente estável, considerou-se
importante ir além apenas da conceção dos componentes, realizando-se, deste modo,
análises estruturais por elementos finitos a alguns dos componentes mais críticos do
equipamento. Foram alvo de estudo o veio e lâminas do 1º estágio de trituração, o veio
do 2º estágio de trituração bem como a estrutura de ambos os estágios, face às
condições de carregamento do 1º estágio, sendo estas as mais exigentes.
4.1 Lâminas e veio do 1º estágio
Iniciaram-se as análises estruturais pelo subconjunto veio + lâminas, onde foram
simuladas as condições de funcionamento. Estas são, nomeadamente, as forças
aplicadas nas lâminas, previamente calculadas, e as zonas de constrangimento, que
correspondem às zonas onde o veio se encontra suportado pelos rolamentos e à zona
do escatel do veio, que está conectado às engrenagens.
Deste modo, para se iniciar a simulação, considerou-se a situação mais exigente, onde
as lâminas encontram-se a triturar o material, ou seja, está a ser aplicada força sobre
as mesmas, mas o veio encontra-se numa posição estática e preso pelos elementos
transmissores. Na Figura 4.1 é possível identificar visualmente a modelação das cargas
e constrangimentos.
Figura 4.1 – Modelo de elementos finitos do 1º estágio
Realizando-se o estudo e observando-se primeiro o comportamento das lâminas,
identifica-se, na Figura 4.2, um valor máximo de tensão de Von Mises de 23,47 MPa.
Sendo a tensão de cedência do material 300 MPa, é possível concluir que que as
mesmas se encontram em segurança, durante o processo de trituração.
37

Figura 4.2 – Resultados da análise por elementos finitos às lâminas
De seguida analisou-se o comportamento do veio face às mesmas condições. Iniciou-
se o estudo utilizando uma dimensão de malha de elementos finitos de 10 mm e obteve-
se um valor máximo de tensão de Von Mises de 181,9 MPa (Figura 4.3 à esquerda).
Visto este valor ser elevado e estar localizado numa zona de mudança de geometria,
optou-se por realizar um estudo de refinamento de malha local, começando-se com uma
dimensão de elementos de malha de 10 mm e finalizando-se com 0,5 mm. A Figura 4.3
à direita ilustra o resultado da simulação com a malha de 0,5 mm, podendo-se identificar
o local sob maior esforço.
Figura 4.3 – À esquerda: modelo de simulação do 1º estágio com malha de 10 mm. À direita:
modelo de simulação do 1º estágio com malha final refinada de 0,5 mm.
De acordo com a Tabela 4.1 e a Figura 4.4, observa-se que, ao refinar a malha, o valor
de tensão máxima aumenta drasticamente, o que leva a concluir que se está perante
uma singularidade de tensões, devido à zona ser de mudança de geometria e aplicação
38

de constrangimentos. Com isto, não se possui confiança nos resultados obtidos, ou seja,
não é possível estimar o valor real de tensão máxima no veio.
Tabela 4.1 – Evolução dos valores de tensão de von Mises conforme a dimensão da malha,
para o modelo inicial do veio do 1º estágio
| Dimensão dos elementos  |               |                  | Tensão von  |
| ----------------------- | ------------- | ---------------- | ----------- |
| Iteração                | H=1/dimensão  |                  |             |
| de malha [mm]           |               | Mises [σ] [MPa]  |             |
| 1                       | 10            | 0,1              | 181,9       |
| 2                       | 8             | 0,125            | 164,6       |
| 3                       | 6             | 0,167            | 171,1       |
| 4                       | 4             | 0,25             | 198,4       |
| 5                       | 2             | 0,5              | 214,6       |
| 6                       | 1             | 1                | 346,1       |
| 7                       | 0,5           | 2                | 596,9       |

Figura 4.4 – Evolução dos valores de tensão de von-Mises conforme a dimensão da malha,
para o modelo inicial do veio do 1º estágio
Para ultrapassar este desafio, optou-se por alterar ligeiramente a configuração do
modelo de elementos finitos. Deste modo, desenvolveu-se o modelo da Figura 4.5 onde
se alterou a geometria do veio, removendo-se as mudanças bruscas de geometria,
através  de  boleados  e  optou-se  por  adicionar  uma  chaveta  onde  se  aplicou  o
constrangimento que limita a rotação do veio. De forma a simular a limitação de
movimento provocada pelo acoplamento, adicionou-se um constrangimento axial, na
extremidade esquerda do veio, correspondendo este modelo à situação real.
39

Figura 4.5 – Modelo otimizado por elementos finitos do 1º estágio
De forma semelhante ao que foi feito para o modelo anterior, realizou-se um refinamento
de malha local na zona de maior tensão para ser possível identificar o valor real de
tensão máxima. Na Figura 4.6 observa-se a iteração inicial (à esquerda), com dimensão
de elementos de malha de 10 mm e a final (à direita), com 0,5 mm, observando-se que
a zona mais critica não altera.
Figura 4.6 – À esquerda: modelo otimizado de simulação do 1º estágio com malha de 10 mm. À
direita: modelo otimizado de simulação do 1º estágio com malha final refinada de 0,5 mm.
Após realizar o segundo estudo observou-se que o problema da singularidade de
tensões, embora diminuísse, persistia ao refinar a malha, como se observa na Tabela
4.2 e na Figura 4.7, de evolução dos valores de tensão máxima. Outro parâmetro que
se considerou importante analisar foi o deslocamento máximo das lâminas, de modo a
entender se este iria pôr em causa o correto funcionamento do triturador. Analisando-
se o deslocamento para as várias dimensões de elementos da malha, observou-se que
este se mantém praticamente constante, variando apenas 0,001 mm e não excedendo
0,056 mm.
40

Tabela 4.2 – Evolução dos valores de tensão de von Mises conforme a dimensão da malha,
para o modelo otimizado do veio do 1º estágio
| Dimensão dos elementos  |                |        | Tensão von        | Deslocamento     |
| ----------------------- | -------------- | ------ | ----------------- | ---------------- |
| Iteração                | H=1/dimensão   |        |                   |                  |
|                         | de malha [mm]  |        | Misses [σ] [MPa]  | Máximo [δ] [mm]  |
| 1                       | 10             | 0,1    | 131,8             | 0,055            |
| 2                       | 8              | 0,125  | 138,6             | 0,055            |
| 3                       | 6              | 0,167  | 141,6             | 0,055            |
| 4                       | 4              | 0,25   | 145,5             | 0,056            |
| 5                       | 2              | 0,5    | 155,9             | 0,056            |
| 6                       | 1              | 1      | 225,5             | 0,056            |
| 7                       | 0,5            | 2      | 332,6             | 0,056            |

Figura 4.7 – Evolução dos valores de tensão de von Mises conforme a dimensão da malha,
para o modelo otimizado do veio do 1º estágio
De modo a ser possível identificar o valor máximo real de tensão de Von-Mises optou-
se por utilizar a ferramenta probe do software e analisar como evoluía a tensão na zona
mais crítica, sendo esta onde o valor da tensão é mais elevado, ou seja, no boleado.

41

Tabela 4.3 – Evolução dos valores de tensão de von Mises conforme a dimensão da malha,
para o modelo otimizado do veio do 1º estágio, utilizando a ferramenta probe
| Dimensão dos elementos  |               | Tensão von Mises  |            |
| ----------------------- | ------------- | ----------------- | ---------- |
| Iteração                | H=1/dimensão  |                   |            |
| de malha [mm]           |               |                   | [σ] [MPa]  |
1
|     | 10  | 0,1    | 129,6  |
| --- | --- | ------ | ------ |
| 2   | 8   | 0,125  | 138,6  |
| 3   | 6   | 0,167  | 138,6  |
| 4   | 4   | 0,25   |        |
135
5
|     | 2    | 0,5  | 133,7  |
| --- | ---- | ---- | ------ |
| 6   | 1    | 1    | 135,6  |
| 7   | 0,5  | 2    | 137,1  |

Figura 4.8 – Evolução dos valores de tensão de von Mises conforme a dimensão da malha,
para o modelo otimizado do veio do 1º estágio, utilizando a ferramenta probe
Na Tabela 4.3 e Figura 4.8, que apresentam os resultados do último estudo, observa-
se que o valor de tensão máxima de von Mises converge para 135,5 MPa, podendo
concluir que este é o valor real de tensão máxima a que o veio está sujeito, estando
este em segurança com coeficiente de 1,4.
4.2  Navalhas e veio do 2º estágio
Para  o  2º  estágio  de  trituração  procedeu-se  à  análise  por  elementos  finitos  do
subconjunto composto pelo veio e as navalhas de corte. De forma semelhante ao
realizado para o 1º estágio, simularam-se as forças e os constrangimentos aplicados ao
conjunto. Relativamente à força, esta corresponde à força de corte do polímero (1000
42

N). Os constrangimentos correspondem às zonas onde o veio se encontra suportado
pelo rolamento e a pelo acoplamento de veios, como se observa na Figura 4.9.
Apoios F = 1000 N
Figura 4.9 – Modelo de elementos finitos do 2º estágio
Foi realizada a análise estrutural, onde foi analisado, inicialmente, o comportamento das
navalhas de corte.
Figura 4.10 – Resultados da análise por elementos finitos às navalhas
Do resultado da simulação, observado na Figura 4.10, observa-se que o valor de tensão
máxima sobre o qual as navalhas estão sujeitas, é bastante reduzido, podendo concluir
que as mesmas se encontram em segurança, durante o processo de trituração.
De seguida analisou-se o comportamento do veio face às mesmas condições.
Semelhantemente à primeira análise estrutural, são propensas a zonas de concentração
de tensões, a zona de aplicação do constrangimento do rolamento e a zona de mudança
43

brusca de geometria do veio. De modo a minimizar o efeito da mesma, optou-se por
adicionar um boleado à zona de mudança de geometria. Como este é o local mais critico
do veio, será onde a tensão real será mais elevada e, portanto, foi este o local onde foi
analisado o valor de tensão máxima para estudar a integridade estrutural do veio.
A Figura 4.11 ilustra o estudo de convergência de malha elaborado para se tentar obter
o valor de tensão máxima no veio. Observa-se que, a zona de singularidade de tensões
permanece em torno do apoio de rolamento e, desta forma, avaliou-se o valor máximo
de tensão na zona do boleado.

Figura 4.11 – À esquerda: modelo de simulação do 2º estágio com malha de 10 mm. À direita:
modelo de simulação do 2º estágio com malha final refinada de 0,5 mm.
Tabela 4.4 – Evolução dos valores de tensão de Von-Mises conforme a dimensão da malha,
para o veio do 2º estágio, utilizando a ferramenta probe
| Dimensão dos elementos  |               |                   | Tensão von  |
| ----------------------- | ------------- | ----------------- | ----------- |
| Iteração                | H=1/dimensão  |                   |             |
| de malha [mm]           |               | Misses [σ] [MPa]  |             |
| 1                       | 10            | 0,1               | 26,06       |
| 2                       | 8             | 0,125             | 25,57       |
| 3                       | 6             | 0,167             | 25,63       |
| 4                       | 4             | 0,25              | 25,86       |
| 5                       | 2             | 0,5               | 26,17       |
| 6                       | 1             | 1                 | 27,24       |
7
|     | 0,5  | 2   | 27,95  |
| --- | ---- | --- | ------ |

44

Figura 4.12 - Evolução dos valores de tensão de von Mises conforme a dimensão da malha,
para o veio do 2º estágio, utilizando a ferramenta probe
Realizando-se o processo iterativo observa-se, na Tabela 4.4 e Figura 4.12, que o valor
de tensão máxima de von Mises converge para cerca de 28 MPa, podendo concluir que
este é o valor real de tensão máxima a que o veio está sujeito, estando este em
segurança à cedência.
4.3 Estrutura
Para redução de custos de projeto e sendo os dois estágios de trituração
geometricamente semelhantes, utilizou-se a mesma estrutura para acomodar ambos.
Sendo crucial que a estrutura se encontre estruturalmente estável durante o
funcionamento do equipamento, analisou-se qual o estágio de trituração possui o maior
peso, ou seja, que exerce uma maior carga sobre a estrutura. Tendo-se todos os
componentes projetados, concluiu-se que o 1º estágio possui um peso total de 92 kg e
o 2º estágio 73 kg.
Para analisar estruturalmente a estrutura onde assenta o 1º estágio de trituração,
realizou-se uma análise estática onde se simulou uma situação extrema onde o
equipamento encrava e o binário máximo produzido pela trituração (T) de 317,5 Nm é
transmitido para a estrutura. Para esta simulação, o binário foi convertido em duas
forças, com sentidos opostos e aplicadas nos rasgos de retenção do motor elétrico,
como é possível observar na Figura 4.13. Através da equação 4.1, multiplicando o
binário (T) pela distância entre os rasgos onde as mesmas serão aplicadas (dist), que
corresponde a 187,5 mm, obtiveram-se valores de força de 29,8 N.
45

𝐹
𝑇= (4.1)
𝑑𝑖𝑠𝑡
Figura 4.13 – Cargas aplicadas no modelo de análise da estrutura
Na Figura 4.14, observam-se os constrangimentos da simulação, estes correspondem
às zonas onde o triturador se encontra aparafusado à estrutura.
Figura 4.14 – Constrangimentos aplicados no modelo de análise da estrutura
Realizando-se a simulação, como se verifica na Figura 4.15, observa-se que a estrutura
se encontra em segurança face às cargas aplicadas, sendo que o valor máximo de
tensão de von Mises máximo é 7,74 MPa, bastante abaixo da tensão de cedência do
material.
46

Figura 4.15 – Resultados da análise por elementos finitos à estrutura
Desta forma, é possível concluir que a estrutura se encontra estruturalmente estável e
capaz de suportar ambos os estágios de trituração em segurança.
47

5 Conclusões e trabalho futuro
O quinto, e último capítulo, consiste na conclusão do TFM bem como propostas para
possível trabalho futuro.
5.1 Conclusões
Em relação aos objetivos definidos no início do documento, é seguro dizer que estes
foram cumpridos, tendo-se efetivamente projetado um equipamento especializado na
trituração de polímero, otimizado especificamente para a trituração de PLA e ABS. O
projeto encontra-se totalmente definido, desde os componentes modelados, aos
componentes normalizados e de catálogo que, funcionando em sincronia, permitem o
correto funcionamento do triturador.
Devido à necessidade de identificação das propriedades mecânicas do PLA e ABS,
numa fase inicial do projeto foram realizados ensaios de macrodureza Vickers, onde se
pode concluir que as propriedades mecânicas das peças testadas em PLA são
semelhantes aos estudos encontrados na literatura. Por outro lado, para o ABS, os
valores das propriedades mecânicas obtidos experimentalmente, diferem dos
identificados na literatura. Porém, como o PLA apresenta uma maior dureza e tensão
de rotura, dimensionou-se o equipamento para o mesmo material, não se considerando
preocupante o desvio de dureza detetado no ABS.
Relativamente ao funcionamento do triturador, é de salientar a importância da utilização
de dois estágios de trituração distintos, sendo que, ao utilizarem mecanismos de corte
diferentes, permitem a obtenção de granulado de diferente exigência dimensional.
Sendo o primeiro estágio focado na trituração de peças de maiores dimensões,
eliminando a sua forma original. Ao passo que o segundo estágio, através de um corte
refinado de alta velocidade, permite a transformação de material já na forma de
granulado, em granulado de dimensões inferiores, capaz de ser admitido num
equipamento de conversão de granulado em filamento (extrusora).
Em relação aos materiais utilizados no equipamento, salienta-se a utilização do aço AISI
310S em componentes de alta precisão dimensional, como as lâminas e navalhas. Aços
carbono AISI 1010 e AISI 1050 em componentes estruturais, como os veios. A liga de
alumínio EN-AW 2017A em componentes de exigência estrutural inferior, como as
placas laterais de ambos os estágios e, ainda o polímero PET em componentes onde a
principal função é a forma do mesmo e não as propriedades mecânicas.
48

5.2 Trabalho futuro
Propõem-se para trabalho futuro alguns aspetos que poderiam melhorar e otimizar o
projeto, como a realização de análises estruturais a outros componentes, embora menos
exigentes para o funcionamento do equipamento, podendo estes ser, possivelmente,
redimensionados. A realização de análises de otimização topológica a alguns
componentes como por exemplo os veios, lâminas e navalhas, de modo a reduzir os
possíveis custos de fabrico.
De modo a testar a exequibilidade do projeto, seria interessante proceder-se à definição
dos processos de fabrico de cada componente com o objetivo de produzi-los e realizar
a montagem do mesmo, segundo os desenhos de definição.
49

Referências Bibliográficas
3D Printing Technology Comparison: FDM vs. SLA vs. SLS | Formlabs. (n.d.).
Retrieved September 11, 2023, from https://formlabs.com/eu/blog/fdm-vs-
sla-vs-sls-how-to-choose-the-right-3d-printing-technology/
3D printing with PLA vs. ABS: What’s the difference? | Hubs. (n.d.). Retrieved
October 26, 2023, from https://www.hubs.com/knowledge-base/pla-vs-abs-
whats-difference/
Agrawal, A. P., Kumar, V., Kumar, J., Paramasivam, P., Dhanasekaran, S., &
Prasad, L. (2023). An investigation of combined effect of infill pattern, density,
and layer thickness on mechanical properties of 3D printed ABS by fused
filament fabrication. Heliyon, 9(6).
https://doi.org/10.1016/J.HELIYON.2023.E16531
AISI 310S (S31008) Stainless Steel :: MakeItFrom.com. (n.d.). Retrieved
February 20, 2024, from https://www.makeitfrom.com/material-
properties/AISI-310S-S31008-Stainless-Steel
Beltrán, F. R., Arrieta, M. P., Moreno, E., Gaspar, G., Muneta, L. M., Carrasco-
Gallego, R., Yáñez, S., Hidalgo-Carvajal, D., de la Orden, M. U., & Urreaga,
J. M. (2021). Evaluation of the Technical Viability of Distributed Mechanical
Recycling of PLA 3D Printing Wastes. Polymers 2021, Vol. 13, Page 1247,
13(8), 1247. https://doi.org/10.3390/POLYM13081247
Costabile, G., Fera, M., Fruggiero, F., Lambiase, A., & Pham, D. (2017). Cost
models of additive manufacturing: A literature review. International Journal of
Industrial Engineering Computations, 8, 263–282.
https://doi.org/10.5267/j.ijiec.2016.9.001
Durga Rajesh, K. V., Ganesh, N., Yaswanth Kalyan Reddy, S., Mishra, H., & Teja
Naidu, T. M. V. P. S. (2023). Experimental research on the mechanical
characteristics of fused deposition modelled ABS, PLA and PETG specimens
printed in 3D. Materials Today: Proceedings.
https://doi.org/10.1016/J.MATPR.2023.06.343
GP20 Plastic Shredder Hybrid | 3devo. (n.d.). Retrieved November 17, 2023, from
https://www.3devo.com/gp20-plastic-shredder
Hill, R. M. (1986). THREE TYPES OF LOW SPEED SHREDDER DESIGN.
Kanishka, K., & Acherjee, B. (2023). Revolutionizing manufacturing: A
comprehensive overview of additive manufacturing processes, materials,
developments, and challenges. In Journal of Manufacturing Processes (Vol.
50

107, pp. 574–619). Elsevier Ltd.
https://doi.org/10.1016/j.jmapro.2023.10.024
Keresztes, R., Kalácska, G., Zsidai, L., & Dobrocsi, Z. (2011). Machinability of
engineering polymers. International Journal Sustainable Construction &
Design, 2(1), 106–114. https://doi.org/10.21825/SCAD.V2I1.20467
Kolyuda, V. (2021). Desenvolvimento de uma Cabeça de Maquinagem para uma
Impressora 3D FDM de 5 eixos.
Kumar Patro, P., Kandregula, S., Suhail Khan, M. N., & Das, S. (2023).
Investigation of mechanical properties of 3D printed sandwich structures
using PLA and ABS. Materials Today: Proceedings.
https://doi.org/10.1016/J.MATPR.2023.08.366
Muthiah, E., Rathanasamy, R., Ravichandran, D., Palanichamy, D., & Sivaraj, S.
(2022). Experimental analysis on shredder for recycling thermoplastics using
injection moulder. Materials Today: Proceedings, 66, 797–803.
https://doi.org/10.1016/J.MATPR.2022.04.353
Nasr, M., & Yehia, K. (2019). Stress Analysis of a Shredder Blade for Cutting
Waste Plastics. Journal of International Society for Science and Engineering.
https://doi.org/10.21608/JISSE.2019.20292.1017
Oliveira, D. M. V. (2018). Estação de reciclagem de polímeros termoplásticos para
impressão 3D.
Rodríguez-Reyna, S. L., Mata, C., Díaz-Aguilera, J. H., Acevedo-Parra, H. R., &
Tapia, F. (2022). Mechanical properties optimization for PLA, ABS and Nylon
+ CF manufactured by 3D FDM printing. Materials Today Communications,
33. https://doi.org/10.1016/J.MTCOMM.2022.104774
SAE-AISI 1010 (S10C, G10100) Carbon Steel :: MakeItFrom.com. (n.d.).
Retrieved February 20, 2024, from https://www.makeitfrom.com/material-
properties/SAE-AISI-1010-S10C-G10100-Carbon-Steel
Saviello, D., Andena, L., Gastaldi, D., Toniolo, L., & Goidanich, S. (2018). Multi-
analytical approach for the morphological, molecular, and mechanical
characterization after photo-oxidation of polymers used in artworks. Journal
of Applied Polymer Science, 135(17). https://doi.org/10.1002/APP.46194
Sedani, C. M., & Sudarshan, M. (2022). FEA AND DESIGN MODIFICATION OF
SHREDDER BLADE USED FOR RECYCLING PLASTIC. International
Journal Of Advanced Research And Innovative Ideas In Education.
https://www.researchgate.net/publication/361163744_FEA_AND_DESIGN_
51

MODIFICATION_OF_SHREDDER_BLADE_USED_FOR_RECYCLING_PL
ASTIC
Shredding Machines: Types, Applications, Advantages, and Standards. (n.d.).
Retrieved October 26, 2023, from
https://www.iqsdirectory.com/articles/shredder/shredding-machine.html
SHREDIITM 5.0 | Mechanical Kit | Action BOX. (n.d.). Retrieved November 17,
2023, from https://actionbox.ca/products/shredii-
5?utm_medium=product_shelf&utm_source=youtube&utm_content=YT-
APM2gMDbzUx-
hObcKxZ_D43rf2OXWdc33cjYFTkqVKquL9E2vuysmMgtZhGHjc8NMNNV0
yHiJXo87tmTfwf8v4GfE6GHEv9rGhd-
Zg6T_7JnzJz17eQCPr1toX_GvsL59iwKIE9PsT2QTk8INg4D9Rog3PV9Aai
MvtN9PPYK1q3NT5TbgGr0sw%3D%3D
Stainless steel mini plastic shredder with NRV050 Reducer(hardening blade) –
DIY Chen. (n.d.). Retrieved November 17, 2023, from
https://diychen.net/product/stainless-steel-mini-plastic-shredder-with-
nrv050-reducer/
Tolerances to EN 10051 for continuously rolled hot rolled plate sheet and strip –
British Stainless Steel Association. (n.d.). Retrieved August 25, 2024, from
https://bssa.org.uk/bssa_articles/tolerances-to-en-10051-for-continuously-
rolled-hot-rolled-plate-sheet-and-strip/
Valavanidis, A. (2022). Recent Developments in Plastic Waste Recycling. Plastic
recycling still remains a challenging area in the waste management sector.
https://www.grandviewresearch.com/industry-analysis/global-plastics-
market
Vicente, C. M. S., Sardinha, M., & Reis, L. (2019). Failure analysis of a coupled
shaft from a shredder. Engineering Failure Analysis, 103, 384–391.
https://doi.org/10.1016/J.ENGFAILANAL.2019.05.011
William F. Smith. (1998). Princípios de Ciência e Engenharia dos Materiais (3a).
Zhang, P., Li, S. X., & Zhang, Z. F. (2011). General relationship between strength
and hardness. Materials Science and Engineering: A, 529(1), 62–73.
https://doi.org/10.1016/J.MSEA.2011.08.061
52

Apêndice A: Desenhos técnicos
53

7
 1931
4
 1491   630
ESCALA:
| NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:5 PB
| DESENHOU | 03/10/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| -------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU
CONJUNTO:
COMPONENTE:
Triturador
TOLERÂNCIA GERAL: NOTAS:
|     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | ----------- | --- | ---------------- | -------- |
ACABAMENTOS: A2
|     |     | 10  |     |     | -   |
| --- | --- | --- | --- | --- | --- |
1/3
SOLIDWORKS Educational Product. For Instructional Use Only.

1
9
8
2
5
6
3
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:5 DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO:
COMPONENTE:
Triturador
TOLERÂNCIA GERAL: NOTAS:
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A2
10 2/3 -
SOLIDWORKS Educational Product. For Instructional Use Only.

NORMA
|     | Nº  |     | DESIGNAÇÃO | QUANT. |     | MATERIAL | OBS. |     |
| --- | --- | --- | ---------- | ------ | --- | -------- | ---- | --- |
DES. Nº
|     | 1   |     | 1º estágio | 1   | 10.10 |     |     |     |
| --- | --- | --- | ---------- | --- | ----- | --- | --- | --- |
|     | 2   |     | 2º estágio | 1   | 10.20 |     |     |     |
Ref:
|     | 3   | Roda com travão D160 F |     | 4   |     |     | Bosch Rexroth |     |
| --- | --- | ---------------------- | --- | --- | --- | --- | ------------- | --- |
3842562057
3.1325 (EN-AW
|     | 4   | Conector de estágios |     | 4   | 10.70 |     |     |     |
| --- | --- | -------------------- | --- | --- | ----- | --- | --- | --- |
2017A)
|     | 5   | Suporte da caixa do granulado |     | 1   | 10.50 | PLA |     |     |
| --- | --- | ----------------------------- | --- | --- | ----- | --- | --- | --- |
|     | 6   | Caixa do granulado            |     | 1   | 10.60 | PLA |     |     |
3.1325 (EN-AW
|     | 7   |     | Pega | 2   | 10.40 |     |     |     |
| --- | --- | --- | ---- | --- | ----- | --- | --- | --- |
2017A)
|     | 8   | Botões de emergência |     | 2   |     |     | Comunidade  |     |
| --- | --- | -------------------- | --- | --- | --- | --- | ----------- | --- |
GRABCAD
3.1325 (EN-AW
|     | 9   | Caixa dos botões de emergência |     | 1   | 10.30 |     |     |     |
| --- | --- | ------------------------------ | --- | --- | ----- | --- | --- | --- |
2017A)
|     | ESCALA: |     | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |     |
| --- | ------- | --- | --------- | --- | ------------------------------------------ | --- | --- | --- |
1:5
DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- | --- |
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     |             | Triturador |        |           |          |
| ----------------- | --- | ------ | --- | ----------- | ---------- | ------ | --------- | -------- |
|                   |     |        |     | DESENHO N.º |            | FOLHA: | MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |        |     | A4          |            |        |           |          |
-
|     |     |     |     | 10  |     | 3/3 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

1
| 4   |     |     | 14  |     | 15  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
 815
 1243
2
3
|     |     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:10
|     |     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --------- | ------- | --- | --------- | --- | --- | --- |
COMPONENTE:
|     | TOLERÂNCIA GERAL: | NOTAS: |     |             | 1º Estágio |                  |          |
| --- | ----------------- | ------ | --- | ----------- | ---------- | ---------------- | -------- |
|     |                   |        |     | DESENHO N.º |            | FOLHA: MASSA[g]: | REVISÃO: |
|     | ACABAMENTOS:      |        |     | A3          |            |                  |          |
-
|     |     |     |     | 10.10 |     | 1/2 |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

6
7
NORMA
|     |     |     |     | Nº  |     | DESIGNAÇÃO |     | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | --- | -------- | ---- |
DES. Nº
|     |     |     |     | 1   | Placa acrilico superior - 1º estágio |                                   |     | 1   | 10.10.60 | Acrílico |     |
| --- | --- | --- | --- | --- | ------------------------------------ | --------------------------------- | --- | --- | -------- | -------- | --- |
|     |     |     |     | 2   |                                      | Placa acrilico maior - 1º estágio |     | 1   | 10.10.40 | Acrílico |     |
13
|     |     |     |     | 3   |     | Placa acrilico menor - 1º estágio |     | 1   | 10.10.50 | Acrílico |     |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | -------- | -------- | --- |
Parafuso de cabeça cilindrica -
| 8   |     |     |     | 4   |     |     |     | 4   | ISO 7045  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
M10 x 20 - Z - 20N
5
|     |     |     |     | 5   |     | Triturador de lâminas |     | 1   | 10.10.10 |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------- | --- | --- |
9 12
|     |     |     |     | 6   |     | Estrutura - 1º estágio |     | 1   | 10.10.30 |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | -------- | --- | --- |
|     |     |     |     | 7   |     | Funil de alimentação   |     | 1   | 10.10.20 |     |     |
Acoplamento de garras em
|     |     |     |     | 8   |     |     |     | 1   | Ref: 23022-25 |     | Norelem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- |
elastómero
11
Parafuso de cabeça cilindrica -
|     |     |     |     | 9   |     |     |     | 6   | ISO 7045 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
M6 x 10 - Z - 10N
|     |     |     |     | 10  |     | Tremonha - 1º estágio |     | 1   | 10.10.15 | PLA |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------- | --- | --- |
Ref:
|     |     |     |     | 11  |     | Motor - 1º estágio |     | 1   |     |     | Sew Eurodrive |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | ------------- |
R77DRN90L4
Parafuso de cabeça hexagonal -
|     |     |  298  |     | 12  |     | M12 x 55 x 30-WN |     | 6   | ISO 4016 |     |     |
| --- | --- | ----- | --- | --- | --- | ---------------- | --- | --- | -------- | --- | --- |
Parafuso de cabeça hexagonal -
|     |     |     |     | 13  |     |     |     | 4   | ISO 4016 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
M16 x 65 x 38-WN
|     |     |     |     | 14      |     | Porca hexagonal - M16 - N |     | 4   | ISO 4034                                   |     |     |
| --- | --- | --- | --- | ------- | --- | ------------------------- | --- | --- | ------------------------------------------ | --- | --- |
|     |     |     |     | 15      |     | Porca hexagonal - M12 - N |     | 6   | ISO 4034                                   |     |     |
|     |     |     |     | ESCALA: |     | NOME DATA                 |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
1:10
|     |     |     |     |     | DESENHOU | PB 08/12/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | --- | -------- | ------------- | --- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     | 10  |     | MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |     |
| --- | --- | --- | --------- | --- | ------- | --- | --------- | --- | --- | --- | --- |
COMPONENTE:
|     |     |     | TOLERÂNCIA GERAL: |     | NOTAS: |     |     |     | 1º estágio |     |     |
| --- | --- | --- | ----------------- | --- | ------ | --- | --- | --- | ---------- | --- | --- |
Vistas sem as placas de
acrilico para ser possivel
|     |     |     |              |     |                               |     | DESENHO N.º |     |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | ------------ | --- | ----------------------------- | --- | ----------- | --- | --- | ---------------- | -------- |
|     |     |     | ACABAMENTOS: |     | identificar os componentes A3 |     |             |     |     |                  |          |
-
|     |     |     |     |     | no interior. |     | 10.10 |     |     | 2/2 |     |
| --- | --- | --- | --- | --- | ------------ | --- | ----- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

1
3
 815
 1247
2
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:10
|     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     |             | 2º estágio |                  |          |
| ----------------- | ------ | --- | ----------- | ---------- | ---------------- | -------- |
|                   |        |     | DESENHO N.º |            | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |        |     | A3          |            |                  |          |
-
|     |     |     | 10.20 |     | 1/1 |     |
| --- | --- | --- | ----- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

10 6
5
NORMA
|     |     |     | Nº  |     |     | DESIGNAÇÃO |     | QUANT. |     |     | MATERIAL | OBS. |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | --- | --- | -------- | ---- |
DES. Nº
9
|     |     |     | 1   |     | Placa acrilico maior - 2º estágio |     |     | 1   |  10.20.30 |     | Acrílico |     |
| --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --------- | --- | -------- | --- |
|     | 4   |     | 2   |     | Placa acrilico menor - 2º estágio |     |     | 1   |  10.20.40 |     | Acrílico |     |
| 9   |     |     | 3   |     | Porca Hexagonal - M12 - N         |     |     | 10  | ISO 4034  |     |          |     |
|     |     |     | 4   |     | Triturador de navalhas            |     |     | 1   | 10.20.10  |     |          |     |
|     |     |     | 5   |     | Estrutura - 2º estágio            |     |     | 1   | 10.20.20  |     |          |     |
8
|     |     |     | 6   |     | Acoplamento de garras em  |     |     | 1   | Ref: 23022-25 |     |     |     |
| --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ------------- | --- | --- | --- |
elastómero
|     |     |     | 7   |     | Tremonha - 2º estágio           |     |     | 1   |  10.20.50 |     | PLA |     |
| --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
|     |     |     | 8   |     | Parafuso de cabeça hexagonal -  |     |     | 8   | ISO 4016  |     |     |     |
M6 x 45 x 18-WN
 064
Parafuso de cabeça hexagonal -
|     |     |     | 9   |     |     |     |     | 10  | ISO 4016 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
M12 x 55 x 30-WN
Ref:
|     |     |     | 10  |     | Motor - 2º estágio |     |     | 1   |     |     |     | Sew Eurodrive |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | ------------- |
R57DRN100LS4
|     |     |     | ESCALA: |     | NOME | DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |     |
| --- | --- | --- | ------- | --- | ---- | ---- | --- | --- | ------------------------------------------ | --- | --- | --- |
1:10
|     |     |     |     | DESENHOU | PB  | 08/12/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |     |
| --- | --- | --- | --- | -------- | --- | ---------- | --- | --- | ----------------------------------------- | --- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     | MATERIAL: |     | APROVOU |     |     | CONJUNTO: |     |     |     |     |     |
| --- | --- | --------- | --- | ------- | --- | --- | --------- | --- | --- | --- | --- | --- |
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: |     | NOTAS:                   |     |     |     |     | 2º estágio |     |     |     |
| --- | --- | ----------------- | --- | ------------------------ | --- | --- | --- | --- | ---------- | --- | --- | --- |
| 7   |     |                   |     | Vistas sem as placas de  |     |     |     |     |            |     |     |     |
acrílico para ser possível
|     |     |              |     |                               |     |     | DESENHO N.º |     |     | FOLHA: | MASSA[g]: | REVISÃO: |
| --- | --- | ------------ | --- | ----------------------------- | --- | --- | ----------- | --- | --- | ------ | --------- | -------- |
|     |     | ACABAMENTOS: |     | identificar os componentes A3 |     |     |             |     |     |        |           |          |
-
|     |     |     |     |     |     |     | 10.20 |     |     | 1/1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
no interior.
SOLIDWORKS Educational Product. For Instructional Use Only.

6
 064
2 1
4 NORMA
|     | Nº  |     |     | DESIGNAÇÃO |     | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | --- | ---------- | --- | ------ | --- | -------- | ---- |
DES. Nº
Ref:
|     | 1   |     | Calha Bosch perfil 80x80x1082 mm |     |     | 2   |     |     | Bosch rexroth |
| --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993133
Ref:
|     | 2   |     | Suporte de canto bosch |     |     | 8   |     |     | Bosch rexroth |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | ------------- |
3842548871
3
 815
Ref:
|     | 3   |     | Calha Bosch perfil 80x80x357 mm |     |     | 2   |     |     | Bosch rexroth |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993133
|     | 4   |     | Placa inferior - 1º estágio |     |     | 1   | 10.10.30.10 | AISI 316 |     |
| --- | --- | --- | --------------------------- | --- | --- | --- | ----------- | -------- | --- |
Ref:
|     | 5   |     | Calha Bosch perfil 40x40x357 mm |     |     | 1   |     |     | Bosch rexroth |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993120
Ref:
|     | 6   |     | Calha Bosch perfil 80x80x460 mm |     |     | 4   |     |     | Bosch rexroth |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993133
|     | ESCALA: |     | NOME | DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --- | ---- | ---- | --- | --- | ------------------------------------------ | --- | --- |
5 1:10
|     |     | DESENHOU | PB  | 03/10/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | -------- | --- | ---------- | --- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
 1243  TRITURADOR
| MATERIAL: |     | APROVOU |     |     | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --- | --- | --------- | --- | --- | --- | --- |
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     |     |             | Estrutura - 1º estágio |     |                  |          |
| ----------------- | --- | ------ | --- | --- | ----------- | ---------------------- | --- | ---------------- | -------- |
|                   |     |        |     |     | DESENHO N.º |                        |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |        |     |     | A3          |                        |     |                  |          |
-
|     |     |     |     |     | 10.10.30 |     |     | 1/1 |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 064
6
2 1
NORMA
|     | Nº  |     |     | DESIGNAÇÃO |     | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | --- | ---------- | --- | ------ | --- | -------- | ---- |
DES. Nº
4
Ref:
|     | 1   |     | Calha Bosch perfil 80x80x1082 mm |     |     | 2   |     |     | Bosch rexroth |
| --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993133
|     | 2   |     | Suporte de canto Bosch |     |     | 8   | Ref:  |     | Bosch rexroth |
| --- | --- | --- | ---------------------- | --- | --- | --- | ----- | --- | ------------- |
3842548871
Ref:
|     | 3   |     | Calha Bosch perfil 80x80x357 mm |     |     | 2   |     |  10.20.40 | Bosch rexroth |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --------- | ------------- |
3842993133
3
|     | 4   |     | Placa inferior - 2º estágio |     |     | 1   | 10.20.20.10 | AISI 316 |     |
| --- | --- | --- | --------------------------- | --- | --- | --- | ----------- | -------- | --- |
 815
Ref:
|     | 5   |     | Calha Bosch perfil 40x40x357 mm |     |     | 1   |     |     | Bosch rexroth |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993120
Ref:
|     | 6   |     | Calha Bosch perfil 80x80x460 mm |     |     | 4   |     |     | Bosch rexroth |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- |
3842993133
|     | ESCALA: |     | NOME | DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --- | ---- | ---- | --- | --- | ------------------------------------------ | --- | --- |
1:10
|     |     | DESENHOU | PB  | 03/10/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | -------- | --- | ---------- | --- | --- | ----------------------------------------- | --- | --- |
5 MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     |     | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --- | --- | --------- | --- | --- | --- | --- |
 1243  COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     |     |             | Estrutura - 2º estágio |     |                  |          |
| ----------------- | --- | ------ | --- | --- | ----------- | ---------------------- | --- | ---------------- | -------- |
|                   |     |        |     |     | DESENHO N.º |                        |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |        |     |     | A3          |                        |     |                  |          |
-
|     |     |     |     |     | 10.20.20 |     |     | 1/1 |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

| 1   | 11  | 12  | 14  | 7   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5
NORMA
|     |     |     |     |     |     | Nº  |     | DESIGNAÇÃO |     | QUANT. | DES. Nº | MATERIAL | OBS. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------- | -------- | ---- |
6
Empilhamento lâminas e
|     |     |     |     |     |     | 1   |     |     |     | 1   | 10.10.10.10 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
espaçadores
|     |     |     |     |     |     | 2   |     | Lâminas Fixas |     | 1   | 10.10.10.20 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ----------- | --- | --- |
3.1325 (EN-AW
|     |     |     |     |     |     | 3   | Placa Suporte Rolamentos Inferior |     |     | 2   | 10.10.10.40 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ----------- | --- | --- |
2017A)
3
|     |     |     |     |     |     | 4   |     | Rolamento de esferas SKF 306 |     | 4   |     |     | SKF |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
3.1325 (EN-AW
|     |     |     |     |     |     | 5   |     | Placa Lateral Superior |     | 2   | 10.10.10.25 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------- | --- | --- |
2017A)
|     |     |     |     |     |     | 6   |     | Placa Lateral Inferior |     | 2   | 10.10.10.30 | 3.1325 (EN-AW  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------- | -------------- | --- |
2017A)
8
3.1325 (EN-AW
|     |     |     |     |     |     | 7   | Placa Suporte Rolamentos Superior |     |     | 2   | 10.10.10.50 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ----------- | --- | --- |
2017A)
|     |     |     |     |     |     | 8   |     | Fecho de Alavanca |     | 4   |     |     | Comunidade  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | ----------- |
GRABCAD
13
Engrenagem Helicoidal KHG2-
|     |     |     |     |     |     | 9   |     |     |     | 1   |     |     | KHK Gears |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
45RJ25
|     |     |     |     |     |     | 10  |     | Engrenagem Helicoidal KHG2- |     | 1   |     |     | KHK Gears |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --------- |
10 60LJ25
9
|     |     |     |     |     |     | 11  |     | Peça final inferior |     | 1   | 10.10.10.70 | AISI 310S |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ----------- | --------- | --- |
|     |     |     |     |     |     | 12  |     | Peça final superior |     | 1   | 10.10.10.60 | AISI 310S |     |
| 4   | 2   |     |     |     |     |     |     |                     |     |     |             |           |     |
Parafuso de cabeça lisa - M5 x 12 -
|     |     |     |     |     |     | 13  |     |     |     | 16  | ISO 10642 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
12N
|     |     |     |     |     |     | 14  | Parafuso de cabeça hexagonal -  |     |     | 8   | ISO 4016 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | -------- | --- | --- |
M6 x 30 x 18-WN
|     |     |     |     |     |     | ESCALA: |     | NOME DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --------- | --- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     |     |     |     |     |     | DESENHOU | PB 05/10/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     |     |     |     | MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ------- | --- | --------- | --- | --- | --- | --- |
SUBCONJUNTO:
|     |     |     |     |     | TOLERÂNCIA GERAL: |     | NOTAS: |     |     | Triturador de lâminas |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | ------ | --- | --- | --------------------- | --- | --- | --- |

|     |     |     |     |     |              |     |     |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ----------- | --- | ---------------- | -------- |
|     |     |     |     |     | ACABAMENTOS: |     |     |     | A3  |             |     |                  |          |
-
|     |     |     |     |     |     |     |     |     |     | 10.10.10 |     | 1/2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 512
 345   377
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
|     | DESENHOU | PB 05/10/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
COMPONENTE:
TOLERÂNCIA GERAL: NOTAS: Triturador de lâminas
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     | 10.10.10 |     | 2/2 |     |
| --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 336
 512
 350
| 1   |     | 5   | 2   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3
NORMA
|     |     |     |     |     |     | Nº  | DESIGNAÇÃO |     | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | --- | -------- | ---- |
DES. Nº
|     |     |     |     |     |     | 1   | Placa traseira - 2º estágio |     | 1   | 10.20.10.40 | 3.1325 (EN-AW  |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ----------- | -------------- | --- |
2017A)
|     |     |     |     |     |     | 2   | Mecanismo de corte         |     | 1   | 10.20.10.10 |                |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ----------- | -------------- | --- |
|     |     |     |     |     |     | 3   | Placa lateral - 2º estágio |     | 1   | 10.20.10.20 | 3.1325 (EN-AW  |     |
2017A)
3.1325 (EN-AW
|     |     |     |     |     |     | 4   | Rede 2º - estágio |     | 1   | 10.20.10.60 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ----------- | --- | --- |
2017A)
Rolamento de esferas SKF 62208-
|     |     |     |     |     |     | 5   |     |     | 1   |     |     | SKF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6 2RS1
|     |     |     |     |     |     | 6   | Placa dianteira - 2º estágio |     | 1   | 10.20.10.50 | 3.1325 (EN-AW  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ----------- | -------------- | --- |
2017A)
Parafuso de cabeça hexagonal -
|     |     |     |     |     |     | 7   |     |     | 8   | ISO 4016 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
M6 x 45 x 18-WN
|     |     |     |     |     |     | ESCALA: | NOME DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     |     |     |     |     | DESENHOU | PB 05/10/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     |     |     |     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ------- | --- | --------- | --- | --- | --- | --- |
COMPONENTE:
|     | 4   |     |     | 7   | TOLERÂNCIA GERAL: | NOTAS: |     |             | Triturador de navalhas |     |                  |          |
| --- | --- | --- | --- | --- | ----------------- | ------ | --- | ----------- | ---------------------- | --- | ---------------- | -------- |
|     |     |     |     |     |                   |        |     | DESENHO N.º |                        |     | FOLHA: MASSA[g]: | REVISÃO: |
|     |     |     |     |     | ACABAMENTOS:      |        |     | A3          |                        |     |                  |          |
-
|     |     |     |     |     |     |     |     | 10.20.10 |     |     | 1/1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 773
 223
 911
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
|     | DESENHOU | PB 03/10/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     | Empilhamento lâminas e espaçadores |     |                  |          |
| ----------------- | ------ | --- | ---------------------------------- | --- | ---------------- | -------- |
|                   |        |     | DESENHO N.º                        |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |        |     | A3                                 |     |                  |          |
-
|     |     |     | 10.10.10.10 |     | 1/3 |     |
| --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

2
|     |     |     | 5   |     | 4   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     | 6   | 5   | 3       |           |     |                                            |     |     |
| --- | --- | --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
|     |     |     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
1:2
|     |     |     | DESENHOU | PB 03/10/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
7
TRITURADOR
| 8   |     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --- | --------- | ------- | --- | --------- | --- | --- | --- |
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: | NOTAS: |     | Empilhamento lâminas e espaçadores |     |                  |          |
| --- | --- | ----------------- | ------ | --- | ---------------------------------- | --- | ---------------- | -------- |
|     |     |                   |        |     | DESENHO N.º                        |     | FOLHA: MASSA[g]: | REVISÃO: |
|     |     | ACABAMENTOS:      |        |     | A3                                 |     |                  |          |
-
|     |     |     |     |     | 10.10.10.10 |     | 2/3 |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

NORMA
|     | Nº  |     | DESIGNAÇÃO | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | ---------- | ------ | --- | -------- | ---- |
DES. Nº
AISI 1010,
|     | 1   | Veio secundário do 1º estágio |     | 1 10.10.10.10.15 |     | laminado a  |     |
| --- | --- | ----------------------------- | --- | ---------------- | --- | ----------- | --- |
quente
|     | 2   |                | Lâmina | 40 10.10.10.10.10 |     | AISI 310S |     |
| --- | --- | -------------- | ------ | ----------------- | --- | --------- | --- |
|     | 3   | Espaçador 5 mm |        | 38 10.10.10.10.30 |     | AISI 310S |     |
AISI 1010,
|     | 4   | Rosca de compressão |     | 2 10.10.10.10.80 |     | laminado a  |     |
| --- | --- | ------------------- | --- | ---------------- | --- | ----------- | --- |
quente
|     | 5   | Espaçador 4.5 mm |     | 2 10.10.10.10.40 |     | AISI 310S |     |
| --- | --- | ---------------- | --- | ---------------- | --- | --------- | --- |
AISI 1010,
|     | 6   | Batente pentagonal |     | 2 10.10.10.10.60 |     | laminado a  |     |
| --- | --- | ------------------ | --- | ---------------- | --- | ----------- | --- |
quente
AISI 1010,
|     | 7   |     | Chaveta | 2 10.10.10.10.70 |     | laminado a  |     |
| --- | --- | --- | ------- | ---------------- | --- | ----------- | --- |
quente
AISI 1010,
|     | 8   | Veio do 1º estágio |     | 1 10.10.10.10.20 |     | laminado a  |     |
| --- | --- | ------------------ | --- | ---------------- | --- | ----------- | --- |
quente
|     | ESCALA: |     | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- |
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     | Empilhamento lâminas e espaçadores |     |        |                    |
| ----------------- | --- | ------ | --- | ---------------------------------- | --- | ------ | ------------------ |
|                   |     |        |     | DESENHO N.º                        |     | FOLHA: | MASSA[g]: REVISÃO: |
| ACABAMENTOS:      |     |        |     | A4                                 |     |        |                    |
-
|     |     |     |     | 10.10.10.10 |     | 3/3 |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

6
3
1
 051
5
4
|     |     |     |     |     | 7          |     |        |     | 2            |     |          |      |
| --- | --- | --- | --- | --- | ---------- | --- | ------ | --- | ------------ | --- | -------- | ---- |
|     |     | Nº  |     |     | DESIGNAÇÃO |     | QUANT. |     | NORMA        |     | MATERIAL | OBS. |
DES. Nº
|       |     | 1   |     | Lamina Fixa Pequena 5.5 mm |                  |     |     | 1   | 10.10.10.20.20 |     | AISI 310S |     |
| ----- | --- | --- | --- | -------------------------- | ---------------- | --- | --- | --- | -------------- | --- | --------- | --- |
|       |     | 2   |     |                            | Lamina Fixa 4 mm |     |     | 38  | 10.10.10.20.40 |     | AISI 310S |     |
|  181  |     | 3   |     | Lamina Fixa Pequena 5 mm   |                  |     |     | 39  | 10.10.10.20.10 |     | AISI 310S |     |
|       |     | 4   |     |                            | Lamina Fixa 5 mm |     |     | 1   | 10.10.10.20.30 |     | AISI 310S |     |
AISI 1010,
|     |     | 5   |     | Veio de união das lâminas fixas |     |     |     | 4   | 10.10.10.20.60 | laminado a  |     |     |
| --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | -------------- | ----------- | --- | --- |
quente
|     |     | 6       |     |                         | Lamina Fixa 4.5 mm |     |     | 1   | 10.10.10.20.50                             |     | AISI 310S |               |
| --- | --- | ------- | --- | ----------------------- | ------------------ | --- | --- | --- | ------------------------------------------ | --- | --------- | ------------- |
|     |     | 7       |     | Porca sextavada M10x1x3 |                    |     |     | 4   | ISO 4032                                   |     |           | ifm eletronic |
|     |     | ESCALA: |     |                         | NOME DATA          |     |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |           |               |
1:2
|     |     |     | DESENHOU |     | PB 03/10/2024 |     |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |     |
| --- | --- | --- | -------- | --- | ------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     | MATERIAL: |     | APROVOU |     |     | CONJUNTO: |     |     |     |     |     |     |
| --- | --------- | --- | ------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
COMPONENTE:
 69
|     | TOLERÂNCIA GERAL: |     | NOTAS: |     |     |             |     | Lâminas Fixas |     |        |           |          |
| --- | ----------------- | --- | ------ | --- | --- | ----------- | --- | ------------- | --- | ------ | --------- | -------- |
|     |                   |     |        |     |     | DESENHO N.º |     |               |     | FOLHA: | MASSA[g]: | REVISÃO: |
|     | ACABAMENTOS:      |     |        |     |     | A3          |     |               |     |        |           |          |
-
|     |     |     |     |     |     | 10.10.10.20 |     |     |     | 1/1 |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 152
 310
4
3
NORMA
|     | Nº  |     | DESIGNAÇÃO |     | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | ---------- | --- | ------ | --- | -------- | ---- |
DES. Nº
AISI 1050,
|     | 1   |     | Veio 2º do estágio |     | 1   | 10.20.10.10.20 | laminado a  |     |
| --- | --- | --- | ------------------ | --- | --- | -------------- | ----------- | --- |
2 quente
AISI 1050,
|     | 2   |     | Batente das navalhas |     | 2   | 10.20.10.10.30 | laminado a  |     |
| --- | --- | --- | -------------------- | --- | --- | -------------- | ----------- | --- |
quente
|     | 3   |     | Navalha de corte |     | 3   | 10.20.10.10.10 | AISI 310S |     |
| --- | --- | --- | ---------------- | --- | --- | -------------- | --------- | --- |
1
|     | 4   |     | Parafuso de cabeça cilindrica -  |     | 12  | ISO 7045 |     |     |
| --- | --- | --- | -------------------------------- | --- | --- | -------- | --- | --- |
M10 x 20 - Z - 20N
|     | ESCALA: |     | NOME DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --- | --------- | --- | --- | ------------------------------------------ | --- | --- |
1:2
|     |     | DESENHOU | PB 05/10/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | -------- | ------------- | --- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- | --- |
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     | Mecanismo de corte - 2º estágio |     |     |                  |          |
| ----------------- | --- | ------ | --- | ------------------------------- | --- | --- | ---------------- | -------- |
|                   |     |        |     | DESENHO N.º                     |     |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |        |     | A3                              |     |     |                  |          |
-
|     |     |     |     | 10.20.10.10 |     |     | 1/1 |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 304
 281
 200
NORMA
|     | Nº  |     | DESIGNAÇÃO | QUANT. |     | MATERIAL | OBS. |
| --- | --- | --- | ---------- | ------ | --- | -------- | ---- |
DES. Nº
|     | 1   | Placa Acrilico - Funil Alimentação |     | 2   | 10.10.20.10 | Acrílico |     |
| --- | --- | ---------------------------------- | --- | --- | ----------- | -------- | --- |
3.1325 (EN-AW
|     | 2   |     | Chapa Exterior | 1   | 10.10.20.20 |     |     |
| --- | --- | --- | -------------- | --- | ----------- | --- | --- |
2017A)
3.1325 (EN-AW
|     | 3   |     | Chapa Interior | 1   | 10.10.20.30 |     |     |
| --- | --- | --- | -------------- | --- | ----------- | --- | --- |
2017A)
ESCALA:
|     |     |          | NOME DATA  |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | -------- | ---------- | --- | ------------------------------------------ | --- | --- |
|     | 1:2 |          | PB         |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA  |     |     |
|     |     | DESENHOU | 28/08/2024 |     |                                            |     |     |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
| MATERIAL: |     | APROVOU |     | TRITURADOR |     |     |     |
| --------- | --- | ------- | --- | ---------- | --- | --- | --- |
CONJUNTO:
COMPONENTE:
Funil de alimentação
| TOLERÂNCIA GERAL: |     | NOTAS: |     |             |     |                  |          |
| ----------------- | --- | ------ | --- | ----------- | --- | ---------------- | -------- |
|                   |     |        |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |        | A2  |             |     |                  |          |
|                   |     |        |     | 10.10.20    |     |                  | -        |
1/1
SOLIDWORKS Educational Product. For Instructional Use Only.

Detalhe A
(2 : 1)

2
7
°

 R6
A
 21
 R1

3
|     |     |     |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- |
°
|  021 |  401 |     | 4   |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- |
0
 8
|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
 R
5 5

 9
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
DESENHOU PB 22/09/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
 TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AAIISSII  331100SS
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS:                  |     |             | Lâmina |                  |          |
| ----------------- | ----------------------- | --- | ----------- | ------ | ---------------- | -------- |
| EN 10051          | Chapa de aço AISI 310S  |     |             |        |                  |          |
|                   | de espessura 4 mm       |     | DESENHO N.º |        | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |                         |     | A4          |        |                  |          |
-
|     |     |     | 10.10.10.10 |     | 1/1 |     |
| --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

Detalhe A
(1 : 1)

°
0
2
1

 5.3x03M
 7   21
A
 5f 03
|  65  04 |  52  02 |     |     |     |     |     |     |     |  5f 03 |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | ------ |
|         |         |     |     |     |     |     |     |     |        |

 30
|     |     |  45  |     |  25  |  182  |     |     |  75  |     |
| --- | --- | ---- | --- | ---- | ----- | --- | --- | ---- | --- |
 377
|     |     |     |     | ESCALA: | NOME DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |
| --- | --- | --- | --- | ------- | --------- | --- | --- | ------------------------------------------ | --- |
1:1
|       |     |     |     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |                                 |     |
| ----- | --- | --- | --- | -------- | ------------- | --- | ----------------------------------------- | ------------------------------- | --- |
| NOTA: |     |     |     |          |               |     |                                           | MESTRADO EM ENGENHARIA MECÂNICA |     |
VERIFICOU
Escatel normalizado segundo a norma DIN 6885/1 com largura 8N9 mm e  TRITURADOR
|     |     |     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --- | --- | --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010, laminado a quente
| profundidade 7N9 mm. |     |     |                   |        |     | COMPONENTE: |                    |     |     |
| -------------------- | --- | --- | ----------------- | ------ | --- | ----------- | ------------------ | --- | --- |
|                      |     |     | TOLERÂNCIA GERAL: | NOTAS: |     |             | Veio do 1º estágio |     |     |
ISO 2768-mK
|     |     |     |              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
|     |     |     | ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     |     |     |     | 10.10.10.20 |     | 1/1   |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

65 04
Detalhe A
(1 : 1)
°
0
2
1
A
75
5f
03
52 5f
03
21
25 182
7
332
5.3x03M
30
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:1 DESENHOU PB 08/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
NOTA: VERIFICOU
Escatel normalizado segundo a norma DIN 6885/1 com largura 8N9 mm e MATERIAL: APROVOU CONJUNTO: TRITURADOR
AISI 1010, laminado a quente COMPONENTE:
profundidade 7N9 mm. TOLERÂNCIA GERAL: NOTAS: Veio secundário do 1º estágio
ISO 2768-mK
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A3
10.10.10.15 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

Detalhe A
(5 : 1)

R
2

 160
0
|  80  |     |  40  |     |     |     |     | 1   |     |
| ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
M
x
|     |     |     |     |  R  |     |     | 6   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

4
0

A
 48

 5f 03 °
 04 4
 931  B 1
|     |     |     |     |  85  |     |     |  18  |     |
| --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
|     |     |     |     |      |     |     |      |     |

 51
 100

2
4
|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
6
|  20  |     |     | x   |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |

M
Detalhe B 1
0

(1 : 1)
 297
NOTAS:
OS 12 FUROS TÊM A MESMA PROFUNDIDADE E COMPRIMENTO DE ROSCA.
|     | ESCALA: |     | NOME DATA |     |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --- | --------- | --- | --- | ------------------------------------------ | --- | --- |
1:2
|     |     | DESENHOU | PB 08/12/2024 |     |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | -------- | ------------- | --- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- | --- |
 16  AISI 1010, laminado a quente
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     |     | Veio do 2º estágio |     |     |     |
| ----------------- | --- | ------ | --- | --- | ------------------ | --- | --- | --- |
 20
ISO 2768-mK
|              |     |     |     | DESENHO N.º |     |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | --- | ----------- | --- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     |     | A3          |     |     |                  |          |
-
|     |     |     |     | 10.20.10.10.20 |     |     | 1/1 |     |
| --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 20
 6
 22
12
 2x
 34
 05
 4
0
°

 160
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
|     | DESENHOU | PB 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     |     | Navalha |     |     |
| ----------------- | ------ | --- | --- | ------- | --- | --- |
EN 10051
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     | 10.20.10.10.10 |     | 1/1 |     |
| --- | --- | --- | -------------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

288
181
R5
5
75
B B
C
5
1
R
15
543
5
R
5
191
104
5
46
°
0
8
204
3
401
272
B-B
7
8
6
21
Detalhe C
(2 : 1)
12
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:2 DESENHOU PB 31/08/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
PET COMPONENTE:
Tremonha - 1º estágio
TOLERÂNCIA GERAL: NOTAS:
240 furos de 6 mm DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A2
10.10.15 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

287
86
20
R20
5
12
2x
471
A
301
551
183
28
67
50
°
4
2
287
033
Detalhe A
Detalhe B
(2 : 1)
(2 : 1)
R
5
5
R
B
5
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:2 DESENHOU RP 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
PET COMPONENTE:
Tremonha - 2º estágio
TOLERÂNCIA GERAL: NOTAS:
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A2
10.20.50 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 174
 01M
 01M
 3
 g6 01  4,50

|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
2:1
|     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     | Veio de União de Lâminas |     |     |     |
| ----------------- | ------ | --- | ------------------------ | --- | --- | --- |
ISO 2768-mK
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     | 10.10.10.20.60 |     | 1/1   |     |
| --- | --- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

1
5
0
8
5
0
4
3
1
9
2 8
3
0
x
1
0
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:1 DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
AISI 1010, laminado a quente COMPONENTE:
Batente das navalhas
TOLERÂNCIA GERAL: NOTAS:
Chapa de aço AISI 1010,
ISO 2768-mK
de espessura 6 mm. DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: Furos igualmente A3
10.20.10.10.30 1/1 -
espaçados
SOLIDWORKS Educational Product. For Instructional Use Only.

|     |  94 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
4
0

|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
2:1
DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010
COMPONENTE:
TOLERÂNCIA GERAL: NOTAS: Batente Pentagonal
| ISO 2768-mK  | Chapa de aço AISI 1010  |     |             |     |                  |          |
| ------------ | ----------------------- | --- | ----------- | --- | ---------------- | -------- |
|              | de espessura 1 mm       |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS: |                         |     | A4          |     |                  |          |
-
|     |     |     | 10.10.10.10.60 |     | 1/1   |     |
| --- | --- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

260
011
5
5
831
75
831
021
A
01
Detalhe A
(1 : 1)
5
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
25 1:2 DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
PET COMPONENTE:
Caixa do granulado
TOLERÂNCIA GERAL: NOTAS:
ISO 2768-mK
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A3
10.60 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 31   68
 08
|  63  |     |  03  |     |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- |
A
 22
|     |     |  5  |     |     |  5  |     |
| --- | --- | --- | --- | --- | --- | --- |
 30
Detalhe A
(2 : 1)
 3
 6
|     |     |  21  |     |  01  |     |     |
| --- | --- | ---- | --- | ---- | --- | --- |
 08
 6
   51
 150
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
|     | DESENHOU | PB 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     | Caixa dos botões de emergência |     |     |     |
| ----------------- | ------ | --- | ------------------------------ | --- | --- | --- |
ISO 2768-mK
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     | 10.30 |     | 1/1 |     |
| --- | --- | --- | ----- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

A
0
2 4

A

°
9
2
1

 631
A-A
DETALHE A

1
| 2   |     |     | (1 : 1) |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- |
1
°

 4
1

0
 1 A
| 0   | 5   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2   | 0   |     |     |     |     |     |     |     |
|     |     |     | 1   |     |     |     |     |     |
2
1
°

 44
B B
 2   60
 3

 3
| 2   | x   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

6
 05
 002
 05
 05
ESCALA:
|     |     |     | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:2 PB
|     |     |     | DESENHOU | 22/09/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | -------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
|     |     | MATERIAL: | APROVOU |     | TRITURADOR |     |     |     |
| --- | --- | --------- | ------- | --- | ---------- | --- | --- | --- |
CONJUNTO:
|     |     | 3.1325 (EN-AW 2017A) |     | COMPONENTE: |     |     |     |     |
| --- | --- | -------------------- | --- | ----------- | --- | --- | --- | --- |
B-B
Chapa exterior
|     |     | TOLERÂNCIA GERAL: | NOTAS: |     |     |     |     |     |
| --- | --- | ----------------- | ------ | --- | --- | --- | --- | --- |
ISO 2768-mK
|     |     |              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
|     |     | ACABAMENTOS: |     | A2  |             |     |                  |          |
|     |     |              |     |     | 10.10.20.20 |     |                  | -        |
1/1
SOLIDWORKS Educational Product. For Instructional Use Only.

8
9
1
7
0
°
2
3 1
77
60
2
A
A
DETALHE A
(1 : 1)
A-A
1
2
1
°
A
2 0
0 B B
2
1
0
002
6
x
3
05
05
05
B-B
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:2 DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
3.1325 (EN-AW 2017A) COMPONENTE:
Chapa interior
TOLERÂNCIA GERAL: NOTAS:
ISO 2768-mK
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A2
10.10.20.30 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 74
3
R

 47
0
1
x
8

 02
 20
 02
|     |  07     |           |     |  03                                        |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
1:1
DESENHOU PB 08/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     | Conector de estágios |     |     |     |
| ----------------- | ------ | --- | -------------------- | --- | --- | --- |
ISO 2768-mK
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A4          |     |                  |          |
-
|     |     |     | 10.70 |     | 1/1 |     |
| --- | --- | --- | ----- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

3
2

 04  08
|     |     |     |  1  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
2 0
°
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
DESENHOU PB 13/08/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS:                  |     |             | Espaçador 4.5 mm |                  |          |
| ----------------- | ----------------------- | --- | ----------- | ---------------- | ---------------- | -------- |
| EN 10051          | Chapa de aço AISI 310S  |     |             |                  |                  |          |
|                   | de espessura 4.5 mm     |     | DESENHO N.º |                  | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |                         |     | A4          |                  |                  |          |
-
|     |     |     | 10.10.10.10.40 |     | 1/1   |     |
| --- | --- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

3
2

 04  08
|     |     |     |  1  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
2
0
°
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
DESENHOU PB 13/08/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS:                  |     |             | Espaçador 5 mm |                  |          |
| ----------------- | ----------------------- | --- | ----------- | -------------- | ---------------- | -------- |
| EN 10051          | Chapa de aço AISI 310S  |     |             |                |                  |          |
|                   | de espessura 5 mm       |     | DESENHO N.º |                | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |                         |     | A4          |                |                  |          |
-
|     |     |     | 10.10.10.10.30 |     | 1/1   |     |
| --- | --- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

|     |  70  |     |     |     |  70  |     |
| --- | ---- | --- | --- | --- | ---- | --- |
 2
x
R
2
8
|  57  |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- |
 245
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     |     | Espaçador final |     |     |
| ----------------- | ------ | --- | --- | --------------- | --- | --- |
EN 10051
Espessura: 32 mm
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A4          |     |                  |          |
-
|     |     |     | 10.10.10.10.50 |     | 1/1 |     |
| --- | --- | --- | -------------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 29
 17
 71
|     |     |     |  2x | 10  |     |     |
| --- | --- | --- | --- | --- | --- | --- |
 R
4
1

 051
 140°
 69
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     |     | Lâmina Fixa 4 mm |     |     |
| ----------------- | ------ | --- | --- | ---------------- | --- | --- |
Chapa de aço AISI 310S de
EN 10051
espessura 4 mm.
|              |                      |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | -------------------- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: | Furos simétricos em  |     | A4          |     |                  |          |
-
|     | relativamente ao componente. |     | 10.10.10.20.40 |     | 1/1   |     |
| --- | ---------------------------- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 29
 140°
 2x M10
 R
4
1

 051
 71
 17
 69
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
TOLERÂNCIA GERAL: NOTAS: Lâmina Fixa 4.5 mm
| EN 10051     | Chapa de aço AISI 310S  |     |             |     |                  |          |
| ------------ | ----------------------- | --- | ----------- | --- | ---------------- | -------- |
|              | de espessura 4.5 mm     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS: |                         |     | A4          |     |                  |          |
-
|     |     |     | 10.10.10.20.50 |     | 1/1   |     |
| --- | --- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

29
R41
140°
71
A
17
8
1
x
2
2
x
1
0
A
69
051
A-A
5
3
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:1 DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
AISI 310S COMPONENTE:
Lâmina Fixa 5 mm
TOLERÂNCIA GERAL: NOTAS:
EN 10051 Furos simétricos em
relação ao DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: componente A4 10.10.10.20.30 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

051
29
140°
R
6
0
0
1.
x
0
1
M
x
2
50
71
17
68
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:1 DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
AISI 310S COMPONENTE:
Lâmina Fixa Pequena 5 mm
TOLERÂNCIA GERAL: NOTAS:
EN 10051 Chapa de aço AISI 310S de
espessura 4.5 mm.
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: Furos simétricos relativamente A4
ao componente. 10.10.10.20.10 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

29
A
2x
140°
18
R
6
0
2x
10
A
50
68
051
A-A
5,5
3
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:1 DESENHOU PB 03/10/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
AISI 310S COMPONENTE:
Lâmina Fixa Pequena 5.5 mm
TOLERÂNCIA GERAL: NOTAS:
EN 10051 Furos simétricos em
relação ao DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: componente. A4 10.10.10.20.20 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 53
 R
|     |     |     | 7   |     |  4  |     |
| --- | --- | --- | --- | --- | --- | --- |
9

3
8
R

 34   34
 881
A
Detalhe A
 210
(1 : 1)
4

 9
 9
 6
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS:         |              |             | Rede - 2º estágio |                  |          |
| ----------------- | -------------- | ------------ | ----------- | ----------------- | ---------------- | -------- |
| ISO 2768-mK       | 480 furos      | 4 espaçados  |             |                   |                  |          |
|                   | uniformemente. |              | DESENHO N.º |                   | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |                |              | A4          |                   |                  |          |
-
|     |     |     | 10.20.10.60 |     | 1/1 |     |
| --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

|     |     |  10  |  21  |     |     |     |
| --- | --- | ---- | ---- | --- | --- | --- |
 7
 5.3x03M
 35

 05,2
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
2:1
DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     | Rosca de Compressão |     |     |     |
| ----------------- | ------ | --- | ------------------- | --- | --- | --- |
ISO 2768-mK
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A4          |     |                  |          |
-
|     |     |     | 10.10.10.10.70 |     | 1/1   |     |
| --- | --- | --- | -------------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

A
A-A
 23
 4

R
1
6

 7
x2
 51

R
3
6
|  041  |     |     |     |     | x2  |      |     |
| ----- | --- | --- | --- | --- | --- | ---- | --- |
|  4    |     |     |     |     |     |  10  |     |
 08
 90
A
 10
 11
 22
 285
|     |     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
|     |     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --------- | ------- | --- | --------- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
|     | TOLERÂNCIA GERAL: | NOTAS:                 |     | Placa de suporte de rolamentos inferior |     |                  |          |
| --- | ----------------- | ---------------------- | --- | --------------------------------------- | --- | ---------------- | -------- |
|     | ISO 2768-mK       | Todos os boleados têm  |     |                                         |     |                  |          |
|     |                   | raio de 1mm.           |     | DESENHO N.º                             |     | FOLHA: MASSA[g]: | REVISÃO: |
|     | ACABAMENTOS:      |                        |     | A3                                      |     |                  |          |
|     |                   | Peça simétrica.        |     |                                         |     |                  | -        |
|     |                   |                        |     | 10.10.10.40                             |     | 1/1              |          |
SOLIDWORKS Educational Product. For Instructional Use Only.

 25
 21
 21
 9
 285
A-A
A
 4
 51
 51
x2
 7
6
3
|  57  | x2  |     |     |     |     |     |  10  |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- |
R

6
1
R

 5
 3
 23
A
 54
 22
 90
|     |     |     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
|     |     |     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --- | --------- | ------- | --- | --------- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: | NOTAS:                 |     | Placa de Suporte de Rolamentos Superior |     |                  |          |
| --- | --- | ----------------- | ---------------------- | --- | --------------------------------------- | --- | ---------------- | -------- |
|     |     | ISO 2768-mK       | Todos os boleados têm  |     |                                         |     |                  |          |
|     |     |                   | raio de 1 mm.          |     | DESENHO N.º                             |     | FOLHA: MASSA[g]: | REVISÃO: |
|     |     | ACABAMENTOS:      |                        |     | A3                                      |     |                  |          |
|     |     |                   | Peça simétrica.        |     |                                         |     |                  | -        |
|     |     |                   |                        |     | 10.10.10.50                             |     | 1/1              |          |
SOLIDWORKS Educational Product. For Instructional Use Only.

A-A
 35
A
 8   01
 6M x2
|     |     |     |     |     |     |     |  82  |     |  12  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
 10
 12
 20
 57
 4x M
5
 03
 3
 52
A
 9
 6
x
 M
|  50  |  13  | 6   |  37  |  13  |  50  |     |     |     |     |     |     |     |
| ---- | ---- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |

 02
 37
 213
|     |     |     |     |     |     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:1
|     |     |     |     |     |     |     | DESENHOU PB | 22/09/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     |     |     |     | MATERIAL: |     | APROVOU | CONJUNTO: |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ------- | --------- | --- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
|     |     |     |     |     | TOLERÂNCIA GERAL: |     | NOTAS: |     | Placa lateral superior |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | ------ | --- | ---------------------- | --- | --- | --- |
ISO 2768-mK
Todos os boleados têm
|     |     |     |     |     |              |     | raio de 1 mm. |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | ----------- | --- | ---------------- | -------- |
|     |     |     |     |     | ACABAMENTOS: |     |               | A3  |             |     |                  |          |
A
|     |     |     |     |     |     |     |     |     | 10.10.10.25 |     | 1/1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

28
78
61
56
10
08
A
6
M
x
2
541
35 17
85
10
213
4
x
M
5
G G
53
53
107
5
Detalhe A
(2 : 1)
10
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:1 DESENHOU PB 04/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
3.1325 (EN-AW 2017A) COMPONENTE:
Placa Lateral Inferior
TOLERÂNCIA GERAL: NOTAS:
ISO 2768-mK
Todos os boleados têm
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: raio de 1 mm. A3
10.10.10.30 1/2 -
SOLIDWORKS Educational Product. For Instructional Use Only.

G-G
 20
 12
|     |     |  21   01  |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- |
 3x
12
 51
|     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:1
|     |     | DESENHOU PB | 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --------- | --- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS:                 |     | Placa Lateral Inferior |     |                  |          |
| ----------------- | --- | ---------------------- | --- | ---------------------- | --- | ---------------- | -------- |
| ISO 2768-mK       |     | Todos os boleados têm  |     |                        |     |                  |          |
|                   |     | raio de 1 mm.          |     | DESENHO N.º            |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |                        | A3  |                        |     |                  |          |
-
|     |     |     |     | 10.10.10.30 |     | 2/2   |     |
| --- | --- | --- | --- | ----------- | --- | ----- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

08
32 186
03
R
1
2
150
8
R
1
32
250
02
01
72
A
44
84
51 6
6
3
01 21
Detalhe A
(2 : 1)
13
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:2 DESENHOU PB 08/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
3.1325 (EN-AW 2017A) COMPONENTE:
Pega
TOLERÂNCIA GERAL: NOTAS:
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A3
10.40 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 215
| 6   | 5°  |     |     |     |      |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| 8   | 3   |     |     |     |  02  |     |     |     |     |     |
|     | 1   |     |     |     |      |     |     |     |     |     |

 54
  1
3
5
 43  °

|  74  |     |  191  |     |     |     |  22  |     |     |     |     |
| ---- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- | --- |
 383
 882
 381
|     |     |     |     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:2
|     |     |     |     |     | DESENHOU PB | 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     |     | MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --- | --- | --------- | --- | ------- | --- | --------- | --- | --- | --- |
Acrílico
COMPONENTE:
|     |     |     | TOLERÂNCIA GERAL: |     | NOTAS: |     | Placa acrílico menor - 2º estágio |     |     |     |
| --- | --- | --- | ----------------- | --- | ------ | --- | --------------------------------- | --- | --- | --- |
Chapa de acrílico de
|     |     |     |              |     | espessura 10 mm. |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | ------------ | --- | ---------------- | --- | ----------- | --- | ---------------- | -------- |
|     |     |     | ACABAMENTOS: |     |                  |     | A3          |     |                  |          |
-
|     |     |     |     |     |     |     | 10.20.40 |     | 1/1 |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

Detalhe A
(2 : 5)
 54
 4
x
1
0

A
 45
 07
 66
 082
 784
 208
 1212
|     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     | DESENHOU PB | 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --------- | --- | --- | --- | --- |
Acrílico
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS:                |     | Placa acrílico superior - 1º estágio |     |                  |          |
| ----------------- | --- | --------------------- | --- | ------------------------------------ | --- | ---------------- | -------- |
| ISO 2768-mK       |     | Chapa de acrílico de  |     |                                      |     |                  |          |
|                   |     | espessura 10 mm.      |     | DESENHO N.º                          |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |                       | A3  |                                      |     |                  |          |
-
|     |     |     |     | 10.10.60 |     | 1/1 |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 70   70
 R
2
8

 57
 245
|     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:1
|     |     | DESENHOU PB | 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU | CONJUNTO: |     |     |     |     |
| --------- | --- | ------- | --------- | --- | --- | --- | --- |
AISI 310S
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS:                  |     | Placa final inferior |     |                  |          |
| ----------------- | --- | ----------------------- | --- | -------------------- | --- | ---------------- | -------- |
| ISO 2768-mK       |     | Chapa de aço AISI 310S  |     |                      |     |                  |          |
|                   |     | de espessura 32 mm.     |     | DESENHO N.º          |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |                         | A3  |                      |     |                  |          |
-
|     |     |     |     | 10.10.10.70 |     | 1/1 |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 245
 57
8
2
R

 70   70
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:1
|     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 310S
COMPONENTE:
Placa final superior
TOLERÂNCIA GERAL: NOTAS:
ISO 2768-mK
Chapa de aço AISI 310S
|              |                     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | ------------------- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: | de espessura 32 mm. |     | A3          |     |                  |          |
-
|     |     |     | 10.10.10.60 |     | 1/1 |     |
| --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 1236
 811
 89
 364
 061
 119   53   53
 071
8
|  115  |  191  |  146  |     |     |     |     |     |     |     |
| ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
R

 59
 85   195
 6x
12
 08
 80
|     |     |     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     |     |     | DESENHOU PB | 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     | MATERIAL: |     | APROVOU | CONJUNTO: |     |     |     |     |
| --- | --- | --------- | --- | ------- | --------- | --- | --- | --- | --- |
AISI 316
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: |     | NOTAS: |     | Placa inferior - 1º estágio |     |     |     |
| --- | --- | ----------------- | --- | ------ | --- | --------------------------- | --- | --- | --- |
ISO 2768-mK Chapa de aço
|     |     |     |     | inoxidável AISI 316 de  |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | --- | ----------------------- | --- | ----------- | --- | ---------------- | -------- |
ACABAMENTOS: A3
-
|     |     |     |     | espessura 3 mm. |     | 10.10.30.10 |     | 1/1 |     |
| --- | --- | --- | --- | --------------- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 1236
 481
 419
 101
 471
|  142  |  46   46  |     |     |     |     |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
 115   531
 471
9
R
 106
|  97  |  183  |  59  |     |     |     |     |     |     |     |
| ---- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
 6
x
1
2
 08
 80
|     |     |     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     |     |     | DESENHOU PB | 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     | MATERIAL: |     | APROVOU | CONJUNTO: |     |     |     |     |
| --- | --- | --------- | --- | ------- | --------- | --- | --- | --- | --- |
AISI 316
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: |     | NOTAS: |     | Placa inferior - 2º estágio |     |     |     |
| --- | --- | ----------------- | --- | ------ | --- | --------------------------- | --- | --- | --- |
ISO 2768-mK Chapa de aço
|     |     |     |     | inoxidável AISI 316 de  |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | --- | --- | ----------------------- | --- | ----------- | --- | ---------------- | -------- |
ACABAMENTOS: A3
|     |     |     |     | espessura 3 mm. |     |             |     |     | -   |
| --- | --- | --- | --- | --------------- | --- | ----------- | --- | --- | --- |
|     |     |     |     |                 |     | 10.20.20.10 |     | 1/1 |     |
SOLIDWORKS Educational Product. For Instructional Use Only.

B-B
B  20
 12
 13
 03
M6
 4x
| 4   |   4 |     |     |     |     |       |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- |
| 4   | 1   |     |     |     |     |       |     |     |
|     | °   |     |     |     |     |  512  |     |     |

 92
 4
 54
 61
 83   188
B
 98
 64
 64
 64
|     |     |     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
|     |     |     | DESENHOU | PB 20/08/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --- | --------- | ------- | --- | --------- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: | NOTAS: |     | Placa lateral - 2º estágio |     |     |     |
| --- | --- | ----------------- | ------ | --- | -------------------------- | --- | --- | --- |
 20
 25  ISO 2768-mK
|  33  |     |              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ---- | --- | ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
|      |     | ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     |     |     | 10.20.10.20 |     | 1/1 |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 260
 210
|  25  |  42  |     |     |     |  37  |     |     |     |
| ---- | ---- | --- | --- | --- | ---- | --- | --- | --- |
 03
 05
0
8
R

 512
6
x
4
   54
 13   25
|     |     |     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | --- | --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:2
|     |     |     | DESENHOU | PB 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
|     |     | MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --- | --- | --------- | ------- | --- | --------- | --- | --- | --- |
3.1325 (EN-AW 2017A)
COMPONENTE:
|     |     | TOLERÂNCIA GERAL: | NOTAS: |     | Placa dianteira - 2º estágio |     |     |     |
| --- | --- | ----------------- | ------ | --- | ---------------------------- | --- | --- | --- |
ISO 2768-mK
|     |     |              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| --- | --- | ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
|     |     | ACABAMENTOS: |     |     | A3          |     |                  |          |
-
|     |     |     |     |     | 10.20.10.50 |     | 1/1 |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

512
260
8
0
6
x
4
13
54
25 210
43
0
8
R
511
130
03
33
23
05
10
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:2 DESENHOU PB 08/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
3.1325 (EN-AW 2017A) COMPONENTE:
Placa traseira - 2º estágio
TOLERÂNCIA GERAL: NOTAS:
ISO 2768-mK
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: A3
10.20.10.40 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 002
 571
Detalhe B B
(1 : 1)
 10
 5
 10
Detalhe A  40
(1 : 2)
 021
A
 02
 51
 537
 10
 02
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
1:5
|     | DESENHOU | PB 01/09/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | -------- | ------------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
PET
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     | Suporte da caixa do granulado |     |                  |          |
| ----------------- | ------ | --- | ----------------------------- | --- | ---------------- | -------- |
|                   |        |     | DESENHO N.º                   |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |        |     | A3                            |     |                  |          |
-
|     |     |     | 10.50 |     | 1/1 |     |
| --- | --- | --- | ----- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 11h7
 9h8
 21
|     | ESCALA: | NOME DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | --------- | --- | ------------------------------------------ | --- | --- |
2:1
DESENHOU PB 08/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | ------- | --- | --------- | --- | --- | --- |
AISI 1010
COMPONENTE:
| TOLERÂNCIA GERAL: | NOTAS: |     |     | Chaveta |     |     |
| ----------------- | ------ | --- | --- | ------- | --- | --- |
DIN 6885/1
|              |     |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     |     | A4          |     |                  |          |
-
|     |     |     | 10.10.10.10.70 |     | 1/1 |     |
| --- | --- | --- | -------------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

004
303
231
1
1
4
8
3
2
8
8
1
2
2
4
77
1
5
0
04
°
9
2
1
7
0
°
174
ESCALA: NOME DATA INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA
1:2 DESENHOU PB 08/12/2024 ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
MATERIAL: APROVOU CONJUNTO: TRITURADOR
Acrílico COMPONENTE:
Placa acrílico - Funil alimentação
TOLERÂNCIA GERAL: NOTAS:
Chapa de acrílico de
DESENHO N.º FOLHA: MASSA[g]: REVISÃO:
ACABAMENTOS: espessura 2 mm. A3
10.10.20.10 1/1 -
SOLIDWORKS Educational Product. For Instructional Use Only.

 890
3
0
1

 135°
 43   35
 593
 882
 1106
|     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     | DESENHOU PB | 03/10/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- |
Acrílico
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS:                |     | Placa acrílico maior - 2º estágio |     |                  |          |
| ----------------- | --- | --------------------- | --- | --------------------------------- | --- | ---------------- | -------- |
| ISO 2768-mk       |     | Chapa de acrílico de  |     |                                   |     |                  |          |
|                   |     | espessura 10 mm.      |     | DESENHO N.º                       |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |                       | A3  |                                   |     |                  |          |
-
|     |     |     |     | 10.20.30 |     | 1/1 |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 882
 381
|     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:2
|     |     | DESENHOU PB | 04/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- |
Acrílico
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS: |     | Placa acrílico menor - 1º estágio |     |     |     |
| ----------------- | --- | ------ | --- | --------------------------------- | --- | --- | --- |
Chapa de acrílico de
|              |     |                  |     | DESENHO N.º |     | FOLHA: MASSA[g]: | REVISÃO: |
| ------------ | --- | ---------------- | --- | ----------- | --- | ---------------- | -------- |
| ACABAMENTOS: |     | espessura 10 mm. |     | A3          |     |                  |          |
-
|     |     |     |     | 10.10.50 |     | 1/1 |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

 882
 1106
|     | ESCALA: | NOME | DATA |     | INSTITUTO SUPERIOR DE ENGENHARIA DE LISBOA |     |     |
| --- | ------- | ---- | ---- | --- | ------------------------------------------ | --- | --- |
1:5
|     |     | DESENHOU PB | 08/12/2024 |     | ÁREA DEPARTAMENTAL DE ENGENHARIA MECÂNICA |     |     |
| --- | --- | ----------- | ---------- | --- | ----------------------------------------- | --- | --- |
MESTRADO EM ENGENHARIA MECÂNICA
VERIFICOU
TRITURADOR
| MATERIAL: |     | APROVOU |     | CONJUNTO: |     |     |     |
| --------- | --- | ------- | --- | --------- | --- | --- | --- |
Acrílico
COMPONENTE:
| TOLERÂNCIA GERAL: |     | NOTAS:                |     | Placa acrílico maior - 1º estágio |     |                  |          |
| ----------------- | --- | --------------------- | --- | --------------------------------- | --- | ---------------- | -------- |
| ISO 2768-mK       |     | Chapa de acrílico de  |     |                                   |     |                  |          |
|                   |     | espessura 10 mm.      |     | DESENHO N.º                       |     | FOLHA: MASSA[g]: | REVISÃO: |
| ACABAMENTOS:      |     |                       | A3  |                                   |     |                  |          |
-
|     |     |     |     | 10.10.40 |     | 1/1 |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
SOLIDWORKS Educational Product. For Instructional Use Only.

Anexo 1: Catálogos

R..DRN..[mm]
DRN
(  7.3) 63M 71MS 71M 80MK 80M 90S 90L 100LS 100L/L 112M 132S 132M 132L 160..
M
| AC  | 115 139 | 139 156 | 156 179 | 179 197 | 197 221 | 221 261 | 261 314  |
| --- | ------- | ------- | ------- | ------- | ------- | ------- | -------- |
| AD  | 98 118  | 118 128 | 128 140 | 140 157 | 157 170 | 170 228 | 228 253  |
| ADS | 98 129  | 129 139 | 139 150 | 150 158 | 158 172 | 172 228 | 228 253  |
| L   | 491 492 | 512 523 | 568 570 | 602 598 | 648 679 | 729 747 | 773 839  |
| LS  | 547 560 | 580 604 | 649 663 | 695 692 | 742 791 | 841 885 | 910 1028 |
| LB  | 191 192 | 212 223 | 268 270 | 302 298 | 348 379 | 429 447 | 473 539  |
| LBS | 247 260 | 280 304 | 349 363 | 395 392 | 442 491 | 541 585 | 610 728  |

|     | KHG   Module 2 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Ground Helical Gears |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
Ground Helical Gears
|     |     |     |     |     |     |     |     | J   |     |     |     |     |     |     |     | J   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Series
Usable in the assembly distance of the spur gear.
|     |     |     |     |     |                | Specifications                    |     | G   |     |     |     |                                 |     |     |     |     | G   |       |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |                |                                   |     |     |     |     |     |                                 |     |     |     |     | E   | F     |     |     |     |     |     |
|     |     |     |     |     | P r e ci sion  |                                   |     | E   | F   |     |     | KHG ground helical gears use a  |     |     |     |     |     | J=F/2 |     |     |     |     |     |
|     |     |     |     |     | gr a d e       | JIS grade N6 (JIS B1702-1: 1998)* |     |     |     |     |     |                                 |     |     |     |     |     | J     |     |     |     |     |     |
“transverse” module.
|     |     |     |     |     | R e fe r e n c e   |                |     | G   |     |     |     |                                    |     |     |     |     | G   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |                    | Rotating plane |     |     |     |     |     | The assembly distance is the same  |     |     |     |     |     |     |     |     |     |     |     |
se c ti o n   o f  gear
 rupS sraeG Gear teeth Standard full depth as spur gear pairs with the same   rupS sraeG
|     |     |     |     |     | Transverse     |     |     |     |     |     |     | module and number of teeth. |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | pressure angle | 20° |     |     |     |     |     |                             |     |     |     |     |     |     |     |     |     |     |     |
Improved strength and low noise:
|          |     |     |     |     | Helix angle | 21°30’                         |     |     |     |     |     |                                  |     |     |     |     |     |       |     |     |     |     |          |
| -------- | --- | --- | --- | --- | ----------- | ------------------------------ | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | -------- |
|          |     |     |     |     |             |                                |     |     | A B | C D |     | Take the next step up from spur  |     |     |     |     |     | A B C | D   |     |     |     |          |
|          |     |     |     |     | Material    | SCM440                         |     |     |     |     |     |                                  |     |     |     |     |     |       |     |     |     |     |          |
|          |     |     |     |     | Heat        | Thermal refined, gear teeth    |     |     |     |     |     | gears.                           |     |     |     |     |     |       |     |     |     |     |          |
|  lacileH |     |     |     |     | treatment   | induction hardened             |     |     |     |     |     |                                  |     |     |     |     |     |       |     |     |     |     |  lacileH |
| sraeG    |     |     |     |     | Tooth       |                                |     |     |     |     |     |                                  |     |     |     |     |     |       |     |     |     |     | sraeG    |
|          |     |     |     |     |             | 50 to 60HRC                    |     |     |     | S1  |     |                                  |     |     |     |     |     |       |     |     |     |     |          |
|          |     |     |     |     | hardness    |                                |     |     |     |     |     |                                  |     |     |     |     |     |       | S1K |     |     |     |          |
|          |     |     |     |     | Surface     | Black oxide coated except for  |     |     |     |     |     |                                  |     |     |     |     |     |       |     |     |     |     |          |
|          |     |     |     |     | treatment   | teeth                          |     |     |     |     |     |                                  |     |     |     |     |     |       |     |     |     |     |          |
*  The precision grade of J Series products is  To order J Series products, please specify: Catalog No. + J + BORE.
equivalent to the value shown in the table.
|           |     |     |     |     |     |     |     |     |     |     |     | Bore H7    |         | * The product shapes of J Series items are identified by background color. |        |     |     |         |         |        |        |     |           |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------------------------------------------------------------------------- | ------ | --- | --- | ------- | ------- | ------ | ------ | --- | --------- |
|  lanretnI |     |     |     |     |     |     |     |     |     |     |     |            |         |                                                                            |        |     |     |         |         |        |        |     |  lanretnI |
| sraeG     |     |     |     |     |     |     |     |     |     |     |     |            |         |                                                                            |        |     |     |         |         |        |        |     | sraeG     |
|           |     |     |     |     |     |     |     |     |     |     |     | Keyway Js9 | 12  14  | 15  16                                                                     | 17 18  | 19  | 20  | 22  25  | 28  30  | 32 35  | 40  45 | 50  |           |
No. of Direction  Bore Hub dia. Pitch dia. Outside dia. Face widthHub widthTotal lengthAllowable torque (N·m)Allowable torque (kgf·m) Backlash Weight Screw size 4×1.8 5×2.3 6×2.8 8×3.3 10×3.3 12×3.3 14×3.8
|     | Catalog Number |     | Shape |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
teeth of helix AH7 B C D E F G Bending strengthSurface durabilityBending strengthSurface durability (mm) (kg) Catalog Number M4 M5 M6 M8 M10
|     | KHG2-15R | R   |     |     |     |     |       |       |             |     |      | KHG2-15R J BORE | S1K |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | ----- | ----- | ----------- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |          | 15  |     | 24  | 30  | 34  | 40.5  | 22.8  | 4.13  2.32  |     | 0.11 |                 |     |     |     |     |     |     |     |     |     |     |     |
|     | KHG2-15L | L   |     |     |     |     |       |       |             |     |      | KHG2-15L J BORE | S1K |     |     |     |     |     |     |     |     |     |     |
12
| skcaR | KHG2-18R | R   |     |     |     |     |       |       |             |     |      | KHG2-18R J BORE | S1K S1K | S1K S1K | S1K |     |     |     |     |     |     |     | skcaR |
| ----- | -------- | --- | --- | --- | --- | --- | ----- | ----- | ----------- | --- | ---- | --------------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|       |          | 18  |     | 30  | 36  | 40  | 48.5  | 31.9  | 4.95  3.25  |     | 0.17 |                 |         |         |     |     |     |     |     |     |     |     |       |
|       | KHG2-18L | L   |     |     |     |     |       |       |             |     |      | KHG2-18L J BORE | S1K S1K | S1K S1K | S1K |     |     |     |     |     |     |     |       |
|       | KHG2-20R | R   |     |     |     |     |       |       |             |     |      | KHG2-20R J BORE |         | S1K S1K | S1K |     |     |     |     |     |     |     |       |
|       |          | 20  |     | 32  | 40  | 44  | 56.6  | 40.8  | 5.77  4.16  |     | 0.20 |                 |         |         |     |     |     |     |     |     |     |     |       |
|       | KHG2-20L | L   |     |     |     |     |       |       |             |     |      | KHG2-20L J BORE |         | S1K S1K | S1K |     |     |     |     |     |     |     |       |
|       | KHG2-22R | R   |     |     |     |     |       |       |             |     |      | KHG2-22R J BORE |         |         |     |     |     |     |     |     |     |     |       |
  & skcaR PC 22 36 44 48 64.9  50.6  6.62  5.16  0.25 S1K S1K S1K S1K S1K S1K   & skcaR PC
|         | KHG2-22L | L   |     |     |     |     |       |       |             |     |      | KHG2-22L J BORE |     |         |         |     |     |         |     |     |     |     |         |
| ------- | -------- | --- | --- | --- | --- | --- | ----- | ----- | ----------- | --- | ---- | --------------- | --- | ------- | ------- | --- | --- | ------- | --- | --- | --- | --- | ------- |
|         |          |     |     |     |     |     |       |       |             |     |      |                 |     | S1K S1K | S1K S1K | S1K | S1K |         |     |     |     |     |         |
| snoiniP |          |     |     |     |     |     |       |       |             |     |      |                 |     |         |         |     |     |         |     |     |     |     | snoiniP |
|         | KHG2-25R | R   |     |     |     |     |       |       |             |     |      | KHG2-25R J BORE |     | S1K S1K | S1K S1K | S1K | S1K | S1K     |     |     |     |     |         |
|         |          | 25  | 15  | 40  | 50  | 54  | 77.5  | 67.3  | 7.90  6.86  |     | 0.33 |                 |     |         |         |     |     |         |     |     |     |     |         |
|         | KHG2-25L | L   |     |     |     |     |       |       |             |     |      | KHG2-25L J BORE |     | S1K S1K | S1K S1K | S1K | S1K | S1K     |     |     |     |     |         |
|         | KHG2-26R | R   |     |     |     |     |       |       |             |     |      | KHG2-26R J BORE |     | S1K S1K | S1K S1K | S1K | S1K | S1K     |     |     |     |     |         |
|         |          | 26  |     | 42  | 52  | 56  | 81.8  | 73.4  | 8.34  7.49  |     | 0.37 |                 |     |         |         |     |     |         |     |     |     |     |         |
|         | KHG2-26L | L   |     |     |     |     |       |       |             |     |      | KHG2-26L J BORE |     | S1K S1K | S1K S1K | S1K | S1K | S1K     |     |     |     |     |         |
|         | KHG2-28R | R   |     |     |     |     |       |       |             |     |      | KHG2-28R J BORE |     | S1K S1K | S1K S1K | S1K | S1K | S1K S1K |     |     |     |     |         |
|  retiM  |          | 28  |     | 45  | 56  | 60  | 90.4  | 86.6  | 9.21  8.83  |     | 0.43 |                 |     |         |         |     |     |         |     |     |     |     |  retiM  |
sraeG KHG2-28L L KHG2-28L J BORE S1K S1K S1K S1K S1K S1K S1K S1K sraeG
|     | KHG2-30R | R   |     |     |     |     |            |       |       |     |      | KHG2-30R J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | ---------- | ----- | ----- | --- | ---- | --------------- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- |
|     |          | 30  |     | 50  | 60  | 64  | 99.1  101  | 10.1  | 10.3  |     | 0.50 |                 |     |     |     |     |     |         |         |     |     |     |     |
|     | KHG2-30L | L   |     |     |     |     |            |       |       |     |      | KHG2-30L J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |     |     |     |     |
|     | KHG2-32R | R   |     |     |     |     |            |       |       |     |      | KHG2-32R J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |     |     |     |     |
|     |          | 32  |     | 50  | 64  | 68  | 108  117   | 11.0  | 11.9  |     | 0.55 |                 |     |     |     |     |     |         |         |     |     |     |     |
|     | KHG2-32L | L   |     |     |     |     |            |       |       |     |      | KHG2-32L J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |     |     |     |     |
18
 leveB KHG2-35R R KHG2-35R J BORE S1K S1K S1K S1K S1K S1K S1K  leveB
| sraeG  |          | 35  |     | 50  | 70  | 74       | 121  142  | 12.3  | 14.5  |           | 0.63 |                 |     |     |     |     |     |         |         |         |     |     | sraeG  |
| ------ | -------- | --- | --- | --- | --- | -------- | --------- | ----- | ----- | --------- | ---- | --------------- | --- | --- | --- | --- | --- | ------- | ------- | ------- | --- | --- | ------ |
|        | KHG2-35L | L   |     |     |     |          |           |       |       |           |      | KHG2-35L J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |         |     |     |        |
|        |          |     | S1  |     |     | 16 13 29 |           |       |       | 0.10~0.20 |      |                 |     |     |     |     |     |         |         |         |     |     |        |
|        | KHG2-36R | R   |     |     |     |          |           |       |       |           |      | KHG2-36R J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |         |     |     |        |
|        |          | 36  |     | 50  | 72  | 76       | 126  151  | 12.8  | 15.4  |           | 0.65 |                 |     |     |     |     |     |         |         |         |     |     |        |
|        | KHG2-36L | L   |     |     |     |          |           |       |       |           |      | KHG2-36L J BORE |     |     | S1K | S1K | S1K | S1K S1K | S1K S1K |         |     |     |        |
|        | KHG2-40R | R   |     |     |     |          |           |       |       |           |      | KHG2-40R J BORE |     |     |     |     | S1K | S1K S1K | S1K S1K | S1K S1K |     |     |        |
|        |          | 40  |     | 60  | 80  | 84       | 143  191  | 14.6  | 19.5  |           | 0.85 |                 |     |     |     |     |     |         |         |         |     |     |        |
|        | KHG2-40L | L   |     |     |     |          |           |       |       |           |      | KHG2-40L J BORE |     |     |     |     | S1K | S1K S1K | S1K S1K | S1K S1K |     |     |        |
|  wercS |          |     |     |     |     |          |           |       |       |           |      |                 |     |     |     |     |     |         |         |         |     |     |  wercS |
sraeG KHG2-45R R KHG2-45R J BORE S1K S1K S1K S1K S1K S1K S1K sraeG
|           |           | 45  | 20  | 60  | 90  | 94  | 166  248  | 16.9  | 25.3  |     | 1.02  |                  |     |     |     |     |     |         |         |         |         |     |           |
| --------- | --------- | --- | --- | --- | --- | --- | --------- | ----- | ----- | --- | ----- | ---------------- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ------- | --- | --------- |
|           | KHG2-45L  | L   |     |     |     |     |           |       |       |     |       | KHG2-45L J BORE  |     |     |     |     | S1K | S1K S1K | S1K S1K | S1K S1K |         |     |           |
|           | KHG2-48R  | R   |     |     |     |     |           |       |       |     |       | KHG2-48R J BORE  |     |     |     |     | S1K | S1K S1K | S1K S1K | S1K S1K |         |     |           |
|           |           | 48  |     | 60  | 96  | 100 | 172  273  | 17.5  | 27.9  |     | 1.13  |                  |     |     |     |     |     |         |         |         |         |     |           |
|           | KHG2-48L  | L   |     |     |     |     |           |       |       |     |       | KHG2-48L J BORE  |     |     |     |     | S1K | S1K S1K | S1K S1K | S1K S1K |         |     |           |
|           | KHG2-50R  | R   |     |     |     |     |           |       |       |     |       | KHG2-50R J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K |         |     |           |
|           |           | 50  |     | 60  | 100 | 104 | 181  299  | 18.4  | 30.5  |     | 1.16  |                  |     |     |     |     |     |         |         |         |         |     |           |
|  mroW     | KHG2-50L  | L   |     |     |     |     |           |       |       |     |       | KHG2-50L J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K |         |     |  mroW     |
| sraeG     |           |     |     |     |     |     |           |       |       |     |       |                  |     |     |     |     |     |         |         |         |         |     | sraeG     |
|           | KHG2-60R  | R   |     |     |     |     |           |       |       |     |       | KHG2-60R J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K |         |     |           |
|           |           | 60  |     | 65  | 120 | 124 | 225  447  | 22.9  | 45.6  |     | 1.65  |                  |     |     |     |     |     |         |         |         |         |     |           |
|           | KHG2-60L  | L   |     |     |     |     |           |       |       |     |       | KHG2-60L J BORE  |     |     |     |     |     |         |         |         |         |     |           |
|           |           |     |     |     |     |     |           |       |       |     |       |                  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K |         |     |           |
|           | KHG2-70R  | R   |     |     |     |     |           |       |       |     |       | KHG2-70R J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K     |     |           |
|           |           | 70  |     | 70  | 140 | 144 | 269  625  | 27.4  | 63.7  |     | 2.21  |                  |     |     |     |     |     |         |         |         |         |     |           |
|           | KHG2-70L  | L   |     |     |     |     |           |       |       |     |       | KHG2-70L J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K     |     |           |
| sexobraeG |           |     | 25  |     |     |     |           |       |       |     |       |                  |     |     |     |     |     |         |         |         |         |     | sexobraeG |
|           | KHG2-80R  | R   |     |     |     |     |           |       |       |     |       | KHG2-80R J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K S1K |     |           |
|           |           | 80  |     | 80  | 160 | 164 | 301  799  | 30.7  | 81.4  |     | 2.93  |                  |     |     |     |     |     |         |         |         |         |     |           |
|           | KHG2-80L  | L   |     |     |     |     |           |       |       |     |       | KHG2-80L J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K S1K |     |           |
|           | KHG2-90R  | R   |     |     |     |     |           |       |       |     |       | KHG2-90R J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K S1K | S1K |           |
|           |           | 90  |     | 90  | 180 | 184 | 344  1030 | 35.0  | 105   |     | 3.73  |                  |     |     |     |     |     |         |         |         |         |     |           |
|           | KHG2-90L  | L   |     |     |     |     |           |       |       |     |       | KHG2-90L J BORE  |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K S1K | S1K |           |
|           | KHG2-100R | R   |     |     |     |     |           |       |       |     |       | KHG2-100R J BORE |     |     |     |     |     | S1K     | S1K S1K | S1K S1K | S1K S1K | S1K |           |
|           |           | 100 |     | 100 | 200 | 204 | 387  1290 | 39.4  | 132   |     | 4.64  |                  |     |     |     |     |     |         |         |         |         |     |           |
stcudorP KHG2-100L L KHG2-100L J BORE S1K S1K S1K S1K S1K S1K S1K S1K stcudorP
|  rehtO |                     |     |     |          |     |                                            |     |     |     |             |     |     |     |     |     |     |     |     |     |     |     |     |  rehtO |
| ------ | ------------------- | --- | --- | -------- | --- | ------------------------------------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
|        | Product Precautions |     |     | Page 191 |     | Precautions for Standard Machined Products |     |     |     | Pages 38~40 |     |     |     |     |     |     |     |     |     |     |     |     |        |
| 198    |                     |     |     |          |     |                                            |     |     |     |             |     |     |     |     |     |     |     |     |     |     |     |     | 119999 |

1/ 3
Strut profile 80x80L
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

2/ 3
Product description
Quick & Easy profile finishes
Introduction to strut profiles
Technical data
Quick & Easy profile finishes
Dimensions
Section profile AL 80x80 L
Strut profile 80x80L
Ordering codes
The following cover caps can be used:
Cover cap 80x80, signal gray (1x)
Cover cap 80x80, black (1x)
|     | L   | ESD | No. |
| --- | --- | --- | --- |
mm
| Strut profile 80x80L         | 50 … 6070  | 1   | 3842993133 |
| ---------------------------- | ---------- | --- | ---------- |
| Strut profile 80x80L M12/-   | 60 … 6000  | 1   | 3842993134 |
| Strut profile 80x80L M12/M12 | 110 … 6000 | 1   | 3842993147 |
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

1/ 3
Strut profile 40x40L
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

2/ 3
Product description
Quick & Easy profile finishes
Introduction to strut profiles
Technical data
Quick & Easy profile finishes
Dimensions
Strut profile 40x40L
Ordering codes
The following caps with holes are needed:
40x40 signal gray (1 item)
40x40 black (1 item)

The following cover caps are needed:
40x40 signal gray (1 item)
40x40 black (1 item)
L ESD No.
mm
| Strut profile 40x40L               | 50 … 6070  | 1   | 3842993120 |
| ---------------------------------- | ---------- | --- | ---------- |
| Strut profile 40x40L M12/-         | 60 … 6000  | 1   | 3842993121 |
| Strut profile 40x40L M12/M12       | 110 … 6000 | 1   | 3842993122 |
| Strut profile 40x40L M12/D17       | 90 … 6000  | 1   | 3842993123 |
| Strut profile 40x40L D17/-         | 60 … 6000  | 1   | 3842993124 |
| Strut profile 40x40L D17/D17       | 80 … 6000  | 1   | 3842993125 |
| Strut profile 40x40L D17/D17V      | 80 … 6000  | 1   | 3842993126 |
| Strut profile 40x40L D9,8/D9,8     | 80 … 6000  | 1   | 3842993129 |
| Strut profile 40x40L, 20xL=6070mm  | 6070 20    |     | 3842529339 |
| Strut profile 40x40L Q&E, L50-6000 | 50 … 6070  |     | 3842993724 |
| Cover cap 40x40, signal gray       |            | 100 | 3842548746 |
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

1/ 5
Bracket 80/80
▪ Brackets with centering lugs for rapid, precise
assembly with protection against turning
▪ Centering lugs can be easily broken off for
assembly on plates or at right angles to the slot
▪ Version designLINE with special silver paint
(RAL 9006) for an especially high-quality design
▪ Cover cap to protect from dirt, available in signal
gray (RAL 7004) and black ESD (RAL 9005)
▪ Profile finishing: not required
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

2/ 5
Product description
Connection elements, selection criteria
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

3/ 5
Technical data
ES
|     | Groove D Material entry |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- |
|     |                         |     |     | F   | M   | M   |
|     |                         |     |     | max | max | max |
|     |                         |     |     | N   | Nm  | Nm  |
Bracket: Diecast aluminum, vibratory ground
|     | 10  |     |     | 14000 | 500 | 1000 |
| --- | --- | --- | --- | ----- | --- | ---- |
Fastening material: steel; galvanized
Bracket designLINE: Diecast aluminum; vibratory ground,
Bracket
|     | 10 painted (RAL 9006) |     |     | 14000 | 500 | 1000 |
| --- | --------------------- | --- | --- | ----- | --- | ---- |
Fastening material: steel; galvanized
10 Bracket: Diecast aluminum, vibratory ground 14000 500 1000
PP
Cover cap
for bracket
PP
M
max
Nm
400
400
400
Typ
| 80 / 80 |     | 14000 N | 500 Nm | 1000 Nm |     | 400 Nm |
| ------- | --- | ------- | ------ | ------- | --- | ------ |
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

4/ 5
Dimensions
Bracket 80/80 with cover cap
Accessories
Recommended accessories
Cover cap for bracket 80/80, signal gray
Cover cap for bracket 80/80, black
Delivery notes
FS7
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

1/ 4
Heavy-duty wheel
▪ Heavy-duty wheel with mounting flange
▪ Available as a caster wheel with lock, caster, and
trestle wheel
▪ Heavy-duty, particularly suited for workshop
applications
▪ Wheels with excellent running properties
▪ Screw-on plate for attachment to 40 mm or 45 mm
profiles
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

2/ 4
Product description
Technical data
No. 3842536737 3842536738 3842536701 3842562057 3842562058 3842562059
Housing: Steel; zinc-plated Housing: Steel; zinc-plated
Material Galvanized steel
Wheel: TPU Wheel: TPU, 94° shore A, gray
Dimensions
Heavy-duty wheel, LR with lock, F3000
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

Dimensions 3/ 4
Heavy-duty wheel, LR
Trestle wheel
Screw-on plate, heavy duty wheel
Assembly-Technology, PDF version, 2023-08-223, © Bosch Rexroth AG, subject to change.
Valid edition only on the Internet. Copies of any type are not subject to change.

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Descrição do artigo/Imagens dos produtos
Descrição
Material:
Cubo em alumínio.
Coroa dentada em poliuretano.
Versão:
Superfície do cubo sem proteção anticorrosiva.
Coroa dentada azul 80 Shore A.
Coroa dentada amarela 92 Shore A.
Coroa dentada vermelha 98 Shore A.
Indicação:
O acoplamento de garras em elastômero é composto por dois cubos e uma coroa
dentada em elastômero. Destinam-se a compensar erros de alinhamento axiais,
radiais e angulares, bem como para amortecer oscilações e choques de torque.
A coroa dentada em poliuretano está disponível em diferentes graus de dureza.
Quanto mais elevada a dureza da coroa dentada para acoplamento, mais elevado
será o torque transmitido e a rigidez. Quanto menor for a dureza, a capacidade de
deslocamento e de amortecimento aumenta.
A pré-tensão das coroas dentadas de acoplamento nos cubos de acoplamento torna
esta variante livre de folgas.
A entrega ocorre desmontada.
Faixa de temperatura:
Azul 80 Shore A: -50 °C até +80 °C. Em curto espaço de tempo -60 °C até +120 °C.
Amarelo 92 Shore A: -30 °C até +90 °C. Em curto espaço de tempo -50 °C até
+120 °C.
Vermelho 98 Shore A: -30 °C até +90 °C. Em curto espaço de tempo -40 °C até
+120 °C.
Montagem:
Os acoplamentos de garras em elastômero têm um ajuste de H7. A folga de ajuste
recomendada é de 0,02 mm–0,05 mm. Esta folga de ajuste e olear as pontas do
eixo facilita a montagem e desmontagem.
Para a montagem, os cubos do acoplamento de garras em elastômero são colocados
em cima do eixo e bloqueadas por meio de cubos de aperto.
Sob consulta:
Furos do cubo D1 e D2 desejados separadamente com classe ou faixa de tolerância.
Rasgo de chaveta de acordo com DIN 6885.
© norelem www.norelem.com 1/9

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Desenhos
Visão geral dos artigos
Código do artigo Tamanho Cor Momento de inércia Rigidez à torção Rigidez à torção Rigidez da mola Desvio máx. do eixo
|                      | dos componentes | (gm²) | estática | dinâmica | radial          | radial |
| -------------------- | --------------- | ----- | -------- | -------- | --------------- | ------ |
|                      |                 |       | (Nm/rad) | (Nm/rad) | (N/mm)          | (mm)   |
| 23022-25-24980581925 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-19920501414 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-28920621414 | 28 amarelo      | 0,266 | 4080     | 6745     | 1780            | 0,15   |
| 23022-25-14980320814 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-24980581920 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-24980582025 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-19980500808 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-24980581819 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-19980501214 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-19920501515 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-24920582025 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-24920582525 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-24980582020 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-19980501215 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-19980501515 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-19980501616 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-42920944545 | 42 amarelo      | 1,832 | 10870    | 20500    | 4100            | 0,19   |
| 23022-25-28920623232 | 28 amarelo      | 0,266 | 4080     | 6745     | 1780            | 0,15   |
| 23022-25-19980501414 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-14980321012 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-38920861818 | 38 amarelo      | 0,79  | 6525     | 12000    | 2350            | 0,17   |
| 23022-25-14980321014 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-19920501216 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-14980320812 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-14980321414 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-24980581825 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-28920622424 | 28 amarelo      | 0,266 | 4080     | 6745     | 1780            | 0,15   |
| 23022-25-24920581819 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-19980501516 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-14980320810 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-38920862828 | 38 amarelo      | 0,79  | 6525     | 12000    | 2350            | 0,17   |
| 23022-25-48921105050 | 48 amarelo      | 3,101 | 12968    | 22800    | 4500            | 0,23   |
| 23022-25-24920581920 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-28920622828 | 28 amarelo      | 0,266 | 4080     | 6745     | 1780            | 0,15   |
| 23022-25-14980320404 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| © norelem            |                 |       |          |          | www.norelem.com | 2/9    |

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Visão geral dos artigos
Código do artigo Tamanho Cor Momento de inércia Rigidez à torção Rigidez à torção Rigidez da mola Desvio máx. do eixo
|                      | dos componentes | (gm²) | estática | dinâmica | radial          | radial |
| -------------------- | --------------- | ----- | -------- | -------- | --------------- | ------ |
|                      |                 |       | (Nm/rad) | (Nm/rad) | (N/mm)          | (mm)   |
| 23022-25-48921102222 | 48 amarelo      | 3,101 | 12968    | 22800    | 4500            | 0,23   |
| 23022-25-19920501415 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-48921103838 | 48 amarelo      | 3,101 | 12968    | 22800    | 4500            | 0,23   |
| 23022-25-19980501216 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-24920581825 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-42920943232 | 42 amarelo      | 1,832 | 10870    | 20500    | 4100            | 0,19   |
| 23022-25-19980501415 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-42920942222 | 42 amarelo      | 1,832 | 10870    | 20500    | 4100            | 0,19   |
| 23022-25-38920863838 | 38 amarelo      | 0,79  | 6525     | 12000    | 2350            | 0,17   |
| 23022-25-24920581820 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-19980501212 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-24980581919 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-48921104545 | 48 amarelo      | 3,101 | 12968    | 22800    | 4500            | 0,23   |
| 23022-25-19920501516 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-19980501416 | 19 vermelho     | 0,019 | 1512     | 2540     | 2010            | 0,06   |
| 23022-25-14980320808 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-24980582525 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-24920582020 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-14980321214 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-24920581925 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-42920943838 | 42 amarelo      | 1,832 | 10870    | 20500    | 4100            | 0,19   |
| 23022-25-19920501416 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-24980581818 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-24920581010 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-28980621414 | 28 vermelho     | 0,266 | 6410     | 9920     | 3200            | 0,11   |
| 23022-25-24980581820 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-24980581010 | 24 vermelho     | 0,121 | 3700     | 8130     | 2940            | 0,11   |
| 23022-25-19920501616 | 19 amarelo      | 0,019 | 1090     | 1815     | 1120            | 0,1    |
| 23022-25-14980321010 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-38920863232 | 38 amarelo      | 0,79  | 6525     | 12000    | 2350            | 0,17   |
| 23022-25-24920581818 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-24920581919 | 24 amarelo      | 0,121 | 2300     | 5130     | 1900            | 0,15   |
| 23022-25-14980321212 | 14 vermelho     | 0,006 | 171,9    | 513      | 654             | 0,09   |
| 23022-25-14800320404 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800320808 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800320810 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800320812 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800320814 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800321010 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800321012 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800321014 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800321212 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800321214 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-14800321414 | 14 azul         | 0,006 | 60,2     | 180      | 153             | 0,21   |
| 23022-25-19800500808 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501212 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501214 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501215 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501216 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501414 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501415 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501416 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501515 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501516 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-19800501616 | 19 azul         | 0,019 | 618      | 1065     | 582             | 0,15   |
| 23022-25-24800581010 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581818 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581819 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581820 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581825 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581919 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581920 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800581925 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| 23022-25-24800582020 | 24 azul         | 0,121 | 860      | 1390     | 840             | 0,2    |
| © norelem            |                 |       |          |          | www.norelem.com | 3/9    |

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Visão geral dos artigos
Código do artigo Tamanho Cor Momento de inércia Rigidez à torção Rigidez à torção Rigidez da mola Desvio máx. do eixo
|                      | dos componentes |          | (gm²) |     | estática |     | dinâmica | radial |     | radial |
| -------------------- | --------------- | -------- | ----- | --- | -------- | --- | -------- | ------ | --- | ------ |
|                      |                 |          |       |     | (Nm/rad) |     | (Nm/rad) | (N/mm) |     | (mm)   |
| 23022-25-24800582025 | 24              | azul     | 0,121 |     | 860      |     | 1390     | 840    |     | 0,2    |
| 23022-25-24800582525 | 24              | azul     | 0,121 |     | 860      |     | 1390     | 840    |     | 0,2    |
| 23022-25-28800621414 | 28              | azul     | 0,266 |     | 1370     |     | 2350     | 990    |     | 0,2    |
| 23022-25-28800622424 | 28              | azul     | 0,266 |     | 1370     |     | 2350     | 990    |     | 0,2    |
| 23022-25-28800622828 | 28              | azul     | 0,266 |     | 1370     |     | 2350     | 990    |     | 0,2    |
| 23022-25-28800623232 | 28              | azul     | 0,266 |     | 1370     |     | 2350     | 990    |     | 0,2    |
| 23022-25-14920320404 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920320808 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920320810 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920320812 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920320814 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920321010 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920321012 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920321014 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920321212 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920321214 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-14920321414 | 14              | amarelo  | 0,006 |     | 114,6    |     | 344      | 336    |     | 0,15   |
| 23022-25-19920500808 | 19              | amarelo  | 0,019 |     | 1090     |     | 1815     | 1120   |     | 0,1    |
| 23022-25-19920501212 | 19              | amarelo  | 0,019 |     | 1090     |     | 1815     | 1120   |     | 0,1    |
| 23022-25-19920501214 | 19              | amarelo  | 0,019 |     | 1090     |     | 1815     | 1120   |     | 0,1    |
| 23022-25-19920501215 | 19              | amarelo  | 0,019 |     | 1090     |     | 1815     | 1120   |     | 0,1    |
| 23022-25-28980622424 | 28              | vermelho | 0,266 |     | 6410     |     | 9920     | 3200   |     | 0,11   |
| 23022-25-28980622828 | 28              | vermelho | 0,266 |     | 6410     |     | 9920     | 3200   |     | 0,11   |
| 23022-25-28980623232 | 28              | vermelho | 0,266 |     | 6410     |     | 9920     | 3200   |     | 0,11   |
| 23022-25-38980861818 | 38              | vermelho | 0,79  |     | 11800    |     | 21850    | 4400   |     | 0,12   |
| 23022-25-38980862828 | 38              | vermelho | 0,79  |     | 11800    |     | 21850    | 4400   |     | 0,12   |
| 23022-25-38980863232 | 38              | vermelho | 0,79  |     | 11800    |     | 21850    | 4400   |     | 0,12   |
| 23022-25-38980863838 | 38              | vermelho | 0,79  |     | 11800    |     | 21850    | 4400   |     | 0,12   |
| 23022-25-42980942222 | 42              | vermelho | 1,832 |     | 21594    |     | 37692    | 5940   |     | 0,14   |
| 23022-25-42980943232 | 42              | vermelho | 1,832 |     | 21594    |     | 37692    | 5940   |     | 0,14   |
| 23022-25-42980943838 | 42              | vermelho | 1,832 |     | 21594    |     | 37692    | 5940   |     | 0,14   |
| 23022-25-42980944545 | 42              | vermelho | 1,832 |     | 21594    |     | 37692    | 5940   |     | 0,14   |
| 23022-25-48981102222 | 48              | vermelho | 3,101 |     | 25759    |     | 49400    | 6820   |     | 0,16   |
| 23022-25-48981103838 | 48              | vermelho | 3,101 |     | 25759    |     | 49400    | 6820   |     | 0,16   |
| 23022-25-48981104545 | 48              | vermelho | 3,101 |     | 25759    |     | 49400    | 6820   |     | 0,16   |
| 23022-25-48981105050 | 48              | vermelho | 3,101 |     | 25759    |     | 49400    | 6820   |     | 0,16   |
Código do artigo Desalinhamento máx. do eixo Desalinhamento Torque Coroa dentada Torque nominal Rotação
|                      |     | axial       |     | máx. angular |     | máximo | dureza     |     | Nm              | máx   |
| -------------------- | --- | ----------- | --- | ------------ | --- | ------ | ---------- | --- | --------------- | ----- |
|                      |     | (mm)        |     |              | (°) | Nm     |            |     |                 | Rpm   |
| 23022-25-24980581925 |     | +1,4 / -0,5 |     |              | 0,9 | 120    | 98 Shore A |     | 60              | 7000  |
| 23022-25-19920501414 |     | +1,2 / -0,5 |     |              | 1   | 24     | 92 Shore A |     | 12              | 10000 |
| 23022-25-28920621414 |     | +1,5 / -0,7 |     |              | 1   | 190    | 92 Shore A |     | 95              | 6000  |
| 23022-25-14980320814 |     | +1 / -0,5   |     |              | 0,9 | 25     | 98 Shore A |     | 12,5            | 13000 |
| 23022-25-24980581920 |     | +1,4 / -0,5 |     |              | 0,9 | 120    | 98 Shore A |     | 60              | 7000  |
| 23022-25-24980582025 |     | +1,4 / -0,5 |     |              | 0,9 | 120    | 98 Shore A |     | 60              | 7000  |
| 23022-25-19980500808 |     | +1,2 / -0,5 |     |              | 0,9 | 42     | 98 Shore A |     | 21              | 10000 |
| 23022-25-24980581819 |     | +1,4 / -0,5 |     |              | 0,9 | 120    | 98 Shore A |     | 60              | 7000  |
| 23022-25-19980501214 |     | +1,2 / -0,5 |     |              | 0,9 | 42     | 98 Shore A |     | 21              | 10000 |
| 23022-25-19920501515 |     | +1,2 / -0,5 |     |              | 1   | 24     | 92 Shore A |     | 12              | 10000 |
| 23022-25-24920582025 |     | +1,4 / -0,5 |     |              | 1   | 70     | 92 Shore A |     | 35              | 7000  |
| 23022-25-24920582525 |     | +1,4 / -0,5 |     |              | 1   | 70     | 92 Shore A |     | 35              | 7000  |
| 23022-25-24980582020 |     | +1,4 / -0,5 |     |              | 0,9 | 120    | 98 Shore A |     | 60              | 7000  |
| 23022-25-19980501215 |     | +1,2 / -0,5 |     |              | 0,9 | 42     | 98 Shore A |     | 21              | 10000 |
| 23022-25-19980501515 |     | +1,2 / -0,5 |     |              | 0,9 | 42     | 98 Shore A |     | 21              | 10000 |
| 23022-25-19980501616 |     | +1,2 / -0,5 |     |              | 0,9 | 42     | 98 Shore A |     | 21              | 10000 |
| 23022-25-42920944545 |     | +2 / -1     |     |              | 1   | 830    | 92 Shore A |     | 265             | 4000  |
| 23022-25-28920623232 |     | +1,5 / -0,7 |     |              | 1   | 190    | 92 Shore A |     | 95              | 6000  |
| 23022-25-19980501414 |     | +1,2 / -0,5 |     |              | 0,9 | 42     | 98 Shore A |     | 21              | 10000 |
| 23022-25-14980321012 |     | +1 / -0,5   |     |              | 0,9 | 25     | 98 Shore A |     | 12,5            | 13000 |
| 23022-25-38920861818 |     | +1,8 / -0,7 |     |              | 1   | 380    | 92 Shore A |     | 190             | 5000  |
| 23022-25-14980321014 |     | +1 / -0,5   |     |              | 0,9 | 25     | 98 Shore A |     | 12,5            | 13000 |
| 23022-25-19920501216 |     | +1,2 / -0,5 |     |              | 1   | 24     | 92 Shore A |     | 12              | 10000 |
| 23022-25-14980320812 |     | +1 / -0,5   |     |              | 0,9 | 25     | 98 Shore A |     | 12,5            | 13000 |
| © norelem            |     |             |     |              |     |        |            |     | www.norelem.com | 4/9   |

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Visão geral dos artigos
Código do artigo Desalinhamento máx. do eixo Desalinhamento Torque Coroa dentada Torque nominal Rotação
|                      | axial       | máx. angular | máximo | dureza     | Nm              | máx   |
| -------------------- | ----------- | ------------ | ------ | ---------- | --------------- | ----- |
|                      | (mm)        | (°)          | Nm     |            |                 | Rpm   |
| 23022-25-14980321414 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-24980581825 | +1,4 / -0,5 | 0,9          | 120    | 98 Shore A | 60              | 7000  |
| 23022-25-28920622424 | +1,5 / -0,7 | 1            | 190    | 92 Shore A | 95              | 6000  |
| 23022-25-24920581819 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-19980501516 | +1,2 / -0,5 | 0,9          | 42     | 98 Shore A | 21              | 10000 |
| 23022-25-14980320810 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-38920862828 | +1,8 / -0,7 | 1            | 380    | 92 Shore A | 190             | 5000  |
| 23022-25-48921105050 | +2,1 / -1   | 1            | 620    | 92 Shore A | 310             | 3750  |
| 23022-25-24920581920 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-28920622828 | +1,5 / -0,7 | 1            | 190    | 92 Shore A | 95              | 6000  |
| 23022-25-14980320404 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-48921102222 | +2,1 / -1   | 1            | 620    | 92 Shore A | 310             | 3750  |
| 23022-25-19920501415 | +1,2 / -0,5 | 1            | 24     | 92 Shore A | 12              | 10000 |
| 23022-25-48921103838 | +2,1 / -1   | 1            | 620    | 92 Shore A | 310             | 3750  |
| 23022-25-19980501216 | +1,2 / -0,5 | 0,9          | 42     | 98 Shore A | 21              | 10000 |
| 23022-25-24920581825 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-42920943232 | +2 / -1     | 1            | 830    | 92 Shore A | 265             | 4000  |
| 23022-25-19980501415 | +1,2 / -0,5 | 0,9          | 42     | 98 Shore A | 21              | 10000 |
| 23022-25-42920942222 | +2 / -1     | 1            | 830    | 92 Shore A | 265             | 4000  |
| 23022-25-38920863838 | +1,8 / -0,7 | 1            | 380    | 92 Shore A | 190             | 5000  |
| 23022-25-24920581820 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-19980501212 | +1,2 / -0,5 | 0,9          | 42     | 98 Shore A | 21              | 10000 |
| 23022-25-24980581919 | +1,4 / -0,5 | 0,9          | 120    | 98 Shore A | 60              | 7000  |
| 23022-25-48921104545 | +2,1 / -1   | 1            | 620    | 92 Shore A | 310             | 3750  |
| 23022-25-19920501516 | +1,2 / -0,5 | 1            | 24     | 92 Shore A | 12              | 10000 |
| 23022-25-19980501416 | +1,2 / -0,5 | 0,9          | 42     | 98 Shore A | 21              | 10000 |
| 23022-25-14980320808 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-24980582525 | +1,4 / -0,5 | 0,9          | 120    | 98 Shore A | 60              | 7000  |
| 23022-25-24920582020 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-14980321214 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-24920581925 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-42920943838 | +2 / -1     | 1            | 830    | 92 Shore A | 265             | 4000  |
| 23022-25-19920501416 | +1,2 / -0,5 | 1            | 24     | 92 Shore A | 12              | 10000 |
| 23022-25-24980581818 | +1,4 / -0,5 | 0,9          | 120    | 98 Shore A | 60              | 7000  |
| 23022-25-24920581010 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-28980621414 | +1,5 / -0,7 | 0,9          | 320    | 98 Shore A | 160             | 6000  |
| 23022-25-24980581820 | +1,4 / -0,5 | 0,9          | 120    | 98 Shore A | 60              | 7000  |
| 23022-25-24980581010 | +1,4 / -0,5 | 0,9          | 120    | 98 Shore A | 60              | 7000  |
| 23022-25-19920501616 | +1,2 / -0,5 | 1            | 24     | 92 Shore A | 12              | 10000 |
| 23022-25-14980321010 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-38920863232 | +1,8 / -0,7 | 1            | 380    | 92 Shore A | 190             | 5000  |
| 23022-25-24920581818 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-24920581919 | +1,4 / -0,5 | 1            | 70     | 92 Shore A | 35              | 7000  |
| 23022-25-14980321212 | +1 / -0,5   | 0,9          | 25     | 98 Shore A | 12,5            | 13000 |
| 23022-25-14800320404 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800320808 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800320810 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800320812 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800320814 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800321010 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800321012 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800321014 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800321212 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800321214 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-14800321414 | +1 / -0,5   | 1,1          | 8      | 80 Shore A | 4               | 13000 |
| 23022-25-19800500808 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501212 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501214 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501215 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501216 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501414 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501415 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501416 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| 23022-25-19800501515 | +1,2 / -0,5 | 1,1          | 12     | 80 Shore A | 6               | 10000 |
| © norelem            |             |              |        |            | www.norelem.com | 5/9   |

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Visão geral dos artigos
Código do artigo Desalinhamento máx. do eixo Desalinhamento Torque Coroa dentada Torque nominal Rotação
|                      | axial       |     | máx. angular | máximo | dureza     | Nm  | máx   |
| -------------------- | ----------- | --- | ------------ | ------ | ---------- | --- | ----- |
|                      | (mm)        |     | (°)          | Nm     |            |     | Rpm   |
| 23022-25-19800501516 | +1,2 / -0,5 |     | 1,1          | 12     | 80 Shore A | 6   | 10000 |
| 23022-25-19800501616 | +1,2 / -0,5 |     | 1,1          | 12     | 80 Shore A | 6   | 10000 |
| 23022-25-24800581010 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581818 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581819 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581820 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581825 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581919 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581920 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800581925 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800582020 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800582025 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-24800582525 | +1,4 / -0,5 |     | 1            | 34     | 80 Shore A | 17  | 7000  |
| 23022-25-28800621414 | +1,5 / -0,7 |     | 1,3          | 92     | 80 Shore A | 46  | 6000  |
| 23022-25-28800622424 | +1,5 / -0,7 |     | 1,3          | 92     | 80 Shore A | 46  | 6000  |
| 23022-25-28800622828 | +1,5 / -0,7 |     | 1,3          | 92     | 80 Shore A | 46  | 6000  |
| 23022-25-28800623232 | +1,5 / -0,7 |     | 1,3          | 92     | 80 Shore A | 46  | 6000  |
| 23022-25-14920320404 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920320808 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920320810 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920320812 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920320814 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920321010 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920321012 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920321014 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920321212 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920321214 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-14920321414 | +1 / -0,5   |     | 1            | 15     | 92 Shore A | 7,5 | 13000 |
| 23022-25-19920500808 | +1,2 / -0,5 |     | 1            | 24     | 92 Shore A | 12  | 10000 |
| 23022-25-19920501212 | +1,2 / -0,5 |     | 1            | 24     | 92 Shore A | 12  | 10000 |
| 23022-25-19920501214 | +1,2 / -0,5 |     | 1            | 24     | 92 Shore A | 12  | 10000 |
| 23022-25-19920501215 | +1,2 / -0,5 |     | 1            | 24     | 92 Shore A | 12  | 10000 |
| 23022-25-28980622424 | +1,5 / -0,7 |     | 0,9          | 320    | 98 Shore A | 160 | 6000  |
| 23022-25-28980622828 | +1,5 / -0,7 |     | 0,9          | 320    | 98 Shore A | 160 | 6000  |
| 23022-25-28980623232 | +1,5 / -0,7 |     | 0,9          | 320    | 98 Shore A | 160 | 6000  |
| 23022-25-38980861818 | +1,8 / -0,7 |     | 0,9          | 650    | 98 Shore A | 325 | 5000  |
| 23022-25-38980862828 | +1,8 / -0,7 |     | 0,9          | 650    | 98 Shore A | 325 | 5000  |
| 23022-25-38980863232 | +1,8 / -0,7 |     | 0,9          | 650    | 98 Shore A | 325 | 5000  |
| 23022-25-38980863838 | +1,8 / -0,7 |     | 0,9          | 650    | 98 Shore A | 325 | 5000  |
| 23022-25-42980942222 | +2 / -1     |     | 0,9          | 900    | 98 Shore A | 450 | 4000  |
| 23022-25-42980943232 | +2 / -1     |     | 0,9          | 900    | 98 Shore A | 450 | 4000  |
| 23022-25-42980943838 | +2 / -1     |     | 0,9          | 900    | 98 Shore A | 450 | 4000  |
| 23022-25-42980944545 | +2 / -1     |     | 0,9          | 900    | 98 Shore A | 450 | 4000  |
| 23022-25-48981102222 | -2,1 / -1   |     | 0,9          | 1050   | 98 Shore A | 525 | 3750  |
| 23022-25-48981103838 | -2,1 / -1   |     | 0,9          | 1050   | 98 Shore A | 525 | 3750  |
| 23022-25-48981104545 | -2,1 / -1   |     | 0,9          | 1050   | 98 Shore A | 525 | 3750  |
| 23022-25-48981105050 | -2,1 / -1   |     | 0,9          | 1050   | 98 Shore A | 525 | 3750  |
Código do artigo A C D1 D2 D1/D2 D1/D2 D4 K L L1 L2 L3 L4 R Torque de
|     | (ISO 4029) (H7) | (H7) mín. | máx. |     |     | aperto dos |     |
| --- | --------------- | --------- | ---- | --- | --- | ---------- | --- |
parafusos Nm
23022-25-24980581925 20 M6 19 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-19920501414 14,5 M6 14 14 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-28920621414 25 M8 14 14 14 37 65 17 62 21 20 9 28 73 40
23022-25-14980320814 10,5 M4 8 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-24980581920 20 M6 19 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24980582025 20 M6 20 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-19980500808 14,5 M6 8 8 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-24980581819 20 M6 18 19 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-19980501214 14,5 M6 12 14 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19920501515 14,5 M6 15 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-24920582025 20 M6 20 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24920582525 20 M6 25 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24980582020 20 M6 20 20 10 32 55 16 58 20 18 8 26 57,5 15
| © norelem |     |     |     |     |     | www.norelem.com | 6/9 |
| --------- | --- | --- | --- | --- | --- | --------------- | --- |

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Visão geral dos artigos
Código do artigo A C D1 D2 D1/D2 D1/D2 D4 K L L1 L2 L3 L4 R Torque de
(ISO 4029) (H7) (H7) mín. máx. aperto dos
parafusos Nm
23022-25-19980501215 14,5 M6 12 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19980501515 14,5 M6 15 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19980501616 14,5 M6 16 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-42920944545 32 M10 45 45 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-28920623232 25 M8 32 32 14 37 65 17 62 21 20 9 28 73 40
23022-25-19980501414 14,5 M6 14 14 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-14980321012 10,5 M4 10 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-38920861818 30 M8 18 18 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-14980321014 10,5 M4 10 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-19920501216 14,5 M6 12 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-14980320812 10,5 M4 8 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14980321414 10,5 M4 14 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-24980581825 20 M6 18 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-28920622424 25 M8 24 24 14 37 65 17 62 21 20 9 28 73 40
23022-25-24920581819 20 M6 18 19 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-19980501516 14,5 M6 15 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-14980320810 10,5 M4 8 10 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-38920862828 30 M8 28 28 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-48921105050 36 M12 50 50 22 57 105 30 110 41 28 14 50 105 145
23022-25-24920581920 20 M6 19 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-28920622828 25 M8 28 28 14 37 65 17 62 21 20 9 28 73 40
23022-25-14980320404 10,5 M4 4 4 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-48921102222 36 M12 22 22 22 57 105 30 110 41 28 14 50 105 145
23022-25-19920501415 14,5 M6 14 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-48921103838 36 M12 38 38 22 57 105 30 110 41 28 14 50 105 145
23022-25-19980501216 14,5 M6 12 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-24920581825 20 M6 18 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-42920943232 32 M10 32 32 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-19980501415 14,5 M6 14 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-42920942222 32 M10 22 22 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-38920863838 30 M8 38 38 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-24920581820 20 M6 18 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-19980501212 14,5 M6 12 12 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-24980581919 20 M6 19 19 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-48921104545 36 M12 45 45 22 57 105 30 110 41 28 14 50 105 145
23022-25-19920501516 14,5 M6 15 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19980501416 14,5 M6 14 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-14980320808 10,5 M4 8 8 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-24980582525 20 M6 25 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24920582020 20 M6 20 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-14980321214 10,5 M4 12 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-24920581925 20 M6 19 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-42920943838 32 M10 38 38 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-19920501416 14,5 M6 14 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-24980581818 20 M6 18 18 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24920581010 20 M6 10 10 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-28980621414 25 M8 14 14 14 37 65 17 62 21 20 9 28 73 40
23022-25-24980581820 20 M6 18 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24980581010 20 M6 10 10 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-19920501616 14,5 M6 16 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-14980321010 10,5 M4 10 10 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-38920863232 30 M8 32 32 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-24920581818 20 M6 18 18 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24920581919 20 M6 19 19 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-14980321212 10,5 M4 12 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800320404 10,5 M4 4 4 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800320808 10,5 M4 8 8 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800320810 10,5 M4 8 10 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800320812 10,5 M4 8 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800320814 10,5 M4 8 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800321010 10,5 M4 10 10 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800321012 10,5 M4 10 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800321014 10,5 M4 10 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800321212 10,5 M4 12 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
© norelem www.norelem.com 7/9

23022-25 Acoplamentos de garras em elastômero, forma de estrutura curta com
cubo de aperto removível
Visão geral dos artigos
Código do artigo A C D1 D2 D1/D2 D1/D2 D4 K L L1 L2 L3 L4 R Torque de
(ISO 4029) (H7) (H7) mín. máx. aperto dos
parafusos Nm
23022-25-14800321214 10,5 M4 12 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14800321414 10,5 M4 14 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-19800500808 14,5 M6 8 8 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501212 14,5 M6 12 12 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501214 14,5 M6 12 14 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501215 14,5 M6 12 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501216 14,5 M6 12 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501414 14,5 M6 14 14 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501415 14,5 M6 14 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501416 14,5 M6 14 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501515 14,5 M6 15 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501516 14,5 M6 15 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19800501616 14,5 M6 16 16 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-24800581010 20 M6 10 10 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581818 20 M6 18 18 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581819 20 M6 18 19 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581820 20 M6 18 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581825 20 M6 18 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581919 20 M6 19 19 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581920 20 M6 19 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800581925 20 M6 19 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800582020 20 M6 20 20 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800582025 20 M6 20 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-24800582525 20 M6 25 25 10 32 55 16 58 20 18 8 26 57,5 15
23022-25-28800621414 25 M8 14 14 14 37 65 17 62 21 20 9 28 73 40
23022-25-28800622424 25 M8 24 24 14 37 65 17 62 21 20 9 28 73 40
23022-25-28800622828 25 M8 28 28 14 37 65 17 62 21 20 9 28 73 40
23022-25-28800623232 25 M8 32 32 14 37 65 17 62 21 20 9 28 73 40
23022-25-14920320404 10,5 M4 4 4 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920320808 10,5 M4 8 8 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920320810 10,5 M4 8 10 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920320812 10,5 M4 8 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920320814 10,5 M4 8 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920321010 10,5 M4 10 10 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920321012 10,5 M4 10 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920321014 10,5 M4 10 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920321212 10,5 M4 12 12 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920321214 10,5 M4 12 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-14920321414 10,5 M4 14 14 4 16 30 7,8 32 9,5 13 4,5 16,4 35 4,5
23022-25-19920500808 14,5 M6 8 8 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19920501212 14,5 M6 12 12 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19920501214 14,5 M6 12 14 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-19920501215 14,5 M6 12 15 8 21 40 14,5 50 17 16 8 21 46 15
23022-25-28980622424 25 M8 24 24 14 37 65 17 62 21 20 9 28 73 40
23022-25-28980622828 25 M8 28 28 14 37 65 17 62 21 20 9 28 73 40
23022-25-28980623232 25 M8 32 32 14 37 65 17 62 21 20 9 28 73 40
23022-25-38980861818 30 M8 18 18 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-38980862828 30 M8 28 28 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-38980863232 30 M8 32 32 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-38980863838 30 M8 38 38 18 48 80 24 86 31 24 12 38 83,5 40
23022-25-42980942222 32 M10 22 22 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-42980943232 32 M10 32 32 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-42980943838 32 M10 38 38 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-42980944545 32 M10 45 45 22 50 95 25 94 34,5 25 12,5 44 93,5 84
23022-25-48981102222 36 M12 22 22 22 57 105 30 110 41 28 14 50 105 145
23022-25-48981103838 36 M12 38 38 22 57 105 30 110 41 28 14 50 105 145
23022-25-48981104545 36 M12 45 45 22 57 105 30 110 41 28 14 50 105 145
23022-25-48981105050 36 M12 50 50 22 57 105 30 110 41 28 14 50 105 145
© norelem www.norelem.com 8/9