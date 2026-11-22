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

### Ambiente e evidências

A coleta foi realizada em um Dell Inspiron 15 3511 (Intel Core i5-1135G7, 8 GB de RAM), Fedora Linux 44 (Sway Spin), Mozilla Firefox e conexão Wi-Fi de 5 GHz, sem VPN. Os horários e as condições de cada execução constam do arquivo de dados brutos.

Os registros visuais incluem a abertura do histórico e a emissão da segunda via em ambos os períodos, além da [mensagem de indisponibilidade às 08:46](../evidencias/M3/segundaVia-19112026-erro-01-arthur.jpeg). As capturas representativas estão relacionadas na [documentação de coleta da M3](../dados-coleta/M3/M3-resultados.md).

O resultado da M3 descreve os fluxos e períodos observados. O julgamento integral de G2 depende também das métricas M4 e M11, analisadas separadamente.

## M4 — Retomada após interrupção local da conexão

As medições da M4, vinculadas ao cenário R-02, foram realizadas em 20/11/2026, entre 19h29 e 19h36. Foram executadas cinco tentativas independentes de interrupção local da conexão (por 5 segundos) durante a consulta de leitura do relatório de Nada Consta, sem envio de formulários ou alteração de dados cadastrais.

**Tabela 2 — Resultados das tentativas de retomada**

| Tentativa | Horário | Desconexão local | Ação manual | Tempo de retomada | Resultado observado | Classificação |
|---|---:|---:|---:|---:|---|---|
| `M4-R02-20112026-01` | 19:29 | 5 s | Nenhuma | 18 s | Retomada automática dentro de 30 s | Sucesso |
| `M4-R02-20112026-02` | 19:31 | 5 s | Nenhuma | 20 s | Retomada automática dentro de 30 s | Sucesso |
| `M4-R02-20112026-03` | 19:33 | 5 s | Nenhuma | 19 s | Retomada automática dentro de 30 s | Sucesso |
| `M4-R02-20112026-04` | 19:35 | 5 s | Nenhuma | 23 s | Retomada automática dentro de 30 s | Sucesso |
| `M4-R02-20112026-05` | 19:36 | 5 s | Nenhuma | 22 s | Retomada automática dentro de 30 s | Sucesso |

_Fonte: [M4-registros.csv](../dados-coleta/M4/M4-registros.csv), Equipe Radia Perlman, 2026._

Nas cinco tentativas, ao desativar a interface de rede local por 5 segundos, o navegador sinalizou momentaneamente a perda de conexão, mas retomou automaticamente o carregamento após o restabelecimento da rede, concluindo a consulta sem encerrar a sessão autenticada nem reiniciar a jornada do usuário. Os tempos totais de retomada variaram entre 18 s e 23 s (média de 20,4 s e mediana de 20,0 s), todos abaixo do limite máximo de 30 segundos estipulado no protocolo.

O cálculo da métrica considerou todas as cinco tentativas elegíveis:

- **M4:** `M4 = 100 × R / N = 100 × 5 / 5 = 100%`.

A classificação consolidada da M4 é **Excelente** (faixa de 95% ou mais). A hipótese H4, que exige pelo menos 80% das interrupções locais com retomada bem-sucedida, foi **sustentada**.

### Ambiente e evidências

A coleta foi realizada em um computador pessoal (desktop), sistema operacional Windows 11, navegador Microsoft Edge (versão `157.0.4341.60`, com cache padrão habilitado) e conexão cabeada (Ethernet), utilizando conta própria autorizada. Os horários e metadados completos de cada execução constam do arquivo de dados brutos.

Os registros visuais incluem as capturas anonimizadas da conclusão de cada uma das cinco tentativas ([execução 01](../evidencias/M4/M4-R02-20112026-01.png), [execução 02](../evidencias/M4/M4-R02-20112026-02.png), [execução 03](../evidencias/M4/M4-R02-20112026-03.png), [execução 04](../evidencias/M4/M4-R02-20112026-04.png) e [execução 05](../evidencias/M4/M4-R02-20112026-05.png)). O detalhamento completo da análise e das limitações está disponível na [documentação de coleta da M4](../dados-coleta/M4/M4-resultados.md).

O resultado da M4 reflete a recuperabilidade observada no ambiente cliente (interação entre o navegador de referência e a aplicação web) em consulta de leitura, não avaliando isoladamente mecanismos de tolerância a falhas nos servidores.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da estrutura da página | Beatriz |
| 1.1 | 22/11/2026 | Inclusão dos cálculos e resultados da M3 | Arthur de Lima Sobreira |
| 1.2 | 22/11/2026 | Inclusão de cálculos e resultados da M4 | Henrique |
