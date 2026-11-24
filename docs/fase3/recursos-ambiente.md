# Recursos e ambiente de avaliação

A avaliação será realizada na Agência Virtual da Neoenergia Brasília, por meio da interface web disponível aos usuários. Como a equipe não possui acesso ao código-fonte, aos bancos de dados ou aos recursos administrativos da concessionária, as observações ficarão restritas ao comportamento apresentado durante a navegação.

Este documento reúne os recursos necessários para executar os procedimentos descritos em [Método e procedimentos de avaliação](metodo-procedimentos.md). As condições foram definidas a partir do escopo da [Fase 1](../fase1/produto-avaliado.md), das métricas e do [Protocolo de coleta da Fase 2](../fase2/protocolo-coleta.md), além do cronograma da equipe.

## 1. Ambiente de execução

| Recurso | Especificação para a avaliação | Registro necessário |
|---|---|---|
| Produto | Agência Virtual da Neoenergia Brasília, acessada pelo endereço utilizado pela equipe durante a coleta. | URL, data e horário de acesso. |
| Dispositivo | Notebook ou computador de mesa com teclado e mouse ou touchpad. Recomenda-se pelo menos 8 GB de RAM e resolução de 1366 × 768 ou superior; esses valores são referências operacionais do estudo, não requisitos oficiais da Neoenergia. | Modelo, processador, memória RAM, resolução e sistema operacional. |
| Navegador | Versão estável e atualizada do Chrome, Firefox ou Edge. A equipe deverá escolher um navegador de referência antes das medições de desempenho e manter a mesma versão durante cada série. | Nome, versão, zoom e extensões habilitadas. |
| Conexão | Conexão de banda larga estável. Nas comparações de desempenho, utilizar a mesma rede e o mesmo tipo de conexão. Evitar VPN ou proxy; se forem necessários, registrar seu uso. | Wi-Fi ou cabo, rede utilizada e oscilações observadas. |
| Perfil do navegador | Perfil dedicado à avaliação, sem extensões que interfiram na página. O salvamento automático de senhas deverá permanecer desativado. | Identificação do perfil e configurações relevantes. |
| Cronometragem | Gravação de tela local com marcação temporal, preferencialmente a pelo menos 30 quadros por segundo. Se isso não estiver disponível, utilizar cronômetro com resolução de 0,1 segundo, mantendo o mesmo método em toda a série. | Ferramenta, método, resolução e arquivos associados. |
| Registro e consolidação | Planilha ou arquivo CSV para registrar tentativas, horários, resultados, exclusões e evidências. | Nome e versão do arquivo de coleta. |
| Repositório | Repositório Git da equipe para armazenar procedimentos, dados anonimizados e evidências que possam ser publicadas. | Caminho dos arquivos e commit correspondente. |

O dispositivo principal será utilizado como referência para as medições de tempo. Caso seja necessário utilizar outro computador, navegador ou tipo de conexão, os resultados deverão ser identificados separadamente. Não serão reunidos tempos obtidos em ambientes diferentes sem que essa diferença seja registrada.

Antes de cada sessão, os avaliadores deverão conferir se o relógio do dispositivo está correto, se a conexão está funcionando e se não há atualizações ou downloads em andamento que possam interferir na navegação.

## 2. Ferramentas de apoio

Para esta avaliação, serão suficientes:

- navegador web para acessar a Agência Virtual;
- ferramenta de captura de tela ou gravação local, quando necessária para conferir etapas e tempos;
- cronômetro padronizado, caso não seja possível utilizar gravação com marcação temporal;
- planilha eletrônica para organizar os dados brutos e calcular percentuais, medianas e percentil 90;
- repositório Git para manter os procedimentos, as fichas de coleta e as evidências anonimizadas.

A gravação deverá ser utilizada apenas quando necessária. Antes de publicar imagens ou vídeos, a equipe deverá verificar se aparecem nomes, CPF, endereço, número da unidade consumidora, valores de faturas, códigos de barras, QR Codes, tokens ou outras informações que permitam identificar uma pessoa ou conta. Quando não for possível ocultar esses dados com segurança, a evidência não deverá ser publicada; o resultado poderá ser registrado em uma ficha sem reproduzir a informação sensível.

## 3. Dados de teste e condições de acesso

