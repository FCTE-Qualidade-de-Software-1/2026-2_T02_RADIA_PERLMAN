---
hide:
  - toc
---

# Critérios de julgamento

As medidas serão interpretadas em três etapas: classificação de cada métrica, resposta à hipótese correspondente e julgamento do objetivo GQM. As faixas estão em [Métricas e níveis de pontuação](metricas.md); a relação entre objetivos, questões e métricas aparece no [gráfico GQM](grafico-gqm.md).

## Níveis adotados

| Nível | Significado |
|---|---|
| Insatisfatório | A medição não atendeu ao limite mínimo definido. |
| Mínimo aceitável | O resultado indica funcionamento parcial ou desempenho limitado, com possibilidade de melhoria. |
| Alvo | O resultado atingiu o patamar estabelecido para a avaliação. |
| Excelente | O resultado superou o patamar esperado para aquela métrica. |
| Inconclusivo | As informações disponíveis não permitem uma classificação válida. |

Para M1–M4, M6, M7 e M8, aplicam-se os quatro níveis graduais da tabela de métricas. A M6 tem escala própria: seu nível **Alvo** começa em 95%, coincidindo com o limite de H6. A M5, relativa à confidencialidade, tem apenas dois resultados possíveis após amostra suficiente: **Excelente**, quando todas as verificações impedem o acesso a dados protegidos sem sessão, ou **Insatisfatório**, quando ocorre ao menos uma falha de bloqueio. Os níveis intermediários não são usados para essa métrica. Se não houver dados suficientes, M5 será inconclusiva.

Os níveis acima são distintos das notas de ênfase atribuídas na Fase 1. As ênfases 5 e 4 representam prioridades do estudo, não pontuações obtidas pelo produto.

## Cálculo e interpretação das medidas

**M1, M2, M4 e M6.** Registrar numerador, denominador, percentual e justificativa para cada exclusão. O resultado é classificado pelas faixas correspondentes. Uma hipótese é sustentada quando o limite previsto para ela é atingido e a quantidade mínima de casos elegíveis foi observada.

**M3 — maturidade.** Calcular a taxa de execuções sem falha para cada fluxo: `100 × execuções sem falha / execuções elegíveis do próprio fluxo`. Os fluxos devem ter pelo menos dez execuções cada, distribuídas em dois períodos. H3 é sustentada somente se todos os fluxos elegíveis previamente incluídos atingirem pelo menos 80%. Para o julgamento de G2, será utilizada a pior faixa entre os resultados desses fluxos. Não será calculada média geral que compense a falha de uma funcionalidade com o bom desempenho de outra. Se um fluxo previsto não atingir o mínimo, a conclusão de M3 e de H3 ficará inconclusiva, com divulgação dos demais resultados válidos.

**M5 — confidencialidade.** O percentual de bloqueios corretos será informado com seu numerador e denominador, mas o julgamento é binário: `M5 = 100%` sustenta H5 e recebe **Excelente**; `M5 < 100%` não sustenta H5 e recebe **Insatisfatório**. O critério considera o acesso efetivo a dados protegidos sem sessão ativa. Uma tela antiga exibida pelo histórico local do navegador deve ser diferenciada de conteúdo protegido que ainda possa ser consultado no sistema. Qualquer exposição efetiva terá registro de ocorrência crítica, sem divulgação de informações pessoais.

**M7 e M8 — tempo de resposta.** Calcular mediana e percentil 90 individualmente para cada fluxo, utilizando pelo menos dez medições concluídas e comparáveis. Os timeouts serão apresentados à parte. A pior classificação entre os fluxos válidos será utilizada para cada métrica; depois, a pior entre M7 e M8 determinará o resultado de G4.

**M6 — limite de interpretação.** A repetição de consultas permite observar inconsistências entre dados apresentados na interface, mas não confirma a proteção de dados internos contra modificações não autorizadas. As conclusões sobre integridade serão restritas a essa evidência.

## Resultado dos objetivos GQM

G1 reúne M1 e M2; G2, M3 e M4; G3, M5 e M6; G4, M7 e M8. O nível de cada objetivo será o menor entre suas duas métricas, segundo a ordem:

`Insatisfatório < Mínimo aceitável < Alvo < Excelente`

Se uma métrica for inconclusiva, o objetivo correspondente também será inconclusivo, mesmo quando a outra apresentar resultado favorável. Essa regra não impede relatar os resultados parciais. No caso de G3, uma ocorrência crítica em M5 determina julgamento **Insatisfatório**, ainda que M6 seja inconclusiva.

## Síntese da avaliação

Não será feita uma média única dos quatro objetivos. A síntese apresentará G1–G4 separadamente, destacando problemas observados em características de ênfase 5 e os limites de cada coleta.

| Condição encontrada | Síntese |
|---|---|
| Todos os objetivos conclusivos em Alvo ou Excelente, sem ocorrência crítica | Atendimento satisfatório no escopo observado. |
| Todos conclusivos, nenhum Insatisfatório e ao menos um em Mínimo aceitável | Atendimento parcial, com oportunidades de melhoria. |
| Ao menos um objetivo Insatisfatório ou ocorrência crítica | Melhorias prioritárias necessárias; informar também qualquer resultado inconclusivo. |
| Nenhum objetivo Insatisfatório, mas um ou mais inconclusivos | Avaliação global inconclusiva; apresentar os resultados parciais e as lacunas. |

Como exemplo de aplicação da regra, uma taxa de 90% na M1 seria classificada como **Alvo**, e uma taxa de 100% na M2 seria **Excelente**. Nesse cenário, G1 receberia **Alvo**, pela menor classificação. O exemplo ilustra apenas o procedimento de consolidação.

Na Fase 4, cada conclusão será acompanhada dos registros de origem: funcionalidade, identificadores de execução, valores brutos, cálculo, faixa atribuída, resultado da hipótese e evidências correspondentes. Os critérios de registro constam no [Protocolo de coleta](protocolo-coleta.md).
