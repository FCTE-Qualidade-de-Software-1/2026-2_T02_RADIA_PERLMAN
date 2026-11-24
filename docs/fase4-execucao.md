# Fase 4 — Execução da Avaliação

Esta seção consolida os resultados da execução prática da avaliação de qualidade da **Agência Virtual da Neoenergia Brasília**, conduzida entre **16/11/2026 e 23/11/2026** conforme o [Plano de Avaliação](fase3-plano-avaliacao.md) definido na Fase 3 e os critérios estabelecidos na [Fase 2](fase2-especificacao.md).

A coleta abrangeu os 14 indicadores definidos no modelo GQM (M1 a M14), distribuídos entre sessões moderadas com voluntários externos, testes funcionais e de segurança em conta autorizada, monitoramento contínuo de disponibilidade e medições de desempenho. Ao final da consolidação, a equipe também desenvolveu e validou um protótipo funcional para mitigar o principal gargalo de usabilidade identificado.

## Síntese dos Resultados por Objetivo

Conforme as regras definidas em [Critérios de julgamento](fase2/criterios-julgamento.md), cada objetivo GQM é avaliado separadamente e recebe a menor classificação obtida entre suas métricas elegíveis:

| Objetivo | Característica (Ênfase) | Métricas | Nível Consolidado | Hipóteses Sustentadas | Detalhamento |
|---|---|---|---|---|---|
| **G1** | Capacidade de Interação (5) | M1, M2, M9, M10 | **Insatisfatório** | H1 e H9 *(H2 não sustentada; H10 inconclusiva)* | [Resultados de G1](fase4/resultados-g1-capacidade-interacao.md) |
| **G2** | Confiabilidade (4) | M3, M4, M11 | **Mínimo aceitável** | H3 e H4 *(H11 não sustentada)* | [Resultados de G2](fase4/resultados-g2-confiabilidade.md) |
| **G3** | Segurança (5) | M5, M6, M12, M13 | **Insatisfatório** | H5 e H6 *(H12 e H13 não sustentadas)* | [Resultados de G3](fase4/resultados-g3-seguranca.md) |
| **G4** | Eficiência de Desempenho (4) | M7, M8, M14 | **Inconclusivo** | H8 *(H7 não sustentada; H14 inconclusiva)* | [Resultados de G4](fase4/resultados-g4-desempenho.md) |

## Estrutura da Documentação da Fase 4

* **[Obtenção das medidas](fase4/obtencao-medidas.md):** acompanhamento da execução dos blocos do cronograma, datas efetivas e registros de auditoria da coleta.
* **[Dados brutos e evidências](fase4/dados-brutos.md):** rastreabilidade completa entre métricas, arquivos CSV, fichas de coleta e capturas de tela anonimizadas.
* **[Resultados de G1 — Capacidade de Interação](fase4/resultados-g1-capacidade-interacao.md):** análise de localização de funcionalidades (M1), tratamento de entradas inválidas (M2), reconhecimento da finalidade das telas (M9), tarefas de operação (M10) e oportunidades de melhoria (OM-01 a OM-04).
* **[Resultados de G2 — Confiabilidade](fase4/resultados-g2-confiabilidade.md):** análise de maturidade dos fluxos (M3), retomada após interrupção local da rede (M4) e disponibilidade nas verificações agendadas (M11).
* **[Resultados de G3 — Segurança](fase4/resultados-g3-seguranca.md):** análise de bloqueio pós-logout (M5), consistência de dados estáveis (M6), autenticidade e responsabilização (M12) e verificabilidade documental do Nada Consta (M13).
* **[Resultados de G4 — Eficiência de Desempenho](fase4/resultados-g4-desempenho.md):** análise da mediana (M7) e do percentil 90 (M8) dos tempos de resposta, além da avaliação de capacidade entre janelas de pico e fora de pico (M14).
* **[Julgamento e conclusões](fase4/julgamento-conclusoes.md):** síntese final da qualidade do produto, relação com o propósito estabelecido na Fase 1 e limitações do estudo.
* **[Ação de melhoria](fase4/acao-melhoria.md) e [Plano de validação](fase4/plano-validacao.md):** especificação, protótipo funcional e testes exploratórios com usuários para a reformulação da tela de *Indicadores de Continuidade* (OM-01).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 24/11/2026 | Criação da visão geral consolidada da Fase 4 | Dara Maria Barbosa de Sousa |