A avaliação utilizará páginas públicas e contas próprias ou cujo uso tenha sido expressamente autorizado pelo titular. A [Fase 1](../fase1/produto-avaliado.md) prevê o uso de dados reais de uma unidade consumidora autorizada. Essa condição não autoriza a divulgação dos dados: a conta deverá ser acessada somente por integrante autorizado, e nenhuma informação que identifique o titular ou a unidade consumidora será publicada no repositório.

| Situação | Condição de uso |
|---|---|
| Páginas públicas | Podem ser acessadas pelos integrantes da equipe sem autenticação. |
| Páginas restritas | Exigem conta própria ou autorização do titular. O responsável pela conta deverá realizar ou acompanhar a autenticação. |
| Dados de fatura e consumo | Serão consultados somente quando houver autorização. Nos registros, será anotado o resultado da comparação, sem copiar valores pessoais ou financeiros. |
| Formulários | Serão utilizados valores de teste não sensíveis e entradas inválidas apenas nas etapas em que a resposta possa ser observada sem concluir uma operação. |
| Cadastro e alterações | Não serão concluídos cadastros, alterações cadastrais, solicitações ou operações que possam produzir efeitos reais. |
| Credenciais | Senhas, tokens e códigos de autenticação não serão armazenados em planilhas, capturas de tela, vídeos ou arquivos do Git. |
| Emissão de documentos | Será realizada somente com conta autorizada e quando a emissão não causar alteração indevida. Os documentos não serão publicados no repositório. |

Se uma funcionalidade exigir dados ou permissões que a equipe não possui, o teste correspondente não deverá ser improvisado. A limitação será registrada e a métrica ficará inconclusiva quando não houver observações suficientes.

## 4. Avaliadores e participantes

Os integrantes da equipe serão responsáveis por preparar o ambiente, executar os procedimentos técnicos, observar o comportamento da interface e registrar as evidências. Os avaliadores deverão saber navegar em páginas web, seguir o roteiro, identificar o resultado esperado e preencher a ficha de coleta. Para a M4, o operador também deverá conseguir interromper somente a conexão do dispositivo de teste.

Sempre que possível, cada sessão contará com três papéis:

| Papel | Responsabilidade |
|---|---|
| Operador | Executar as etapas previstas no roteiro, sem improvisar ações durante a medição. |
| Observador | Acompanhar a execução, conferir o resultado esperado e identificar ocorrências. |
| Registrador | Preencher a ficha de coleta e relacionar os dados às evidências. |

Os papéis podem ser acumulados quando a quantidade de integrantes não permitir essa divisão. A pessoa que executar uma tentativa deverá registrar essa condição. Nas repetições de M3, M7, M8 e M14, a equipe deverá manter o mesmo procedimento e, sempre que possível, o mesmo operador.

As métricas M1, M9 e M10 dependem de participantes voluntários. O planejamento prevê cinco pessoas externas à equipe, que não tenham utilizado a Agência Virtual recentemente. Os mesmos participantes serão convidados para as três métricas, para evitar recrutamentos diferentes para tarefas que fazem parte da mesma sessão. Cada pessoa receberá as mesmas instruções e não deverá receber ajuda durante a execução.

### 4.1. Critérios de seleção

A seleção será feita por conveniência, entre pessoas que aceitarem o convite e atenderem aos seguintes critérios. Os convites poderão ser encaminhados pelos integrantes a familiares, amigos, conhecidos ou pessoas de sua rede de contatos. Ter vínculo familiar ou pessoal com um integrante não impede a participação, desde que a pessoa não faça parte da equipe do projeto e cumpra os demais critérios de elegibilidade.

- não integrar a equipe do projeto;
- ter 18 anos ou mais. A participação de menores não está prevista neste plano e só poderá ser considerada após orientação da docente e definição das autorizações necessárias;
- conseguir utilizar um navegador e compreender instruções simples em português;
- não ter utilizado a Agência Virtual da Neoenergia Brasília nos últimos seis meses. Esse intervalo é uma definição operacional proposta para tornar verificável a expressão “sem experiência recente” utilizada na Fase 2;
- aceitar participar voluntariamente e registrar o consentimento antes do início das tarefas.

