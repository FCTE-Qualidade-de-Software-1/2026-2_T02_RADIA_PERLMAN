---
hide:
  - toc
---

# Métricas e Níveis de Pontuação

Esta página apresenta as **métricas** que respondem às questões, formando o nível quantitativo do GQM. Para cada métrica são documentados: definição, procedimento de cálculo, fonte dos dados, procedimento de coleta, critérios de interpretação, **níveis de pontuação** e **critérios de julgamento**.

=== "M1"
    ### M1 — *Nome da métrica* { #m1 }
    === "Definição"

        | Campo | Descrição |
        |-------|-----------|
        | **Questão associada** | [Q1](questoes-hipoteses.md), [Q2](questoes-hipoteses.md) |
        | **Definição** | *O que a métrica mede.* |
        | **Fórmula / cálculo** | *X = A / B, onde A = ... e B = ...* |
        | **Unidade / escala** | *Ex.: %, segundos, contagem* |
        | **Fonte dos dados** | *Ex.: testes com usuários, logs, ferramenta X* |
        | **Procedimento de coleta** | *Passos, responsável e momento da coleta* |
        | **Interpretação** | *Quanto maior/menor, melhor* |

    === "Níveis de pontuação"

        | Nível | Faixa |
        |-------|-------|
        | Insatisfatório | *X < ...* |
        | Mínimo aceitável | *... ≤ X < ...* |
        | Alvo | *... ≤ X < ...* |
        | Excelente | *X ≥ ...* |

    === "Critério de julgamento"

        *Como o resultado desta métrica confirma ou refuta a hipótese e responde à questão Q1.*

=== "M2"
    ### M2 — *Nome da métrica* { #m2 }
    === "Definição"

        | Campo | Descrição |
        |-------|-----------|
        | **Questão associada** | [Q1](questoes-hipoteses.md) |
        | **Definição** | *O que a métrica mede.* |
        | **Fórmula / cálculo** | *X = A / B, onde A = ... e B = ...* |
        | **Unidade / escala** | *Ex.: %, segundos, contagem* |
        | **Fonte dos dados** | *Ex.: testes com usuários, logs, ferramenta X* |
        | **Procedimento de coleta** | *Passos, responsável e momento da coleta* |
        | **Interpretação** | *Quanto maior/menor, melhor* |

    === "Níveis de pontuação"

        | Nível | Faixa |
        |-------|-------|
        | Insatisfatório | *X < ...* |
        | Mínimo aceitável | *... ≤ X < ...* |
        | Alvo | *... ≤ X < ...* |
        | Excelente | *X ≥ ...* |

    === "Critério de julgamento"

        *Como o resultado desta métrica confirma ou refuta a hipótese e responde à questão Q1.*


??? abstract "Escala de níveis de pontuação adotada"
    | Nível | Significado |
    |-------|-------------|
    | :material-circle:{ style="color:#d32f2f" } **Insatisfatório** | Resultado não atende ao requisito; exige ação corretiva. |
    | :material-circle:{ style="color:#f9a825" } **Mínimo aceitável** | Atende parcialmente; recomenda-se melhoria. |
    | :material-circle:{ style="color:#18B551" } **Alvo** | Atende ao requisito definido. |
    | :material-circle:{ style="color:#1565c0" } **Excelente** | Supera o requisito esperado. |