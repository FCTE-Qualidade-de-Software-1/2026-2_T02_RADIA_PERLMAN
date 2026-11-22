---
hide:
  - toc
---

# Cronograma de Execução 

Este documento define a alocação de tarefas e os prazos para a execução da Fase 4 (Execução da avaliação), com base nos 14 cenários de teste definidos no [Protocolo de coleta da Fase 2](../fase2/protocolo-coleta.md). Os procedimentos detalhados estão em [Método e procedimentos de avaliação](metodo-procedimentos.md), e os recursos necessários, em [Recursos e ambiente](recursos-ambiente.md).

Devido ao prazo final do projeto (22/11/2026), este cronograma reflete um esforço de "Sprint Final", estruturado em blocos de execução alinhados às especificações e quantidades mínimas definidas na Fase 2.

## Matriz de Distribuição e Cronograma

| Bloco de Execução | Cenários e Métricas | Responsáveis Sugeridos | Restrições e Regras de Coleta | Data/Turno |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1: Capacidade de Interação com Voluntários** | U-01 (M1)<br>U-03 (M9)<br>U-04 (M10) | **Beatriz** (Mediação)<br>**Dara** (Anotação) | Exige 5 voluntários. U-01: interromper aos 3 min. U-03: observar por até 30s. U-04: limite de 5 min. | **17/11 a 19/11**<br>(Conforme agenda dos voluntários) |
| **Bloco 2: Testes Funcionais e Segurança** | U-02 (M2)<br>R-02 (M4)<br>S-01 (M5)<br>S-02 (M6)<br>S-03 (M12)<br>S-04 (M13) | **Henrique**<br>**Isabella** | Conta autorizada. S-02 (M6) exige 20 comparações válidas. S-03 (M12) exige testes em **2 dias diferentes**. R-02 exige queda local de rede por 5s. | **16/11** (1ª rodada)<br>**17/11** (2ª rodada M12) |
| **Bloco 3: Desempenho e Maturidade (Fora de Pico)** | R-01 (M3)<br>D-01 (M7)<br>D-02 (M8)<br>D-03 (M14 - Fora de Pico) | **Tiago** | Realizar 10 execuções válidas por fluxo para as medições previstas. Para M14, coletar 10 durações válidas em cada um dos fluxos C-F1 e C-F2 na janela fora de pico. Usar a ferramenta de cronometragem padronizada. | **16/11**<br>(Noite / Fora de Pico) |
| **Bloco 4: Desempenho e Maturidade (Horário de Pico)** | R-01 (M3)<br>D-01 (M7)<br>D-02 (M8)<br>D-03 (M14 - Pico) | **Arthur** | Realizar 10 execuções válidas por fluxo para as medições previstas. Para M14, coletar 10 durações válidas em cada um dos fluxos C-F1 e C-F2 na janela de pico. **Obrigatório:** usar o mesmo dispositivo, navegador e tipo de conexão do Bloco 3. | **17/11**<br>(Horário Comercial / Pico) |
| **Bloco 5: Monitoramento Contínuo (Disponibilidade)** | R-03 (M11) | **Toda a equipe** (Revezamento) | Exige **4 verificações por dia** (manhã, almoço, tarde e noite) da 2ª via e do Nada Consta, durante **4 dias consecutivos**. Isso gera 16 verificações por função (32 registros no total). | **17/11 a 20/11** |
| **Bloco 6: Consolidação dos Dados** | M1 a M14 | **Toda a equipe** | Consolidar planilhas, excluir *timeouts* do denominador de desempenho, calcular medianas, percentil 90 e razões. Aplicar níveis de julgamento e redigir o relatório final. | **21/11** (Cálculos)<br>**22/11** (Redação Final) |

## Ações de Gestão (PSM/CID)

Para que a automação dos indicadores de gestão continue refletindo com precisão o esforço da equipe:

- É imprescindível que as *Issues* relativas a cada bloco de execução acima sejam abertas e estimadas antes do início das tarefas.
- As horas reais trabalhadas devem ser registradas diariamente na seção **Horas reais**, no corpo de cada Issue, no formato esperado pelo script: `DD/MM/AAAA - Nome do integrante - X h`. O script `coletar_metricas_psm.py` lê esse campo do corpo da Issue; horas lançadas somente nos comentários não serão contabilizadas no **PSM-3 (Razão de esforço)**.

## Definições consolidadas para a coleta

- **M11 e M6:** quantidades amostrais alinhadas à Fase 2, com 16 verificações por função em 4 dias (17/11 a 20/11) para M11 e 20 comparações válidas para M6.
- **M14:** janelas de pico (17/11, horário comercial) e fora de pico (16/11, período noturno) definidas com horários efetivos e justificativa registrados na planilha de coleta.
- **M1, M9 e M10:** cinco participantes externos confirmados e agendados para as sessões de usabilidade.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 15/11/2026 | Criação do cronograma | Dara Maria Barbosa de Sousa |
| 1.1 | 15/11/2026 | Esclarecimento da amostra da M11, do apontamento PSM-3 e das pendências metodológicas | Arthur de Lima Sobreira |
| 1.2 | 21/11/2026 | Alinhamento das amostras de M11 e M6 com a Fase 2 e consolidação das definições de coleta | Dara Maria Barbosa de Sousa |