A familiaridade geral com serviços digitais poderá variar entre os participantes. Essa informação será registrada apenas em categorias amplas (por exemplo: baixa, intermediária ou alta familiaridade), sem coletar dados pessoais desnecessários. Quando o convite tiver sido feito por um integrante, a equipe poderá registrar somente a categoria ampla do vínculo (familiar, amigo/conhecido ou sem vínculo prévio), sem nome ou grau de parentesco específico, para caracterizar a composição da amostra e reconhecer possíveis limitações. O objetivo é descrever o perfil geral da pequena amostra, não criar subgrupos para comparação.

### 4.2. Recrutamento e confirmação

O convite poderá ser encaminhado individualmente a familiares, amigos, conhecidos ou outras pessoas da rede de contatos dos integrantes, ou divulgado em canais acadêmicos, sem pressão para aceitar. O vínculo pessoal com quem fez o convite não cria obrigação de participação. Sempre que possível, a sessão deverá ser conduzida por outro integrante que não seja a pessoa responsável pelo convite, para reduzir constrangimentos e evitar influência sobre as respostas. A mensagem deverá informar que se trata de uma atividade acadêmica de avaliação da interface, apresentar uma estimativa de duração e esclarecer que a participação é voluntária.

Antes de confirmar a sessão, um integrante fará uma triagem breve para verificar os critérios acima. Serão convidados participantes elegíveis até completar cinco confirmações. Se houver mais pessoas elegíveis do que vagas, a equipe poderá realizar um sorteio simples entre elas. Como se trata de uma amostra pequena, por conveniência e sem seleção probabilística da população, os resultados não deverão ser generalizados para todos os usuários da Agência Virtual.

A previsão é realizar as sessões entre 17/11 e 19/11, conforme a disponibilidade dos participantes, ainda a ser confirmada por Dara e Beatriz. A equipe deverá registrar apenas o código do participante, a confirmação da elegibilidade e a data da sessão; nomes e contatos não deverão constar nas fichas públicas de coleta.

O convite deverá apresentar a atividade de forma neutra, sem sugerir que o participante está sendo avaliado. Sugestão de texto:

> Estamos realizando uma atividade acadêmica da disciplina Qualidade de Software 1 para observar a facilidade de uso de algumas telas da Agência Virtual da Neoenergia Brasília. A participação é voluntária e deve durar aproximadamente 20 a 30 minutos. Serão propostas tarefas simples de localização e utilização de funcionalidades. Não é uma prova do participante; queremos observar a interface. Você poderá interromper a participação quando quiser. Caso tenha interesse, faremos algumas perguntas rápidas para verificar se você atende aos critérios da atividade.

A triagem deverá confirmar somente as condições necessárias. Familiares, amigos e conhecidos podem participar; o vínculo com um integrante não substitui nem dispensa os critérios abaixo:

1. A pessoa tem 18 anos ou mais?
2. A pessoa integra a equipe responsável pelo projeto? (Se sim, não será incluída como voluntária externa.)
3. A pessoa utilizou a Agência Virtual da Neoenergia Brasília nos últimos seis meses? (Se sim, não atende ao critério de ausência de experiência recente.)
4. A pessoa tem disponibilidade para participar de uma sessão entre 17/11 e 19/11?

A equipe não deverá solicitar CPF, endereço, número de unidade consumidora ou informações de conta durante a triagem. A confirmação de disponibilidade não substitui o consentimento, que será solicitado antes da sessão. A pessoa convidada poderá recusar sem precisar justificar a decisão; o integrante responsável pelo convite não deverá insistir nem condicionar qualquer relação pessoal à participação.

### 4.3. Consentimento e proteção dos participantes

Antes das tarefas, o responsável deverá explicar o objetivo da atividade, o que será solicitado, quais dados serão anotados, como os resultados serão utilizados e que a pessoa poderá interromper sua participação a qualquer momento, sem precisar justificar a decisão. O consentimento deverá ser registrado antes do início da sessão, utilizando o [modelo de termo de consentimento](modelo-consentimento.md), após revisão e autorização da docente.

A participação não exige gravação de voz ou imagem. O procedimento padrão será o registro manual das respostas, dos tempos e das ocorrências pelo observador. Se a equipe considerar necessária uma gravação de tela, deverá explicar sua finalidade e solicitar autorização específica e opcional, separada do consentimento para participar. A recusa à gravação não poderá impedir a participação. Não deverão ser gravados rosto, voz, credenciais ou dados pessoais.

