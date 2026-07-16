---
description: Importado de 'PPT-02_Levantamento_de_Projetos_Referência.pdf'.
resource: drive://1hYXoncR0JaCe4kz2xkwcmMTcNAZhIizE
tags: []
timestamp: '2026-07-16T02:44:17Z'
title: Ppt 02 Levantamento De Projetos Referência
type: Conceito
---

Levantamento de Projetos de
Referência: Sistemas de Trituração de
Plástico
Nome: Heitor Pascoal de Oliveira
Objetivo: Estudo aprofundado de referências comerciais e open-source para embasar o
desenvolvimento da Trituradora de Eixo Único para resíduos de PLA e PETG.
1. Felfil Shredder+ e Variante 750
O Felfil Shredder+ é projetado especificamente para laboratórios e entusiastas de impressão
3D, com forte foco na eficiência energética, design compacto e segurança operacional no
manuseio de termoplásticos.
● Especificações Mecânicas e Motorização: A versão de maior capacidade (750) é
equipada com um motor de indução de 750W acoplado a uma caixa de engrenagens
planetárias. Este conjunto reduz a rotação para cerca de 33 RPM, multiplicando o torque
para atingir 36 Nm. Esta relação de alta força e baixa velocidade é fundamental para
"mastigar" o plástico sem gerar fricção excessiva que poderia derreter o PLA (cujo limite
de transição vítrea é muito baixo, próximo a 60°C).
● Arquitetura das Lâminas: O eixo da máquina acomoda 12 lâminas independentes e
substituíveis, fabricadas em aço inoxidável. O design engenhoso distribui essas lâminas
em 4 perfis geométricos distintos ao longo de um arranjo helicoidal (em espiral). Isso
garante que, em qualquer momento da rotação, apenas uma ou duas lâminas estejam
mordendo o material contra a contra-faca (bed knife), evitando picos de tensão mecânica
no eixo e travamentos do motor.
● Controle Eletrônico (Intellishredding): Este é o aspecto mais relevante para a
integração com o projeto atual. O Felfil possui um controlador que monitora a corrente
elétrica do motor em tempo real. Quando uma peça de plástico muito espessa entra na
câmara, o motor demanda mais corrente para manter o torque. Se a corrente atinge um
limite crítico, o sistema aciona um feedback loop que reverte o sentido do motor por
alguns segundos, reposicionando a peça e evitando a quebra mecânica. O uso do sensor
ACS712 proposto para a trituradora de eixo único cumpre exatamente esta mesma
função em caráter de protótipo.
● Granulometria: Entrega flocos de tamanho misto, girando em torno de 6x4 mm.
2. Polystruder GR PRO
O Polystruder GR PRO é um triturador de nível premium que se destaca por incorporar
inteligência algorítmica diretamente no processo de redução de volume, sendo um excelente
case de inovação tecnológica.
● Mecanismo de Corte Escalonado no Eixo Único: Ao contrário dos rotores que utilizam

