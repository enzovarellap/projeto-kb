---
description: Importado de 'Trituradora_6_Metodos_SDE_UFABC (1).pptx'.
resource: drive://1h-qHZdfvfTishu_REnW86t2vmzFn7-tO
tags: []
timestamp: '2026-06-24T01:36:16Z'
title: Trituradora 6 Metodos Sde Ufabc (1)
type: Conceito
---

<!-- Slide number: 1 -->

ESMA001-23 · UFABC · 2026.2
6 MANEIRAS DE CONSTRUIR UM
MÓDULO DE
TRITURAÇÃO FDM

Análise técnica comparativa — Grupo Trituradora · SDE 2026.2
Etapa 1 do Sistema de Economia Circular para Resíduos de Impressão 3D

Duplo Rotor

Eixo Único

Granulador

Manivela

Martelos

Tesoura Rotativa

### Notes:

<!-- Slide number: 2 -->
Como esta apresentação está organizada
Para cada método de trituração você encontrará:

Como funciona
O que você precisa
🔍
🔧
Princípio físico e mecanismo de corte
Lista de componentes e requisitos

Vantagens
Custo estimado
✅
💰
Pontos fortes do método
Faixa de investimento em R$

Desvantagens
Tempo de construção
⚠️
⏱️
Limitações e riscos do método
Prazo estimado para implementar
Recomendação para o projeto UFABC:
= Altamente recomendado

### Notes:

<!-- Slide number: 3 -->

Triturador de Duplo Rotor
⚙️

Recomendação

01
Double Shaft Shredder
Referência: Precious Plastic v4 Pro, projetos universitários (U. Arizona, 2025)

💬  O padrão da comunidade maker — dois eixos contra-rotativos com facas intercaladas

🔍  COMO FUNCIONA
Dois eixos hexagonais paralelos giram em sentidos opostos a baixa rotação (40–80 RPM) e alto torque. As facas metálicas intercaladas entre os eixos criam um efeito de tesoura que corta e rasga o plástico. Uma peneira na base controla a granulometria de saída (3–10 mm ajustável).

✅  VANTAGENS
⚠️  DESVANTAGENS
Padrão da indústria maker — Precious Plastic tem documentação aberta completa
Granulometria controlada pela peneira (3–10 mm ajustável sem desmontagem)
Auto-reversão em caso de atolamento — protege o motor
Produção contínua — alimentação por gravidade sem empurrador
Comprovado com PLA, PETG, ABS, HDPE, PA-C e mistos
Usinagem das facas exige precisão e material específico (aço SAE 4140 HRC 50+)
Dois eixos sincronizados aumentam complexidade mecânica
Custo de fabricação maior que soluções de eixo único
Manutenção requer desmontagem para troca de facas

💰 Custo Est.
🔧 Dificuldade
⏱️ Prazo
R$ 1.500 – 3.500
Alta
6–10 semanas

### Notes:

<!-- Slide number: 4 -->

01 · Triturador de Duplo Rotor
O QUE VOCÊ PRECISA PARA REALIZAR

2× eixos hexagonais de aço (25–32 mm), com engrenagens sincronizadoras
Facas de aço SAE 4140 temperado (HRC 50+), espessura 6 mm, ~12–16 unid.

1

2

Contra-facas (spacers) em aço intercaladas entre as facas do rotor
Motor elétrico 0,75–1,5 kW + caixa redutora (saída 40–80 RPM, torque 100–200 Nm)

3

4

Peneira de aço inox removível (malha 3 mm, 5 mm ou 8 mm)
Caixa estrutural em chapa de aço 3–5 mm soldada + funil de alimentação

5

6

Botão de emergência + sensor de atolamento (inversão automática)

7

### Notes:

<!-- Slide number: 5 -->

Triturador de Eixo Único
🔩

Recomendação

02
Single Shaft Shredder
Referência: Felfil Shredder+, Polystruder GR PRO, Conair

💬  Eixo único com empurrador hidráulico — maior controle de granulometria

🔍  COMO FUNCIONA
Um único rotor giratório com facas corta o material contra contra-facas fixas (bed knives) posicionadas na base. Um empurrador lateral (hidráulico, pneumático ou por mola) força o plástico contra o rotor continuamente. O material passa pela peneira quando atinge o tamanho certo — o que não passou recircula.