Os formulários de consentimento preenchidos deverão ser armazenados separadamente das fichas de coleta, em local com acesso restrito à equipe responsável. Eles não deverão ser enviados ao repositório público. No GitHub serão disponibilizados somente o modelo em branco e dados de coleta anonimizados, sem nomes, assinaturas, contatos ou outros identificadores. O prazo e o responsável pela guarda dos termos deverão ser definidos com a docente antes das sessões.

O consentimento do participante não substitui a autorização do titular de eventual conta da Agência Virtual. Se uma tarefa exigir acesso a uma conta autenticada, a equipe deverá confirmar previamente que o uso da conta e a exposição das informações necessárias foram autorizados pelo titular. Sempre que possível, deverão ser ocultados dados pessoais e financeiros. Se não for possível proteger essas informações, a tarefa não deverá ser realizada com o voluntário; a limitação deverá ser registrada e a métrica tratada conforme a quantidade de observações efetivamente obtida.

### 4.4. Amostra e tratamento da ausência de voluntários

A amostra prevista é:

- **M1:** cinco participantes e, no mínimo, dez oportunidades de localização;
- **M9:** os mesmos cinco participantes, com duas apresentações de tela por pessoa, totalizando dez apresentações;
- **M10:** os mesmos cinco participantes, com duas tarefas de operação por pessoa, totalizando dez tarefas.

Se não houver cinco participantes externos disponíveis, a equipe poderá realizar uma análise exploratória interna para revisar os roteiros e identificar dificuldades. Essas observações deverão ser identificadas separadamente e não serão contabilizadas como participação de usuários finais. Se a quantidade de participantes externos ficar abaixo da prevista, a equipe deverá informar o número efetivamente obtido e avaliar as métricas conforme as regras da Fase 2, sem apresentar a amostra parcial como se estivesse completa. Na ausência de dados suficientes, M1, M9 e M10, assim como H1, H9 e H10, permanecerão inconclusivas.

## 5. Recursos específicos por métrica

| Métrica | Recursos e condições específicos |
|---|---|
| M1 — Localização de funcionalidades | Cinco participantes voluntários, roteiro de tarefas, observador e ficha individual. Duas oportunidades por participante, sem orientação durante a tentativa. |
| M2 — Tratamento de entradas inválidas | Formulários acessíveis, lista de entradas sintaticamente inválidas e ficha para registrar mensagem, impedimento e orientação. Não enviar dados sensíveis nem concluir operações. |
| M3 — Execuções sem falhas | Fluxos do histórico de consumo definidos antes da coleta, dispositivo e navegador registrados, roteiro de execução e ficha de ocorrências. Dez execuções elegíveis por fluxo, distribuídas em pelo menos dois períodos. |
| M4 — Retomada da conexão | Dispositivo cuja conexão possa ser interrompida sem afetar outros usuários da rede, cronômetro e fluxo de consulta que não altere dados. Cinco tentativas seguras. |
| M5 — Bloqueio sem sessão | Conta própria ou autorizada, acesso prévio a páginas restritas e procedimento de encerramento de sessão. Cinco verificações, preferencialmente em pelo menos duas páginas. |
| M6 — Consistência de informações | Conta autorizada, referência estável e ficha de comparação. Vinte comparações válidas. |
| M7 — Mediana do tempo de resposta | Dispositivo e navegador de referência, conexão registrada, ferramenta de cronometragem e definição prévia dos eventos inicial e final de cada fluxo. Dez durações válidas por fluxo. |
| M8 — Percentil 90 do tempo de resposta | Os mesmos registros válidos da M7, com lista ordenada das durações e indicação do posto utilizado no cálculo do P90. |
| M9 — Reconhecimento da finalidade da tela | Cinco participantes, telas de Nada Consta e de indicadores de continuidade, pergunta padronizada com quatro alternativas e ficha de resposta. Dez apresentações no total. |
| M10 — Tarefas de operação concluídas | Cinco participantes, instruções padronizadas e ficha de observação para emissão da 2ª via e alteração do período do gráfico de consumo. Dez tarefas no total, com limite de cinco minutos por tarefa. |
| M11 — Disponibilidade | Quatro verificações diárias (manhã, almoço, tarde e noite), de 17/11 a 20/11, para a 2ª via e o Nada Consta, totalizando dezesseis verificações por função (32 registros no total). |
| M12 — Autenticidade e responsabilização | Conta autorizada e checklist dos itens A1–A4, R1 e R2. Cada item deverá ser verificado duas vezes, em dias diferentes; pelo menos cinco dos seis itens precisam ser elegíveis. A verificação de expiração de sessão exige até sessenta minutos de inatividade. |
| M13 — Autenticidade dos documentos | Conta autorizada, cinco relatórios de Nada Consta e acesso ao mecanismo ou canal oficial de verificação indicado no documento. Os documentos não serão publicados. |
| M14 — Razão de tempo entre pico e fora de pico | Dispositivo, navegador e conexão iguais nas duas janelas. Dez execuções válidas por fluxo C-F1 (PDF da 2ª via) e C-F2 (gráfico do histórico) em cada janela. As janelas e seus horários exatos deverão ser registrados antes da coleta. |

