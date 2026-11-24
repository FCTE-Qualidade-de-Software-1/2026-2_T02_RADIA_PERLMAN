# Resultados de G1 — Capacidade de Interação

Esta página apresenta os resultados do objetivo G1 obtidos com voluntários (M1, M9 e M10). A M2 (tratamento de entradas inválidas) é coletada pela equipe, sem voluntários.

As fórmulas, as faixas de pontuação e as quantidades mínimas são as definidas em [Métricas](../fase2/metricas.md) e nos [Critérios de julgamento](../fase2/criterios-julgamento.md). Os dados brutos estão nas fichas do roteiro de coleta de capacidade de interação.

## 1. M1 — Localização de funcionalidades
 
**Questão Q1:** Os usuários conseguem localizar as funções sem auxílio?
 
**Hipótese H1:** ao menos 80% das tarefas de localização serão concluídas na primeira tentativa e sem ajuda.
 
**Fórmula:** `M1 = 100 × S / N`, em que **S** = tarefas localizadas corretamente na primeira tentativa e sem ajuda; **N** = tarefas de localização elegíveis.
 
**Cálculo:** `M1 = 100 × 10 / 10 = 100%`.
 
**Classificação:** **Excelente** (95% ou mais).
 
**Resultado da hipótese:** **H1 sustentada** (M1 ≥ 80%, com amostra mínima).
 
**Análise:**
 
- **Desempenho por tarefa.** Todas as tarefas foram concluídas na primeira tentativa, sem ajuda e muito abaixo do limite de 3 minutos. A mediana foi de 10 s em T1 e de 11 s em T2. Nenhum participante seguiu caminho incorreto.
- **Sucesso com hesitação.** P03 e P04 acharam a tela inicial pouco intuitiva. P04 encontrou o histórico, mas não teve certeza de que estava no lugar certo, o que é coerente com a tela observada: uma tabela de leituras e valores.
- **Tempos.** Como o tempo não entra no cálculo de M1, a classificação não muda, mas os tempos não devem ser comparados entre sessões.
- **Resposta a Q1:** sim. Todos os participantes localizaram a 2ª via e o histórico de consumo sem auxílio, embora parte deles tenha considerado a tela inicial pouco intuitiva.
 
## 2. M2 — Tratamento de entradas inválidas

**Questão Q2:** Os formulários ajudam a corrigir entradas inválidas?

**Hipótese H2:** ao menos 80% das entradas inválidas serão sinalizadas antes do envio, com orientação para a correção.

**Fórmula:** `M2 = 100 × V / N`, em que **V** = tentativas inválidas tratadas adequadamente e **N** = tentativas inválidas elegíveis. Uma tentativa só é considerada adequada quando a interface impede ou sinaliza o erro **e** apresenta orientação compreensível para a correção.

**Dados da coleta:** a avaliação foi realizada por Isabella em 16/11/2026, às 18h40, no cenário U-02. Foram registrados onze casos (T01 a T11); T09 foi excluído conforme a ficha de coleta, restando dez tentativas elegíveis.

**Tabela — Consolidação das tentativas da M2**

| Classificação | Tentativas | Registros |
|---|---:|---|
| Adequadas | 4 | T06, T07, T08 e T11 |
| Inadequadas | 6 | T01, T02, T03, T04, T05 e T10 |
| Excluída | 1 | T09 |
| **Total registrado** | **11** | **10 elegíveis + 1 excluída** |

**Cálculo:** `M2 = 100 × 4 / 10 = 40%`.

**Classificação:** **Insatisfatório** (abaixo de 60%).

**Resultado da hipótese:** **H2 não sustentada** (M2 = 40%, abaixo do requisito de 80%).

**Análise:**

