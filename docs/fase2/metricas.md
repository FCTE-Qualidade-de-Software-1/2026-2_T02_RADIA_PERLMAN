---
hide:
  - toc
---

# Métricas e níveis de pontuação

Definimos oito métricas para responder às [questões do GQM](questoes-hipoteses.md). M1 a M6 são medidas percentuais; M7 e M8 descrevem o tempo de resposta das funcionalidades. A coleta se concentrará nos trechos acessíveis da Agência Virtual, sem modificar informações das contas utilizadas.

| Métrica | Questão | Subcaracterística | Unidade |
|---|---|---|---|
| [M1](#m1) — Localização na primeira tentativa | [Q1](questoes-hipoteses.md#q1) | Apreensibilidade | % |
| [M2](#m2) — Tratamento de entradas inválidas | [Q2](questoes-hipoteses.md#q2) | Proteção contra erros do usuário | % |
| [M3](#m3) — Execuções sem falhas | [Q3](questoes-hipoteses.md#q3) | Maturidade | % |
| [M4](#m4) — Retomada após perda local de conexão | [Q4](questoes-hipoteses.md#q4) | Tolerância a falhas | % |
| [M5](#m5) — Bloqueio de acesso sem sessão | [Q5](questoes-hipoteses.md#q5) | Confidencialidade | % |
| [M6](#m6) — Consistência de dados estáveis | [Q6](questoes-hipoteses.md#q6) | Integridade (indicador indireto) | % |
| [M7](#m7) — Mediana de resposta | [Q7](questoes-hipoteses.md#q7) | Comportamento no tempo | s |
| [M8](#m8) — Percentil 90 de resposta | [Q8](questoes-hipoteses.md#q8) | Comportamento no tempo | s |

## Escalas de avaliação

Adotamos quatro níveis para classificar os resultados: insatisfatório, mínimo aceitável, alvo e excelente. Como M1 a M4 expressam proporções de situações bem-sucedidas, usam a mesma escala. Em M5, exigimos bloqueio em todas as verificações; M6 tem limites próprios, alinhados à hipótese H6. Para os tempos de resposta, M7 e M8, valores menores são preferíveis.

| Métrica | Insatisfatório | Mínimo aceitável | Alvo | Excelente |
|---|---|---|---|---|
| **M1 a M4** | abaixo de 60% | de 60% a menos de 80% | de 80% a menos de 95% | 95% ou mais |
| **M5** | abaixo de 100% | não se aplica | não se aplica | 100% |
| **M6** | abaixo de 80% | de 80% a menos de 95% | de 95% a menos de 100% | 100% |
| **M7** | acima de 5 s | acima de 3 s até 5 s | acima de 2 s até 3 s | até 2 s |
| **M8** | acima de 8 s | acima de 5 s até 8 s | acima de 3 s até 5 s | até 3 s |

### Fundamentação dos limites

As faixas estabelecem níveis de comparação para a avaliação exploratória. Diferenciamos os limites conforme a natureza de cada medida e o impacto potencial de um resultado inadequado:

| Métricas | Critério adotado |
|---|---|
| M1–M4 | A faixa **Alvo** começa em 80%, valor também previsto nas hipóteses H1–H4. Resultados abaixo de 60% indicam que a situação avaliada não foi atendida em uma parcela expressiva das tentativas; 95% ou mais caracteriza desempenho próximo da totalidade dos casos. |
| M5–M6 | Para M5, qualquer exposição efetiva de dados protegidos torna o resultado insatisfatório. Na M6, o **Alvo** começa em 95%, em concordância com H6; a classificação não equivale a uma verificação da integridade interna do sistema. |
| M7–M8 | Os limites das hipóteses são mediana de até 3 segundos e P90 de até 5 segundos por fluxo. As faixas adicionais distinguem respostas mais rápidas e situações de lentidão acentuada. |

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

## Registro dos resultados

Guardaremos os valores necessários para refazer cada cálculo: contagens de casos adequados e elegíveis ou lista de durações, além de funcionalidade, data, ambiente, exclusões e evidências. Quando não houver observações suficientes, registraremos **inconclusivo**, sem atribuir nota zero. Os detalhes da coleta estão no [protocolo](protocolo-coleta.md), e a consolidação dos resultados, nos [critérios de julgamento](criterios-julgamento.md).