As fórmulas, os limites das hipóteses e os critérios de julgamento permanecem os definidos na [Fase 2](../fase2/metricas.md) e em seus [critérios de julgamento](../fase2/criterios-julgamento.md). Este documento está totalmente alinhado a essas definições.

## 6. Limitações do ambiente

A avaliação possui limitações que deverão acompanhar a interpretação dos resultados:

- O produto é mantido por uma organização externa. A equipe não possui acesso ao código-fonte, aos bancos de dados, aos logs internos ou à infraestrutura da concessionária.
- As medidas serão obtidas pela interface web e representam o comportamento observado nas condições registradas. Não permitem afirmar como os componentes internos estão implementados.
- A M4 verifica a retomada da navegação após uma interrupção local no dispositivo de teste; não representa um teste de recuperação dos servidores da Neoenergia.
- A M5 observa o bloqueio de páginas restritas após o encerramento da sessão; não substitui uma auditoria de segurança ou um teste de invasão.
- A M6 verifica a consistência de informações apresentadas em consultas comparáveis; não comprova a integridade do banco de dados.
- M7, M8 e M14 serão calculadas com quantidade limitada de observações e sem teste de carga. Os resultados não deverão ser apresentados como desempenho sob alta concorrência.
- A quantidade e a disponibilidade de contas autorizadas podem limitar os fluxos executáveis.
- A ausência de voluntários externos impede o julgamento de M1, M9 e M10 conforme a amostra prevista.

## 7. Verificação antes da coleta

Antes de iniciar uma sessão, a equipe deverá conferir:

- [ ] O dispositivo, o navegador e a conexão foram registrados.
- [ ] O fluxo e a métrica que serão avaliados foram identificados.
- [ ] A conta utilizada é própria ou possui autorização de uso.
- [ ] O procedimento não exige alteração de dados ou confirmação de operação real.
- [ ] A ferramenta de registro está funcionando, quando necessária.
- [ ] O consentimento de cada participante foi registrado antes das tarefas.
- [ ] A equipe confirmou que a sessão não expõe dados pessoais ou financeiros de uma conta real sem autorização específica.
- [ ] Os arquivos de evidência não expõem dados pessoais ou credenciais.
- [ ] Os termos preenchidos estão guardados fora do repositório público, com acesso restrito.
- [ ] Os participantes externos necessários para M1, M9 e M10 foram confirmados, ou as métricas foram marcadas como dependentes dessa disponibilidade.
- [ ] As quantidades mínimas definidas na Fase 2 foram conferidas antes da coleta.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 15/11/2026 | Criação do documento de recursos e ambiente de avaliação | Arthur de Lima Sobreira |
| 1.1 | 15/11/2026 | Ampliação para M1–M14 e alinhamento ao cronograma da Fase 4 | Arthur de Lima Sobreira |
| 1.2 | 15/11/2026 | Inclusão dos critérios de seleção, recrutamento, consentimento e proteção dos participantes | Arthur de Lima Sobreira |
| 1.3 | 15/11/2026 | Esclarecimento de que familiares, amigos e conhecidos dos integrantes podem participar, com registro amplo do vínculo e cuidados para evitar pressão | Arthur de Lima Sobreira |
| 1.4 | 21/11/2026 | Alinhamento das amostras de M11 (16 verificações por função em 4 dias) e M6 (20 comparações válidas) com a Fase 2 | Dara Maria Barbosa de Sousa |