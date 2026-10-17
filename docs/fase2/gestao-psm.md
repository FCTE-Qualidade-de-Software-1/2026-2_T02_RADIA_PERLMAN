---
hide:
  - toc
---

# Acompanhamento do projeto com PSM/CID

O acompanhamento do trabalho utiliza indicadores de gestão baseados em PSM/CID, separados das métricas M1–M8 da Agência Virtual. Enquanto o [GQM](../fase2-especificacao.md) organiza a avaliação da qualidade do produto, os indicadores desta página acompanham as atividades necessárias à sua realização. O propósito é identificar desvios no planejamento e registrar as decisões tomadas a partir deles.

## Indicadores de gestão

| Categoria | Indicador | Cálculo | Fonte de dados | Uso dos resultados |
|---|---|---|---|---|
| Desempenho dos Processos | **PSM-1 — Retrabalho** | `100 × issues fechadas no período que foram reabertas até a data de apuração / issues fechadas no mesmo período` | Histórico de issues e revisões do repositório. | Identificar tarefas que voltam para revisão e verificar se os critérios de conclusão precisam melhorar. |
| Calendário e Progresso | **PSM-2 — Progresso do marco** | `100 × tarefas concluídas do marco / tarefas previstas na linha de base do marco` | Issues vinculadas a milestones. | Verificar a distância entre execução e planejamento, considerando o prazo da entrega. |
| Recursos e Custos | **PSM-3 — Razão de esforço** | `soma das horas registradas / soma das horas previstas para as mesmas tarefas` | Estimativas e apontamentos de tempo nas issues ou registros de equipe. | Identificar diferenças de esforço e ajustar a distribuição de atividades. |

Em PSM-1, uma issue é contada uma única vez, mesmo que tenha sido reaberta mais de uma vez. O período de referência e a data da apuração precisam constar do registro. Em PSM-2, a lista de tarefas do marco será fixada como linha de base; inclusões e exclusões posteriores serão descritas, em vez de alterar silenciosamente o denominador. PSM-3 mede esforço em horas, e não custo financeiro. Quando um denominador for zero, o indicador ficará sem cálculo, acompanhado da justificativa.

## Registro e análise periódica

As tarefas do projeto serão organizadas em issues com responsável, prazo, estimativa de esforço e critério de conclusão. Cada marco de entrega terá as atividades planejadas e os vínculos para commits, revisões e documentos concluídos. Esses registros serão utilizados na apuração dos três indicadores.

Em cada apuração, a equipe registrará a data, os valores obtidos, uma interpretação dos desvios e a ação decidida. A decisão deverá indicar responsável e prazo para acompanhamento. Alterações de escopo e mudanças no calendário também serão documentadas.

| Data/período | Indicador | Dados da apuração | Valor | Interpretação | Decisão, responsável e prazo | Evidência no Git |
|---|---|---|---|---|---|---|
| A preencher | PSM-1 | Issues fechadas / reabertas | A calcular | A registrar | A registrar | Issue, ata ou link |
| A preencher | PSM-2 | Tarefas planejadas / concluídas | A calcular | A registrar | A registrar | Milestone ou issue |
| A preencher | PSM-3 | Horas previstas / registradas | A calcular | A registrar | A registrar | Registro de esforço |

A primeira apuração deve abranger, sempre que houver registros suficientes, a preparação da Entrega 1. Os valores serão preenchidos a partir das issues, milestones e horas registradas pela equipe.

## Relação com a avaliação do software

Os indicadores PSM/CID não alteram os resultados das métricas do produto e não entram no [gráfico GQM](grafico-gqm.md). Eles ajudam a explicar como o trabalho foi conduzido e se mudanças de prazo ou esforço afetaram a preparação da avaliação. A coleta dos dados da Agência Virtual segue o [Protocolo de coleta](protocolo-coleta.md), que tem finalidade diferente dos registros de gestão.
