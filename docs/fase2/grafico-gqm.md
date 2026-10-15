---
hide:
  - toc
---

# Gráfico GQM

O diagrama abaixo representa a hierarquia completa da especificação, do nível **conceitual** (Objetivos) ao **operacional** (Questões) e ao **quantitativo** (Métricas).

```mermaid
flowchart TD
    G1["G1 — [Objetivo 1]"]
    G2["G2 — [Objetivo 2]"]
    Q1["Q1 — [Questão 1]"]
    Q2["Q2 — [Questão 2]"]
    M1["M1 — [Métrica 1]"]
    M2["M2 — [Métrica 2]"]


    G1 --> Q1 & Q2
    G2 --> Q2
    Q1 --> M1 & M2
    Q2 --> M1

```

## Matriz de rastreabilidade

| Objetivo | Questão  | Métrica |
|----------|---------|----------|
| [G1](objetivos.md#g1) | [Q1](questoes-hipoteses.md) | [M1](metricas.md#m1) |
| [G1](objetivos.md#g1) | [Q1](questoes-hipoteses.md) | [M2](metricas.md#m2) |
| [G1](objetivos.md#g1) | [Q2](questoes-hipoteses.md) | [M1](metricas.md#m2) |
| [G2](objetivos.md#g1) | [Q2](questoes-hipoteses.md) | [M1](metricas.md#m2) |


