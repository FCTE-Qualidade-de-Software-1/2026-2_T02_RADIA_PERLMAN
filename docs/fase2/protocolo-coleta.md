# Protocolo de coleta

Este protocolo descreve como pretendemos coletar as medidas da Fase 2. Nele, definimos os cenários de observação, os registros necessários e os casos que não entrarão nos cálculos. A distribuição das atividades, as ferramentas e o cronograma serão detalhados na Fase 3, antes da execução dos testes na Fase 4.

## 1. Funcionalidades e condições de acesso

Vamos observar login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Utilizaremos páginas públicas ou contas próprias e autorizadas. Quando uma tarefa envolver emissão de documentos ou alteração cadastral, interromperemos o teste na última etapa que possa ser percorrida sem modificar dados, registrando até onde foi possível chegar.

Nas verificações de segurança, vamos observar a proteção das páginas da conta autorizada após o logout. Não faremos testes de invasão, de carga ou de alteração de registros, pois o estudo se limita aos recursos disponíveis ao usuário comum.

Antes das tarefas com voluntários, explicaremos a atividade e como as observações serão registradas. A participação será voluntária e poderá ser interrompida a qualquer momento. Se houver entrevistas gravadas, solicitaremos autorização específica para a gravação. Os arquivos publicados no Git não incluirão senhas, CPFs, tokens ou documentos capazes de identificar contas e consumidores.

## 2. Identificação e registro das observações

Para relacionar as observações sem identificar participantes, atribuiremos um código a cada tentativa, como `U01-20261021-P03`. Esse identificador permitirá consultar o cenário e a evidência correspondente. O registro incluirá:

| Informação | Como registrar |
|---|---|
| Identificação do teste | Código do caso, funcionalidade, cenário e métrica associada. |
| Ambiente | Data e horário, navegador e versão, sistema operacional, dispositivo, resolução de tela e tipo de conexão. |
| Dados coletados | Sucesso/insucesso, classificação do erro, duração em segundos ou comparação de campos, conforme a métrica. |
| Situação do caso | Elegível, excluído ou inconclusivo, com justificativa nos dois últimos casos. |
| Evidência | Referência ao registro anonimizado, imagem de tela ou anotação utilizada. |
| Ocorrências | Falhas observadas e medidas tomadas para interromper um cenário, quando necessário. |

**Quantidades mínimas:** prevemos cinco participantes e dez tarefas válidas para M1; dez apresentações de tela para M9 e dez tarefas de operação para M10; dez entradas inválidas para M2; dez execuções por fluxo em M3; cinco interrupções para M4; cinco verificações, distribuídas entre as páginas de segunda via e de histórico de consumo, para M5; vinte comparações para M6; dez durações válidas por fluxo para M7 e M8; vinte e uma verificações por função para M11; cinco dos seis itens elegíveis para M12; cinco documentos emitidos para M13; e dez execuções válidas por fluxo, em cada janela, para M14.. Essas quantidades delimitam o estudo exploratório, não uma amostra representativa dos consumidores.

## 3. Cenários de coleta