✅  VANTAGENS
⚠️  DESVANTAGENS
Granulometria muito uniforme — material recircula até atingir o tamanho da peneira
Menor complexidade que duplo eixo — apenas um eixo para sincronizar
Alta eficiência com resíduos FDM de forma irregular
Motor menor que duplo eixo para mesma vazão
Felfil Shredder+ comprovado em laboratórios: 4 kg/h, 36 Nm, 750W
Necessita de empurrador mecânico (hidráulico ou por mola) — componente adicional
Limpeza mais trabalhosa — rotor único acumula material em volta
Não se auto-alimenta tão bem quanto o duplo eixo com peças grandes
Faca de leito fixo (bed knife) exige alinhamento preciso com o rotor

💰 Custo Est.
🔧 Dificuldade
⏱️ Prazo
R$ 1.000 – 2.500
Média-Alta
5–8 semanas

### Notes:

<!-- Slide number: 6 -->

02 · Triturador de Eixo Único
O QUE VOCÊ PRECISA PARA REALIZAR

Rotor de aço com facas em espiral (ou retas), diâmetro 100–150 mm
Contra-faca (bed knife) de aço temperado fixada na base do barril

1

2

Empurrador lateral: mola de compressão + guia OU cilindro pneumático
Motor 0,5–0,75 kW + redutor (saída 100–200 RPM, torque 30–60 Nm)

3

4

Câmara de corte em chapa de aço 4 mm + peneira removível
Arduino + sensor de corrente para detecção de atolamento e reversão

5

6

### Notes:

<!-- Slide number: 7 -->

Granulador de Facas (Granulator)
🔪

Recomendação

03
Knife Granulator / Beside-the-Press
Referência: Energycle Compact Granulator, Conair Granulator Series

💬  Alta rotação com facas em 'V' — produz granulado fino e uniforme em passe único

🔍  COMO FUNCIONA
Ao contrário do shredder (baixa rotação, alto torque), o granulador opera em alta rotação (1.000–3.000 RPM) com múltiplas facas em V fixadas em um rotor. As facas cortam o plástico contra facas fixas com folga mínima (0,1–0,3 mm), gerando granulado de 3–8 mm em passe único sem recirculação.

✅  VANTAGENS
⚠️  DESVANTAGENS
Granulado muito uniforme em passe único — sem peneira de recirculação necessária
Ideal para plásticos frágeis e quebradiços como PLA impresso (baixa temp. de fusão)
Produção mais rápida que shredder para mesma vazão
Compact — menor footprint que shredder de duplo eixo
Alta rotação gera MUITO mais microplásticos e poeira — risco ambiental aumentado
Nível de ruído significativamente maior (90–105 dB sem carcaça)
Não adequado para peças grandes — precisa de pré-corte ou shredder anterior
Motor em alta rotação consome mais energia por kg processado
Facas exigem reafio frequente (vida útil menor que facas de shredder)

💰 Custo Est.
🔧 Dificuldade
⏱️ Prazo
R$ 1.200 – 3.000
Alta
6–9 semanas

### Notes:

<!-- Slide number: 8 -->

03 · Granulador de Facas (Granulator)
O QUE VOCÊ PRECISA PARA REALIZAR

Rotor de aço com 3–6 facas em V, balanceado dinamicamente
Contra-facas fixas de aço (folga 0,1–0,3 mm do rotor — usinagem de precisão)

1

2

Motor 0,75–1,5 kW em alta rotação (sem redutor ou polia)
Câmara fechada com vedação contra microplásticos — essencial

3

4

Sistema de coleta de pó (filtro ou ciclone) — obrigatório em ambiente acadêmico
EPI obrigatório: protetor auricular + máscara N95 + óculos

5

6

### Notes:

<!-- Slide number: 9 -->

Triturador Manual (Hand Crank)
🖐️

Recomendação

04
Manual / Hand Crank Shredder
Referência: Precious Plastic Shredder Mini V2, Sustainable Design Studio UK

💬  Sem motor, sem eletrônica — prova de conceito de baixíssimo custo

🔍  COMO FUNCIONA
O mesmo princípio do duplo rotor (facas intercaladas em eixo hexagonal) mas acionado manualmente por uma manivela. O operador aplica torque diretamente no eixo. O Precious Plastic Shredder Mini V2 usa eixo hexagonal de 19 mm conectável a qualquer chave inglesa, catraca ou furadeira.

✅  VANTAGENS
⚠️  DESVANTAGENS
Custo mínimo — sem motor, sem eletrônica, sem infraestrutura elétrica
Montagem muito mais simples — menos componentes críticos
Perfeito como protótipo funcional e prova de conceito para a Fase 1
Permite validar o design das facas e a granulometria antes de motorizar
Já existe no mercado por ~R$ 800–1.500 como kit completo (Precious Plastic Bazar)
Produção extremamente baixa: < 0,5 kg/h (inviável para uso contínuo)
Esforço físico significativo — inadequado para resíduos maiores ou rígidos
Não escalável para a produção necessária na sala de impressão
Limitado a materiais finos (< 2 mm de parede) e peças pequenas

💰 Custo Est.
🔧 Dificuldade
⏱️ Prazo
R$ 300 – 800
Baixa
2–4 semanas

### Notes:

<!-- Slide number: 10 -->

04 · Triturador Manual (Hand Crank)
O QUE VOCÊ PRECISA PARA REALIZAR

Eixo hexagonal de aço 19 mm (comprimento ~200 mm)
Facas de aço (versão reduzida do duplo rotor) — menos unidades

1

2

Caixa estrutural em chapa dobrada 2–3 mm (menor que a versão motorizada)
Manivela + mancal de rolamento para o eixo

3

4

Peneira de granulometria + recipiente coletor
Opção: conectar furadeira potente (> 500W) como motor improvosado

5

6

### Notes:

<!-- Slide number: 11 -->

Moinho de Martelos (Hammer Mill)
🔨

Recomendação

05
Hammer Mill / Impact Shredder
Referência: Industrial hammer mills para plástico — uso acadêmico experimental

💬  Alta energia de impacto — quebra o plástico por golpes em vez de cortes

🔍  COMO FUNCIONA
Um rotor de alta velocidade carrega martelos articulados (ou fixos) que giram a 1.500–3.600 RPM. O plástico é lançado contra os martelos e depois contra placas de impacto fixas na câmara. O material é quebrado por impacto repetido até passar pela peneira. Funciona melhor com materiais frágeis e quebradiços.

✅  VANTAGENS
⚠️  DESVANTAGENS
Pode processar peças maiores sem pré-corte em alguns casos
Construção dos martelos mais simples que facas de precisão
Excelente para PLA (frágil a temperatura ambiente)
Custo dos martelos menor que facas de shredder de precisão
Ruído extremamente alto: 95–110 dB — inaceitável em ambiente acadêmico sem isolamento total
Geração massiva de microplásticos e pó — risco grave de saúde
Granulometria muito irregular — difícil controlar tamanho de saída
PETG e ABS (materiais elásticos) NÃO quebram por impacto — entopem o sistema
Alta rotação + impacto causam superaquecimento e degradação do polímero
Praticamente inviável DIY com segurança adequada

💰 Custo Est.
🔧 Dificuldade
⏱️ Prazo
R$ 2.000 – 5.000+
Muito Alta
Inviável no prazo da disciplina

### Notes:

<!-- Slide number: 12 -->

05 · Moinho de Martelos (Hammer Mill)
O QUE VOCÊ PRECISA PARA REALIZAR

Rotor de aço balanceado dinamicamente com martelos intercambiáveis
Câmara de impacto em aço de alta espessura (5–8 mm) — impactos violentos

1

2

Motor de alta potência (1,5–3 kW) em alta rotação
Sistema de isolamento acústico completo (< 80 dB externo)

3

4

Sistema de filtragem de microplásticos (ciclone + filtro HEPA)
EPI rigoroso: protetor auricular Classe 5 + respirador P3 + óculos

5

6

### Notes:

<!-- Slide number: 13 -->

Triturador por Tesoura Rotativa
✂️

Recomendação

06
Rotary Scissor / Disc Cutter Shredder
Referência: Felfil Shredder+ (variante), projetos DIY com discos de corte

💬  Discos dentados empilhados em eixo único — alternativa simples ao duplo rotor

🔍  COMO FUNCIONA
Discos dentados (similares a serras circulares) são empilhados em um eixo único com espaçadores entre eles. O eixo gira a baixa rotação (50–150 RPM) e os dentes dos discos cortam o plástico em movimento de tesoura. A variação de espessura e passo dos dentes define a granulometria de saída.

