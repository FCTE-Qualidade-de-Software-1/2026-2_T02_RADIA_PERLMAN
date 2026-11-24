# Resultados de G4 — Eficiência de desempenho

Esta página apresenta os resultados do objetivo G4, que avalia o tempo de resposta do login e do painel de indicadores de continuidade e a variação de tempo entre os períodos de pico e fora de pico na 2ª via e no histórico de consumo.

As fórmulas, as faixas de pontuação e as quantidades mínimas são as definidas em [Métricas](../fase2/metricas.md) e nos [Critérios de julgamento](../fase2/criterios-julgamento.md). Os dados brutos estão relacionados em [Dados brutos e evidências](dados-brutos.md).

## M7 — Mediana do tempo de resposta

Os registros utilizados nas métricas M7 e M8 foram coletados em 19/11/2026, na janela de pico. Na Fase 2, esses indicadores consideram os fluxos de login/cadastro e de indicadores de continuidade. A geração do PDF da segunda via, incluída no roteiro D-01 da Fase 3, foi registrada como fluxo complementar.

Foram registradas dez durações concluídas em cada fluxo. A mediana, com `n = 10`, corresponde à média entre o quinto e o sexto valor da série ordenada.

**Tabela 1 — Mediana por fluxo**

| Fluxo | n | 5º tempo (s) | 6º tempo (s) | Mediana (s) | Classificação |
|---|---:|---:|---:|---:|---|
| F1 — Login | 10 | 3,40 | 3,45 | **3,425** | Mínimo aceitável |
| F2 — Indicadores de continuidade | 10 | 2,67 | 2,91 | **2,790** | Alvo |
| F3 — PDF da segunda via (complementar) | 10 | 3,98 | 4,30 | **4,140** | Mínimo aceitável |

_Fonte: [M7-registros.csv](../dados-coleta/M7/M7-registros.csv), Equipe Radia Perlman, 2026._

Os cálculos de mediana são:

- **F1:** `(3,40 + 3,45) / 2 = 3,425 s`.
- **F2:** `(2,67 + 2,91) / 2 = 2,790 s`.
- **F3:** `(3,98 + 4,30) / 2 = 4,140 s`.

No escopo de M7 definido na Fase 2 (login/cadastro e indicadores), a classificação consolidada é **Mínimo aceitável**. A hipótese H7, que exige mediana de até 3 segundos nos fluxos previstos, **não foi sustentada** devido ao resultado do login. A medição complementar do PDF também ficou no nível Mínimo aceitável.

No fluxo de indicadores de continuidade, o evento final observado foi a apresentação da mensagem “Unidade sem histórico de indicadores de continuidade”. O tempo registrado corresponde à exibição dessa resposta, e não ao carregamento de um painel com indicadores disponíveis.

Além das dez durações de login, foram registradas **seis ocorrências sem tempo de conclusão informado**: três mensagens de solicitação não concluída e três respostas HTTP 403. Essas ocorrências estão identificadas separadamente no CSV e não foram tratadas como durações nem como timeouts de 30 segundos.

## M8 — Percentil 90 do tempo de resposta

A M8 utiliza as mesmas durações concluídas da M7. O método definido na Fase 2 é o do **posto mais próximo**: `posto = ceil(0,90 × n)`. Com dez durações por fluxo, `posto = 9`; portanto, o P90 é o nono valor da lista ordenada.

**Tabela 2 — Durações ordenadas (s)**

| Fluxo | Valores em ordem crescente |
|---|---|
| Login | 3,26; 3,27; 3,32; 3,39; 3,40; 3,45; 3,53; 3,93; 4,36; 4,96 |
| Indicadores de continuidade | 2,06; 2,20; 2,45; 2,46; 2,67; 2,91; 3,12; 3,45; 4,06; 4,30 |
| PDF da segunda via (complementar) | 3,71; 3,78; 3,79; 3,85; 3,98; 4,30; 4,31; 5,13; 5,38; 5,88 |

**Tabela 3 — Percentil 90 por fluxo**

| Fluxo | n | Posto | P90 (s) | Classificação |
|---|---:|---:|---:|---|
| F1 — Login | 10 | 9º | **4,36** | Alvo |
| F2 — Indicadores de continuidade | 10 | 9º | **4,06** | Alvo |
| F3 — PDF da segunda via (complementar) | 10 | 9º | **5,38** | Mínimo aceitável |

