---
hide:
  - toc
---

# Métricas e níveis de pontuação

As métricas M1 a M8 foram definidas para responder às [questões do GQM](questoes-hipoteses.md) com dados coletados durante o uso da Agência Virtual. A maioria expressa percentuais de situações observadas; M7 e M8 tratam dos tempos de carregamento. Todas as análises serão limitadas aos fluxos que possam ser percorridos legitimamente e sem alterar dados da conta.

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

Para interpretar as medições, adotamos os níveis insatisfatório, mínimo aceitável, alvo e excelente. M1 a M4 usam a mesma escala percentual; M5 exige bloqueio em todas as verificações; e M6 possui faixas próprias para que o nível **Alvo** corresponda à hipótese H6. Nas métricas de tempo (M7 e M8), valores menores representam melhor desempenho.

| Métrica | Insatisfatório | Mínimo aceitável | Alvo | Excelente |
|---|---|---|---|---|
| **M1 a M4** | abaixo de 60% | de 60% a menos de 80% | de 80% a menos de 95% | 95% ou mais |
| **M5** | abaixo de 100% | não se aplica | não se aplica | 100% |
| **M6** | abaixo de 80% | de 80% a menos de 95% | de 95% a menos de 100% | 100% |
| **M7** | acima de 5 s | acima de 3 s até 5 s | acima de 2 s até 3 s | até 2 s |
| **M8** | acima de 8 s | acima de 5 s até 8 s | acima de 3 s até 5 s | até 3 s |

### Fundamentação dos limites

As faixas foram propostas para distinguir diferentes níveis de resultado em uma avaliação exploratória. Sua escolha considera o tipo de ocorrência medida e a importância das falhas para o consumidor:

| Métricas | Critério adotado |
|---|---|
| M1–M4 | A faixa **Alvo** começa em 80%, valor também previsto nas hipóteses H1–H4. Resultados abaixo de 60% indicam que a situação avaliada não foi atendida em uma parcela expressiva das tentativas; 95% ou mais caracteriza desempenho próximo da totalidade dos casos. |
| M5–M6 | Para M5, qualquer exposição efetiva de dados protegidos torna o resultado insatisfatório. Na M6, o **Alvo** começa em 95%, em concordância com H6; a classificação não equivale a uma verificação da integridade interna do sistema. |
| M7–M8 | Os limites das hipóteses são mediana de até 3 segundos e P90 de até 5 segundos por fluxo. As faixas adicionais distinguem respostas mais rápidas e situações de lentidão acentuada. |

São referências de julgamento estabelecidas para o estudo, não limites fornecidos pela ISO/IEC 25010:2011 ou metas contratuais da Neoenergia. Como não resultam de uma linha de base empírica do produto, **a equipe precisa aprová-las e registrar sua justificativa antes da coleta**. A partir do início das medições, os limites devem permanecer fixos. As hipóteses correspondentes estão em [Questões e hipóteses](questoes-hipoteses.md).

Nos percentuais, o cálculo geral é `100 × casos adequados / casos elegíveis`. Um caso excluído deve ter motivo registrado e não integra o denominador. Quando não houver observações válidas — ou quando a quantidade mínima prevista não for atingida — a métrica será inconclusiva. A interpretação conjunta está em [Critérios de julgamento](criterios-julgamento.md).

## M1 — Sucesso na localização de funcionalidades { #m1 }

