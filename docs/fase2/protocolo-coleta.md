---
hide:
  - toc
---

# Protocolo de coleta

O protocolo reúne as condições necessárias para que os resultados das métricas possam ser comparados e conferidos. Ele delimita quais situações serão observadas, o que deve ser registrado e quais casos ficarão fora dos cálculos. Os responsáveis, instrumentos definitivos e datas de execução serão organizados no plano da Fase 3; a coleta dos resultados ocorrerá na Fase 4.

## 1. Funcionalidades e condições de acesso

A avaliação inclui login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Serão utilizadas páginas públicas e contas próprias ou expressamente autorizadas. Em fluxos que envolvam emissão, alteração cadastral ou confirmação, os testes poderão terminar na última etapa segura disponível, desde que esse limite seja registrado.

As verificações de segurança ficarão restritas a acessos legítimos, encerramento de sessão e observação das páginas da conta autorizada. Não serão realizadas tentativas de adivinhar credenciais, manipular identificadores de outros consumidores, provocar sobrecarga ou modificar dados financeiros. Esses procedimentos não são necessários às métricas escolhidas e não fazem parte do acesso concedido à equipe.

Caso participem voluntários, cada pessoa receberá informação sobre a atividade e a forma de registro, podendo recusar ou interromper sua participação. Nas entrevistas eventualmente gravadas, o consentimento deverá abranger também a gravação. Os documentos publicados no Git não conterão senhas, CPFs, tokens, endereços ou faturas identificáveis.

## 2. Identificação e registro das observações

Cada tentativa receberá um código único, por exemplo `U01-20261021-P03`. O código identifica a observação, não o nome do participante. O registro mínimo inclui:

| Informação | Como registrar |
|---|---|
| Identificação do teste | Código do caso, funcionalidade, cenário e métrica associada. |
| Ambiente | Data e horário, navegador e versão, sistema operacional, dispositivo, resolução de tela e tipo de conexão. |
| Dados coletados | Sucesso/insucesso, classificação do erro, duração em segundos ou comparação de campos, conforme a métrica. |
| Situação do caso | Elegível, excluído ou inconclusivo, com justificativa nos dois últimos casos. |
| Evidência | Referência ao registro anonimizado, imagem de tela ou anotação utilizada. |
| Ocorrências | Falhas observadas e medidas tomadas para interromper um cenário, quando necessário. |

**Quantidades mínimas previstas:** M1 requer cinco participantes e dez tarefas válidas; M2, dez entradas inválidas; M3, dez execuções elegíveis **em cada fluxo**; M4, cinco interrupções; M5, cinco verificações, de preferência em duas páginas; M6, cinco comparações; M7 e M8, dez durações válidas por fluxo. Os mínimos delimitam uma avaliação exploratória, sem pretensão de representar estatisticamente todos os consumidores.

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

O procedimento detalhado e os critérios de sucesso estão nas fichas de [Métricas](metricas.md). Para M3, os casos serão consolidados **por fluxo**, e não em um percentual único de todas as telas. Os fluxos previstos, mas não executáveis, terão o impedimento registrado; sua ausência não será computada como falha do produto.

## 4. Medição do tempo de resposta

Antes de começar, será definido o evento que inicia e o que encerra a contagem em cada fluxo. O ponto final deve corresponder à disponibilidade do conteúdo principal para interação; não será substituído automaticamente pelo evento `load` do navegador, que pode ocorrer em outro momento.

Será realizada uma execução de aquecimento, fora da amostra, seguida por dez medições válidas de cada fluxo, preferencialmente divididas entre dois períodos. Para comparar resultados, serão registrados navegador, dispositivo, rede e condição de cache. Tempos obtidos em ambientes diferentes não serão reunidos como se fossem equivalentes.

O instrumento escolhido poderá ser uma gravação de interação com marcação temporal ou método de cronometragem documentado. Em gravações, a imagem será preparada para não expor dados da conta. Quando uma tela não ficar utilizável dentro de trinta segundos, o caso será anotado como timeout, não como uma medição artificial de exatamente 30 segundos. O número de timeouts acompanhará a análise para evitar que os tempos das execuções concluídas produzam uma avaliação otimista demais.

## 5. Tratamento e armazenamento

Os registros necessários para refazer os cálculos serão mantidos no repositório, vinculando cada resultado ao cenário, ao identificador da execução e à evidência correspondente. Antes da publicação, serão retirados dados que possam identificar pessoas ou contas. Registros descartados ou considerados inconclusivos permanecerão documentados com o motivo da exclusão.

Depois da coleta, os dados serão conferidos quanto à elegibilidade, processados pelas fórmulas de M1–M8 e comparados aos limites definidos. Em M3, a classificação será atribuída a cada fluxo e o pior resultado válido orientará G2; em M5, qualquer acesso efetivo a informação protegida sem sessão ativa determinará resultado insatisfatório. As hipóteses e os objetivos serão interpretados de acordo com os [Critérios de julgamento](criterios-julgamento.md), sem reajuste dos limites após a observação dos resultados.
