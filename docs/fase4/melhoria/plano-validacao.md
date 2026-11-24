## 1. Plano de validação

O protótipo será avaliado com **o mesmo protocolo da Fase 4**: mesmas regras de condução, mesmas falas neutras, mesmos códigos de registro e mesma ficha por participante. Assim, os resultados podem ser comparados diretamente com os [Resultados de G1](../resultados-g1-capacidade-interacao.md).

### 1.1 Visão geral da sessão

| Etapa | Cenário | Conteúdo | Tempo previsto |
|---|---|---|---|
| 1 | Abertura | Fala inicial, termo de consentimento e pergunta de perfil (iguais aos da Fase 4) | 5 a 7 min |
| 2 | U-03 (M9) | Tela B (novo protótipo de Indicadores de Continuidade) | Até 30 s de observação por tela, mais a resposta |
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

### 1.4 U-03: observar a tela por até 30 segundos e responder para que ela serve

**(M9) — Reconhecimento da finalidade da tela**

**Objetivo:** verificar se os participantes reconhecem a finalidade da nova tela de Indicadores de Continuidade.

**Procedimento:**

1. Com o participante sem olhar para o monitor, o mediador abre a tela, espera o carregamento completo e afasta o mouse.
2. Ler: "Vou mostrar uma tela por até 30 segundos. Apenas observe, sem clicar. Depois vou fazer uma pergunta."
3. Iniciar a contagem de 30 segundos. O participante pode avisar antes que terminou de observar.
4. Ao final, minimizar ou cobrir a tela e entregar o cartão com as quatro alternativas.
5. Ler: "Para que serve esta tela?" e, em seguida, as quatro alternativas, na ordem do cartão.
6. Registrar a letra escolhida, sem comentar. Se o participante não escolher nenhuma, registrar "sem resposta".

**Pergunta padrão:** "Para que serve esta tela?" 

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
> "Agora, veja essas mesmas informações organizadas em tabela. Depois, volte para a forma como elas estavam antes. Quando terminar, me avise."

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
| M9-U03-20261123-P01-TB | Tela B — Indicadores de Continuidade (protótipo) Alternativa: A| 3 s | S | Elegível | Não demonstrou dúvida entre as alternativas |
| M10-U04-20261123-P01-T4 | T4 — trocar o período | 7 s | S | Elegível | - |
| M10-U04-20261123-P01-T5 | T5 — alternar entre tabela e gráfico | 17 s | S | Elegível | - |

**Observações da entrevista:** Participante comentou que achou a página fácil, mas que o campo de seleção para os indicadores poderia ter mais destaque.

#### Tabela P02

| Identificador | Tarefa | Tempo | Código | Situação | Observações |
|---|---|---|---|---|---|
| M9-U03-20261123-P02-TB | Tela B — Indicadores de Continuidade (protótipo) Alternativa: A| 90 s | S | Elegível | Solicitou que repetice as alternativas. P02 comentou ter ficado em dúvida entre A e D |
| M10-U04-20261123-P02-T4 | T4 — trocar o período | 14 s | S | Elegível | - |
| M10-U04-20261123-P02-T5 | T5 — alternar entre tabela e gráfico | 108 s | S | Elegível | - |

**Observações da entrevista:** Foi solicitado que P02 falasse com as próprias palavras o que achava ser a função da Tela B (protótipo). entrevistadora concluiu que P02 entendeu a função da página, mas as alternativas causaram dúvidas.


### 1.8 Critérios de aceite e amostra

| Métrica | Fórmula | Critério de aceite |
|---|---|---|
| M9 | `100 × K / N` (telas reconhecidas / apresentações elegíveis) | **≥ 80%** (H9). |
| M10 | `100 × O / N` (tarefas concluídas sem erro e sem ajuda / tarefas elegíveis) | **≥ 80%** (H10) |

## 2. Resultados da validação 
 
Esta seção apresenta os resultados das sessões de 23/11/2026 com o protótipo da tela de Indicadores de Continuidade. Foram realizadas **2 sessões**. Por isso, os percentuais abaixo são **descritivos**.

### 2.1 M9 — Reconhecimento da finalidade da tela
 
**Questão Q9:** Os usuários reconhecem de imediato se a tela atende à sua necessidade de informação?
 
**Hipótese H9:** ao menos 80% das telas apresentadas terão sua finalidade reconhecida corretamente.
 
**Cálculo:** `M9 = 100 × 2 / 2 = 100%`.
 
**Classificação:** descritiva, **Excelente** (95% ou mais).
 
**Resultado da hipótese:** *inconclusiva (apenas 2 apresentações; a Fase 4 usou 10).
 