_Fonte: [M7-registros.csv](../dados-coleta/M7/M7-registros.csv) e [M8-registros.csv](../dados-coleta/M8/M8-registros.csv), Equipe Radia Perlman, 2026._

Nos fluxos de login e indicadores de continuidade, previstos na Fase 2, M8 recebeu classificação **Alvo** e a hipótese H8 **foi sustentada**, com P90 de até 5 segundos em ambos. No fluxo complementar de geração do PDF, o P90 foi de **5,38 segundos**, classificado como Mínimo aceitável. A inclusão desse fluxo no julgamento conjunto resultaria em classificação Mínimo aceitável, sem sustentação de H8.

## M14 — Razão de tempo entre pico e fora de pico

A coleta válida da M14 contempla o fluxo **C-F1 — Geração do PDF da segunda via**, na janela de pico de 19/11/2026, entre 09:45 e 09:47. Foram registradas dez durações concluídas.

**Tabela 4 — C-F1 na janela de pico**

| Durações ordenadas (s) | 5º tempo (s) | 6º tempo (s) | Mediana do pico (s) |
|---|---:|---:|---:|
| 3,65; 3,70; 3,71; 3,73; 3,99; 4,04; 4,11; 4,18; 4,26; 4,32 | 3,99 | 4,04 | **4,015** |

A mediana da janela de pico corresponde a `(3,99 + 4,04) / 2 = 4,015 s`.

A razão prevista na Fase 2 é `M14(C-F1) = mediana no pico / mediana fora do pico`. Os registros submetidos para a janela fora de pico (Bloco 3) foram descartados durante a auditoria de qualidade da equipe por não atenderem aos critérios de confiabilidade e evidenciamento do protocolo, permanecendo válidos apenas os dados da janela de pico (Bloco 4). Sem a linha de base fora de pico, **não há valor calculável para a razão**, e a métrica **M14** e a hipótese **H14** são declaradas definitivamente **inconclusivas**. Além disso, o fluxo C-F2, originalmente associado ao gráfico do histórico de consumo, não foi executado porque a interface real do portal apresenta apenas uma tabela estática de leituras e valores, não dispondo de gráfico interativo para renderização.

_Fonte: [M14-registros.csv](../dados-coleta/M14/M14-registros.csv) e [captura de geração do PDF](../evidencias/M14/segundaVia-pdf-pico-20261119-arthur.jpeg), Equipe Radia Perlman, 2026._

## Síntese dos resultados de G4

**Tabela 5 — Consolidação de G4**

| Métrica | Classificação | Hipótese |
|---|---|---|
| M7 — Mediana por fluxo | Mínimo aceitável | H7 não sustentada |
| M8 — P90 por fluxo (escopo da Fase 2) | Alvo | H8 sustentada |
| M14 — Razão pico/fora de pico | Inconclusiva | H14 inconclusiva |

O julgamento final de **G4 — Eficiência de desempenho** encerra como **Inconclusivo**, em razão da ausência de dados auditados na janela fora de pico para o cálculo da razão da M14. Os resultados válidos de M7 e M8 descrevem o comportamento temporal observado na janela de pico de 19/11/2026, sem extrapolação para outros períodos de operação da Agência Virtual.

## Ambiente e evidências das medições de 19/11/2026

As medições de M7, M8 e M14 apresentadas acima utilizaram um Dell Inspiron 15 3511 (Intel Core i5-1135G7, 8 GB de RAM), Fedora Linux 44 (Sway Spin), Mozilla Firefox e Wi-Fi de 5 GHz, sem VPN. A versão numérica do Firefox e a condição de cache não constam dos registros. As evidências de M7 e M8 estão reunidas em `docs/evidencias/M7-M8/` e relacionadas em [Dados brutos e evidências](dados-brutos.md).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da estrutura da página | Beatriz |
| 1.1 | 22/11/2026 | Inclusão dos cálculos e resultados de M7, M8 e M14 | Arthur de Lima Sobreira |
| 1.2 | 23/11/2026 | Inclusão da justificativa da ausência do fluxo C-F2 (interface em tabela estática, sem gráfico interativo) | Dara Maria Barbosa de Sousa |
| 1.3 | 24/11/2026 | Formalização do status inconclusivo definitivo de M14 e G4 após descarte da série fora de pico (Bloco 3) na auditoria interna | Dara Maria Barbosa de Sousa |