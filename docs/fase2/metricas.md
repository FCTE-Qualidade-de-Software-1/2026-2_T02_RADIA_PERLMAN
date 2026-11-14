# Métricas e níveis de pontuação

Definimos 14 métricas para responder às [questões do GQM](questoes-hipoteses.md). M1-M6 e M9–M13 são medidas percentuais; M7 e M8 descrevem o tempo de resposta das funcionalidades; M14 é uma razão entre tempos. A coleta se concentrará nos trechos acessíveis da Agência Virtual, sem modificar informações das contas utilizadas.

**Tabela 1 —** Métricas, subcaracterísticas e funcionalidades
 
| Métrica | Questão | Subcaracterística | Funcionalidades | Unidade |
|---|---|---|---|---|
| [M1](#m1) — Localização na primeira tentativa | [Q1](questoes-hipoteses.md#q1) | Apreensibilidade | 2ª via, histórico de consumo | % |
| [M2](#m2) — Tratamento de entradas inválidas | [Q2](questoes-hipoteses.md#q2) | Proteção contra erros | Login/cadastro | % |
| [M3](#m3) — Execuções sem falhas | [Q3](questoes-hipoteses.md#q3) | Maturidade | Histórico de consumo | % por fluxo |
| [M4](#m4) — Retomada e recuperação após interrupção local | [Q4](questoes-hipoteses.md#q4) | Tolerância a falhas / Recuperabilidade | Histórico de consumo | % |
| [M5](#m5) — Bloqueio de acesso sem sessão | [Q5](questoes-hipoteses.md#q5) | Confidencialidade | 2ª via, histórico de consumo | % |
| [M6](#m6) — Consistência de dados estáveis | [Q6](questoes-hipoteses.md#q6) | Integridade / Não repúdio (indicador indireto) | Nada Consta | % |
| [M7](#m7) — Mediana do tempo de resposta | [Q7](questoes-hipoteses.md#q7) | Comportamento temporal | Login/cadastro, indicadores de continuidade | s por fluxo |
| [M8](#m8) — Percentil 90 do tempo de resposta | [Q8](questoes-hipoteses.md#q8) | Comportamento temporal | Login/cadastro, indicadores de continuidade | s por fluxo |
| [M9](#m9) — Reconhecimento da finalidade da tela | [Q9](questoes-hipoteses.md#q9) | Reconhecimento da adequação | Nada Consta, indicadores de continuidade | % |
| [M10](#m10) — Tarefas de operação concluídas | [Q10](questoes-hipoteses.md#q10) | Operabilidade | 2ª via, histórico de consumo | % |
| [M11](#m11) — Disponibilidade nas verificações agendadas | [Q11](questoes-hipoteses.md#q11) | Disponibilidade | 2ª via, Nada Consta | % por função |
| [M12](#m12) — Itens de autenticidade e responsabilização atendidos | [Q12](questoes-hipoteses.md#q12) | Autenticidade e Responsabilização | Login/cadastro | % |
| [M13](#m13) — Documentos com autenticidade verificável | [Q13](questoes-hipoteses.md#q13) | Integridade / Não repúdio | Nada Consta | % |
| [M14](#m14) — Razão de tempo entre pico e fora de pico | [Q14](questoes-hipoteses.md#q14) | Capacidade | 2ª via (PDF), histórico de consumo (gráfico) | razão por fluxo |
 
_Fonte: Equipe Radia Perlman, 2026._

## Escalas de avaliação

Adotamos quatro níveis para classificar os resultados: insatisfatório, mínimo aceitável, alvo e excelente. Como M1 a M4 expressam proporções de situações bem-sucedidas, usam a mesma escala. Em M5, exigimos bloqueio em todas as verificações; M6 tem limites próprios, alinhados à hipótese H6. Para os tempos de resposta, M7 e M8, valores menores são preferíveis.

**Tabela 2 —** Escalas de pontuação das métricas

| Métrica | Insatisfatório | Mínimo aceitável | Alvo | Excelente |
|---|---|---|---|---|
| **M1, M2, M3, M4, M9, M10, M12** | abaixo de 60% | de 60% a menos de 80% | de 80% a menos de 95% | 95% ou mais |
| **M5, M13** | abaixo de 100% | não se aplica | não se aplica | 100% |
| **M6** | abaixo de 80% | de 80% a menos de 95% | de 95% a menos de 100% | 100% |
| **M7** | acima de 5 s | acima de 3 s até 5 s | acima de 2 s até 3 s | até 2 s |
| **M8** | acima de 8 s | acima de 5 s até 8 s | acima de 3 s até 5 s | até 3 s |
| **M14** | acima de 2,0 | acima de 1,5 até 2,0 | acima de 1,2 até 1,5 | até 1,2 |

_Fonte: Equipe Radia Perlman, 2026._

### Fundamentação dos limites

As faixas estabelecem níveis de comparação para a avaliação exploratória. Diferenciamos os limites conforme a natureza de cada medida e o impacto potencial de um resultado inadequado:

| Métricas | Critério adotado |
|---|---|
| M1–M4, M9, M10, M12 | A faixa **Alvo** começa em 80%, valor também previsto nas hipóteses H1–H4. Resultados abaixo de 60% indicam que a situação avaliada não foi atendida em uma parcela expressiva das tentativas; 95% ou mais caracteriza desempenho próximo da totalidade dos casos. |
| M5, M13 | Qualquer exposição de dados protegidos (M5) ou documento sem autenticidade verificável (M13) torna o resultado insatisfatório. |
| M6, M11 | O **Alvo** começa em 95%, valor de H6 e H11. As quantidades mínimas (20 comparações e 21 verificações) foram definidas para que essa faixa seja alcançável. |
| M7, M8 | Os limites das hipóteses são mediana de até 3 segundos e P90 de até 5 segundos por fluxo. As faixas adicionais distinguem respostas mais rápidas e situações de lentidão acentuada. |
| M14 | O **Alvo** admite degradação de até 50% no pico (razão 1,5); até 20% (1,2) é considerado excelente; acima do dobro (2,0), insatisfatório. |
 
_Fonte: Equipe Radia Perlman, 2026._

Esses valores foram definidos para o estudo e não correspondem a limites da ISO/IEC 25010:2011 nem a metas contratuais da Neoenergia. Como ainda não dispomos de uma linha de base empírica do produto, registraremos a justificativa e a aprovação dos limites antes de iniciar os testes. Depois disso, não os modificaremos em função dos resultados obtidos. As hipóteses estão em [Questões e hipóteses](questoes-hipoteses.md).

Para as métricas percentuais, utilizaremos `100 × casos adequados / casos elegíveis`. As exclusões ficarão registradas com justificativa e não entrarão no denominador. Caso a amostra mínima não seja alcançada, o resultado permanecerá inconclusivo. As regras de consolidação estão em [Critérios de julgamento](criterios-julgamento.md).

## M1 — Sucesso na localização de funcionalidades { #m1 }

Na M1, vamos observar se usuários pouco familiarizados com a plataforma conseguem encontrar uma função sem ajuda. A tarefa termina quando o participante chega à página indicada, sem precisar emitir documentos ou alterar informações.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q1/H1](questoes-hipoteses.md#q1) |
| Cálculo | `M1 = 100 × S / N`; **S** = tarefas localizadas corretamente na primeira tentativa e sem ajuda; **N** = tarefas de localização elegíveis. |
| Fonte | Fichas de observação de tarefas, com participantes identificados por códigos (P01, P02 etc.). |
| Coleta | Convidar preferencialmente cinco voluntários sem experiência recente com o serviço. Cada um recebe instruções iguais para localizar funções como segunda via, histórico ou indicadores, sem orientação durante a tentativa. |
| Quantidade mínima | Cinco participantes e dez oportunidades de tarefa válidas. |
| Sucesso e exclusões | Sucesso significa chegar ao destino sem dica, dentro do limite previamente combinado (sugestão: três minutos). Ajuda, desistência ou caminho incorreto são insucessos. Tarefas indisponíveis ou dependentes de acesso não autorizado ficam fora do cálculo. |
| Interpretação | Quanto maior, melhor; faixas da tabela geral. H1 é sustentada com **M1 ≥ 80%** e amostra mínima. |

A amostra de participantes será de conveniência. Assim, os resultados da M1 descreverão as pessoas observadas, sem representar estatisticamente todos os consumidores do Distrito Federal.

## M2 — Tratamento de entradas inválidas { #m2 }

A M2 examina se os formulários identificam erros de preenchimento e explicam como corrigi-los. Apenas impedir a digitação de um valor não será suficiente para considerar a resposta adequada.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q2/H2](questoes-hipoteses.md#q2) |
| Cálculo | `M2 = 100 × V / N`; **V** = tentativas inválidas tratadas adequadamente; **N** = tentativas inválidas elegíveis. |
| Fonte | Checklist de campos e mensagens exibidas; imagens de tela sem informações identificáveis, quando necessárias. |
| Coleta | Preparar ao menos dez preenchimentos sintaticamente inválidos em dois ou mais campos ou fluxos acessíveis. Registrar o campo, o tipo de erro, a resposta da interface e a orientação apresentada. |
| Quantidade mínima | Dez tentativas elegíveis em pelo menos dois campos ou fluxos. |
| Sucesso e exclusões | A tentativa é adequada quando o erro é impedido ou sinalizado **e** existe orientação compreensível. Serão excluídos campos cuja verificação dependa do envio de dados sensíveis ou da confirmação de uma operação. |
| Interpretação | Quanto maior, melhor; faixas da tabela geral. H2 é sustentada com **M2 ≥ 80%**. |

Um exemplo de teste é preencher um campo numérico com menos dígitos do que o esperado. Vamos observar a resposta apresentada pela interface antes de qualquer confirmação de dados. Assim, a métrica avaliará o feedback recebido pelo usuário, e não a validação interna do sistema.

## M3 — Execuções sem falhas observáveis { #m3 }

Com a M3, vamos verificar a estabilidade de cada fluxo em condições regulares de uso. Anotaremos travamentos, telas em branco, erros inesperados e outras interrupções que impeçam concluir a navegação prevista.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q3/H3](questoes-hipoteses.md#q3) |
| Cálculo | `M3(f) = 100 × E(f) / N(f)`, em que **f** identifica o fluxo; **E(f)** é o número de execuções sem falha nesse fluxo; **N(f)** é o número de execuções elegíveis do mesmo fluxo, incluindo as que apresentaram falhas. |
| Unidade | Percentual (%) por fluxo. |
| Fonte | Roteiro de navegação, fichas de execução e registro de incidentes identificados pelo fluxo. |
| Coleta | Repetir cada fluxo incluído, registrando o estado esperado, o estado alcançado e eventuais problemas. Dividir as repetições entre pelo menos dois períodos de observação, mantendo as condições descritas no protocolo. |
| Quantidade mínima | Dez execuções elegíveis **para cada fluxo**. Fluxos com menos de dez observações não recebem classificação individual. |
| Sucesso e exclusões | É sucesso alcançar o estado esperado sem falha inesperada. Avisos corretos de preenchimento não contam como falha de maturidade. Interrupções intencionais da M4 e problemas comprovadamente locais são registrados separadamente. |
| Interpretação | Aplicar a escala percentual **a cada fluxo**, sem misturar execuções de funcionalidades diferentes. A hipótese H3 só é sustentada quando todos os fluxos elegíveis com coleta prevista atingirem M3(f) ≥ 80% e houver amostra mínima por fluxo. Para o julgamento de G2, usar a pior classificação entre esses fluxos. |

Apresentaremos os resultados da M3 por fluxo, com número de execuções, sucessos, percentual e classificação. Se um dos fluxos previstos ficar abaixo da amostra mínima, registraremos o impedimento e manteremos seus dados separados, sem atribuir zero ou calcular uma média que esconda diferenças entre funcionalidades.

## M4 — Retomada após interrupção local da conexão { #m4 }

Na M4, verificaremos se a navegação pode ser retomada após uma interrupção breve da conexão do dispositivo de teste. Esse cenário será aplicado apenas em consultas de leitura.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q4/H4](questoes-hipoteses.md#q4) |
| Cálculo | `M4 = 100 × R / N`; **R** = tentativas em que a navegação foi retomada conforme o critério; **N** = interrupções locais elegíveis. |
| Fonte | Registro da etapa anterior, duração da desconexão, ação de recuperação e estado alcançado. |
| Coleta | Interromper a rede local por aproximadamente cinco segundos, restabelecê-la e observar a navegação por até trinta segundos. Admite-se uma ação manual de tentar novamente, desde que esteja disponível na própria interface. |
| Quantidade mínima | Cinco tentativas seguras e independentes. |
| Sucesso e exclusões | A retomada é adequada se o fluxo continuar ou retornar à mesma etapa com uma ação, sem reiniciar a jornada. Não serão interrompidos envios de dados, alterações de conta ou processos de confirmação. |
| Interpretação | Quanto maior, melhor; faixas da tabela geral. H4 é sustentada com **M4 ≥ 80%**. |

Esse resultado também depende do navegador e da rede local; portanto, permitirá avaliar a retomada da navegação no ambiente de teste, mas não a recuperação dos servidores diante de falhas internas.

## M5 — Bloqueio de acesso a páginas restritas { #m5 }

A M5 verifica se páginas restritas continuam protegidas após o encerramento da sessão. Para isso, usaremos somente áreas acessadas previamente por uma conta própria ou autorizada.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q5/H5](questoes-hipoteses.md#q5) |
| Cálculo | `M5 = 100 × B / N`; **B** = verificações sem acesso utilizável a informação protegida; **N** = verificações elegíveis realizadas sem sessão ativa. |
| Fonte | Registro do tipo de página, estado da autenticação e resultado observado. |
| Coleta | Abrir normalmente uma página restrita, encerrar a sessão e verificar o comportamento ao tentar voltar à mesma tela ou reabri-la em uma sessão sem autenticação. Distinguir imagem histórica do navegador de acesso ativo aos dados. |
| Quantidade mínima | Cinco verificações, preferencialmente distribuídas por pelo menos duas páginas restritas. |
| Sucesso e exclusões | O resultado é adequado quando a informação protegida não fica utilizável sem autenticação. Documentos já salvos localmente não representam acesso ao servidor. Não serão manipulados identificadores ou endereços de terceiros. |
| Interpretação | H5 é sustentada apenas com **M5 = 100%** e quantidade mínima de verificações. Com M5 < 100%, o resultado é **Insatisfatório**; com 100%, **Excelente**. Não há classificação intermediária para esta métrica. |

Se encontrarmos dados protegidos acessíveis sem autenticação, registraremos a ocorrência como crítica e encerraremos esse cenário. Na análise, distinguiremos conteúdo antigo mantido pelo navegador de informações que continuem acessíveis no sistema.

## M6 — Consistência de informações estáveis { #m6 }

Na M6, compararemos informações que deveriam permanecer estáveis entre duas consultas próximas. Podemos utilizar, por exemplo, a competência ou o identificador de uma mesma fatura já emitida, caso esses campos estejam disponíveis.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q6/H6](questoes-hipoteses.md#q6) |
| Cálculo | `M6 = 100 × C / N`; **C** = comparações consistentes; **N** = comparações elegíveis da mesma referência. |
| Fonte | Checklist de campos comparados, sem transcrever valores pessoais ou financeiros. |
| Coleta | Selecionar registros estáveis, consultá-los duas vezes na mesma sessão e assinalar “igual”, “divergente” ou “não comparável”. Antes de classificar uma divergência como falha, verificar se houve atualização legítima. |
| Quantidade mínima | Cinco comparações válidas. |
| Sucesso e exclusões | Sucesso corresponde a valores iguais para a mesma referência, sem atualização no intervalo. Campos dinâmicos e referências incomparáveis são excluídos com justificativa. |
| Interpretação | Quanto maior, melhor; na escala específica de M6, o nível **Alvo** começa em 95%, limite também exigido por H6. |

A consistência observada na M6 diz respeito à apresentação das informações. Mesmo que os campos coincidam em todas as consultas, não poderemos concluir que o armazenamento esteja protegido contra alterações indevidas.

## M7 — Mediana do tempo de resposta { #m7 }

A M7 representa o tempo típico entre o comando do usuário e a disponibilidade do conteúdo principal. Calcularemos a mediana de cada fluxo separadamente, para não diluir a lentidão de uma funcionalidade nos resultados de outras.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q7/H7](questoes-hipoteses.md#q7) |
| Cálculo | Ordenar os tempos `t1, ..., tn`. Com **n** ímpar, usar `t[(n+1)/2]`; com **n** par, calcular `(t[n/2] + t[n/2+1]) / 2`. |
| Unidade e fonte | Segundos; gravação local com marcação temporal, cronômetro padronizado ou método equivalente documentado. |
| Coleta | Definir, por fluxo, o clique inicial e o momento em que a interface principal pode ser utilizada. Fazer uma passagem de aquecimento, não contabilizada, e registrar as repetições nas mesmas condições. |
| Quantidade mínima | Dez durações válidas por fluxo, preferencialmente em dois períodos. |
| Tratamento das falhas | Se a tela não ficar utilizável em trinta segundos, registrar timeout separadamente; não atribuir automaticamente duração de trinta segundos à mediana. |
| Interpretação | Quanto menor, melhor; escala específica M7. **H7 exige mediana ≤ 3 s em todos os fluxos avaliados**. |

No registro de M7, incluiremos rede, cache, dispositivo e navegador. Com isso, poderemos contextualizar os tempos observados, sem estender os resultados ao desempenho do serviço sob alta carga.

## M8 — Percentil 90 do tempo de resposta { #m8 }

A M8 complementa a mediana ao observar as respostas mais demoradas. Seu cálculo utilizará os mesmos tempos válidos registrados para M7.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q8/H8](questoes-hipoteses.md#q8) |
| Cálculo | Ordenar as durações em ordem crescente e selecionar o posto `ceil(0,90 × n)` (método do posto mais próximo). Com dez observações, o P90 será a nona. |
| Unidade e fonte | Segundos; registros brutos das medições utilizadas na M7. |
| Coleta | Calcular o percentil para cada fluxo, guardando as durações ordenadas e o posto empregado. Não juntar medições de telas ou condições diferentes. |
| Quantidade mínima | Dez durações válidas por fluxo. |
| Tratamento das falhas | Tempos de operações que não terminaram serão reportados como timeouts, fora da lista de durações concluídas. |
| Interpretação | Quanto menor, melhor; escala específica M8. **H8 exige P90 ≤ 5 s em todos os fluxos avaliados**. |

Como teremos poucas observações por fluxo, o percentil 90 pode variar com um único tempo mais alto. Por isso, analisaremos M8 junto da mediana e da quantidade de timeouts.

## M9 — Reconhecimento da finalidade da tela { #m9 }
 
A M9 verifica se os usuários reconhecem de imediato que as telas do Nada Consta e dos indicadores de continuidade são apropriadas para suas necessidades de informação.
 
| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q9/H9](questoes-hipoteses.md#q9) |
| Cálculo | `M9 = 100 × K / N`; **K** = telas cuja finalidade foi reconhecida corretamente; **N** = apresentações de tela elegíveis. |
| Fonte | Fichas de observação com a resposta de cada participante. |
| Coleta | O avaliador abre a tela e o participante a observa por até 30 segundos, sem interagir. Em seguida, responde a uma pergunta padronizada de múltipla escolha ("Para que serve esta tela?"), com quatro alternativas definidas antes da coleta. |
| Quantidade mínima | Cinco participantes e dez apresentações (duas por participante). |
| Sucesso e exclusões | Sucesso é escolher a alternativa correta sem ajuda. Apresentações em que a tela não carregou corretamente ficam fora do cálculo. |
| Interpretação | Quanto maior, melhor; escala da Tabela 2. H9 é sustentada com **M9 ≥ 80%**. |
 
## M10 — Tarefas de operação concluídas { #m10 }
 
A M10 verifica se os usuários conseguem operar a emissão de 2ª via e o histórico de consumo até o resultado esperado.
 
| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q10/H10](questoes-hipoteses.md#q10) |
| Cálculo | `M10 = 100 × O / N`; **O** = tarefas concluídas sem erro e sem ajuda; **N** = tarefas de operação elegíveis. |
| Fonte | Fichas de observação de tarefas. |
| Coleta | Cada tarefa começa na tela da função, mesmo que o participante tenha precisado de ajuda para localizá-la na M1. As instruções são iguais para todos. |
| Quantidade mínima | Cinco participantes e dez tarefas elegíveis (duas por participante). |
| Sucesso e exclusões | Sucesso significa obter o resultado indicado em até **cinco minutos**, sem ajuda e sem erro de operação que obrigue a recomeçar a tarefa. Tarefas interrompidas por falha do sistema ficam fora do cálculo. |
| Interpretação | Quanto maior, melhor; escala da Tabela 2. H10 é sustentada com **M10 ≥ 80%**. |
 
## M11 — Disponibilidade nas verificações agendadas { #m11 }
 
A M11 estima a proporção de tempo em que a emissão de 2ª via e o Nada Consta permanecem operacionais, por meio de verificações distribuídas em dias e horários diferentes.
 
| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q11/H11](questoes-hipoteses.md#q11) |
| Cálculo | `M11(f) = 100 × D(f) / N(f)`, em que **f** identifica a função; **D(f)** = verificações com a função operacional; **N(f)** = verificações elegíveis da função. |
| Fonte | Planilha de verificações com data, horário, função, resultado e evidência. |
| Coleta | Três verificações por dia (manhã, tarde e noite), durante sete dias consecutivos. Em cada verificação, autenticar-se e acionar a função: a 2ª via é considerada operacional quando a lista de faturas é exibida; o Nada Consta, quando a tela de emissão fica pronta para uso. |
| Quantidade mínima | Vinte e uma verificações por função. |
| Sucesso e exclusões | Sucesso é a função ficar operacional em até 30 segundos. Falhas comprovadamente locais (por exemplo, outros sites também inacessíveis) são excluídas. Manutenções anunciadas pela concessionária contam como indisponibilidade, com registro do aviso. |
| Interpretação | Quanto maior, melhor; escala específica de M11, aplicada **a cada função**. H11 é sustentada quando **M11(f) ≥ 95% nas duas funções**. Para o julgamento de G2, usar a pior classificação entre elas. |
 
## M12 — Itens de autenticidade e responsabilização atendidos { #m12 }
 
A M12 verifica, por meio de itens observáveis pelo usuário comum, se a identidade alegada pode ser comprovada e se as ações são associadas ao titular.
 
| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q12/H12](questoes-hipoteses.md#q12) |
| Cálculo | `M12 = 100 × A / N`; **A** = itens atendidos; **N** = itens elegíveis. |
| Itens | **A1** — credencial incorreta é rejeitada; **A2** — a mensagem de falha não indica qual credencial está incorreta; **A3** — a sessão expira após inatividade (observação de até 60 minutos); **A4** — o cadastro exige comprovação de vínculo ou identidade (por exemplo, dados do titular ou confirmação por e-mail ou SMS), observada sem concluir o cadastro; **R1** — o sistema exibe ou notifica o registro de acesso (por exemplo, último acesso ou aviso de novo login); **R2** — as emissões geram identificador ou protocolo associado ao titular. |
| Fonte | Checklist dos itens com evidência de cada verificação. |
| Coleta | Verificar cada item duas vezes, em dias diferentes, com a conta autorizada. Em A1 e A2, usar no máximo uma tentativa incorreta por verificação, para não bloquear a conta. |
| Quantidade mínima | Cinco dos seis itens elegíveis. |
| Sucesso e exclusões | O item é atendido quando as duas verificações forem positivas. Se as verificações divergirem, o item é inconclusivo e sai do denominador, com justificativa. Não serão feitos testes de força bruta nem uso de contas de terceiros. |
| Interpretação | Quanto maior, melhor; escala da Tabela 2. H12 é sustentada com **M12 ≥ 80%**. |
 
## M13 — Documentos com autenticidade verificável { #m13 }
 
A M13 avalia os mecanismos que previnem a modificação não autorizada do relatório de Nada Consta e comprovam sua emissão, como prevê a Fase 1.
 
| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q13/H13](questoes-hipoteses.md#q13) |
| Cálculo | `M13 = 100 × W / N`; **W** = documentos com autenticidade verificada; **N** = documentos emitidos elegíveis. |
| Fonte | Registro de cada emissão, do mecanismo encontrado e do resultado da verificação, sem publicar o documento. |
| Coleta | Emitir o relatório com a conta autorizada (as emissões da M6 podem ser reutilizadas). Para cada documento, verificar **(a)** se possui mecanismo de comprovação (código de autenticação, QR code ou assinatura digital) e **(b)** se o mecanismo, usado no canal oficial indicado no documento ou no leitor de PDF, confirma a autenticidade e os mesmos dados. |
| Quantidade mínima | Cinco documentos emitidos. |
| Sucesso e exclusões | O documento é adequado quando atende (a) **e** (b). Não serão submetidos documentos alterados aos canais de validação. Se a conta não permitir a emissão (por exemplo, por existir débito), o resultado é inconclusivo. |
| Interpretação | Julgamento binário: **M13 = 100%** sustenta H13 e recebe **Excelente**; **M13 < 100%** recebe **Insatisfatório**. |
 
## M14 — Razão de tempo entre pico e fora de pico { #m14 }
 
A M14 avalia como a geração de PDF e a renderização de gráficos se comportam nos períodos de maior demanda natural, sem geração de carga artificial.
 
| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q14/H14](questoes-hipoteses.md#q14) |
| Cálculo | `M14(f) = mediana no pico / mediana fora do pico`, para cada fluxo **f**. As medianas são calculadas como na M7, incluindo a regra de timeouts. |
| Fonte | Registros brutos de tempo, identificados por fluxo e janela. |
| Coleta | As janelas de pico (por exemplo, dias úteis em horário comercial, próximos ao vencimento das faturas) e fora de pico (por exemplo, fim da noite) serão definidas e justificadas no Plano de Avaliação (Fase 3), antes da coleta. Usar o mesmo navegador, dispositivo e conexão nas duas janelas. |
| Quantidade mínima | Dez execuções válidas por fluxo em cada janela. |
| Sucesso e exclusões | As medianas absolutas de cada janela também serão informadas. Se a mediana no pico for um timeout, a razão não é calculada e o fluxo é classificado como **Insatisfatório**. |
| Interpretação | Quanto menor, melhor; escala específica de M14, aplicada **a cada fluxo**. H14 é sustentada quando **M14(f) ≤ 1,5 em C-F1 e C-F2**. Para o julgamento de G4, usar a pior classificação entre os fluxos. |

## Registro dos resultados

Guardaremos os valores necessários para refazer cada cálculo: contagens de casos adequados e elegíveis ou lista de durações, além de funcionalidade, data, ambiente, exclusões e evidências. Quando não houver observações suficientes, registraremos **inconclusivo**, sem atribuir nota zero. Os detalhes da coleta estão no [protocolo](protocolo-coleta.md), e a consolidação dos resultados, nos [critérios de julgamento](criterios-julgamento.md).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 14/10/2026 | Criação do documento das métricas | Beatriz Figueiredo dos Santos |
| 1.1 | 17/10/2026 | Reestruturação do documento | Arthur de Lima Sobreira |
| 1.2 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |
| 1.3 | 13/11/2026 | Inclusão de M9–M14| Beatriz Figueiredo dos Santos |