---
hide:
  - toc
---

# Cronograma de Execução 

Este documento define a alocação de tarefas e os prazos para a execução da Fase 4 (Execução da avaliação), com base nos 14 cenários de teste definidos no [Protocolo de coleta da Fase 2](../fase2/protocolo-coleta.md). Os procedimentos detalhados estão em [Método e procedimentos de avaliação](metodo-procedimentos.md), e os recursos necessários, em [Recursos e ambiente](recursos-ambiente.md).

Devido ao prazo final do projeto (22/11/2026), este cronograma reflete um esforço de "Sprint Final". A métrica **M11 (Disponibilidade)**, que na Fase 2 previa 7 dias com 3 verificações diárias (21 verificações por função), está planejada para **5 dias com 4 verificações diárias** (20 verificações por função). Essa alteração reduz a quantidade prevista em uma observação por função. Não se deve afirmar que as amostras são estatisticamente equivalentes sem justificativa específica; a pendência e as opções para resolvê-la estão registradas no Plano de Avaliação.

## Matriz de Distribuição e Cronograma

| Bloco de Execução | Cenários e Métricas | Responsáveis Sugeridos | Restrições e Regras de Coleta | Data/Turno |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1: Usabilidade com Voluntários** | U-01 (M1)<br>U-03 (M9)<br>U-04 (M10) | **Beatriz** (Mediação)<br>**Dara** (Anotação) | Exige 5 voluntários. U-01: interromper aos 3 min. U-03: observar por até 30s. U-04: limite de 5 min. | **17/11 a 19/11**<br>(Conforme agenda dos voluntários) |
| **Bloco 2: Testes Funcionais e Segurança** | U-02 (M2)<br>R-02 (M4)<br>S-01 (M5)<br>S-02 (M6)<br>S-03 (M12)<br>S-04 (M13) | **Henrique**<br>**Isabella** | Conta autorizada de Taguatinga. S-03 (M12) exige testes em **2 dias diferentes**. R-02 exige queda local de rede por 5s. | **16/11** (1ª rodada)<br>**17/11** (2ª rodada M12) |
| **Bloco 3: Desempenho e Maturidade (Fora de Pico)** | R-01 (M3)<br>D-01 (M7)<br>D-02 (M8)<br>D-03 (M14 - Fora de Pico) | **Tiago** | Realizar 10 execuções válidas por fluxo para as medições previstas. Para M14, coletar 10 durações válidas em cada um dos fluxos C-F1 e C-F2 na janela fora de pico. Usar a ferramenta de cronometragem padronizada. | **16/11**<br>(Noite / Fora de Pico) |
| **Bloco 4: Desempenho e Maturidade (Horário de Pico)** | R-01 (M3)<br>D-01 (M7)<br>D-02 (M8)<br>D-03 (M14 - Pico) | **Arthur** | Realizar 10 execuções válidas por fluxo para as medições previstas. Para M14, coletar 10 durações válidas em cada um dos fluxos C-F1 e C-F2 na janela de pico. **Obrigatório:** usar o mesmo dispositivo, navegador e tipo de conexão do Bloco 3. | **17/11**<br>(Horário Comercial / Pico) |
| **Bloco 5: Monitoramento Contínuo (Disponibilidade)** | R-03 (M11) | **Toda a equipe** (Revezamento) | *Ajuste de prazo:* Exige **4 verificações por dia** (manhã, almoço, tarde e noite) da 2ª via e do Nada Consta, durante **5 dias consecutivos**. Isso gera 20 verificações por função (40 registros no total). | **16/11 a 20/11** |
| **Bloco 6: Consolidação dos Dados** | M1 a M14 | **Toda a equipe** | Consolidar planilhas, excluir *timeouts* do denominador de desempenho, calcular medianas, percentil 90 e razões. Aplicar níveis de julgamento e redigir o relatório final. | **21/11** (Cálculos)<br>**22/11** (Redação Final) |

## Ações de Gestão (PSM/CID)

Para que a automação dos indicadores de gestão continue refletindo com precisão o esforço da equipe:

- É imprescindível que as *Issues* relativas a cada bloco de execução acima sejam abertas e estimadas antes do início das tarefas.
- As horas reais trabalhadas devem ser registradas diariamente na seção **Horas reais**, no corpo de cada Issue, no formato esperado pelo script: `DD/MM/AAAA - Nome do integrante - X h`. O script `coletar_metricas_psm.py` lê esse campo do corpo da Issue; horas lançadas somente nos comentários não serão contabilizadas no **PSM-3 (Razão de esforço)**.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 15/11/2026 | Criação do cronograma | Dara Maria Barbosa de Sousa |
| 1.1 | 15/11/2026 | Esclarecimento da amostra da M11, do apontamento PSM-3 e das pendências metodológicas | Arthur de Lima Sobreira |

## Pendências de consistência antes da coleta

- **M11:** a Fase 2 estabelece 21 verificações por função, enquanto este cronograma prevê 20. Antes de interpretar H11, a equipe deverá adicionar uma 21ª verificação por função ou formalizar a alteração da quantidade mínima nos documentos da Fase 2. A redução não deve ser descrita como estatisticamente equivalente sem análise que a sustente.
- **M6:** `metricas.md` estabelece cinco comparações válidas, enquanto `protocolo-coleta.md` estabelece vinte. A equipe deverá harmonizar os documentos antes de iniciar a coleta dessa métrica.
- **M14:** registrar os horários exatos de início e fim das janelas de pico e fora de pico antes das medições. O cronograma indica 16/11 à noite e 17/11 em horário comercial, mas os horários efetivos e a justificativa deverão constar na planilha.
- **M1, M9 e M10:** confirmar os cinco participantes externos. Se não houver voluntários, registrar essas métricas como inconclusivas; testes internos poderão ser usados somente para revisar os roteiros.

## Registro das horas no PSM-3

O apontamento de esforço deverá ser feito no corpo da Issue, na seção `Horas reais`, e não apenas em comentários. Cada linha deverá seguir o padrão `DD/MM/AAAA - Nome do integrante - X h`, por exemplo: `16/11/2026 - Integrante - 1,5 h`. O script de coleta lê as seções `Estimativa (horas)` e `Horas reais` do corpo das Issues.
