---
hide:
  - toc
---

# Cronograma de Execução 

Este documento define a alocação de tarefas e os prazos para a execução da Fase 4 (Execução da avaliação), com base nos 14 cenários de teste definidos no protocolo de coleta da Fase 2.

Devido ao prazo final do projeto (22/11/2026), este cronograma reflete um esforço de "Sprint Final". A métrica **M11 (Disponibilidade)**, que originalmente previa 7 dias com 3 verificações, foi adaptada metodologicamente para **5 dias com 4 verificações diárias**, mantendo a validade da amostra (20 observações) e viabilizando a consolidação dos dados a tempo da entrega.

## Matriz de Distribuição e Cronograma

| Bloco de Execução | Cenários e Métricas | Responsáveis Sugeridos | Restrições e Regras de Coleta | Data/Turno |
| :--- | :--- | :--- | :--- | :--- |
| **Bloco 1: Usabilidade com Voluntários** | U-01 (M1)<br>U-03 (M9)<br>U-04 (M10) | **Beatriz** (Mediação)<br>**Dara** (Anotação) | Exige 5 voluntários. U-01: interromper aos 3 min. U-03: observar por até 30s. U-04: limite de 5 min. | **17/11 a 19/11**<br>(Conforme agenda dos voluntários) |
| **Bloco 2: Testes Funcionais e Segurança** | U-02 (M2)<br>R-02 (M4)<br>S-01 (M5)<br>S-02 (M6)<br>S-03 (M12)<br>S-04 (M13) | **Henrique**<br>**Isabella** | Conta autorizada de Taguatinga. S-03 (M12) exige testes em **2 dias diferentes**. R-02 exige queda local de rede por 5s. | **16/11** (1ª rodada)<br>**17/11** (2ª rodada M12) |
| **Bloco 3: Desempenho e Maturidade (Fora de Pico)** | R-01 (M3)<br>D-01 (M7)<br>D-02 (M8)<br>D-03 (M14 - Fora de Pico) | **Tiago** | Realizar 10 execuções válidas em janela de BAIXA demanda. Usar ferramenta de cronometragem padrão. | **16/11**<br>(Noite / Fora de Pico) |
| **Bloco 4: Desempenho e Maturidade (Horário de Pico)** | R-01 (M3)<br>D-01 (M7)<br>D-02 (M8)<br>D-03 (M14 - Pico) | **Arthur** | Realizar 10 execuções válidas em janela de ALTA demanda. **Obrigatório:** usar mesmo navegador e tipo de conexão do Bloco 3. | **17/11**<br>(Horário Comercial / Pico) |
| **Bloco 5: Monitoramento Contínuo (Disponibilidade)** | R-03 (M11) | **Toda a equipe** (Revezamento) | *Ajuste de prazo:* Exige **4 verificações por dia** (Manhã, Almoço, Tarde e Noite) da 2ª via e Nada Consta, durante **5 dias consecutivos**. | **16/11 a 20/11** |
| **Bloco 6: Consolidação dos Dados** | M1 a M14 | **Toda a equipe** | Consolidar planilhas, excluir *timeouts* do denominador de desempenho, calcular medianas, percentil 90 e razões. Aplicar níveis de julgamento e redigir o relatório final. | **21/11** (Cálculos)<br>**22/11** (Redação Final) |

## Ações de Gestão (PSM/CID)

Para que a automação dos indicadores de gestão continue refletindo com precisão o esforço da equipe:

- É imprescindível que as *Issues* relativas a cada bloco de execução acima sejam abertas e estimadas antes do início das tarefas.
- As horas reais trabalhadas devem ser registradas diariamente nos comentários das *Issues* para compor a métrica **PSM-3 (Razão de esforço)** no GitHub Actions.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 15/11/2026 | Criação do cronograma | Dara Maria Barbosa de Sousa  |