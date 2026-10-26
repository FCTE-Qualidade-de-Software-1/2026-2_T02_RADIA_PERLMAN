---
hide:
  - toc
---

# Acompanhamento do projeto com PSM/CID

Além das medidas de qualidade da Agência Virtual da Neoenergia Brasília, acompanhamos o desenvolvimento do projeto por meio de indicadores baseados no PSM/CID.

Diferentemente das métricas M1–M8, definidas por meio do [GQM](../fase2-especificacao.md) para avaliar a qualidade do produto, os indicadores PSM/CID são utilizados para acompanhar a gestão das atividades, o progresso das entregas e a distribuição de responsabilidades da equipe.

Para facilitar esse acompanhamento, implementamos uma coleta automatizada de dados utilizando GitHub Actions e um script Python.

## Indicadores de gestão

| Categoria | Indicador | Cálculo | Fonte de dados | Uso dos resultados |
|---|---|---|---|---|
| Desempenho dos Processos | **PSM-1 — Retrabalho** | `100 × issues atualmente fechadas que já foram reabertas / issues atualmente fechadas` | Histórico de eventos das Issues do Milestone. | Identificar tarefas que precisaram retornar ao trabalho após terem sido consideradas concluídas. |
| Calendário e Progresso | **PSM-2 — Progresso do marco** | `100 × issues concluídas / total de issues vinculadas ao marco` | Issues e Milestone do GitHub. | Acompanhar o percentual de conclusão das atividades previstas para a entrega. |
| Recursos e Custos | **PSM-3 — Cobertura de atribuição de tarefas** | `100 × issues com pelo menos um responsável / total de issues vinculadas ao marco` | Campo *Assignees* das Issues. | Identificar atividades sem responsáveis definidos e apoiar a distribuição das tarefas. |

### Considerações sobre os indicadores

**PSM-1 — Retrabalho:** a implementação inicial considera as Issues atualmente fechadas que possuem pelo menos um evento de reabertura em seu histórico. Cada Issue é contabilizada uma única vez, mesmo que tenha sido reaberta várias vezes. Issues reabertas que permanecem abertas não entram no cálculo atual.

Essa implementação representa uma fotografia acumulada das Issues atualmente concluídas e difere da definição inicialmente proposta, que considerava fechamentos e reaberturas em um período específico.

**PSM-2 — Progresso do marco:** considera como conjunto planejado as Issues atualmente vinculadas ao Milestone. Como a inclusão ou exclusão de Issues altera o denominador, mudanças no escopo devem ser registradas e consideradas na interpretação dos resultados. Para avaliações futuras, pretende-se estabelecer uma linha de base fixa.

**PSM-3 — Cobertura de atribuição:** substitui a razão de esforço inicialmente prevista, devido às dificuldades de manter registros consistentes de horas estimadas e realizadas. O indicador utiliza informações disponíveis no GitHub e permite identificar tarefas sem responsáveis definidos.

A cobertura de atribuição é uma medida adaptada ao contexto da equipe. Ela não representa o esforço efetivamente realizado, o equilíbrio da carga de trabalho nem os custos financeiros do projeto.

Quando um denominador for zero, o indicador será apresentado como não calculável, acompanhado de uma justificativa.

## Automatização da coleta de métricas

Para reduzir a necessidade de contagem manual das atividades, desenvolvemos uma automação utilizando **GitHub Actions**, **Python** e a **API do GitHub**.

A automação consulta as Issues vinculadas ao Milestone definido, analisa seus estados, responsáveis e eventos históricos, calcula os indicadores e gera relatórios com os resultados.

### Estrutura da implementação

Os arquivos responsáveis pela automação estão organizados da seguinte forma:

```text
.github/
└── workflows/
    └── metricas-psm.yml

scripts/
└── coletar_metricas_psm.py
```

O arquivo `metricas-psm.yml` define a execução do workflow no GitHub Actions.

O arquivo `coletar_metricas_psm.py` realiza a consulta aos dados do repositório, calcula os indicadores e gera os relatórios.

### Funcionamento

1. O GitHub Actions inicia a execução do workflow.
2. O script consulta as Issues associadas ao Milestone da entrega.
3. São coletadas informações sobre estado das Issues, responsáveis e eventos de reabertura.
4. Os indicadores PSM-1, PSM-2 e PSM-3 são calculados automaticamente.
5. Os resultados são disponibilizados nos logs e em arquivos gerados pela execução.

A automação permite execução manual e agendada, conforme a configuração do workflow.

### Arquivos gerados

Ao final da execução, são disponibilizados dois arquivos:

- **`relatorio.md`:** apresenta os indicadores calculados, os dados utilizados e as limitações da medição.
- **`metricas.json`:** armazena os resultados em formato estruturado, permitindo seu processamento posterior.

Os arquivos são disponibilizados como artefatos do GitHub Actions.

A automatização contempla a coleta e o cálculo dos indicadores. A interpretação dos resultados e a definição de ações de gestão continuam sob responsabilidade da equipe.

## Primeira apuração automatizada

A primeira coleta automatizada foi realizada em **26/10/2026, às 19h17 UTC (16h17, horário de Brasília)**.

**Repositório:** `FCTE-Qualidade-de-Software-1/2026-2_T02_RADIA_PERLMAN`

**Milestone:** `Entrega 1 — Fases 1 e 2`

### Resultados obtidos

| Indicador | Numerador | Denominador | Resultado |
|---|---:|---:|---:|
| PSM-1 — Retrabalho | 0 | 6 | **0,00%** |
| PSM-2 — Progresso do marco | 6 | 11 | **54,55%** |
| PSM-3 — Cobertura de atribuição | 9 | 11 | **81,82%** |

