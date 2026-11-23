## 1. Plano de validação

O protótipo será avaliado com **o mesmo protocolo da Fase 4**: mesmas regras de condução, mesmas falas neutras, mesmos códigos de registro e mesma ficha por participante. Assim, os resultados podem ser comparados diretamente com os [Resultados de G1](../resultados-g1-capacidade-interacao.md).

### 1.1 Visão geral da sessão

| Etapa | Cenário | Conteúdo | Tempo previsto |
|---|---|---|---|
| 1 | Abertura | Fala inicial, termo de consentimento e pergunta de perfil (iguais aos da Fase 4) | 5 a 7 min |
| 2 | U-03 (M9) | Duas telas para reconhecimento: Tela A (Nada Consta, sem alteração) e Tela B (novo protótipo de Indicadores de Continuidade) | Até 30 s de observação por tela, mais a resposta |
| 3 | U-04 (M10) | Duas tarefas de operação no protótipo: T4 (trocar o período) e T5 (alternar entre tabela e gráfico) | Até 5 min por tarefa |
| 4 | Encerramento | Perguntas abertas opcionais e agradecimento | 3 a 5 min |

A Tela A continua na sessão para manter as **duas apresentações por participante** de M9, como na Fase 4, e serve de controle: se o reconhecimento da Tela A cair, o problema está na sessão, não no protótipo.

### 1.2 Definições fixadas no piloto

Executar o roteiro completo uma vez com um integrante da equipe, como na Fase 4. Depois da primeira sessão, estas definições não mudam.

| Item | Valor fixado |
|---|---|
| Endereço da Tela B e das tarefas | `prototipo/index.html?cenario=ficticio&painel=0` (dados fictícios, sem o seletor de cenário) |
| Estado inicial | Período de outubro/2025 a setembro/2026, gráfico de "Tempo sem energia", último mês selecionado |
| Retorno ao ponto de partida | Recarregar a página (F5), que restaura o estado inicial |
| Período-alvo de T4 | Abril/2026 a setembro/2026 |
| Resultado esperado de T4 | Gráfico exibindo somente os seis meses de abril/2026 a setembro/2026 |
| Resultado esperado de T5 | Tabela exibida e, em seguida, gráfico exibido novamente |

### 1.3 Regras de condução

Valem as regras da Fase 4, sem alteração:

- **Falas neutras permitidas:** repetir a instrução com as mesmas palavras; "Faça como faria se estivesse sozinho(a)."; "Quando achar que concluiu, é só me avisar."; se o participante perguntar "É aqui?" ou "Está certo?": "Se acha que concluiu, pode me avisar; se não, pode continuar."
- **Não permitido:** apontar a tela, nomear menus, campos ou botões, confirmar ou negar escolhas, sugerir que volte ou tente outro lugar, ou reagir de modo que indique acerto ou erro.
- **Tempo:** o anotador inicia o cronômetro quando o mediador termina de ler a instrução e o para quando o participante avisa que concluiu, desiste ou atinge o tempo-limite.
- **Entre tarefas:** o mediador recarrega a página, sem comentar o resultado.

| Situação | Registro |
|---|---|
| Pedido de esclarecimento respondido apenas com a repetição literal da instrução | Não é ajuda. Anotar em observações. |
| Qualquer indicação de caminho, rótulo ou resposta, ainda que involuntária | AJ — ajuda: insucesso. |
| O participante diz que não consegue ou que desiste da tarefa | DE — desistência: insucesso. Seguir para a próxima tarefa. |
| Tempo-limite atingido (5 min em U-04) | TE — tempo esgotado: insucesso. |
| Resultado diferente do esperado ao avisar que concluiu | EO — erro de operação: insucesso. |
| Erro do sistema, função indisponível ou conteúdo que não carrega em 30 s | FS — falha do sistema: tarefa excluída do cálculo, com justificativa. A mesma tarefa não é repetida com o mesmo participante. |
| O participante decide encerrar a participação | IP — interrompida: a tarefa em andamento e as seguintes ficam fora do cálculo. |

### 7.4 U-03: observar a tela por até 30 segundos e responder para que ela serve

**(M9) — Reconhecimento da finalidade da tela**

**Objetivo:** verificar se os participantes reconhecem a finalidade da nova tela de Indicadores de Continuidade.

**Procedimento:**

1. Com o participante sem olhar para o monitor, o mediador abre a tela, espera o carregamento completo e afasta o mouse.
2. Ler: "Vou mostrar uma tela por até 30 segundos. Apenas observe, sem clicar. Depois vou fazer uma pergunta."
3. Iniciar a contagem de 30 segundos. O participante pode avisar antes que terminou de observar.
4. Ao final, minimizar ou cobrir a tela e entregar o cartão com as quatro alternativas.
5. Ler: "Para que serve esta tela?" e, em seguida, as quatro alternativas, na ordem do cartão.
6. Registrar a letra escolhida, sem comentar. Se o participante não escolher nenhuma, registrar "sem resposta".
7. Repetir com a outra tela.

