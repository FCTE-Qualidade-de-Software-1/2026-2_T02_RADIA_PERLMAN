---
hide:
  - toc
---

# Fase 2 — Especificação da avaliação

Na [Fase 1](fase1-requisitos.md), delimitamos o estudo da Agência Virtual da Neoenergia Brasília a cinco serviços: login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Também selecionamos quatro características de qualidade com base na ISO/IEC 25010:2011. Nesta segunda fase, definimos como iremos medi-las e quais critérios serão utilizados para analisar os resultados.

## Duas frentes de medição

Organizamos as medições em duas frentes. Para avaliar a qualidade da Agência Virtual, utilizaremos o método *Goal–Question–Metric* (GQM). Para acompanhar a realização do trabalho, adotamos indicadores de *Practical Software and Systems Measurement* (PSM/CID), voltados ao progresso, aos prazos e ao esforço registrado. Essa distinção é importante porque os indicadores de gestão não fazem parte da pontuação de qualidade do software.

| Abordagem | Objeto de medição | Indicadores | Utilização |
|---|---|---|---|
| GQM | Agência Virtual da Neoenergia Brasília | M1–M8 | Responder às questões de qualidade e orientar recomendações de melhoria. |
| PSM/CID | Execução do projeto acadêmico | PSM-1 a PSM-3 | Acompanhar retrabalho, progresso e esforço; registrar as decisões de gestão. |

As métricas do produto serão calculadas durante a avaliação. Já os indicadores de gestão serão atualizados com base nas atividades registradas no repositório, inclusive durante a preparação das entregas. Detalhamos esse acompanhamento na página [PSM/CID](fase2/gestao-psm.md).

## Estrutura GQM

No GQM, partimos das características escolhidas na Fase 1 para formular os objetivos de medição. Cada objetivo dá origem a questões e hipóteses; as métricas indicam quais observações serão necessárias para respondê-las. Desse modo, conseguimos relacionar os resultados obtidos às decisões tomadas no início do projeto.

| Nível | Definição adotada |
|---|---|
| Conceitual — objetivo (G) | Característica a ser investigada, finalidade, ponto de vista e contexto. |
| Operacional — questão (Q) e hipótese (H) | Pergunta que orienta a análise e resultado esperado antes da coleta. |
| Quantitativo — métrica (M) | Dados, cálculo e critérios necessários para responder à questão. |

A especificação reúne quatro objetivos (G1–G4), oito questões (Q1–Q8), oito hipóteses (H1–H8) e oito métricas (M1–M8). O [gráfico GQM](fase2/grafico-gqm.md) apresenta todas as ligações.

## Características avaliadas

| Característica | Ênfase da Fase 1 | Subcaracterísticas | Objetivo GQM |
|---|:---:|---|---|
| Usabilidade | 5 | Apreensibilidade e proteção contra erros do usuário | [G1](fase2/objetivos.md#g1) |
| Confiabilidade | 4 | Maturidade e tolerância a falhas | [G2](fase2/objetivos.md#g2) |
| Segurança | 5 | Confidencialidade e integridade, conforme as evidências acessíveis externamente | [G3](fase2/objetivos.md#g3) |
| Eficiência de desempenho | 4 | Comportamento no tempo | [G4](fase2/objetivos.md#g4) |

As notas de ênfase expressam a prioridade de cada característica na Fase 1, e não uma pontuação do sistema. Vamos observar as funcionalidades por meio de navegação e consultas autorizadas, sem alterar registros de consumidores nem acessar os sistemas internos da concessionária. Duas decisões merecem destaque: na M3, avaliaremos cada fluxo separadamente; na M5, o acesso a dados protegidos sem autenticação será considerado insatisfatório. As respectivas regras estão nas [métricas](fase2/metricas.md) e nos [critérios de julgamento](fase2/criterios-julgamento.md).

## Documentação da Fase 2

| Página | Conteúdo |
|---|---|
| [Objetivos de medição](fase2/objetivos.md) | Objetivos G1–G4 e sua relação com a Fase 1. |
| [Questões e hipóteses](fase2/questoes-hipoteses.md) | Perguntas de avaliação e limites esperados para H1–H8. |
| [Métricas e níveis de pontuação](fase2/metricas.md) | Definições, fontes, fórmulas, coleta e escalas de M1–M8. |
| [Critérios de julgamento](fase2/criterios-julgamento.md) | Regras para interpretar métricas e consolidar resultados por objetivo. |
| [Gráfico GQM](fase2/grafico-gqm.md) | Relações G–Q–H–M em diagrama e tabela. |
| [Rastreabilidade](fase2/rastreabilidade.md) | Correspondência entre características, funcionalidades e medidas. |
| [Protocolo de coleta](fase2/protocolo-coleta.md) | Cenários, registros, elegibilidade e condições de medição. |
| [Acompanhamento do projeto — PSM/CID](fase2/gestao-psm.md) | Indicadores e registro de decisões de gestão. |

As páginas se complementam. Na análise de maturidade, por exemplo, partimos do objetivo G2, formulamos a questão Q3 e utilizamos a M3 para calcular a taxa de execuções sem falhas em cada fluxo. O [protocolo de coleta](fase2/protocolo-coleta.md) define os registros necessários, enquanto os [critérios de julgamento](fase2/criterios-julgamento.md) estabelecem como interpretar o resultado. As demais questões seguem a mesma lógica.

Na Fase 3, essas definições servirão de base ao plano de avaliação, incluindo responsáveis, ambiente e cronograma. Na Fase 4, aplicaremos os procedimentos e compararemos as medidas obtidas com os limites estabelecidos aqui.

---

**Referência:** SILVA, C. V. P. da; MOURA, D. C. de; CAMPOS, D. de C.; NERY, P. *GQM – Goal-Question-Metric*. 2009.
