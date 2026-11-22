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

[preencher]
 
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
 
**Cálculo:** `M10 = 100 × 5 / 5 = 100%`.
 
**Classificação:** **Excelente** (95% ou mais).
 
**Resultado da hipótese:** **H10 sustentada** (M10 ≥ 80%, com a amostra mínima ajustada).
 
**Análise:**
 
- **Conclusão da tarefa.** Todos emitiram a 2ª via, sem ajuda e dentro do limite de 5 minutos. A mediana foi de 19 s.
- **Ícone de impressão.** P02 usou 190 s, quase dois terços do limite. Chegou à tela correta, mas demorou a perceber que o ícone de impressora, que não tem rótulo.
- **Resposta a Q10:** sim, para a emissão da 2ª via. Todos os participantes concluíram T3 sem erro e sem ajuda, ainda que um deles tenha demorado a identificar o comando de impressão.
 
 
## 5. Oportunidades de melhoria

As hipóteses H1, H9 e H10 foram sustentadas, mas as análises acima mostram pontos em que o usuário hesitou, demorou ou errou mesmo com a métrica dentro da meta. Esta seção reúne essas observações como **pré-sugestões de melhoria**.


| ID | Pré-sugestão | Evidência | Métrica de origem | Prioridade |
|---|---|---|---|---|
| **OM-01** | Reformular a funcionalidade **Indicadores de Continuidade**: deixar clara a finalidade da tela, usar linguagem do dia a dia em vez das siglas e mostrar os dados sem exigir que o usuário abra mês a mês | Tela B reconhecida por 3 de 5 participantes (60%); os 2 erros escolheram "histórico de consumo"; 2 dos 3 acertos vieram com pedido de repetição | M9 | **Alta** |
| **OM-02** | Dar rótulo de texto ao ícone de impressora da 2ª via (ex.: "Baixar PDF") | P02 levou 190 s na T3 até perceber que o ícone gerava o PDF | M10 | Média |
| **OM-03** | Tornar a tela inicial mais clara, com acesso às funções por rótulos visíveis em vez do botão verde sem texto | P03 e P04 relataram que a tela inicial "não é nada intuitiva" | M1 (perguntas abertas) | Média |
| **OM-04** | Dar ao Histórico de consumo um título e um gráfico que confirmem ao usuário que ele chegou ao lugar certo | P04 concluiu a T2 sem saber se tinha acertado; a tela tem só uma tabela estática, o que também impediu a tarefa T4 | M1 / M10 | Baixa | 

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Análise de M1, M9 e M10 a partir das fichas P01 a P05 | Beatriz |
| 1.1 | 22/11/2026 | Inclusão da seção de oportunidades de melhoria (pré-sugestões OM-01 a OM-04) e ligação com a página Ação de melhoria; correção de frase incompleta na análise de M10 | Beatriz |