facas de tamanho padronizado, o GR PRO equipa seu eixo com 19 lâminas de aço
inoxidável temperado, que possuem dupla face de corte (podem ser viradas quando
perdem o fio, dobrando a vida útil). O processo ocorre em estágios simultâneos: 1 lâmina
de perfil grande realiza o primeiro "mordisco" para quebrar a peça matriz; 4 lâminas
médias continuam a fratura, e 14 lâminas menores finalizam o rasgo contra as
contra-facas. Essa transição reduz drasticamente o esforço instantâneo exigido do motor.
● Inteligência Computacional (ShredAI): A máquina ajusta seu comportamento
ativamente. O algoritmo ShredAI mapeia a dureza do material processado através de
sensores mecânicos e elétricos e modula a potência do motor (até 800W) e a velocidade
do rotor para otimizar o tempo de corte sem causar empacamento.
● Ergonomia e Segurança: O projeto investe fortemente no enclausuramento acústico
para manter a operação abaixo de 65 dB, algo raro em granuladores. Conta também com
sensores de intertravamento magnético na tremonha de alimentação para impedir o
acionamento caso a entrada esteja exposta.
● Granulometria: Padronizada em grânulos muito finos de cerca de 3 mm, ideais para
extrusão direta de filamentos.
3. Precious Plastic Shredder (V2.1 e V4 Pro)
O projeto da fundação holandesa Precious Plastic é a maior referência mundial de código
aberto para maquinário de reciclagem descentralizada, sendo um modelo vital para validações
de baixo custo em ambientes maker e acadêmicos.
● Construção Baseada em Corte a Laser: A câmara de corte, em vez de exigir
fresamento CNC complexo em blocos sólidos de aço, é desenhada inteiramente a partir
de chapas de aço cortadas a laser (geralmente aço AISI304 de 5 mm ou 6 mm de
espessura). O conjunto é montado intercalando essas chapas entre facas rotativas e
espaçadores.
● Transmissão de Torque por Eixo Hexagonal: Uma característica fundamental deste
design é o uso de um eixo maciço de perfil hexagonal (geralmente de 27 mm). Isso
dispensa o uso de chavetas (keyways) para prender as facas ao eixo principal, o que
elimina pontos de falha e concentração de tensão, garantindo que o alto torque do
motorredutor seja transmitido uniformemente a todas as lâminas.
● Mecanismo de Controle Passivo por Peneira: O sistema utiliza uma malha metálica
semicilíndrica (peneira) acoplada logo abaixo do rotor. O material fragmentado só escapa
da câmara de corte por gravidade quando o floco de plástico atinge a dimensão dos furos
da peneira (normalmente 5 mm). Se for maior, o rotor continua a girar e elevar a peça
contra as facas fixas superiores até que o tamanho correto seja obtido.
4. Filabot Reclaimer
O Filabot Reclaimer é frequentemente integrado em setups industriais focados em economia
circular de alto rendimento. Seu diferencial é o processamento híbrido sequencial.
● Sistema de Duplo Estágio de Redução: A redução de volume do plástico não acontece
em uma câmara única. O equipamento é fisicamente dividido: o andar superior abriga o
módulo Shredder, composto por contra-facas brutas usinadas em aço liga 4140,

responsáveis por mastigar grandes suportes rígidos de impressão e aglomerados
sólidos.
● Fase de Granulação (Granulator): Após a fratura primária, as peças caem em uma
segunda câmara na parte inferior, equipada com um tambor rotativo veloz de alta
precisão. Este módulo finaliza o corte gerando lascas com qualidade industrial e sem
poeira (o pó de polímero atrapalha a alimentação das extrusoras).
● Relevância Analítica: O estudo deste modelo demonstra a justificativa técnica de
projetar o equipamento da equipe como uma unidade condensada de estágio único (com
eixo dotado de facas em espiral e peneira inferior), para evitar a complexidade
construtiva e o custo de usinagem de dois conjuntos independentes de corte, atendendo
aos escopos delimitados para a disciplina.
5. 3devo SHR3D IT
O granulador SHR3D IT da marca holandesa 3devo tem presença massiva na literatura
científica sobre propriedades reológicas de polímeros reciclados.
● Compressão e Fragmentação Laboratorial: O seu motor interno modula a
fragmentação aplicando compressão direcionada sobre o material antes do corte
agressivo, o que ajuda a quebrar plásticos mais rígidos (como o PETG) de maneira
uniforme sem forçar o rotor principal de forma brusca.
● Manutenção Térmica do Plástico: Muitas máquinas caseiras correm o risco de fundir
os polímeros ao invés de cortá-los. O SHR3D IT é projetado com fluxo de ar interno e
geometrias de corte que mantêm a câmara em temperatura ambiente constante,
preservando a integridade das cadeias poliméricas do material a ser re-extrudado.
● Saída Limpa de 4 mm: Possui eficiência de processamento de até 5,1 kg por hora
operando como um triturador "desktop", garantindo que os grânulos finais sejam
impecáveis, com variação máxima na escala de 4 mm, sem finos ou particulados
não-processáveis.
Tabela Comparativa de Especificações Técnicas
Projeto Granulometria e Arquitetura do Integração e
Controle Mecanismo de Corte Controle
Eletromecânico
Felfil Shredder+ ~6x4 mm (peneira de Eixo único; 12 facas Intellishredding:
malha restritiva) espiraladas em aço Reversão automática
inox (4 geometrias) orientada pelo pico
de corrente do motor
(750W).
Polystruder GR 3 mm Eixo único Algoritmo ShredAI:
PRO escalonado; 19 facas Classificação de

