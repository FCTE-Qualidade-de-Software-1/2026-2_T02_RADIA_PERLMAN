---
hide:
  - toc
---

# Método e procedimentos de avaliação

A avaliação será manual, de caixa-preta e baseada na observação do comportamento da Agência Virtual da Neoenergia Brasília pela interface web. Cada tentativa deverá seguir um roteiro definido antes da coleta, com condição inicial, ações, resultado esperado e informações a registrar.

Os procedimentos detalham os cenários U-01 a D-03 do [Protocolo de coleta](../fase2/protocolo-coleta.md) e contemplam as métricas M1–M14. As fórmulas, os limites das hipóteses e os níveis de pontuação permanecem os definidos na [Fase 2](../fase2/metricas.md) e nos [Critérios de julgamento](../fase2/criterios-julgamento.md).

## 1. Condições comuns de execução

Antes de iniciar qualquer cenário, o avaliador deverá:

1. Identificar o código do cenário e a métrica correspondente.
2. Registrar data, horário, avaliador, dispositivo, sistema operacional, navegador e tipo de conexão.
3. Conferir se o fluxo está acessível e se a conta utilizada é própria ou autorizada.
4. Registrar o estado inicial da aplicação e os dados de teste não sensíveis que serão utilizados.
5. Executar somente as ações descritas no roteiro, sem improvisar etapas durante a medição.
6. Registrar o resultado observado, a duração quando aplicável e qualquer ocorrência.
7. Classificar a tentativa como elegível, excluída ou inconclusiva. Toda exclusão deverá ter justificativa.

As evidências deverão ser anonimizadas antes de serem incluídas no repositório. Não serão registrados senhas, CPF, endereço, número de unidade consumidora, valores financeiros, tokens ou documentos identificáveis.

### 1.1. Preparação das sessões com participantes externos

Antes de iniciar as sessões de M1, M9 e M10, a equipe deverá seguir a mesma sequência:

1. Convidar pessoas externas à equipe — incluindo, se disponível, familiares, amigos e conhecidos dos integrantes — e aplicar a triagem descrita em [Recursos e ambiente de avaliação](recursos-ambiente.md#4-avaliadores-e-participantes). O vínculo pessoal com quem fez o convite não impede a participação; a amostra será de conveniência e terá como meta cinco participantes elegíveis.
2. Confirmar que cada participante atende aos critérios de seleção e não utilizou a Agência Virtual nos últimos seis meses. Registrar somente a confirmação dos critérios e, quando aplicável, a categoria ampla do vínculo com quem fez o convite (familiar, amigo/conhecido ou sem vínculo prévio), sem incluir nome, grau de parentesco ou contato na ficha pública.
3. Entregar ou apresentar o [modelo de termo de consentimento](modelo-consentimento.md), explicar a atividade e esclarecer dúvidas antes de solicitar a concordância. Não iniciar a sessão sem consentimento registrado.
4. Atribuir um código de P01 a P05. Sempre que possível, a sessão deverá ser conduzida por um integrante diferente daquele que fez o convite. A relação entre código e identidade, caso seja necessária para organizar os horários, deverá ficar separada das fichas de coleta e não será publicada.
5. Ler a mesma orientação inicial para todos e executar M1, M9 e M10 na sequência definida, sem sugerir caminhos ou respostas.
6. Registrar respostas, conclusão das tarefas, tempos e ocorrências. O participante poderá interromper a sessão a qualquer momento; a interrupção deverá ser anotada sem pressioná-lo a continuar.
7. Ao final, agradecer a participação e verificar se as fichas e eventuais evidências não contêm informações pessoais.

O procedimento padrão não inclui gravação de voz ou imagem. Se houver necessidade de gravação de tela, a autorização deverá ser solicitada separadamente e será opcional. O arquivo não poderá conter rosto, voz, credenciais ou dados pessoais e não será publicado sem anonimização e conferência.

A autorização do participante para a atividade não substitui a autorização do titular da conta da Agência Virtual. Antes de permitir que o participante interaja com uma sessão autenticada, a equipe deverá confirmar que o uso da conta foi autorizado e que não haverá exposição desnecessária de dados pessoais ou financeiros. Se essa condição não puder ser garantida, a tarefa não deverá ser executada com o voluntário e a limitação deverá ser registrada.

## 2. Roteiros de avaliação

### 2.1. U-01 — Localização de funcionalidades (M1)

**Objetivo:** verificar se participantes conseguem localizar funções sem ajuda e na primeira tentativa.

**Preparação:** confirmar os cinco participantes conforme os critérios e o procedimento de recrutamento descritos na Seção 1.1. Verificar o consentimento antes de iniciar. Preparar duas tarefas de localização para cada participante, escolhidas entre segunda via de fatura, histórico de consumo e indicadores de continuidade. Definir previamente o destino correto de cada tarefa.

**Execução:**

1. Atribuir um código ao participante (P01 a P05), sem registrar seu nome na planilha pública.
2. Ler a mesma instrução para todos, sem indicar menus, botões ou caminhos.
3. Iniciar a contagem quando a instrução terminar.
4. Encerrar a tentativa quando o participante chegar à tela definida ou completar três minutos.
5. Registrar se chegou ao destino na primeira tentativa, se pediu ajuda, se desistiu ou se escolheu caminho incorreto.
6. Repetir com a segunda tarefa, sem orientar o participante sobre a primeira.

**Resultado esperado:** dez oportunidades de localização registradas, com sucesso quando o destino for alcançado na primeira tentativa e sem ajuda.

**Quantidade mínima:** cinco participantes e dez oportunidades válidas. Se não houver participantes externos, a equipe poderá testar o roteiro de forma exploratória, mas esses resultados não serão contabilizados em M1; H1 ficará inconclusiva.

### 2.2. U-02 — Tratamento de entradas inválidas (M2)

**Objetivo:** observar se a interface identifica entradas inválidas e apresenta orientação compreensível para correção.

**Preparação:** selecionar pelo menos dois campos ou fluxos acessíveis. Preparar dez entradas sintaticamente inválidas, sem utilizar dados pessoais ou credenciais reais. Não utilizar tentativas repetidas de senha incorreta para evitar bloqueio da conta.

**Execução:**

1. Abrir o formulário ou campo selecionado.
2. Inserir um valor inválido previamente definido.
3. Observar se a interface impede o avanço ou sinaliza o problema.
4. Registrar a mensagem exibida e se ela explica como corrigir a entrada.
5. Interromper o cenário antes de qualquer envio que possa confirmar uma operação ou alterar dados.
6. Repetir até completar dez tentativas elegíveis em pelo menos dois campos ou fluxos.

**Resultado esperado:** cada tentativa será classificada como adequada somente quando o erro for impedido ou sinalizado e houver orientação compreensível.

**Quantidade mínima:** dez tentativas elegíveis em pelo menos dois campos ou fluxos.

### 2.3. R-01 — Execuções sem falhas observáveis (M3)

**Objetivo:** observar a estabilidade dos fluxos do histórico de consumo em condições regulares de uso.

**Preparação:** definir e registrar os fluxos do histórico de consumo que serão repetidos. Para cada fluxo, indicar o estado inicial, as ações e o estado final esperado. Programar as repetições em pelo menos dois períodos distintos, conforme o cronograma.

**Execução:**

1. Abrir o fluxo a partir do estado inicial definido.
2. Executar as etapas na ordem estabelecida, sem provocar interrupção intencional da rede (essa condição pertence à M4).
3. Registrar se o estado final esperado foi alcançado.
4. Registrar travamentos, telas em branco, mensagens inesperadas ou interrupções que impeçam a conclusão.
5. Repetir até obter dez execuções elegíveis para cada fluxo.
6. Manter os resultados separados por fluxo; não calcular um percentual geral que misture funcionalidades diferentes.

**Resultado esperado:** dez execuções elegíveis por fluxo, com registro de sucessos e falhas observáveis.

**Quantidade mínima:** dez execuções por fluxo, distribuídas em pelo menos dois períodos. Fluxos com menos observações não receberão classificação individual.

### 2.4. R-02 — Retomada após interrupção local da conexão (M4)

**Objetivo:** verificar se a navegação pode ser retomada após uma interrupção breve da conexão do dispositivo de teste.

**Preparação:** escolher um fluxo de consulta de leitura, sem envio de dados ou alteração de conta. Garantir que somente o dispositivo de teste será desconectado.

**Execução:**

1. Iniciar o fluxo e avançar até a etapa definida no roteiro.
2. Interromper a conexão de rede somente no dispositivo de teste por aproximadamente cinco segundos.
3. Restabelecer a conexão.
4. Observar o comportamento da interface por até trinta segundos.
5. Se necessário, permitir uma única ação manual de tentar novamente, desde que esteja disponível na própria interface.
6. Registrar se o fluxo continuou ou retornou à mesma etapa sem reiniciar toda a jornada.
7. Repetir em cinco tentativas seguras e independentes.

**Resultado esperado:** retomada da navegação sem perda da etapa alcançada, considerando o critério da M4.

**Quantidade mínima:** cinco tentativas elegíveis. Não interromper operações de envio, alteração cadastral ou confirmação.

### 2.5. S-01 — Bloqueio de acesso sem sessão ativa (M5)

**Objetivo:** verificar se páginas restritas continuam protegidas após o encerramento da sessão.

**Preparação:** utilizar conta própria ou autorizada. Selecionar páginas restritas acessadas legitimamente, preferencialmente em pelo menos duas funcionalidades, como segunda via e histórico de consumo.

**Execução:**

1. Autenticar-se normalmente e abrir uma página restrita.
2. Registrar o tipo de página e confirmar que o conteúdo foi acessado durante a sessão válida.
3. Encerrar a sessão pelo mecanismo de logout.
4. Tentar retornar à página anterior e, em seguida, reabrir o endereço da página restrita.
5. Verificar se o sistema exige nova autenticação e se algum dado protegido permanece utilizável.
6. Distinguir uma imagem antiga mantida no cache do navegador de conteúdo que continue acessível no sistema.
7. Repetir até completar cinco verificações, distribuídas preferencialmente entre duas páginas.

**Resultado esperado:** nenhuma informação protegida permanece utilizável sem autenticação. Se houver exposição efetiva, interromper o cenário e registrar a ocorrência como crítica, sem reproduzir os dados na evidência.

**Quantidade mínima:** cinco verificações elegíveis. Uma falha implica julgamento insatisfatório, conforme a Fase 2.

### 2.6. S-02 — Consistência de informações estáveis (M6)

**Objetivo:** verificar se campos estáveis de uma mesma referência apresentam informações iguais em consultas próximas.

**Preparação:** selecionar uma referência estável, como uma fatura já emitida ou um período de consumo encerrado. Definir os campos que serão comparados e evitar copiar valores pessoais ou financeiros para a ficha.

**Execução:**

1. Abrir a consulta correspondente à referência selecionada.
2. Registrar, por código, os campos estáveis que serão comparados.
3. Consultar novamente a mesma referência, sem realizar alterações entre as consultas.
4. Classificar cada comparação como igual, divergente ou não comparável.
5. Antes de registrar uma divergência como falha, verificar se houve atualização legítima ou mudança de contexto.
6. Registrar o motivo de toda comparação excluída.

**Resultado esperado:** os campos estáveis da mesma referência apresentam os mesmos valores nas duas consultas, desde que não tenha ocorrido atualização legítima.

**Quantidade mínima:** vinte comparações válidas.

### 2.7. D-01 — Mediana do tempo de resposta (M7)

**Objetivo:** medir o tempo típico entre o acionamento de uma função e a disponibilidade do conteúdo principal.

**Fluxos:** utilizar os fluxos de desempenho definidos em G4: envio do formulário de login/cadastro, abertura do painel de indicadores de continuidade, geração do PDF da segunda via (C-F1) e renderização do gráfico do histórico de consumo (C-F2). A M14 utiliza especificamente C-F1 e C-F2.

**Preparação:** para cada fluxo, registrar o evento inicial e o evento final antes da coleta. Manter o mesmo dispositivo, navegador, conexão e condição de cache durante cada série. Fazer uma execução de aquecimento, que não entrará no cálculo.

**Execução:**

1. Abrir o fluxo a partir do estado inicial definido.
2. Iniciar a contagem no evento inicial registrado, como o clique que solicita a abertura ou o envio do formulário.
3. Encerrar a contagem quando o conteúdo principal estiver disponível e puder ser utilizado. A presença de indicador de carregamento ou de tela parcialmente preenchida não será considerada conclusão.
4. Registrar a duração em segundos e as condições do ambiente.
5. Repetir até obter dez durações válidas por fluxo.
6. Se a interface não ficar utilizável em até trinta segundos, registrar timeout separadamente, sem atribuir automaticamente trinta segundos como duração concluída.

**Resultado esperado:** dez durações válidas por fluxo, suficientes para calcular a mediana e compará-la ao limite de H7.

**Quantidade mínima:** dez durações válidas por fluxo. Os timeouts deverão ser apresentados separadamente.

### 2.8. D-02 — Percentil 90 do tempo de resposta (M8)

**Objetivo:** identificar o comportamento das respostas mais demoradas, utilizando os mesmos tempos válidos coletados para M7.

**Execução:**

1. Reunir as durações válidas da M7 para um único fluxo.
2. Ordenar os valores em ordem crescente.
3. Calcular a posição pelo método do posto mais próximo: `ceil(0,90 × n)`.
4. Selecionar o valor correspondente à posição calculada.
5. Registrar a lista ordenada, o número de observações, a posição e o valor do P90.
6. Repetir o cálculo separadamente para cada fluxo.

**Resultado esperado:** obter o P90 por fluxo e compará-lo ao limite de cinco segundos definido para H8.

**Quantidade mínima:** as mesmas dez durações válidas por fluxo utilizadas na M7. Com dez observações, o P90 corresponde ao nono valor da lista ordenada.

### 2.9. U-03 — Reconhecimento da finalidade da tela (M9)

**Objetivo:** verificar se os participantes reconhecem a finalidade das telas do Nada Consta e dos indicadores de continuidade.

**Preparação:** utilizar os mesmos cinco participantes que realizaram M1, com consentimento já registrado. Preparar uma pergunta padronizada de múltipla escolha, com quatro alternativas definidas antes da coleta. Duas telas serão apresentadas a cada participante.

**Execução:**

1. Atribuir ou confirmar o código do participante.
2. Abrir uma das telas selecionadas e permitir que seja observada por até trinta segundos, sem interação.
3. Apresentar a pergunta “Para que serve esta tela?”, com as quatro alternativas previamente definidas.
4. Registrar a alternativa escolhida, sem indicar se está correta.
5. Repetir o procedimento para a outra tela.
6. Repetir com os demais participantes.

**Resultado esperado:** dez apresentações de tela registradas. Será considerada correta a escolha da alternativa que descreve a finalidade real da tela, sem ajuda.

**Quantidade mínima:** cinco participantes e dez apresentações. Se não houver voluntários externos, a análise interna poderá servir apenas para revisar o roteiro; M9 e H9 ficarão inconclusivas.

### 2.10. U-04 — Tarefas de operação concluídas (M10)

**Objetivo:** observar se os participantes conseguem operar a emissão de segunda via e a alteração do período do gráfico de consumo até o resultado esperado.

**Preparação:** utilizar os mesmos cinco participantes de M1 e M9, com consentimento já registrado. Preparar instruções iguais para todos. Cada tarefa deverá começar na tela da função, sem contabilizar a localização realizada em M1. Antes da sessão, confirmar que a conta utilizada pode ser apresentada ao participante sem expor dados pessoais ou financeiros sem autorização; se essa condição não for atendida, não executar a tarefa com o voluntário.

**Execução:**

1. Abrir a tela inicial da função e ler a instrução padronizada.
2. Iniciar a contagem quando a instrução terminar.
3. Solicitar que o participante execute a tarefa sem ajuda.
4. Encerrar a tentativa quando o resultado esperado for obtido ou quando se completarem cinco minutos.
5. Registrar conclusão, erro de operação, ajuda solicitada ou interrupção por falha do sistema.
6. Repetir para a segunda tarefa de cada participante.

**Resultado esperado:** dez tarefas registradas. O sucesso exige conclusão em até cinco minutos, sem ajuda e sem erro de operação que obrigue a reiniciar a tarefa.

**Quantidade mínima:** cinco participantes e dez tarefas elegíveis. Sem participantes externos, M10 e H10 ficarão inconclusivas; a equipe não deverá apresentar testes internos como observações de usuários finais.

### 2.11. R-03 — Disponibilidade nas verificações agendadas (M11)

**Objetivo:** verificar se a segunda via e o Nada Consta ficam operacionais nos horários definidos.

**Preparação:** organizar revezamento entre os integrantes. O planejamento prevê quatro verificações por dia — manhã, almoço, tarde e noite — durante quatro dias consecutivos, de 17/11 a 20/11. Em cada horário, as duas funções deverão ser verificadas separadamente.

**Execução:**

1. Registrar a data e o horário efetivo da verificação.
2. Acessar a Agência Virtual com a conta autorizada.
3. Para a segunda via, verificar se a lista de faturas é exibida em até trinta segundos.
4. Para o Nada Consta, verificar se a tela de emissão fica pronta para uso em até trinta segundos.
5. Registrar o resultado e uma evidência que não exponha dados da conta.
6. Se houver suspeita de falha local, verificar a conectividade por outro acesso público e registrar a justificativa antes de excluir a observação.
7. Repetir nos quatro horários previstos, durante os quatro dias.

**Resultado esperado:** dezesseis verificações por função (trinta e dois registros no total, considerando as duas funções). Manutenções anunciadas pela concessionária contam como indisponibilidade, com registro do aviso; falhas comprovadamente locais podem ser excluídas com justificativa.

### 2.12. S-03 — Itens de autenticidade e responsabilização (M12)

**Objetivo:** verificar os itens observáveis de autenticação e responsabilização definidos na Fase 2.

**Itens:** A1 — rejeição de credencial incorreta; A2 — mensagem de falha sem indicação de qual credencial está incorreta; A3 — expiração da sessão após inatividade; A4 — exigência de comprovação de vínculo ou identidade no cadastro; R1 — exibição ou notificação de registro de acesso; R2 — identificador ou protocolo de emissão associado ao titular.

**Execução:**

1. Utilizar conta própria ou autorizada e registrar a data da primeira rodada.
2. Verificar A1 e A2 com, no máximo, uma tentativa incorreta por verificação, evitando risco de bloqueio da conta.
3. Para A3, deixar a sessão sem atividade e observar se expira em até sessenta minutos.
4. Para A4, observar a exigência de comprovação no fluxo de cadastro, sem concluir o cadastro.
5. Para R1 e R2, verificar se a interface exibe ou notifica o registro de acesso e se as emissões apresentam identificador ou protocolo associado ao titular.
6. Repetir cada item em um segundo dia, conforme o cronograma.
7. Considerar atendido somente o item com resultado positivo nas duas verificações. Se os resultados divergirem, classificar o item como inconclusivo e retirá-lo do denominador, com justificativa.

**Resultado esperado:** checklist preenchido para os seis itens, com pelo menos cinco itens elegíveis.

**Quantidade mínima:** cinco dos seis itens elegíveis, verificados duas vezes em dias diferentes. Não realizar testes de força bruta nem utilizar contas de terceiros.

### 2.13. S-04 — Documentos com autenticidade verificável (M13)

**Objetivo:** verificar se o relatório de Nada Consta possui mecanismo que permita comprovar sua autenticidade e emissão.

**Preparação:** utilizar conta autorizada e confirmar se a emissão do documento está disponível. Não publicar os documentos gerados nem seus códigos de autenticação.

**Execução:**

1. Emitir o relatório de Nada Consta pela interface autorizada.
2. Verificar se o documento apresenta mecanismo de comprovação, como código de autenticação, QR Code ou assinatura digital.
3. Utilizar o canal oficial indicado no documento ou o leitor de PDF apropriado para verificar o mecanismo.
4. Registrar se a verificação confirma a autenticidade e os mesmos dados do documento.
5. Repetir até obter cinco documentos emitidos e elegíveis.

**Resultado esperado:** cada documento deverá apresentar mecanismo de comprovação e ter sua autenticidade confirmada. Uma única falha implica julgamento insatisfatório, conforme a regra da Fase 2.

**Quantidade mínima:** cinco documentos emitidos. Se a conta não permitir a emissão, o resultado será inconclusivo, com justificativa.

### 2.14. D-03 — Razão de tempo entre pico e fora de pico (M14)

**Objetivo:** comparar o tempo de geração do PDF da segunda via e de renderização do gráfico de consumo em períodos de pico natural e fora de pico, sem gerar carga artificial.

**Fluxos:** C-F1 — geração do PDF da segunda via; C-F2 — renderização do gráfico do histórico de consumo.

**Preparação:** utilizar o mesmo dispositivo, navegador, versão, conexão e condição de cache nas duas janelas. O cronograma prevê a janela fora de pico em 16/11, no período noturno, e a janela de pico em 17/11, no horário comercial. Os horários exatos de início e fim deverão ser registrados antes da coleta, junto da justificativa para a classificação de cada janela.

**Execução:**

1. Registrar a janela, o horário, o dispositivo, o navegador e a conexão.
2. Executar o fluxo C-F1 e medir o tempo entre a solicitação da geração e o momento em que o PDF estiver disponível para uso.
3. Repetir até obter dez durações válidas para C-F1 naquela janela.
4. Executar o fluxo C-F2 e medir o tempo entre a solicitação do gráfico e sua renderização utilizável.
5. Repetir até obter dez durações válidas para C-F2 naquela janela.
6. Repetir os procedimentos na outra janela, sem alterar o ambiente de referência.
7. Calcular as medianas separadamente por fluxo e janela; depois, calcular a razão entre a mediana de pico e a mediana fora de pico.
8. Registrar timeouts separadamente. Se a mediana no pico for um timeout, aplicar a regra de julgamento definida na Fase 2.

**Resultado esperado:** dez execuções válidas por fluxo em cada janela, com medianas absolutas e razão pico/fora de pico registradas.

**Quantidade mínima:** dez execuções válidas por fluxo em cada uma das duas janelas. Não será gerada carga artificial nem serão misturados resultados de ambientes diferentes.

## 3. Registro e rastreabilidade dos dados

Cada tentativa deverá receber um identificador único. Sugere-se o formato `METRICA-CENARIO-DATA-ORDEM`, por exemplo, `M3-R01-20261116-01`. Para participantes, será utilizado somente o código atribuído, como P01.

A ficha de coleta deverá conter, no mínimo:

| Campo | Conteúdo |
|---|---|
| Identificação | Código da tentativa, cenário e métrica. |
| Data e horário | Momento efetivo da execução. |
| Avaliador | Integrante responsável pelo procedimento e pelo registro. |
| Participante | Código anônimo, quando houver participante externo. |
| Ambiente | Dispositivo, sistema operacional, navegador, conexão e condição de cache. |
| Condição inicial | Estado da aplicação antes da tentativa. |
| Entrada ou ação | Dado de teste não sensível ou ação realizada. |
| Resultado esperado | Comportamento definido no roteiro. |
| Resultado observado | Comportamento apresentado pela interface. |
| Medida | Sucesso/falha, classificação, duração ou comparação, conforme a métrica. |
| Situação | Elegível, excluída ou inconclusiva. |
| Justificativa | Motivo da exclusão ou da impossibilidade de concluir o teste. |
| Evidência | Nome ou caminho do arquivo anonimizado relacionado à tentativa. |

Os dados brutos deverão ser preservados antes do cálculo das métricas. As planilhas ou arquivos CSV deverão permitir relacionar cada resultado à tentativa que o originou. Evidências com dados pessoais, financeiros ou credenciais não deverão ser publicadas.

## 4. Alinhamento com o cronograma

A execução seguirá o [Cronograma da Fase 4](cronograma.md):

- **16/11:** primeira rodada de M2, M4, M5, M6, M12 e M13, além das medições fora de pico de M3, M7, M8 e M14.
- **17/11:** segunda rodada de M12, medições em horário de pico, início da M11 e início das sessões com voluntários.
- **17/11 a 19/11:** sessões de M1, M9 e M10, conforme disponibilidade dos participantes.
- **17/11 a 20/11:** verificações diárias da M11 (4 turnos por dia).
- **21/11:** conferência dos dados, exclusões, cálculos e aplicação dos critérios de julgamento.
- **22/11:** consolidação do relatório e do artigo.

As datas não substituem os registros de horário efetivo. Para M12, deverão ficar comprovados os dois dias diferentes. Para M14, deverão ser registrados os horários exatos das janelas de pico e fora de pico.

## 5. Definições consolidadas para a coleta

1. **M11 e M6:** quantidades mínimas alinhadas à Fase 2, sendo 16 verificações por função em 4 dias (17/11 a 20/11) para M11 e 20 comparações válidas para M6.
2. **M1, M9 e M10:** cinco participantes externos confirmados para a execução das sessões de capacidade de interação.
3. **M14:** horários exatos das janelas de pico e fora de pico definidos e mantidos com o mesmo dispositivo, navegador e conexão nas duas medições.
4. **M13:** disponibilidade de emissão dos cinco documentos de Nada Consta confirmada na conta autorizada.

## Documentos relacionados

- [Plano consolidado da Fase 3](../fase3-plano-avaliacao.md)
- [Recursos e ambiente de avaliação](recursos-ambiente.md)
- [Modelo de termo de consentimento](modelo-consentimento.md)
- [Cronograma de execução](cronograma.md)
- [Métricas e pontuações](../fase2/metricas.md)
- [Questões e hipóteses](../fase2/questoes-hipoteses.md)
- [Protocolo de coleta](../fase2/protocolo-coleta.md)
- [Critérios de julgamento](../fase2/criterios-julgamento.md)

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 15/11/2026 | Criação do documento de método e procedimentos de avaliação | Arthur de Lima Sobreira |
| 1.1 | 15/11/2026 | Ampliação dos roteiros para M1–M14 e alinhamento ao cronograma da Fase 4 | Arthur de Lima Sobreira |
| 1.2 | 15/11/2026 | Inclusão do procedimento padronizado de recrutamento, consentimento e condução das sessões com participantes | Arthur de Lima Sobreira |
| 1.3 | 15/11/2026 | Inclusão de familiares, amigos e conhecidos no recrutamento por conveniência e de cuidados para reduzir influência do convite | Arthur de Lima Sobreira |
| 1.4 | 21/11/2026 | Alinhamento das amostras de M11 e M6 com a Fase 2 e consolidação das definições de coleta | Dara Maria Barbosa de Sousa |