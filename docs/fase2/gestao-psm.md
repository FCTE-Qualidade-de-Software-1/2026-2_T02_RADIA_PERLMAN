---
hide:
  - toc
---

# Acompanhamento do projeto com PSM/CID

Além das medidas de qualidade da Agência Virtual da Neoenergia Brasília, acompanhamos o desenvolvimento do projeto por meio de indicadores baseados no PSM/CID.

Diferentemente das métricas M1–M14, definidas por meio do [GQM](../fase2-especificacao.md) para avaliar a qualidade do produto, os indicadores PSM/CID são utilizados para acompanhar a gestão das atividades, o progresso das entregas e a distribuição de responsabilidades da equipe.

Para facilitar esse acompanhamento, implementamos uma coleta automatizada utilizando GitHub Actions, Python e a API do GitHub. A automação consulta as Issues das Entregas 1 e 2, calcula os indicadores PSM/CID e gera relatórios e gráficos individuais e consolidados, permitindo acompanhar a evolução do projeto.

## Indicadores de gestão

| Categoria | Indicador | Cálculo | Fonte de dados | Uso dos resultados |
|---|---|---|---|---|
| Desempenho dos Processos | **PSM-1 — Retrabalho** | `100 × Issues atualmente fechadas que já foram reabertas / Issues atualmente fechadas` | Histórico de eventos das Issues. | Identificar atividades concluídas que precisaram ser reabertas. |
| Calendário e Progresso | **PSM-2 — Progresso do marco** | `100 × Issues concluídas / total de Issues do Milestone` | Estados das Issues e Milestones. | Acompanhar o percentual de conclusão das entregas. |
| Recursos e Custos | **PSM-3 — Razão de esforço** | `Horas reais registradas / horas estimadas` | Campos de estimativa e horas reais no corpo das Issues. | Comparar o esforço realizado com o esforço planejado. |

### Considerações sobre os indicadores

**PSM-1 — Retrabalho:** a implementação inicial considera as Issues atualmente fechadas que possuem pelo menos um evento de reabertura em seu histórico. Cada Issue é contabilizada uma única vez, mesmo que tenha sido reaberta várias vezes. Issues reabertas que permanecem abertas não entram no cálculo atual.

Essa implementação representa uma fotografia acumulada das Issues atualmente concluídas e difere da definição inicialmente proposta, que considerava fechamentos e reaberturas em um período específico.

**PSM-2 — Progresso do marco:** considera como conjunto planejado as Issues atualmente vinculadas ao Milestone. Como a inclusão ou exclusão de Issues altera o denominador, mudanças no escopo devem ser registradas e consideradas na interpretação dos resultados. Para avaliações futuras, pretende-se estabelecer uma linha de base fixa.

**PSM-3 — Razão de esforço:** compara o total de horas efetivamente registradas pela equipe com o total de horas estimadas para as atividades. As informações são extraídas automaticamente das seções `Estimativa (horas)` e `Horas reais` presentes no corpo das Issues.

O resultado é interpretado da seguinte forma:

- **Menor que 1:** o esforço registrado é inferior ao estimado.
- **Igual a 1:** o esforço registrado corresponde ao estimado.
- **Maior que 1:** o esforço registrado ultrapassa o estimado.

O indicador deve ser interpretado considerando o andamento das atividades, pois Issues ainda em execução podem apresentar esforço parcial. Quando alguma Issue não possui estimativa válida, a razão de esforço do conjunto é apresentada como não calculável (`N/A`).

Os registros de horas são informados manualmente pela equipe e interpretados como horas decimais. Por exemplo, `2,25 h` corresponde a 2 horas e 15 minutos.

## Automatização da coleta de métricas

Para reduzir a coleta manual de informações, desenvolvemos uma automação utilizando **GitHub Actions**, **Python** e a **API do GitHub**.

A automação consulta as Issues vinculadas aos Milestones `Entrega 1 — Fases 1 e 2` e `Entrega 2 — Fases 3 e 4`, identifica seus estados e eventos históricos e extrai as estimativas e os registros de horas presentes no corpo das Issues.

Com essas informações, calcula os indicadores PSM-1, PSM-2 e PSM-3, além de gerar relatórios e gráficos separados por entrega e um consolidado do projeto.

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