### Análise dos resultados

**PSM-1 — Retrabalho (0,00%)**

Entre as seis Issues que estavam fechadas no momento da coleta, nenhuma apresentava evento anterior de reabertura.

Entretanto, o relatório identificou que a **Issue #5** já havia sido reaberta e permanecia aberta. Por esse motivo, ela não foi contabilizada no indicador.

Assim, o resultado de 0,00% não significa ausência total de retrabalho no projeto. Ele representa apenas a proporção de Issues atualmente fechadas que possuem histórico de reabertura, conforme a implementação inicial.

Essa limitação indica a necessidade de revisar a definição operacional do indicador para que reaberturas ainda não resolvidas também possam ser consideradas.

**PSM-2 — Progresso do marco (54,55%)**

Das 11 Issues vinculadas ao Milestone, seis estavam concluídas no momento da coleta.

O resultado indica que pouco mais da metade das atividades registradas havia sido concluída. As cinco Issues restantes ainda estavam abertas.

Considerando a proximidade do prazo da Entrega 1, esse resultado indica a necessidade de acompanhar as pendências e verificar quais atividades devem ser priorizadas.

**PSM-3 — Cobertura de atribuição (81,82%)**

Das 11 Issues do Milestone, nove possuíam pelo menos um responsável definido.

O resultado indica que duas Issues estavam sem responsáveis atribuídos no momento da coleta.

Essa informação pode ser utilizada para revisar a distribuição das responsabilidades e garantir que as atividades pendentes tenham responsáveis identificados.

### Ações de acompanhamento propostas

| Indicador | Ação proposta | Responsável | Prazo |
|---|---|---|---|
| PSM-1 | Revisar a definição do indicador para considerar também reaberturas ainda não resolvidas. | A definir pela equipe | A definir |
| PSM-2 | Verificar as cinco Issues abertas e priorizar as atividades necessárias para concluir a entrega. | A definir pela equipe | A definir |
| PSM-3 | Identificar as duas Issues sem responsáveis e definir sua atribuição. | A definir pela equipe | A definir |

As ações apresentadas são propostas decorrentes da análise dos resultados. Sua execução deverá ser registrada posteriormente, com responsáveis, prazos e evidências correspondentes.

## Registro e análise periódica

As atividades do projeto são organizadas por meio de Issues, com responsáveis, status e vínculos com as entregas.

Os indicadores serão acompanhados por meio das execuções do GitHub Actions, permitindo registrar diferentes momentos do desenvolvimento.

A cada apuração, serão considerados:

- Data e horário da coleta.
- Milestone e conjunto de Issues analisados.
- Valores dos indicadores.
- Limitações e alterações no escopo da medição.
- Interpretação dos resultados.
- Ações propostas e decisões tomadas pela equipe.
- Evidências disponíveis no repositório.

| Data/período | Indicador | Dados da apuração | Valor | Interpretação | Evidência |
|---|---|---|---|---|---|
| 26/10/2026 | PSM-1 | 0 Issues atualmente fechadas com reabertura / 6 fechadas | 0,00% | A Issue #5 foi reaberta, mas permanece aberta e não integra o cálculo atual. | Relatório do GitHub Actions |
| 26/10/2026 | PSM-2 | 6 concluídas / 11 vinculadas ao Milestone | 54,55% | Cinco atividades permaneciam abertas. | Milestone e relatório automatizado |
| 26/10/2026 | PSM-3 | 9 com responsáveis / 11 vinculadas ao Milestone | 81,82% | Duas atividades estavam sem responsáveis definidos. | Issues e relatório automatizado |

Os resultados apresentados representam a situação do repositório no momento da coleta, não necessariamente a situação atual do projeto.

## Limitações e melhorias previstas

A implementação inicial automatiza a coleta e o cálculo das três métricas, mas ainda apresenta algumas limitações.

**Retrabalho:** o cálculo considera apenas Issues atualmente fechadas. Pretende-se aprimorar o indicador para considerar também as Issues reabertas que permanecem abertas, mantendo uma definição consistente de numerador e denominador.

**Progresso:** o conjunto de Issues vinculadas ao Milestone pode sofrer alterações. Uma melhoria prevista é estabelecer uma linha de base fixa, permitindo comparar a execução com o planejamento original.

**Cobertura de atribuição:** o indicador verifica a existência de responsáveis, mas não mede a carga de trabalho de cada integrante nem o esforço dedicado às atividades.

**Análise dos resultados:** a automação gera os dados quantitativos, mas a interpretação e as decisões de gestão ainda são registradas manualmente pela equipe.

Essas limitações serão consideradas na evolução da automação e na interpretação das próximas medições.

## Relação com a avaliação do software

Os indicadores PSM/CID acompanham a gestão do projeto e não alteram diretamente as notas de qualidade atribuídas ao software.

Por esse motivo, não integram o [gráfico GQM](grafico-gqm.md), que representa os objetivos, questões e métricas da avaliação do produto.

Os resultados PSM/CID permitem acompanhar a execução do trabalho, identificar necessidades de ajuste e apoiar decisões relacionadas à organização da equipe.

Para a avaliação da Agência Virtual da Neoenergia Brasília, será utilizado o [protocolo de coleta](protocolo-coleta.md) definido na Fase 2.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 17/10/2026 | Criação do documento do PSM | Arthur de Lima Sobreira |
| 1.1 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |
| 1.2 | 26/10/2026 | Atualização dos indicadores, documentação da automação e registro da primeira apuração | A definir |