✅  VANTAGENS
⚠️  DESVANTAGENS
Fabricação mais simples que o duplo rotor — apenas um eixo
Discos dentados são mais fáceis de fabricar ou adquirir que facas intercaladas
Funcionamento silencioso comparado ao granulador e hammer mill
Baixo torque necessário para materiais finos de impressão 3D
Manutenção facilitada — discos são removíveis individualmente
Menor eficiência com peças espessas (> 5 mm de parede)
Dentes se desgastam mais rapidamente que facas de shredder em aço temperado
Granulometria menos uniforme que duplo rotor com peneira
Risco de enrolamento de material flexível (PETG) nos discos
Sem peneira de controle — tamanho de saída menos previsível

💰 Custo Est.
🔧 Dificuldade
⏱️ Prazo
R$ 700 – 1.800
Média
4–7 semanas

### Notes:

<!-- Slide number: 14 -->

06 · Triturador por Tesoura Rotativa
O QUE VOCÊ PRECISA PARA REALIZAR

Eixo de aço (25 mm) com chaveta para fixação dos discos
Discos dentados de aço SAE 1045 ou 4140, diâmetro 80–120 mm, ~10–20 unidades

1

2

Espaçadores (spacers) entre os discos para definir largura do corte
Motor 0,37–0,75 kW + redutor (saída 50–150 RPM, torque 30–60 Nm)

3

4

Carcaça com funil de alimentação e gaveta coletora
Mancais de rolamento para suporte do eixo nas duas extremidades

5

6

### Notes:

<!-- Slide number: 15 -->
COMPARATIVO GERAL DOS 6 MÉTODOS
Resumo lado a lado para tomada de decisão do grupo
| Método | Mecanismo | Granulometria | Complexidade | Custo Est. | Recomend. |
| --- | --- | --- | --- | --- | --- |
| 01 · Duplo Rotor | Duplo eixo + facas + peneira | 3–10 mm ajustável | Alta | R$ 1.500–3.500 | ⭐⭐⭐⭐⭐ |
| 02 · Eixo Único | Rotor + bed knife + empurrador | 3–8 mm (peneira) | Média-Alta | R$ 1.000–2.500 | ⭐⭐⭐⭐ |
| 03 · Granulador | Facas em V, alta rotação | 3–8 mm uniforme | Alta | R$ 1.200–3.000 | ⭐⭐⭐ |
| 04 · Manivela | Duplo rotor manual | 3–10 mm | Baixa | R$ 300–800 | ⭐⭐⭐ |
| 05 · Martelos | Impacto de alta rotação | Irregular (3–20mm) | Muito Alta | R$ 2.000–5.000+ | ⭐ |
| 06 · Tesoura Rotativa | Discos dentados, eixo único | 5–15 mm | Média | R$ 700–1.800 | ⭐⭐⭐ |
🏆  Recomendação final: Método 01 (Duplo Rotor) como sistema principal + Método 04 (Manivela) como protótipo inicial de baixo custo para validação das facas e granulometria.

### Notes:

<!-- Slide number: 16 -->

RECOMENDAÇÃO ESTRATÉGICA PARA O GRUPO
Como atingir o objetivo dentro do cronograma da disciplina (entrega Fase 1: 23/07)

Fase 1 · Protótipo de Validação
Semanas 1–3 (até 18/06)

🎯 Entregável
Conjunto de facas funcional + granulometria confirmada (3–5 mm)
📌 Método 04 (Manivela) — construir versão manual do duplo rotor
Por quê: Fabrica o conjunto de facas e a caixa com custo mínimo. Valida o desenho das facas, a granulometria e a interface com a extrusora — sem depender de motor. Pode ser acionado por furadeira para testes rápidos.

Fase 2 · Produto Final
Semanas 4–10 (entrega 23/07)

🎯 Entregável
Trituradora motorizada completa, produzindo fragmentos 3–5 mm de PLA/PETG
📌 Método 01 (Duplo Rotor Motorizado) — adicionar motor ao protótipo da Fase 1
Por quê: Reaproveitando as facas e a caixa já fabricados, integrar o motor com redutor, o sistema elétrico (botão de emergência + inversão por Arduino) e a peneira intercambiável. Este é o produto final para a apresentação.

Paralelo · Interface Crítica
Antes de 18/06 — urgente

🎯 Entregável
Ata de reunião com especificação de interface: granulometria máx. acordada
📌 Alinhamento formal com grupo da Extrusora
Por quê: Confirmar: qual o tamanho máximo de fragmento que a extrusora aceita? A resposta define o tamanho da tela de saída da nossa trituradora. Sem essa informação, não conseguimos fechar o projeto.

### Notes: