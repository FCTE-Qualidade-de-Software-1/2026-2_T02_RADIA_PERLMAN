---
hide:
  - toc
---

# Gráfico GQM

O diagrama apresenta o desdobramento das quatro características selecionadas na Fase 1. Cada objetivo possui duas questões, e cada questão está ligada à métrica que será utilizada na resposta. As hipóteses correspondentes estão na página de [questões e hipóteses](questoes-hipoteses.md).

```mermaid
flowchart LR
    subgraph N1["Objetivos"]
        direction TB
        G1["G1 — Usabilidade"]
        G2["G2 — Confiabilidade"]
        G3["G3 — Segurança"]
        G4["G4 — Eficiência de desempenho"]
    end
    subgraph N2["Questões"]
        direction TB
        Q1["Q1 — Localização de funções"]
        Q2["Q2 — Erros de preenchimento"]
        Q3["Q3 — Falhas observáveis"]
        Q4["Q4 — Retomada de navegação"]
        Q5["Q5 — Proteção de acesso"]
        Q6["Q6 — Consistência de dados"]
        Q7["Q7 — Tempo típico"]
        Q8["Q8 — Respostas mais lentas"]
    end
    subgraph N3["Métricas"]
        direction TB
        M1["M1 — Localização (%)"]
        M2["M2 — Validação (%)"]
        M3["M3 — Execuções sem falha (%)"]
        M4["M4 — Recuperação (%)"]
        M5["M5 — Bloqueio (%)"]
        M6["M6 — Consistência (%)"]
        M7["M7 — Mediana (s)"]
        M8["M8 — P90 (s)"]
    end
    G1 --> Q1 --> M1
    G1 --> Q2 --> M2
    G2 --> Q3 --> M3
    G2 --> Q4 --> M4
    G3 --> Q5 --> M5
    G3 --> Q6 --> M6
    G4 --> Q7 --> M7
    G4 --> Q8 --> M8
```

*Figura 1 — Hierarquia GQM da avaliação da Agência Virtual da Neoenergia Brasília. Fonte: elaboração própria.*

## Matriz G–Q–H–M

| Objetivo | Subcaracterística | Questão/hipótese | Métrica | Unidade |
|---|---|---|---|---|
| [G1](objetivos.md#g1) | Apreensibilidade | [Q1/H1](questoes-hipoteses.md#q1) | [M1](metricas.md#m1) | % |
| [G1](objetivos.md#g1) | Proteção contra erros | [Q2/H2](questoes-hipoteses.md#q2) | [M2](metricas.md#m2) | % |
| [G2](objetivos.md#g2) | Maturidade | [Q3/H3](questoes-hipoteses.md#q3) | [M3](metricas.md#m3) | % |
| [G2](objetivos.md#g2) | Tolerância a falhas | [Q4/H4](questoes-hipoteses.md#q4) | [M4](metricas.md#m4) | % |
| [G3](objetivos.md#g3) | Confidencialidade | [Q5/H5](questoes-hipoteses.md#q5) | [M5](metricas.md#m5) | % |
| [G3](objetivos.md#g3) | Integridade (indireta) | [Q6/H6](questoes-hipoteses.md#q6) | [M6](metricas.md#m6) | % |
| [G4](objetivos.md#g4) | Comportamento no tempo | [Q7/H7](questoes-hipoteses.md#q7) | [M7](metricas.md#m7) | s |
| [G4](objetivos.md#g4) | Comportamento no tempo | [Q8/H8](questoes-hipoteses.md#q8) | [M8](metricas.md#m8) | s |

A ligação com as funcionalidades e prioridades da Fase 1 está detalhada em [Rastreabilidade](rastreabilidade.md). Em M3, a taxa de execuções sem falhas é calculada por fluxo; M5 exige bloqueio integral de acesso a dados protegidos. As fórmulas estão em [Métricas](metricas.md) e as regras de interpretação, em [Critérios de julgamento](criterios-julgamento.md). Os indicadores de gestão [PSM/CID](gestao-psm.md) não fazem parte da hierarquia GQM, pois acompanham a execução do projeto, não a qualidade do produto.
