---
hide:
- toc
---

# Plano de Medição PSM/CID

Para acompanhar o desempenho do processo de trabalho da equipe, adotamos três indicadores baseados na abordagem **PSM/CID** (*Practical Software and Systems Measurement*).

## Tabela de Indicadores

| Categoria | Indicador | Cálculo | Fonte de dados | Uso dos resultados |
|---|---|---|---|---|
| Desempenho dos Processos | **PSM-1 — Retrabalho** | `100 × Issues atualmente fechadas que já foram reabertas / Issues atualmente fechadas` | Histórico de eventos das Issues. | Identificar atividades concluídas que precisaram ser reabertas. |
| Calendário e Progresso | **PSM-2 — Progresso do marco** | `100 × Issues concluídas / total de Issues do Milestone` | Estados das Issues e Milestones. | Acompanhar o percentual de conclusão das entregas. |
| Recursos e Custos | **PSM-3 — Razão de esforço** | `Horas reais registradas / horas estimadas` | Campos de estimativa e horas reais no corpo das Issues. | Comparar o esforço realizado com o esforço planejado. |

## Detalhamento e Critérios de Interpretação

### PSM-1 — Retrabalho
* **Definição operacional:** Contabiliza as Issues *atualmente fechadas* que possuem pelo menos um evento de reabertura (`reopened`) em seu histórico. Cada Issue é contada apenas uma vez, independentemente de quantas vezes foi reaberta.
* **Observação:** Issues que foram reabertas e ainda permanecem abertas não entram no cálculo atual. O resultado representa uma fotografia acumulada das entregas finalizadas, diferindo de medições baseadas em janelas de tempo fixas.

### PSM-2 — Progresso do marco
* **Definição operacional:** Mede a proporção de Issues fechadas em relação ao total de Issues vinculadas ao Milestone (`Entrega 1` ou `Entrega 2`).
* **Observação:** Como a criação ou remoção de Issues ao longo do semestre altera o denominador, mudanças de escopo devem ser consideradas ao analisar a evolução percentual.

### PSM-3 — Razão de esforço
* **Definição operacional:** Compara o somatório das horas reais registradas com o somatório das horas estimadas nas Issues do conjunto analisado.
* **Faixas de interpretação:**
  * **Menor que 1:** O esforço registrado até o momento é inferior ao estimado.
  * **Igual a 1:** O esforço registrado corresponde exatamente ao estimado.
  * **Maior que 1:** O esforço registrado ultrapassou o planejamento inicial.
* **Observação:** O resultado deve ser lido em conjunto com o **PSM-2**, pois entregas em andamento naturalmente apresentam esforço parcial. Caso alguma Issue do conjunto não possua estimativa válida preenchida, o indicador é exibido como não calculável (`N/A`).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 17/10/2026 | Definição inicial dos indicadores PSM/CID | Arthur de Lima Sobreira |
| 1.2 | 26/10/2026 | Atualização das fórmulas e considerações | [Isabella Choukaira](https://github.com/isabellachoukaira) |
| 1.4 | 14/11/2026 | Substituição do PSM-3 para Razão de Esforço | [Isabella Choukaira](https://github.com/isabellachoukaira) |
| 2.0 | 22/11/2026 | Extração do plano de medição para página dedicada | [Isabella Choukaira](https://github.com/isabellachoukaira) |