1. O GitHub Actions inicia a execução manual ou agendada do workflow.
2. O script consulta os Milestones das duas entregas por meio da API do GitHub.
3. São coletados os estados das Issues, os eventos de fechamento e reabertura, as estimativas e os registros de horas reais.
4. Os indicadores PSM-1, PSM-2 e PSM-3 são calculados para cada entrega.
5. São gerados gráficos de horas registradas por dia, Issues concluídas ao longo do tempo e esforço por integrante.
6. Os resultados das duas entregas são consolidados, evitando a duplicação de Issues.
7. Os relatórios e gráficos são disponibilizados como artefatos do GitHub Actions.

A automação permite acompanhar as entregas individualmente e visualizar os resultados gerais do projeto.rkflow.

### Arquivos gerados

A automação gera relatórios em Markdown, dados estruturados em JSON e gráficos em PNG.

Os resultados são organizados na pasta `relatorios/psm/`, com relatórios separados para cada entrega e um consolidado.

```text
relatorios/psm/
├── relatorio.md
├── metricas.json
├── entrega_1/
│   ├── relatorio.md
│   ├── metricas.json
│   └── gráficos PNG
├── entrega_2/
│   ├── relatorio.md
│   ├── metricas.json
│   └── gráficos PNG
└── consolidado/
    ├── relatorio.md
    ├── metricas.json
    └── gráficos PNG
```

São gerados três tipos de gráficos:

- **Horas ao longo do tempo:** apresenta o esforço registrado por dia.
- **Issues concluídas ao longo do tempo:** acompanha a evolução das atividades concluídas, considerando fechamentos e reaberturas.
- **Esforço por integrante:** apresenta a soma das horas registradas por cada integrante.

Os arquivos são disponibilizados como artefatos do GitHub Actions. A publicação automática desses resultados no GitHub Pages será realizada por meio da integração com o MkDocs.

## Primeira apuração automatizada

> **Registro histórico:** esta apuração corresponde à versão inicial da automação, na qual o PSM-3 era representado pela cobertura de atribuição de tarefas. Posteriormente, esse indicador foi substituído pela razão de esforço. Os resultados abaixo foram preservados para documentar a evolução do acompanhamento do projeto e não devem ser comparados diretamente com o PSM-3 atual.

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

## Resultados automatizados das entregas

A automação PSM/CID permite acompanhar os indicadores de gestão de cada entrega e do projeto como um todo.

Os relatórios apresentam os valores atualizados de retrabalho, progresso e razão de esforço, além de gráficos sobre as horas registradas, a conclusão de Issues e a distribuição do esforço entre os integrantes.

Os resultados serão disponibilizados em uma página específica da documentação, organizada em:

- **Entrega 1:** indicadores e gráficos referentes às Fases 1 e 2.
- **Entrega 2:** indicadores e gráficos referentes às Fases 3 e 4.
- **Consolidado:** visão geral das duas entregas.

A interpretação dos resultados, o registro de decisões e a definição de ações de melhoria permanecem sob responsabilidade da equipe.

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

**Razão de esforço:** depende do preenchimento correto das estimativas e dos registros de horas nas Issues. Quando alguma Issue não possui estimativa válida, o indicador consolidado é apresentado como `N/A`. Além disso, as horas registradas representam os apontamentos realizados pela equipe, podendo estar incompletas ou sofrer alterações posteriores.

**Interpretação do esforço:** a razão de esforço não deve ser utilizada isoladamente para avaliar produtividade. É necessário considerar o estágio de execução das atividades, a complexidade das tarefas e eventuais mudanças de escopo.

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
| 1.2 | 26/10/2026 | Atualização dos indicadores, documentação da automação e registro da primeira apuração | [Isabella Choukaira](https://github.com/isabellachoukaira) |
| 1.3 | 14/11/2026 | Alinhamento à Fase 1 | Beatriz Figueiredo dos Santos |
| 1.4 | 14/11/2026 | Atualização do PSM-3 para razão de esforço, coleta das duas entregas e documentação dos relatórios e gráficos automatizados | [Isabella Choukaira](https://github.com/isabellachoukaira) |