- **Ausência de orientação específica no cadastro.** Em T01, T02 e T03, o campo CPF ficou destacado em vermelho, mas não apresentou mensagem explicativa que indicasse o problema ou como corrigi-lo.
- **Campo obrigatório sem instrução.** Em T04, o campo vazio impediu o prosseguimento, porém não houve orientação textual para o usuário.
- **Mensagens genéricas.** Em T05 e T10, a interface exibiu “Realize o procedimento de segurança”, sem indicar qual informação precisava ser corrigida.
- **Respostas adequadas.** T06, T07 e T08 apresentaram avisos relacionados ao preenchimento do CPF/CNPJ no login. Em T11, foi exibida a mensagem “Senha é obrigatória”. Esses quatro registros atenderam ao critério definido para a métrica.
- **Interpretação.** O destaque visual de um campo ou o bloqueio do avanço, isoladamente, não garantem que o usuário compreenda o erro. A métrica exige também uma orientação clara e útil para a correção.
- **Resposta a Q2:** parcialmente. Quatro das dez tentativas elegíveis foram tratadas adequadamente (40%). Nas demais, faltou mensagem explicativa ou foi apresentada uma mensagem genérica, sem indicação clara do dado a corrigir. Portanto, os formulários não atingiram a hipótese H2.

**Oportunidades de melhoria:** apresentar mensagens textuais junto aos campos inválidos; diferenciar campos obrigatórios de valores em formato incorreto; substituir mensagens genéricas por instruções específicas que não exponham informações sensíveis; e padronizar o feedback entre cadastro e login.

**Evidências:** a [ficha consolidada da M2](../evidencias/M2/M2-Tabela-16112026-03.png) reúne os onze registros, as classificações e a elegibilidade. As [capturas das entradas inválidas — parte 1](../evidencias/M2/M2-U02-16112026-01.png) e [parte 2](../evidencias/M2/M2-U02-16112026-02.png) ilustram as respostas observadas. Os dados individuais estão no [CSV da M2](../dados-coleta/M2/M2-registros.csv), e o procedimento e a consolidação estão descritos no [registro individual da coleta](../dados-coleta/M2/M2-resultados.md).

**Limitações:** a coleta representa os campos e fluxos acessíveis nas condições observadas em 16/11/2026. Não foram realizados envios que pudessem concluir operações ou alterar dados. A métrica avalia o feedback perceptível ao usuário, não a implementação interna da validação. O registro T09 foi excluído conforme a ficha original e não integra o denominador.
 
## 3. M9 — Reconhecimento da finalidade da tela
 
**Questão Q9:** Os usuários reconhecem de imediato se a tela atende à sua necessidade de informação?
 
**Hipótese H9:** ao menos 80% das telas apresentadas terão sua finalidade reconhecida corretamente.
 
**Fórmula:** `M9 = 100 × K / N`, em que **K** = telas cuja finalidade foi reconhecida corretamente; **N** = apresentações de tela elegíveis.
 
**Cálculo:** `M9 = 100 × 8 / 10 = 80%`.

**Classificação:** **Alvo** (de 80% a menos de 95%).
 
**Resultado da hipótese:** **H9 sustentada** (M9 ≥ 80%, com amostra mínima).
 
**Análise:**
 
- **A tela de indicadores concentra as dificuldades.** Quatro dos cinco participantes tiveram dificuldade com a Tela B: dois erraram e dois só acertaram depois de pedir a repetição das alternativas. Apenas P05 respondeu sem hesitar.
- **Confusão com o histórico de consumo.** Os dois erros na Tela B escolheram a mesma alternativa: “acompanhar o histórico de consumo”.
- **Nada Consta.** Todos os participantes reconheceram a finalidade da tela.
- **Perfil e erros.** P02, a única pessoa com baixa familiaridade digital, acertou o Nada Consta e errou a tela de indicadores, assim como P03, que tem alta familiaridade. Os dados não indicam relação entre familiaridade e erro, mas a amostra é pequena demais para conclusões nesse sentido.
- **Resultado por tela.** A Fase 2 define M9 como uma única proporção. Os percentuais de 100% e 60% são descritivos e ajudam a localizar a dificuldade; a classificação usa os 80% agregados.
- **Registro das sessões.** Os tempos anotados em M9 correspondem ao tempo para escolher a alternativa e não entram no cálculo.
- **Resposta a Q9:** sim, no limite previsto, mas com diferença entre as telas: a finalidade do Nada Consta foi reconhecida por todos, enquanto a dos Indicadores de Continuidade foi reconhecida por três dos cinco participantes.
 
## 4. M10 — Tarefas de operação
 
**Questão Q10:** Os usuários conseguem operar as funções até o resultado esperado sem erro e sem ajuda?
 
**Hipótese H10:** ao menos 80% das tarefas de operação serão concluídas sem erro e sem ajuda.
 