**Pergunta padrão:** "Para que serve esta tela?"

**Tela A — Relatório de Nada Consta** (sem alteração)   
- a. Emitir a segunda via detalhada da última fatura de energia.    
- b. Comprovar que não existem débitos pendentes vinculados à unidade consumidora. **(Correta)**    
- c. Solicitar o religamento da energia após um corte por falta de pagamento.   
- d. Atualizar os dados cadastrais e o nome do titular da conta.    

**Tela B — Indicadores de Continuidade** (protótipo)    
- a. Exibir os indicadores e a qualidade do fornecimento de energia na unidade consumidora. **(Correta)**   
- b. Acompanhar o histórico de consumo de energia da residência nos últimos meses.  
- c. Cadastrar a conta de energia para pagamento em débito automático.  
- d. Informar a falta de energia na residência em tempo real.   

As alternativas são as mesmas da Fase 4, para que a comparação com o resultado anterior (3 de 5 na Tela B) seja direta.

**Códigos:** S — sucesso (alternativa correta); IN — alternativa incorreta ou sem resposta.

### 1.5 U-04: usar o gráfico do protótipo

**(M10) — Tarefas de operação concluídas**

**Objetivo:** observar se os participantes conseguem usar o gráfico de forma dinâmica, trocando o período e alternando entre tabela e gráfico, até o resultado esperado.

**Condição:** cada tarefa começa no estado inicial da Tela B, já aberta pelo mediador.

**Instruções (ler exatamente):**

**T4 — Trocar o período**
> "Nesta tela, faça aparecer somente os meses de abril a setembro de 2026. Quando terminar, me avise."

**T5 — Alternar entre tabela e gráfico**
> "Agora, veja essas mesmas informações organizadas em linhas e colunas. Depois, volte para a forma como elas estavam antes. Quando terminar, me avise."

As instruções descrevem a necessidade sem usar os rótulos da interface ("Período", "De", "até", "Ver tabela", "Ver gráfico"), para não indicar o caminho. Se o piloto mostrar que alguma fala é ambígua, ajustá-la antes da primeira sessão.

**Fim da tentativa:** quando o participante avisa que terminou, desiste ou completa 5 minutos.

Desvios corrigidos pelo próprio participante sem recomeçar a tarefa, como escolher um mês errado e corrigi-lo, não são erros de operação, mas devem ser anotados em observações.

**Códigos:** S — sucesso; CI — caminho incorreto; AJ — ajuda; DE — desistência; TE — tempo esgotado; EO — erro de operação; FS — falha do sistema; IP — interrompida.

### 1.6 Encerramento

**Perguntas abertas (opcionais):** não entram no cálculo das métricas e são anotadas sem dados que identifiquem o participante.
- "Qual das tarefas foi mais difícil? O que dificultou?"
- "Alguma palavra ou tela deixou você em dúvida?"

### 1.7 Ficha de registro por participante
#### Tabela P01

| Identificador | Tarefa | Tempo | Código | Situação | Observações |
|---|---|---|---|---|---|
| M9-U03-AAAAMMDD-Pxx-TA | Tela A — Nada Consta | | | | |
| M9-U03-AAAAMMDD-Pxx-TB | Tela B — Indicadores de Continuidade (protótipo) | | | | |
| M10-U04-AAAAMMDD-Pxx-T4 | T4 — trocar o período | | | | |
| M10-U04-AAAAMMDD-Pxx-T5 | T5 — alternar entre tabela e gráfico | | | | |

#### Tabela P02

| Identificador | Tarefa | Tempo | Código | Situação | Observações |
|---|---|---|---|---|---|
| M9-U03-AAAAMMDD-Pxx-TA | Tela A — Nada Consta | | | | |
| M9-U03-AAAAMMDD-Pxx-TB | Tela B — Indicadores de Continuidade (protótipo) | | | | |
| M10-U04-AAAAMMDD-Pxx-T4 | T4 — trocar o período | | | | |
| M10-U04-AAAAMMDD-Pxx-T5 | T5 — alternar entre tabela e gráfico | | | | |

### 1.8 Critérios de aceite e amostra

| Métrica | Fórmula | Critério de aceite |
|---|---|---|
| M9 | `100 × K / N` (telas reconhecidas / apresentações elegíveis) | **≥ 80%** (H9). |
| M10 | `100 × O / N` (tarefas concluídas sem erro e sem ajuda / tarefas elegíveis) | **≥ 80%** (H10) |


## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 23/11/2026 | Criação da página de plano de validação | Beatriz |