**Objetivo:** observar a facilidade com que usuários pouco familiarizados com a plataforma encontram uma função pela primeira vez. Não será necessário concluir a emissão de um documento: a tarefa termina quando o participante alcançar a página previamente definida.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q1/H1](questoes-hipoteses.md#q1) |
| Cálculo | `M1 = 100 × S / N`; **S** = tarefas localizadas corretamente na primeira tentativa e sem ajuda; **N** = tarefas de localização elegíveis. |
| Fonte | Fichas de observação de tarefas, com participantes identificados por códigos (P01, P02 etc.). |
| Coleta | Convidar preferencialmente cinco voluntários sem experiência recente com o serviço. Cada um recebe instruções iguais para localizar funções como segunda via, histórico ou indicadores, sem orientação durante a tentativa. |
| Quantidade mínima | Cinco participantes e dez oportunidades de tarefa válidas. |
| Sucesso e exclusões | Sucesso significa chegar ao destino sem dica, dentro do limite previamente combinado (sugestão: três minutos). Ajuda, desistência ou caminho incorreto são insucessos. Tarefas indisponíveis ou dependentes de acesso não autorizado ficam fora do cálculo. |
| Interpretação | Quanto maior, melhor; faixas da tabela geral. H1 é sustentada com **M1 ≥ 80%** e amostra mínima. |

A amostra será de conveniência. Portanto, o percentual descreve os participantes avaliados, sem representar estatisticamente a população de consumidores do Distrito Federal.

## M2 — Tratamento de entradas inválidas { #m2 }

**Objetivo:** verificar se os formulários reconhecem erros de preenchimento e oferecem informação útil para corrigi-los. Uma restrição silenciosa de digitação, por si só, não será considerada orientação suficiente.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q2/H2](questoes-hipoteses.md#q2) |
| Cálculo | `M2 = 100 × V / N`; **V** = tentativas inválidas tratadas adequadamente; **N** = tentativas inválidas elegíveis. |
| Fonte | Checklist de campos e mensagens exibidas; imagens de tela sem informações identificáveis, quando necessárias. |
| Coleta | Preparar ao menos dez preenchimentos sintaticamente inválidos em dois ou mais campos ou fluxos acessíveis. Registrar o campo, o tipo de erro, a resposta da interface e a orientação apresentada. |
| Quantidade mínima | Dez tentativas elegíveis em pelo menos dois campos ou fluxos. |
| Sucesso e exclusões | A tentativa é adequada quando o erro é impedido ou sinalizado **e** existe orientação compreensível. Serão excluídos campos cuja verificação dependa do envio de dados sensíveis ou da confirmação de uma operação. |
| Interpretação | Quanto maior, melhor; faixas da tabela geral. H2 é sustentada com **M2 ≥ 80%**. |

Um campo numérico preenchido com quantidade insuficiente de dígitos é um exemplo de entrada para esse teste. A avaliação será feita até a etapa segura de validação; não inclui criação de contas fictícias nem envio de documentos ao sistema. O resultado descreve a interface, não os mecanismos de validação internos.

## M3 — Execuções sem falhas observáveis { #m3 }

**Objetivo:** medir a estabilidade de cada fluxo de navegação em condições regulares. Serão registrados travamentos, telas em branco, erros inesperados e interrupções não previstas.

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

Os resultados serão apresentados em uma tabela com fluxo, execuções sem falha, total de execuções, percentual e classificação. Se algum fluxo previsto não puder atingir o volume mínimo, a situação será identificada como inconclusiva; os demais resultados serão apresentados individualmente, sem transformar a lacuna em zero nem esconder uma falha pela média geral.

## M4 — Retomada após interrupção local da conexão { #m4 }

**Objetivo:** observar a recuperação da navegação quando há uma perda breve de conectividade no dispositivo utilizado para avaliar o sistema. O cenário será aplicado somente em consultas de leitura.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q4/H4](questoes-hipoteses.md#q4) |
| Cálculo | `M4 = 100 × R / N`; **R** = tentativas em que a navegação foi retomada conforme o critério; **N** = interrupções locais elegíveis. |
| Fonte | Registro da etapa anterior, duração da desconexão, ação de recuperação e estado alcançado. |
| Coleta | Interromper a rede local por aproximadamente cinco segundos, restabelecê-la e observar a navegação por até trinta segundos. Admite-se uma ação manual de tentar novamente, desde que esteja disponível na própria interface. |
| Quantidade mínima | Cinco tentativas seguras e independentes. |
| Sucesso e exclusões | A retomada é adequada se o fluxo continuar ou retornar à mesma etapa com uma ação, sem reiniciar a jornada. Não serão interrompidos envios de dados, alterações de conta ou processos de confirmação. |
| Interpretação | Quanto maior, melhor; faixas da tabela geral. H4 é sustentada com **M4 ≥ 80%**. |

A medição envolve também o comportamento do navegador e da rede utilizada. Ela não permite inferir como os servidores da Neoenergia se comportariam diante de uma falha interna.

## M5 — Bloqueio de acesso a páginas restritas { #m5 }

**Objetivo:** verificar se informações protegidas permanecem inacessíveis quando não há sessão autenticada. Serão usadas apenas páginas conhecidas por meio do acesso legítimo à própria conta ou a uma conta expressamente autorizada.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q5/H5](questoes-hipoteses.md#q5) |
| Cálculo | `M5 = 100 × B / N`; **B** = verificações sem acesso utilizável a informação protegida; **N** = verificações elegíveis realizadas sem sessão ativa. |
| Fonte | Registro do tipo de página, estado da autenticação e resultado observado. |
| Coleta | Abrir normalmente uma página restrita, encerrar a sessão e verificar o comportamento ao tentar voltar à mesma tela ou reabri-la em uma sessão sem autenticação. Distinguir imagem histórica do navegador de acesso ativo aos dados. |
| Quantidade mínima | Cinco verificações, preferencialmente distribuídas por pelo menos duas páginas restritas. |
| Sucesso e exclusões | O resultado é adequado quando a informação protegida não fica utilizável sem autenticação. Documentos já salvos localmente não representam acesso ao servidor. Não serão manipulados identificadores ou endereços de terceiros. |
| Interpretação | H5 é sustentada apenas com **M5 = 100%** e quantidade mínima de verificações. Com M5 < 100%, o resultado é **Insatisfatório**; com 100%, **Excelente**. Não há classificação intermediária para esta métrica. |

Se houver acesso efetivo a dados protegidos sem autenticação, o caso será registrado como ocorrência crítica e a coleta correspondente será interrompida. Páginas históricas mantidas no cache do navegador serão distinguidas de conteúdo privado novamente acessível no sistema.

## M6 — Consistência de informações estáveis { #m6 }

**Objetivo:** conferir se a interface apresenta o mesmo valor ao consultar, duas vezes e em curto intervalo, uma informação que não deveria mudar. Podem ser utilizados, quando disponíveis, a competência ou o identificador de uma fatura já emitida.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q6/H6](questoes-hipoteses.md#q6) |
| Cálculo | `M6 = 100 × C / N`; **C** = comparações consistentes; **N** = comparações elegíveis da mesma referência. |
| Fonte | Checklist de campos comparados, sem transcrever valores pessoais ou financeiros. |
| Coleta | Selecionar registros estáveis, consultá-los duas vezes na mesma sessão e assinalar “igual”, “divergente” ou “não comparável”. Antes de classificar uma divergência como falha, verificar se houve atualização legítima. |
| Quantidade mínima | Cinco comparações válidas. |
| Sucesso e exclusões | Sucesso corresponde a valores iguais para a mesma referência, sem atualização no intervalo. Campos dinâmicos e referências incomparáveis são excluídos com justificativa. |
| Interpretação | Quanto maior, melhor; na escala específica de M6, o nível **Alvo** começa em 95%, limite também exigido por H6. |

A M6 é uma medida indireta: consistência entre consultas não demonstra proteção dos dados armazenados contra modificações não autorizadas. A conclusão ficará restrita a possíveis divergências visíveis.

## M7 — Mediana do tempo de resposta { #m7 }

**Objetivo:** identificar o tempo típico entre a ação do usuário e a disponibilidade do conteúdo principal. O cálculo será feito por fluxo, pois juntar operações diferentes poderia ocultar lentidão em uma funcionalidade específica.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q7/H7](questoes-hipoteses.md#q7) |
| Cálculo | Ordenar os tempos `t1, ..., tn`. Com **n** ímpar, usar `t[(n+1)/2]`; com **n** par, calcular `(t[n/2] + t[n/2+1]) / 2`. |
| Unidade e fonte | Segundos; gravação local com marcação temporal, cronômetro padronizado ou método equivalente documentado. |
| Coleta | Definir, por fluxo, o clique inicial e o momento em que a interface principal pode ser utilizada. Fazer uma passagem de aquecimento, não contabilizada, e registrar as repetições nas mesmas condições. |
| Quantidade mínima | Dez durações válidas por fluxo, preferencialmente em dois períodos. |
| Tratamento das falhas | Se a tela não ficar utilizável em trinta segundos, registrar timeout separadamente; não atribuir automaticamente duração de trinta segundos à mediana. |
| Interpretação | Quanto menor, melhor; escala específica M7. **H7 exige mediana ≤ 3 s em todos os fluxos avaliados**. |

As condições de rede, cache, dispositivo e navegador serão mantidas no registro. A medida descreve a experiência no ambiente de teste e não o desempenho do serviço sob carga de muitos usuários.

## M8 — Percentil 90 do tempo de resposta { #m8 }

**Objetivo:** complementar a mediana com um indicador das respostas mais demoradas. A M8 utiliza exatamente as mesmas durações válidas obtidas para M7.

| Campo | Especificação |
|---|---|
| Questão e hipótese | [Q8/H8](questoes-hipoteses.md#q8) |
| Cálculo | Ordenar as durações em ordem crescente e selecionar o posto `ceil(0,90 × n)` (método do posto mais próximo). Com dez observações, o P90 será a nona. |
| Unidade e fonte | Segundos; registros brutos das medições utilizadas na M7. |
| Coleta | Calcular o percentil para cada fluxo, guardando as durações ordenadas e o posto empregado. Não juntar medições de telas ou condições diferentes. |
| Quantidade mínima | Dez durações válidas por fluxo. |
| Tratamento das falhas | Tempos de operações que não terminaram serão reportados como timeouts, fora da lista de durações concluídas. |
| Interpretação | Quanto menor, melhor; escala específica M8. **H8 exige P90 ≤ 5 s em todos os fluxos avaliados**. |

Com amostras pequenas, o percentil 90 pode variar bastante por causa de poucas observações. Por essa razão, seu resultado deverá ser discutido junto da mediana e da ocorrência de timeouts.

## Registro dos resultados

Para cada métrica, serão mantidos os valores necessários ao recálculo: numerador e denominador dos percentuais ou lista das durações de tempo, além da funcionalidade, data, ambiente, exclusões e evidências correspondentes. Quando não houver dados suficientes, o registro ficará como **inconclusivo**, em vez de receber nota zero. Os procedimentos são complementados pelo [protocolo de coleta](protocolo-coleta.md) e as regras de síntese por [critérios de julgamento](criterios-julgamento.md).