**Fórmula:** `M10 = 100 × O / N`, em que **O** = tarefas concluídas sem erro e sem ajuda; **N** = tarefas de operação elegíveis.
 
**Dados da coleta e exclusão da T4:** o protocolo da Fase 2 prevê duas tarefas por participante (total mínimo de 10 tarefas elegíveis): emissão da 2ª via (T3) e alteração do período do gráfico de consumo (T4). Durante a execução, constatou-se que a interface real do Histórico de Consumo exibe apenas uma **tabela estática**, sem gráfico interativo ou seletor de período. Por essa razão, a tarefa T4 foi excluída, restando apenas **5 tarefas elegíveis** (referentes à T3), abaixo da amostra mínima de 10 tarefas estabelecida na Fase 2.

**Resultado descritivo (T3):** 5 de 5 participantes concluíram a emissão da 2ª via sem erro e sem ajuda (`100%` na tarefa executável).
 
**Classificação:** **Inconclusiva** (amostra elegível de 5 tarefas, inferior ao mínimo de 10 definido na Fase 2).
 
**Resultado da hipótese:** **H10 inconclusiva** (não é possível sustentar ou refutar a hipótese sem atingir a amostra mínima prevista).
 
**Análise:**
 
- **Conclusão da tarefa executável (T3).** Todos os cinco participantes emitiram a 2ª via sem ajuda e dentro do limite de 5 minutos, com mediana de 19 s.
- **Ícone de impressão.** P02 levou 190 s, quase dois terços do limite. Chegou à tela correta, mas demorou a perceber que o ícone de impressora — que não possui rótulo textual — era o comando para gerar o PDF.
- **Impedimento metodológico (T4).** Conforme a regra de transparência dos critérios de julgamento, a amostra mínima não foi alterada após a coleta; a impossibilidade de executar T4 torna M10 e H10 formalmente inconclusivas.
- **Resposta a Q10:** inconclusiva para o escopo completo planejado. Embora todos os participantes tenham concluído a emissão da 2ª via (T3) sem erro e sem ajuda, a ausência de gráfico interativo no Histórico de Consumo impediu a avaliação da segunda tarefa prevista (T4).
 
## 5. Oportunidades de melhoria

As hipóteses H1 e H9 foram sustentadas (enquanto H10 permaneceu inconclusiva), mas as análises acima mostram pontos em que o usuário hesitou, demorou ou errou mesmo com a métrica dentro da meta. Esta seção reúne essas observações como **pré-sugestões de melhoria**.


| ID | Pré-sugestão | Evidência | Métrica de origem | Prioridade |
|---|---|---|---|---|
| **OM-01** | Reformular a funcionalidade **Indicadores de Continuidade**: deixar clara a finalidade da tela, usar linguagem do dia a dia em vez das siglas e mostrar os dados sem exigir que o usuário abra mês a mês | Tela B reconhecida por 3 de 5 participantes (60%); os 2 erros escolheram "histórico de consumo"; 2 dos 3 acertos vieram com pedido de repetição | M9 | **Alta** |
| **OM-02** | Dar rótulo de texto ao ícone de impressora da 2ª via (ex.: "Baixar PDF") | P02 levou 190 s na T3 até perceber que o ícone gerava o PDF | M10 | Média |
| **OM-03** | Tornar a tela inicial mais clara, com acesso às funções por rótulos visíveis em vez do botão verde sem texto | P03 e P04 relataram que a tela inicial "não é nada intuitiva" | M1 (perguntas abertas) | Média |
| **OM-04** | Dar ao Histórico de consumo um título e um gráfico que confirmem ao usuário que ele chegou ao lugar certo | Impediu a tarefa T4 prevista para a M10|  M10 | Baixa | 

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Análise de M1, M9 e M10 a partir das fichas P01 a P05 | Beatriz |
| 1.1 | 22/11/2026 | Análise da M2 | Isabella |
| 1.2 | 22/11/2026 | Inclusão da seção de oportunidades de melhoria (pré-sugestões OM-01 a OM-04) e ligação com a página Ação de melhoria; correção de frase incompleta na análise de M10 | Beatriz |
| 1.3 | 23/11/2026 | Formalização de M10/H10 como inconclusiva devido à exclusão da T4 (ausência de gráfico interativo na interface) | Dara Maria Barbosa de Sousa |