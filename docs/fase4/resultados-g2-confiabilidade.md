# Resultados de G2 — Confiabilidade

Esta página apresenta os resultados do objetivo G2, que avalia a maturidade do histórico de consumo, a disponibilidade da 2ª via e do Nada Consta e a retomada da navegação após interrupção local da conexão.

As fórmulas, as faixas de pontuação e as quantidades mínimas são as definidas em [Métricas](../fase2/metricas.md) e nos [Critérios de julgamento](../fase2/criterios-julgamento.md). Os dados brutos estão relacionados em [Dados brutos e evidências](dados-brutos.md).

## M3 — Execuções sem falhas observáveis

As medições da M3, vinculadas ao cenário R-01, foram realizadas em 19/11/2026. Foram observados dois fluxos vinculados ao Histórico de Consumo: abertura da página e emissão de segunda via a partir da tabela de faturas. Cada fluxo teve dez execuções elegíveis, distribuídas entre manhã e tarde.

**Tabela 1 — Resultados por fluxo**

| Fluxo | Manhã | Tarde | Sem falha (E) | Elegíveis (N) | M3 = 100 × E/N | Classificação |
|---|---:|---:|---:|---:|---:|---|
| F1 — Abertura do Histórico de Consumo | 5 | 5 | 10 | 10 | 100% | Excelente |
| F2 — Emissão de segunda via pelo histórico | 5 | 5 | 9 | 10 | 90% | Alvo |

_Fonte: [M3-resultados.csv](../dados-coleta/M3/M3-resultados.csv), Equipe Radia Perlman, 2026._

A abertura do histórico apresentou a tabela de faturas nas dez execuções, sem falhas observáveis. Na emissão de segunda via, uma das dez tentativas não foi concluída: às 08:46, a interface exibiu a mensagem “Nosso sistema está indisponível no momento”. A ocorrência foi mantida entre os casos elegíveis. As demais nove emissões foram concluídas.

O cálculo foi realizado por fluxo, sem reunir as duas funcionalidades em um percentual geral:

- **F1:** `M3(F1) = 100 × 10 / 10 = 100%`.
- **F2:** `M3(F2) = 100 × 9 / 10 = 90%`.

A classificação consolidada da M3 corresponde ao menor nível entre os fluxos: **Alvo**. A hipótese H3, que exige pelo menos 80% de execuções sem falha em cada fluxo elegível com amostra mínima, foi **sustentada** nos dois fluxos avaliados.

## Ambiente e evidências

A coleta foi realizada em um Dell Inspiron 15 3511 (Intel Core i5-1135G7, 8 GB de RAM), Fedora Linux 44 (Sway Spin), Mozilla Firefox e conexão Wi-Fi de 5 GHz, sem VPN. Os horários e as condições de cada execução constam do arquivo de dados brutos.

Os registros visuais incluem a abertura do histórico e a emissão da segunda via em ambos os períodos, além da [mensagem de indisponibilidade às 08:46](../evidencias/M3/segundaVia-19112026-erro-01-arthur.jpeg). As capturas representativas estão relacionadas na [documentação de coleta da M3](../dados-coleta/M3/M3-resultados.md).

O resultado da M3 descreve os fluxos e períodos observados. O julgamento integral de G2 depende também das métricas M4 e M11, analisadas separadamente.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da estrutura da página | Beatriz |
| 1.1 | 22/11/2026 | Inclusão dos cálculos e resultados da M3 | Arthur de Lima Sobreira |