| Participante | Familiaridade digital | Alternativa | Código | Tempo | Observação |
|---|---|---|---|---|---|
| P01 | Alta | A (correta) | S | 3 s | Respondeu sem demonstrar dúvida |
| P02 | **Baixa** | A (correta) | S | 90 s | Pediu a repetição das alternativas; ficou em dúvida entre A e D |
 
**Análise:**
 
- **A confusão com o consumo não apareceu.** Na Fase 4, os dois erros da Tela B escolheram a alternativa B ("histórico de consumo"). Com o protótipo, nenhum participante a considerou, o que indica que o subtítulo, o gráfico e os cartões do mês deixam claro que a tela não trata de consumo. O título "Indicadores de Continuidade" foi mantido.
- **Comparação com a Fase 4.** A tela original foi reconhecida por 3 de 5 participantes (60%), e só 1 respondeu sem hesitar. Com o protótipo, 2 de 2 reconheceram a tela e 1 respondeu sem hesitar. O resultado é favorável, mas a amostra ainda é pequena para comparação.
- **Nova dúvida: alternativa D.** P02 hesitou entre A ("indicadores e qualidade do fornecimento") e D ("informar a falta de energia em tempo real"). O subtítulo fala de quando "a energia faltou", e isso pode ser lido como um serviço de aviso de falta. Ver a mudança S1.
- **Resposta com as próprias palavras.** A pedido da entrevistadora, P02 explicou a tela com as próprias palavras e mostrou ter entendido a função, o que reforça que a dúvida veio da proximidade entre as alternativas. Essa pergunta não faz parte do roteiro, então é registrada só como observação qualitativa e não muda o cálculo.
- **Perfil.** P02, de baixa familiaridade digital, reconheceu a tela. Na Fase 4, a única pessoa de baixa familiaridade errou a tela original, escolhendo "histórico de consumo". A hesitação de P02 mostra, porém, que o reconhecimento ainda exige mais esforço desse perfil. Com um participante por perfil, não é possível tirar conclusões sobre a relação entre familiaridade e resultado.
- **Tempos.** Os tempos de M9 correspondem ao tempo para escolher a alternativa e não entram no cálculo. Os 90 s de P02 incluem a repetição das alternativas.

### 2.2 M10 — Tarefas de operação
 
**Questão Q10:** Os usuários conseguem operar as funções até o resultado esperado sem erro e sem ajuda?
 
**Hipótese H10:** ao menos 80% das tarefas de operação serão concluídas sem erro e sem ajuda.
 
**Cálculo:** `M10 = 100 × 4 / 4 = 100%`.
 
**Classificação:** descritiva, **Excelente** (95% ou mais).
 
**Resultado da hipótese:** inconclusiva (apenas 4 tarefas; mínimo de 10).
 
| Tarefa | P01 (familiaridade alta) | P02 (familiaridade baixa) | Sucessos |
|---|---|---|---|
| T4 — trocar o período | S, 7 s | S, 14 s | 2 de 2 |
| T5 — alternar entre tabela e gráfico | S, 17 s | S, 108 s | 2 de 2 |
 
**Análise:**
 
- **Trocar o período (T4).** As duas tarefas foram concluídas em poucos segundos, muito abaixo do limite de 5 minutos. Os campos "De" e "até" foram encontrados e usados sem dificuldade.
- **Alternar entre tabela e gráfico (T5).** As duas tarefas foram concluídas, mas P02 levou 108 s, seis vezes o tempo de P01. Os comandos "Ver tabela" e "Ver gráfico" eram links de texto discretos, o que pode ter atrasado a localização.
- **Destaque das opções.** P01 comentou que achou a página fácil, mas que o seletor de indicadores poderia ter mais destaque. Esse comentário e o tempo de P02 em T5 apontam na mesma direção: os elementos clicáveis precisam se parecer mais com botões.
 
### 2.3 Mudanças a partir da validação
 
| ID | Sugestão | Evidência |
|---|---|---|
| S1 | Incluir "mês a mês" no subtítulo ("Veja, mês a mês, quantas vezes e por quanto tempo a energia faltou no seu endereço"), para indicar que a tela mostra meses anteriores e não avisos em tempo real | P02 (baixa familiaridade) em dúvida entre A e D |
| S2 | Dar mais destaque aos elementos clicáveis: letra um pouco maior, seletor de indicadores com contorno verde e opção ativa preenchida, campos de período com contorno, e "Ver tabela", "Baixar CSV" e "Imprimir" como botões | Comentário de P01 (alta familiaridade); P02 (baixa familiaridade) levou 108 s em T5 |

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 23/11/2026 | Criação da página de plano de validação | Beatriz |
| 1.1 | 23/11/2026 | Adiciona dados de entrevistas d=com voluntários, análises da entrevistadora e sugestões de mudanças | Beatriz |