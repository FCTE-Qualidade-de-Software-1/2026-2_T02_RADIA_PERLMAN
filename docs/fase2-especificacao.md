---
hide:
  - toc
---

# Fase 2 — Especificação da avaliação

Na [Fase 1](fase1-requisitos.md), a equipe definiu o escopo da avaliação da Agência Virtual da Neoenergia Brasília: login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Foram selecionadas quatro características de qualidade com base na ISO/IEC 25010:2011. A Fase 2 estabelece as medidas que serão aplicadas a esse escopo e as regras para interpretar os resultados.

## Duas frentes de medição

O trabalho reúne duas atividades com finalidades distintas. A **avaliação da qualidade do produto** segue o método *Goal–Question–Metric* (GQM); o **acompanhamento do projeto** utiliza indicadores de *Practical Software and Systems Measurement* (PSM/CID). A primeira examina o comportamento da Agência Virtual. A segunda registra o andamento das atividades da equipe, seus prazos e o esforço empregado. As informações de gestão não compõem a pontuação de qualidade do produto.

| Abordagem | Objeto de medição | Indicadores | Utilização |
|---|---|---|---|
| GQM | Agência Virtual da Neoenergia Brasília | M1–M8 | Responder às questões de qualidade e orientar recomendações de melhoria. |
| PSM/CID | Execução do projeto acadêmico | PSM-1 a PSM-3 | Acompanhar retrabalho, progresso e esforço; registrar as decisões de gestão. |

As duas frentes têm registros próprios. As métricas de qualidade serão aplicadas na execução da avaliação, enquanto os indicadores PSM/CID devem ser acompanhados ao longo do trabalho, a partir dos registros do repositório. Os procedimentos de gestão estão em [Acompanhamento do projeto](fase2/gestao-psm.md).

## Estrutura GQM

O GQM organiza a medição em três níveis. Primeiro são definidos os objetivos, vinculados às características de qualidade da Fase 1. Em seguida, cada objetivo é detalhado em questões e hipóteses. Por fim, são escolhidas métricas que permitem responder às questões a partir de dados observáveis.

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

As notas de ênfase representam a importância atribuída às características na Fase 1; não são resultados das medições. Os testes foram delimitados à navegação e às consultas realizadas com acesso legítimo. Não estão previstos ensaios de carga, alterações de registros de consumidores ou inspeção dos sistemas internos da concessionária. Para maturidade (M3), os resultados serão calculados separadamente por fluxo; para confidencialidade (M5), qualquer acesso efetivo a informação protegida sem autenticação configura resultado insatisfatório. Essas regras estão nas fichas de [métricas](fase2/metricas.md) e nos [critérios de julgamento](fase2/criterios-julgamento.md).

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

As páginas seguem uma mesma cadeia: a questão Q3, por exemplo, está vinculada à maturidade (G2), é respondida pela taxa de execuções sem falhas (M3) e depende de registros separados para cada fluxo de navegação. O protocolo descreve a coleta, e os critérios de julgamento indicam como classificar seus resultados. O mesmo encadeamento se aplica às demais questões.

Na Fase 3, as definições desta especificação serão organizadas em um plano com responsáveis, ambiente, recursos e cronograma. Na Fase 4, as medidas coletadas serão comparadas às faixas definidas, sem alterar os critérios depois de conhecidos os resultados.

---

**Referência:** SILVA, C. V. P. da; MOURA, D. C. de; CAMPOS, D. de C.; NERY, P. *GQM – Goal-Question-Metric*. 2009.