| Código | Métrica | Procedimento resumido | Informação registrada |
|---|---|---|---|
| U-01 | M1 | Solicitar a localização de uma função, sem instruir o caminho. | Tarefa, participante codificado, sucesso, ajuda ou desistência. |
| U-02 | M2 | Testar valor sintaticamente inválido em campo seguro. | Tipo de entrada, mensagem, impedimento e orientação. |
| R-01 | M3 | Definir os fluxos antes da coleta e executar ao menos dez vezes cada um, em dois períodos. | Código do fluxo, execução, sucesso/falha e motivo da exclusão. |
| R-02 | M4 | Desconectar apenas o dispositivo de teste por cinco segundos e restabelecer a rede. | Etapa anterior, retomada em até 30 s e eventual ação manual. |
| S-01 | M5 | Encerrar sessão e tentar reabrir página restrita acessada legitimamente. | Estado da sessão, bloqueio efetivo e eventual exposição de dados protegidos. |
| S-02 | M6 | Consultar duas vezes uma referência estável, sem alteração de dados. | Campo e comparação: igual, divergente ou não comparável. |
| D-01 | M7 | Medir o intervalo entre a ação inicial e a interface utilizável. | Durações por fluxo e mediana. |
| D-02 | M8 | Ordenar os mesmos tempos da M7 e selecionar o P90. | Lista ordenada, posição do percentil e valor final. |
| U-03 | M9 | Apresentar as telas de Nada Consta e de indicadores de continuidade por até 30 segundos, sem interação, e aplicar a pergunta de múltipla escolha. | Tela, participante codificado e alternativa escolhida. |
| U-04 | M10 | Solicitar a emissão da 2ª via e a alteração do período do gráfico de consumo, a partir da tela de cada função. | Tarefa, participante codificado, conclusão em até cinco minutos, erro de operação ou ajuda. |
| R-03 | M11 | Verificar a 2ª via e o Nada Consta três vezes por dia (manhã, tarde e noite), durante sete dias consecutivos. | Data, horário, função, operacional em até 30 s ou não, e evidência. |
| S-03 | M12 | Verificar os itens A1–A4, R1 e R2 no login e no cadastro, duas vezes, em dias diferentes. | Item, verificação, atendido ou não, e evidência. |
| S-04 | M13 | Emitir o relatório de Nada Consta e usar o mecanismo de comprovação no canal oficial indicado no documento. | Emissão, mecanismo encontrado e resultado da verificação. |
| D-03 | M14 | Medir a geração do PDF da 2ª via (C-F1) e a renderização do gráfico de consumo (C-F2) em janelas de pico e fora de pico. | Durações por fluxo e janela, medianas e razão. |

As fichas de [Métricas](metricas.md) detalham o critério de sucesso de cada cenário. Para M3, M11 e M14, manteremos os resultados separados **por fluxo** ou função, sem reunir todas as execuções em um percentual único. Quando não conseguirmos testar um fluxo previsto, registraremos o motivo, sem tratá-lo como falha do produto.

## 4. Medição do tempo de resposta

Antes das medições de tempo, definiremos para cada fluxo o evento inicial e o momento em que o conteúdo principal estiver pronto para uso. Não utilizaremos automaticamente o evento `load` do navegador como término da contagem, pois ele pode não coincidir com a disponibilidade da interface.

Prevemos uma execução de aquecimento, que não entrará no cálculo, seguida de dez medições válidas por fluxo, preferencialmente em dois períodos. Registraremos navegador, dispositivo, rede e condição de cache para comparar situações semelhantes, sem juntar tempos obtidos em ambientes distintos.Para M14, repetiremos o procedimento nas janelas de pico e fora de pico definidas na Fase 3, com dez medições válidas por fluxo em cada janela e o mesmo navegador, dispositivo e conexão.

Podemos medir os intervalos por gravação de interação com marcação temporal ou outro método de cronometragem documentado. Antes de publicar qualquer registro visual, ocultaremos dados da conta. Se a tela não ficar utilizável em até trinta segundos, anotaremos um timeout, sem lançar trinta segundos como duração concluída. Também apresentaremos a quantidade de timeouts, pois considerar apenas as execuções bem-sucedidas poderia distorcer a avaliação.

## 5. Tratamento e armazenamento

Manteremos no repositório os dados necessários para reproduzir os cálculos, associados ao cenário e ao identificador de cada execução. Antes da publicação, removeremos informações que possam identificar participantes ou contas. Os casos excluídos e inconclusivos também serão documentados, com seus respectivos motivos.

Após a coleta, vamos conferir os casos elegíveis, aplicar as fórmulas de M1–M14 e comparar os resultados com as faixas estabelecidas. Na M3 e na M11, usaremos a pior classificação entre os fluxos ou funções válidos para julgar G2 e, na M14, para julgar G4; na M5 e na M13, uma única falha implicará resultado insatisfatório. As demais regras estão nos [Critérios de julgamento](criterios-julgamento.md). Os limites definidos nesta fase serão mantidos durante a análise.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 17/10/2026 | Criação do documento dos protocolos de coleta | Arthur de Lima Sobreira |
| 1.1 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |
| 1.2 | 14/11/2026 | Alinhamento à Fase 1 | Beatriz Figueiredo dos Santos |