| Projeto  | Granulometria e  | Arquitetura do      | Integração e  |
| -------- | ---------------- | ------------------- | ------------- |
|          | Controle         | Mecanismo de Corte  | Controle      |
Eletromecânico
|     |     | temperadas dupla  | material e    |
| --- | --- | ----------------- | ------------- |
|     |     | face.             | adequação de  |
velocidade/potência
em tempo real.
Precious Plastic  5 mm (limitado por  Contra-rotativo ou  Construção modular
|     | malha inferior  | single-shaft, eixo  | aberta com          |
| --- | --------------- | ------------------- | ------------------- |
|     | perfurada)      | hexagonal 27mm,     | acionamento         |
|     |                 | corte a laser sem   | analógico simples,  |
|     |                 | chavetas.           | focado em alta      |
reprodutibilidade.
Filabot Reclaimer  Granulação apta  Sistema híbrido  Painel de controle
|     | para extrusão direta  | físico em dois     | com                  |
| --- | --------------------- | ------------------ | -------------------- |
|     |                       | estágios: Módulo   | intertravamentos de  |
|     |                       | Shredder acoplado  | segurança e          |
|     |                       | ao Módulo          | acionamento          |
|     |                       | Granulator.        | estagiado de         |
motores.
3devo SHR3D IT  4 mm exatos,  Câmara fechada de  Gerenciamento
|     | filtragem de pó  | alta precisão          | passivo/ativo de       |
| --- | ---------------- | ---------------------- | ---------------------- |
|     | residual         | baseada em             | calor para não         |
|     |                  | compressão             | exceder limites de     |
|     |                  | direcional pré-corte.  | transição vítrea (Tg)  |
de bioplásticos.

Conclusões Direcionais para o projeto
●  Mecânica: A abordagem do Felfil Shredder+ ao organizar facas de diâmetros e perfis
diferentes ao longo do eixo deve ser considerada no desenho do CAD (Semana 3).
Intercalar um rasgo inicial com o corte secundário contra a contra-faca fixa minimizará o
torque necessário (calculado previamente entre 90-120 Nm) para vencer a tenacidade do
PETG.
●  Eletrônica e Segurança: A necessidade de feedback observada no Intellishredding
confirma que a estratégia do cronograma envolvendo o módulo ACS712 com o relé 5V
para reversão de rotação é altamente alinhada com as melhores práticas de mercado.
●  Fabricação do Protótipo: Se o orçamento restrito exigir adaptações, o esquema aberto
do Precious Plastic demonstra a validade da usinagem via corte a laser das facas

montadas em um eixo sextavado, criando um conjunto robusto com um custo fracionário
se comparado ao torneamento em aço SAE 4140 tradicional.
Referências e Links Úteis
● Felfil Shredder+: Página Oficial | Especificações Felfil 750
● Polystruder GR PRO: Página Oficial do Algoritmo ShredAI e Máquina
● Precious Plastic: Kits e Peças (Bazar) | Documentação FabLab
● Filabot Reclaimer: Especificações Shredder | Setup Híbrido Completo
● 3devo SHR3D IT: Estudo de Caso / Artigo (MDPI) com PLA
● Referência Acadêmica de Base (Projeto UTFPR/Cytrynbaum): Sistema de reciclagem
de resíduos provenientes de manufatura aditiva visando produção de filamentos
destinados à impressão 3D (2022)