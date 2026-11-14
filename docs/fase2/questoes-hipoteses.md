# Questões e hipóteses

Para detalhar os quatro objetivos GQM, formulamos quatorze questões de avaliação. Cada uma possui uma hipótese com o resultado esperado, definida antes da coleta. Os limites numéricos são critérios adotados para este estudo e precisam ter sua justificativa registrada; não foram estabelecidos pela ISO/IEC 25010 nem pela Neoenergia.


**Tabela 1 —** Questões, hipóteses e métricas por objetivo


| Objetivo | Subcaracterística | Questão | Hipótese | Métrica |
|---|---|---|---|---|
| [G1](objetivos.md#g1) | Apreensibilidade | [Q1 — Localização de funções](#q1) | **H1:** ao menos 80% das tarefas de localização serão concluídas na primeira tentativa e sem ajuda. | [M1](metricas.md#m1) |
| [G1](objetivos.md#g1) | Proteção contra erros | [Q2 — Erros de preenchimento](#q2) | **H2:** ao menos 80% das entradas inválidas serão sinalizadas antes do envio, com orientação para a correção. | [M2](metricas.md#m2) |
| [G1](objetivos.md#g1) | Reconhecimento da adequação | [Q9 — Reconhecimento da adequação](#q9) | **H9:** ao menos 80% das telas apresentadas terão sua finalidade reconhecida corretamente. | [M9](metricas.md#m9) |
| [G1](objetivos.md#g1) | Operabilidade | [Q10 — Operação das funções](#q10) | **H10:** ao menos 80% das tarefas de operação serão concluídas sem erro e sem ajuda. | [M10](metricas.md#m10) |
| [G2](objetivos.md#g2) | Maturidade | [Q3 — Falhas observáveis](#q3) | **H3:** cada fluxo do histórico de consumo apresentará ao menos 80% de execuções sem falha observável. | [M3](metricas.md#m3) |
| [G2](objetivos.md#g2) | Disponibilidade | [Q11 — Disponibilidade das funções](#q11) | **H11:** a 2ª via e o Nada Consta estarão operacionais em ao menos 95% das verificações agendadas, cada um. | [M11](metricas.md#m11) |
| [G2](objetivos.md#g2) | Tolerância a falhas / Recuperabilidade | [Q4 — Retomada e recuperação](#q4) | **H4:** ao menos 80% das interrupções locais permitirão retomar o fluxo e restabelecer o estado anterior. | [M4](metricas.md#m4) |
| [G3](objetivos.md#g3) | Confidencialidade | [Q5 — Proteção de acesso](#q5) | **H5:** 100% das verificações sem sessão ativa impedirão o acesso utilizável a dados protegidos. | [M5](metricas.md#m5) |
| [G3](objetivos.md#g3) | Integridade / Não repúdio | [Q6 — Consistência de dados](#q6) | **H6:** ao menos 95% das comparações de campos estáveis do Nada Consta serão consistentes. | [M6](metricas.md#m6) |
| [G3](objetivos.md#g3) | Integridade / Não repúdio | [Q13 — Comprovação do documento](#q13) | **H13:** 100% dos relatórios de Nada Consta emitidos terão autenticidade verificável. | [M13](metricas.md#m13) |
| [G3](objetivos.md#g3) | Autenticidade e Responsabilização | [Q12 — Autenticação e rastreabilidade](#q12) | **H12:** ao menos 80% dos itens de verificação de autenticidade e responsabilização serão atendidos. | [M12](metricas.md#m12) |
| [G4](objetivos.md#g4) | Comportamento temporal | [Q7 — Tempo típico de resposta](#q7) | **H7:** a mediana do tempo de resposta será de até 3 segundos em cada fluxo avaliado. | [M7](metricas.md#m7) |
| [G4](objetivos.md#g4) | Comportamento temporal | [Q8 — Respostas mais lentas](#q8) | **H8:** o percentil 90 do tempo de resposta será de até 5 segundos em cada fluxo avaliado. | [M8](metricas.md#m8) |
| [G4](objetivos.md#g4) | Capacidade | [Q14 — Desempenho em horário de pico](#q14) | **H14:** a mediana no pico será no máximo 1,5 vez a mediana fora do pico em cada fluxo avaliado. | [M14](metricas.md#m14) |
 
_Fonte: Equipe Radia Perlman, 2026._

## G1 — Usabilidade

### Q1 — Os usuários conseguem localizar as funções sem auxílio? { #q1 }

Para analisar a apreensibilidade, acompanharemos tarefas de localização de serviços, como segunda via de fatura ou histórico de consumo, com participantes que não utilizaram a plataforma recentemente. Contaremos como sucesso a chegada à tela estabelecida, sem ajuda e na primeira tentativa. A proporção será calculada pela [M1](metricas.md#m1).

### Q2 — Os formulários ajudam a corrigir entradas inválidas? { #q2 }

Nos formulários de login e de cadastro, vamos observar como a interface responde a entradas inválidas. Para considerar a resposta adequada, não basta impedir o avanço: é necessário que o usuário receba uma orientação compreensível sobre o erro. A frequência desses casos será expressa pela [M2](metricas.md#m2).

### Q9 — Os usuários reconhecem de imediato se a tela atende à sua necessidade de informação? { #q9 }
 
Para analisar o reconhecimento da adequação, apresentaremos aos participantes as telas do relatório de Nada Consta e dos indicadores de continuidade e verificaremos se eles identificam corretamente para que cada tela serve. A proporção de reconhecimentos corretos será calculada pela [M9](metricas.md#m9).

### Q10 — Os usuários conseguem operar as funções até o resultado esperado sem erro e sem ajuda? { #q10 }
 
Para analisar a operabilidade, os participantes executarão a emissão de 2ª via e a alteração do período do gráfico de consumo, a partir da tela de cada função. Registraremos se a tarefa foi concluída sem erro de operação e sem ajuda. A proporção será calculada pela [M10](metricas.md#m10).

## G2 — Confiabilidade

### Q3 — Com que frequência os fluxos são concluídos sem falhas visíveis? { #q3 }

Vamos repetir os fluxos previstos do histórico de consumo e registrar travamentos, telas em branco ou erros inesperados. Calcularemos a [M3](metricas.md#m3) para cada fluxo; H3 exige pelo menos 80% de execuções sem falhas em todos aqueles que tiverem dados suficientes. A apresentação individual dos resultados permitirá identificar em quais fluxos ocorreram problemas.

### Q4 — É possível continuar a navegação após uma perda breve de conexão? { #q4 }

Durante uma consulta de leitura, interromperemos brevemente a conexão do dispositivo utilizado no teste. Em seguida, verificaremos se a navegação pode continuar sem retornar ao início. A [M4](metricas.md#m4) registrará essa recuperação, considerando que o comportamento observado também depende da rede local e do navegador.

### Q11 — A 2ª via e o Nada Consta estão acessíveis quando o usuário precisa deles? { #q11 }
 
Faremos verificações agendadas, em diferentes dias e horários, para registrar se a emissão de 2ª via e o relatório de Nada Consta estão operacionais. A proporção de verificações bem-sucedidas, calculada por função, corresponde à [M11](metricas.md#m11).

## G3 — Segurança

### Q5 — Páginas restritas permanecem protegidas depois do logout? { #q5 }

Vamos acessar uma página restrita com uma conta autorizada, encerrar a sessão e tentar abrir novamente a mesma área. A [M5](metricas.md#m5) será favorável apenas quando todas as verificações bloquearem o acesso a conteúdo protegido. Qualquer exposição efetiva será registrada como ocorrência crítica.

### Q6 — Informações estáveis permanecem iguais em consultas consecutivas? { #q6 }

Na [M6](metricas.md#m6), compararemos campos de uma mesma fatura ou de um mesmo período histórico em consultas próximas, sem modificar os dados. O resultado mostrará se houve divergência na apresentação das informações; não permitirá avaliar os mecanismos internos que impedem alterações indevidas.

### Q13 — O relatório de Nada Consta pode ter sua autenticidade e sua emissão comprovadas? { #q13 }
 
Emitiremos o relatório de Nada Consta e verificaremos se ele possui um mecanismo que permita comprovar sua autenticidade e sua emissão (por exemplo, código de autenticação, QR code ou assinatura digital) e se esse mecanismo confirma o documento quando utilizado. A proporção será calculada pela [M13](metricas.md#m13).

### Q12 — O sistema comprova a identidade do usuário e associa as ações a ele? { #q12 }
 
Verificaremos no login e no cadastro um conjunto de itens observáveis pelo usuário comum: rejeição de credenciais inválidas, mensagens de erro que não revelam qual credencial está incorreta, expiração da sessão por inatividade, exigência de comprovação de identidade no cadastro, registro ou aviso de acesso e associação das emissões ao titular. A proporção de itens atendidos será calculada pela [M12](metricas.md#m12).

## G4 — Eficiência de desempenho

### Q7 — Quanto tempo, normalmente, cada fluxo leva para ficar utilizável? { #q7 }

Mediremos o intervalo entre o acionamento de uma função e o momento em que seu conteúdo principal estiver disponível para uso. A mediana dessas observações, calculada para cada fluxo, corresponde à [M7](metricas.md#m7).

### Q8 — Qual é o comportamento das respostas mais demoradas? { #q8 }

Também calcularemos o percentil 90, a [M8](metricas.md#m8), a partir dos mesmos tempos registrados para M7. Assim, poderemos discutir as respostas mais demoradas sem misturá-las ao tempo típico de cada fluxo.

### Q14 — A geração de PDF e de gráficos se mantém aceitável no horário de pico? { #q14 }
 
Mediremos o tempo de geração do PDF da 2ª via e de renderização dos gráficos do histórico de consumo em janelas de pico natural de uso e fora delas. A razão entre as medianas dos dois períodos, calculada por fluxo, corresponde à [M14](metricas.md#m14). Não geraremos carga artificial, conforme explicado em [G4](objetivos.md#g4).

## Interpretação das hipóteses

Consideraremos uma hipótese **sustentada** quando a métrica correspondente atingir o limite previsto com dados suficientes. Se o resultado ficar abaixo desse limite, a hipótese será **não sustentada**. Na falta de acesso ou de observações válidas, registraremos a situação como **inconclusiva**. As conclusões serão acompanhadas dos valores calculados, das exclusões e das condições dos testes, conforme os [critérios de julgamento](criterios-julgamento.md).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 14/10/2026 | Criação do documento das questões e hipóteses | Beatriz Figueiredo dos Santos |
| 1.1 | 17/10/2026 | Reestruturação do documento | Arthur de Lima Sobreira |
| 1.2 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |
| 1.3 | 13/11/2026 | Inclusão de Q9–Q14 e H9–H14; ampliação de Q4; funcionalidades conforme a Fase 1 | Beatriz Figueiredo dos Santos |