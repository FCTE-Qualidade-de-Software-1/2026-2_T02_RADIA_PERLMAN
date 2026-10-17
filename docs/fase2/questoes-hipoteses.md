---
hide:
  - toc
---

# Questões e hipóteses

Cada objetivo GQM foi dividido em duas questões, totalizando oito perguntas de avaliação. As hipóteses estabelecem, antes da coleta, o resultado esperado para cada uma delas. Os limites numéricos serão usados como referência neste estudo acadêmico; sua escolha deve ser justificada pela equipe e não corresponde a uma exigência da ISO/IEC 25010 ou a um compromisso de desempenho da Neoenergia.

| Objetivo | Questão | Hipótese | Métrica |
|---|---|---|---|
| [G1](objetivos.md#g1) | [Q1 — Localização de funções](#q1) | **H1:** ao menos 80% das tarefas serão concluídas na primeira tentativa e sem ajuda. | [M1](metricas.md#m1) |
| [G1](objetivos.md#g1) | [Q2 — Erros de entrada](#q2) | **H2:** ao menos 80% das entradas inválidas receberão tratamento e orientação adequados. | [M2](metricas.md#m2) |
| [G2](objetivos.md#g2) | [Q3 — Falhas de execução](#q3) | **H3:** cada fluxo elegível apresentará ao menos 80% de execuções sem falha observável. | [M3](metricas.md#m3) |
| [G2](objetivos.md#g2) | [Q4 — Retomada da navegação](#q4) | **H4:** ao menos 80% das interrupções locais permitirão retomar o fluxo. | [M4](metricas.md#m4) |
| [G3](objetivos.md#g3) | [Q5 — Proteção de acesso](#q5) | **H5:** 100% das verificações sem sessão ativa impedirão acesso utilizável a dados protegidos. | [M5](metricas.md#m5) |
| [G3](objetivos.md#g3) | [Q6 — Consistência de dados](#q6) | **H6:** ao menos 95% das comparações de campos estáveis serão consistentes. | [M6](metricas.md#m6) |
| [G4](objetivos.md#g4) | [Q7 — Tempo típico](#q7) | **H7:** a mediana será de até 3 segundos em cada fluxo avaliado. | [M7](metricas.md#m7) |
| [G4](objetivos.md#g4) | [Q8 — Operações mais lentas](#q8) | **H8:** o percentil 90 será de até 5 segundos em cada fluxo avaliado. | [M8](metricas.md#m8) |

## G1 — Usabilidade

### Q1 — Os usuários conseguem localizar as funções sem auxílio? { #q1 }

Apreensibilidade será observada em tarefas curtas de localização de serviços. Participantes sem experiência recente com a Agência Virtual deverão encontrar, por exemplo, a segunda via de fatura ou o histórico de consumo. O registro considera somente a primeira tentativa e a chegada à tela definida para cada tarefa. A [M1](metricas.md#m1) indica a proporção de sucessos.

### Q2 — Os formulários ajudam a corrigir entradas inválidas? { #q2 }

Serão utilizados preenchimentos incorretos que possam ser testados com segurança. Não basta que a interface bloqueie o avanço: a mensagem também deve informar o problema de forma compreensível. A [M2](metricas.md#m2) mede quantas tentativas atendem a esses dois critérios.

## G2 — Confiabilidade

### Q3 — Com que frequência os fluxos são concluídos sem falhas visíveis? { #q3 }

Cada fluxo de navegação será repetido em condições definidas, com registro de travamentos, telas em branco e erros inesperados. A [M3](metricas.md#m3) será calculada separadamente por fluxo; H3 exige pelo menos 80% de execuções sem falhas em todos os fluxos elegíveis. Os resultados individuais serão mantidos para identificar problemas restritos a uma funcionalidade.

### Q4 — É possível continuar a navegação após uma perda breve de conexão? { #q4 }

A conexão será interrompida apenas no dispositivo de teste, durante atividades de leitura. O objetivo é observar se o usuário consegue voltar à etapa anterior sem recomeçar toda a jornada. O resultado será registrado na [M4](metricas.md#m4), sem atribuir à infraestrutura do serviço problemas que possam ser causados pelo navegador ou pela rede local.

## G3 — Segurança

### Q5 — Páginas restritas permanecem protegidas depois do logout? { #q5 }

Após acessar legitimamente uma página da conta, será encerrada a sessão. A equipe verificará se o conteúdo protegido permanece indisponível sem autenticação. A [M5](metricas.md#m5) só terá resultado favorável com bloqueio em todas as verificações válidas; uma exposição efetiva será classificada como insatisfatória e registrada como ocorrência crítica.

### Q6 — Informações estáveis permanecem iguais em consultas consecutivas? { #q6 }

Campos referentes à mesma fatura ou ao mesmo período histórico serão comparados sem que haja alteração voluntária de dados. A [M6](metricas.md#m6) registra a consistência dessas informações. Como se trata de observação da interface, a questão não abrange a proteção interna contra modificações não autorizadas.

## G4 — Eficiência de desempenho

### Q7 — Quanto tempo, normalmente, cada fluxo leva para ficar utilizável? { #q7 }

Será medido o intervalo entre o comando inicial e a disponibilidade do conteúdo principal. A [M7](metricas.md#m7) utiliza a mediana das repetições, calculada individualmente para cada fluxo.

### Q8 — Qual é o comportamento das respostas mais demoradas? { #q8 }

Com as mesmas observações de tempo, será calculado o percentil 90 ([M8](metricas.md#m8)). Essa segunda medida permite identificar lentidões ocasionais que poderiam passar despercebidas na análise do tempo típico.

## Interpretação das hipóteses

Uma hipótese será considerada **sustentada** quando a métrica atingir seu limite e houver dados suficientes para o cálculo. Caso o limite não seja alcançado, ela será **não sustentada**. Se faltar acesso, autorização ou número mínimo de observações, o resultado será **inconclusivo**. A quantidade de registros, as exclusões e as condições de execução deverão acompanhar as conclusões, de acordo com os [critérios de julgamento](criterios-julgamento.md).
