---
type: Playbook
title: Configurando um Agente de IA Dedicado (Claude / ChatGPT)
description: Como configurar Claude e ChatGPT para consultarem o MCP projeto-kb proativamente, sem precisar pedir isso a cada conversa.
resource: ""
tags: [mcp, agente, chatgpt, claude, onboarding]
timestamp: 2026-07-16T00:00:00Z
---

# Configurando um Agente de IA Dedicado

Este playbook resolve um problema observado na prática: o MCP `projeto-kb` estava
conectado e funcionando, mas o ChatGPT não pensou em consultá-lo sozinho. Ao perguntar
"quais métodos de trituração existem no projeto?", ele respondeu com perguntas
genéricas (era sobre um jogo? um projeto Laravel?) e só buscou na KB depois que o
usuário mandou explicitamente: *"Utilize o MCP do Projeto KB para encontrar as
informações necessárias"*. A partir daí, o resultado foi bom — achou o documento certo
e descreveu os dois estágios de trituração corretamente. **O problema não era a
qualidade da busca, era o gatilho: o modelo não decidiu buscar por conta própria.**

As descrições de cada tool (ver `server.py`) ensinam a IA *como* usar o MCP uma vez que
ela decide chamá-lo — mas não garantem que ela vá lembrar de chamá-lo. Isso é papel de
um nível acima: instruções persistentes de agente, configuradas na plataforma (Custom
GPT / Project). Por isso este guia é uma **ação manual** (equivalente às demais
pendências de configuração de plataforma já registradas no [índice de
pendências](../../README.md#pendências--bloqueio-humano) do repositório).

## Texto de instrução (copiar/colar)

Use exatamente este texto no campo de instruções da plataforma escolhida (seções
abaixo). É o mesmo texto para Claude e ChatGPT — a única diferença é onde colar.

```
Você é o assistente do grupo Trituradora FDM — projeto SDE 2026.2 (ESMA001-23, UFABC).
Você tem acesso ao MCP "projeto-kb": uma base de conhecimento com toda a documentação
do projeto (métodos de trituração, viabilidade, cronogramas, atas, relatórios etc.),
sincronizada do Google Drive do grupo.

REGRA OBRIGATÓRIA — consulte a KB antes de perguntar ao usuário:
Se a pergunta mencionar (ou parecer se referir a) o projeto, o grupo, "SDE", "SDE
2026"/"SDE 2026.2", "trituradora", "extrusora", "ESMA001", "UFABC", métodos de
trituração, cronogramas, equipe, viabilidade, componentes, ou qualquer tema técnico que
não esteja no seu conhecimento geral: use as tools do MCP projeto-kb ANTES de responder
ou pedir mais contexto. Nunca peça link de repositório, documentação, ou explicação do
que é "SDE" — a resposta quase certamente já está na KB.

Como navegar (resumo — os detalhes completos estão na descrição de cada tool):
1. Pergunta ampla / não sabe por onde começar -> list_topics ou get_index.
2. Sabe termos técnicos específicos -> search primeiro.
3. search não achou nada, ou a pergunta é conceitual/parafraseada -> semantic_search.
4. Sempre que for citar conteúdo -> fetch pelo id antes de responder (as outras tools só
   devolvem snippets, nunca o texto completo).
5. Pergunta sobre o que mudou recentemente -> get_log. Visão geral do bundle -> get_stats.

Só pergunte ao usuário como último recurso, depois de a KB não retornar nada relevante
(ex: search e semantic_search sem resultado, ou tema claramente fora do escopo do
projeto) — e diga o que você já tentou buscar antes de pedir mais informação.

Responda em português (o KB é todo em PT-BR) e cite o documento de origem (id/título)
quando relevante, como em "conforme o documento X".
```

## ChatGPT

1. Configurações → Connectors/Apps → Developer Mode → adicionar o servidor MCP
   `projeto-kb` (URL pública + API key), se ainda não estiver feito (ver
   [Pendências #3](../../README.md#3-chatgpt--criar-o-connector-e-testar) no README).
2. Duas formas de aplicar o texto acima, em ordem de preferência:
   - **Custom GPT dedicado** (GPT Builder → criar novo GPT, ex: "Assistente SDE —
     Trituradora FDM"): cole o texto no campo *Instructions* e anexe o connector
     `projeto-kb`. Vantagem: fica isolado (não afeta outras conversas do ChatGPT) e é
     compartilhável com o resto do grupo.
   - **Custom Instructions da conta** (Configurações → Personalização): cole o texto lá
     se não for possível/necessário isolar em um GPT dedicado. Desvantagem: vale para
     toda conversa no ChatGPT, não só as do projeto.
3. Lembrete do que já está documentado no `TODO.md` (Fase 5.2): em modo Deep Research/
   Company Knowledge o ChatGPT só enxerga `search`/`fetch` (contrato fixo); as outras 4
   tools (`semantic_search`, `list_topics`, `get_log`, `get_stats`, `get_index`) só
   ficam disponíveis em modo chat normal com Developer Mode ligado. O texto acima cobre
   os dois casos, mas o passo 1 do fluxo (`list_topics`/`get_index`) só se aplica fora
   do Deep Research.

## Claude (claude.ai)

1. Settings → Connectors → adicionar o servidor MCP `projeto-kb` (URL pública + API
   key), igual à configuração já documentada para Claude Desktop no README.
2. Criar um **Project** (ex: "Trituradora FDM — SDE 2026.2"), colar o texto acima no
   campo de instruções do Project ("Project instructions"), e garantir que o connector
   `projeto-kb` esteja habilitado para esse Project. Toda conversa aberta dentro desse
   Project herda as instruções e o acesso ao connector automaticamente.

## Como validar que funcionou

Teste com uma pergunta parecida com a que expôs o problema original — algo que
dependa da KB e que a IA não tenha como responder de outro jeito, **sem** dizer
explicitamente "use o MCP":

> "Quais métodos de trituração existem no projeto SDE?"

Se a IA responder direto (com uma tool call visível ou não) em vez de perguntar "qual
projeto é esse?" ou pedir um link de repositório, a configuração está funcionando.
