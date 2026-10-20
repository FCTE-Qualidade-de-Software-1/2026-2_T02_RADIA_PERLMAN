---
hide:
  - toc
---

# Acompanhamento do projeto com PSM/CID

Além das medidas de qualidade da Agência Virtual, vamos acompanhar o andamento do projeto por meio de indicadores PSM/CID. Diferentemente das métricas M1–M8, que seguem o [GQM](../fase2-especificacao.md) e avaliam o produto, esses indicadores tratam do nosso planejamento: retrabalho, progresso e esforço dedicado às atividades.

## Indicadores de gestão

| Categoria | Indicador | Cálculo | Fonte de dados | Uso dos resultados |
|---|---|---|---|---|
| Desempenho dos Processos | **PSM-1 — Retrabalho** | `100 × issues fechadas no período que foram reabertas até a data de apuração / issues fechadas no mesmo período` | Histórico de issues e revisões do repositório. | Identificar tarefas que voltam para revisão e verificar se os critérios de conclusão precisam melhorar. |
| Calendário e Progresso | **PSM-2 — Progresso do marco** | `100 × tarefas concluídas do marco / tarefas previstas na linha de base do marco` | Issues vinculadas a milestones. | Verificar a distância entre execução e planejamento, considerando o prazo da entrega. |
| Recursos e Custos | **PSM-3 — Razão de esforço** | `soma das horas registradas / soma das horas previstas para as mesmas tarefas` | Estimativas e apontamentos de tempo nas issues ou registros de equipe. | Identificar diferenças de esforço e ajustar a distribuição de atividades. |

Em PSM-1, uma issue é contada uma única vez, mesmo que tenha sido reaberta mais de uma vez. O período de referência e a data da apuração precisam constar do registro. Em PSM-2, a lista de tarefas do marco será fixada como linha de base; inclusões e exclusões posteriores serão descritas, em vez de alterar silenciosamente o denominador. PSM-3 mede esforço em horas, e não custo financeiro. Quando um denominador for zero, o indicador ficará sem cálculo, acompanhado da justificativa.

## Registro e análise periódica

Vamos organizar as atividades em issues com responsável, prazo, estimativa de esforço e critério de conclusão. Em cada marco de entrega, vincularemos as tarefas aos commits, revisões e documentos correspondentes. Esses registros servirão de base para calcular os indicadores.

A cada apuração, registraremos a data, os valores dos indicadores e nossa interpretação dos desvios. Quando houver necessidade de ajuste, indicaremos a ação escolhida, o responsável e o prazo. Também documentaremos mudanças de escopo e de calendário.

| Data/período | Indicador | Dados da apuração | Valor | Interpretação | Decisão, responsável e prazo | Evidência no Git |
|---|---|---|---|---|---|---|
| A preencher | PSM-1 | Issues fechadas / reabertas | A calcular | A registrar | A registrar | Issue, ata ou link |
| A preencher | PSM-2 | Tarefas planejadas / concluídas | A calcular | A registrar | A registrar | Milestone ou issue |
| A preencher | PSM-3 | Horas previstas / registradas | A calcular | A registrar | A registrar | Registro de esforço |

A primeira apuração contemplará a preparação da Entrega 1, desde que existam registros suficientes para os cálculos. Preencheremos os valores com base nas issues, nos marcos e nas horas efetivamente apontadas.

## Relação com a avaliação do software

O PSM/CID não altera as notas de qualidade do software e, por isso, não entra no [gráfico GQM](grafico-gqm.md). Seus registros permitirão avaliar como conduzimos o trabalho e quais ajustes foram necessários ao longo das entregas. Para os testes da Agência Virtual, seguiremos o [protocolo de coleta](protocolo-coleta.md).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 17/10/2026 | Criação do documento do PSM | Arthur de Lima Sobreira |
| 1.1 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |
