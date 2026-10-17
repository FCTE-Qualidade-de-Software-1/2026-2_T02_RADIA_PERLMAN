---
hide:
  - toc
---

# Questões e hipóteses

Para detalhar os quatro objetivos GQM, formulamos oito questões de avaliação. Cada uma possui uma hipótese com o resultado esperado, definida antes da coleta. Os limites numéricos são critérios adotados para este estudo e precisam ter sua justificativa registrada; não foram estabelecidos pela ISO/IEC 25010 nem pela Neoenergia.

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

Para analisar a apreensibilidade, acompanharemos tarefas de localização de serviços, como segunda via de fatura ou histórico de consumo, com participantes que não utilizaram a plataforma recentemente. Contaremos como sucesso a chegada à tela estabelecida, sem ajuda e na primeira tentativa. A proporção será calculada pela [M1](metricas.md#m1).

### Q2 — Os formulários ajudam a corrigir entradas inválidas? { #q2 }

Nos formulários acessíveis, vamos observar como a interface responde a entradas inválidas. Para considerar a resposta adequada, não basta impedir o avanço: é necessário que o usuário receba uma orientação compreensível sobre o erro. A frequência desses casos será expressa pela [M2](metricas.md#m2).

## G2 — Confiabilidade

### Q3 — Com que frequência os fluxos são concluídos sem falhas visíveis? { #q3 }

Vamos repetir os fluxos previstos e registrar travamentos, telas em branco ou erros inesperados. Calcularemos a [M3](metricas.md#m3) para cada fluxo; H3 exige pelo menos 80% de execuções sem falhas em todos aqueles que tiverem dados suficientes. A apresentação individual dos resultados permitirá identificar em quais funcionalidades ocorreram problemas.

### Q4 — É possível continuar a navegação após uma perda breve de conexão? { #q4 }

Durante uma consulta de leitura, interromperemos brevemente a conexão do dispositivo utilizado no teste. Em seguida, verificaremos se a navegação pode continuar sem retornar ao início. A [M4](metricas.md#m4) registrará essa recuperação, considerando que o comportamento observado também depende da rede local e do navegador.

## G3 — Segurança

### Q5 — Páginas restritas permanecem protegidas depois do logout? { #q5 }

Vamos acessar uma página restrita com uma conta autorizada, encerrar a sessão e tentar abrir novamente a mesma área. A [M5](metricas.md#m5) será favorável apenas quando todas as verificações bloquearem o acesso a conteúdo protegido. Qualquer exposição efetiva será registrada como ocorrência crítica.

### Q6 — Informações estáveis permanecem iguais em consultas consecutivas? { #q6 }

Na [M6](metricas.md#m6), compararemos campos de uma mesma fatura ou de um mesmo período histórico em consultas próximas, sem modificar os dados. O resultado mostrará se houve divergência na apresentação das informações; não permitirá avaliar os mecanismos internos que impedem alterações indevidas.

## G4 — Eficiência de desempenho

### Q7 — Quanto tempo, normalmente, cada fluxo leva para ficar utilizável? { #q7 }

Mediremos o intervalo entre o acionamento de uma função e o momento em que seu conteúdo principal estiver disponível para uso. A mediana dessas observações, calculada para cada fluxo, corresponde à [M7](metricas.md#m7).

### Q8 — Qual é o comportamento das respostas mais demoradas? { #q8 }

Também calcularemos o percentil 90, a [M8](metricas.md#m8), a partir dos mesmos tempos registrados para M7. Assim, poderemos discutir as respostas mais demoradas sem misturá-las ao tempo típico de cada fluxo.

## Interpretação das hipóteses

Consideraremos uma hipótese **sustentada** quando a métrica correspondente atingir o limite previsto com dados suficientes. Se o resultado ficar abaixo desse limite, a hipótese será **não sustentada**. Na falta de acesso ou de observações válidas, registraremos a situação como **inconclusiva**. As conclusões serão acompanhadas dos valores calculados, das exclusões e das condições dos testes, conforme os [critérios de julgamento](criterios-julgamento.md).
