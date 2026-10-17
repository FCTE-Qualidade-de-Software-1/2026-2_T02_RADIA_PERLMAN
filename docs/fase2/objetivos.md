---
hide:
  - toc
---

# Objetivos de medição

A Fase 1 delimitou a avaliação à Agência Virtual da Neoenergia Brasília e a cinco funcionalidades: login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. A finalidade do estudo é apontar oportunidades de melhoria a partir de situações de uso. Para isso, adotamos quatro características da ISO/IEC 25010:2011: usabilidade (ênfase 5), confiabilidade (4), segurança (5) e eficiência de desempenho (4).

Os objetivos a seguir foram formulados pelo método *Goal–Question–Metric* (GQM). Em cada um, identificamos o objeto, o propósito, o aspecto de qualidade, o ponto de vista e o contexto da medição. O estudo considera o uso do sistema pela interface web; não depende de acesso ao código-fonte ou à infraestrutura da concessionária.

## G1 — Usabilidade { #g1 }

A Agência Virtual atende consumidores com diferentes níveis de familiaridade com serviços digitais. Nosso primeiro objetivo é verificar se alguém que conhece pouco a plataforma consegue encontrar as funções necessárias e se os formulários ajudam a corrigir erros de preenchimento.

**Objetivo de medição:** analisar a interface da Agência Virtual da Neoenergia Brasília para identificar dificuldades de aprendizagem e de prevenção de erros, sob a perspectiva dos usuários finais, em tarefas de navegação e preenchimento que não alterem informações da conta.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Interfaces das cinco funcionalidades selecionadas na Fase 1. |
| Propósito | Identificar dificuldades de navegação e oportunidades de melhoria nos formulários. |
| Foco | Apreensibilidade e proteção contra erros do usuário. |
| Ponto de vista | Consumidores, com observações registradas pela equipe avaliadora. |
| Contexto | Tarefas realizadas por participantes voluntários e verificação de campos com entradas inválidas, em etapas seguras da navegação. |
| Relação com a Fase 1 | Usabilidade, ênfase 5. |

O objetivo se desdobra em [Q1](questoes-hipoteses.md#q1), sobre localização de funções, e [Q2](questoes-hipoteses.md#q2), sobre tratamento de erros de preenchimento.

## G2 — Confiabilidade { #g2 }

Para observar a estabilidade do serviço, cada fluxo de consulta ou navegação será repetido e analisado separadamente. Também será verificado o comportamento da interface quando o dispositivo de teste perde a conexão por alguns segundos, observando se a atividade pode ser retomada sem reiniciar todo o caminho.

**Objetivo de medição:** examinar os fluxos selecionados da Agência Virtual para identificar falhas perceptíveis e dificuldades de recuperação, considerando a maturidade e a tolerância a falhas, do ponto de vista dos usuários e da equipe avaliadora, em consultas realizadas sob condições registradas.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Fluxos de navegação e consulta contemplados no escopo. |
| Propósito | Medir falhas observáveis durante o uso e a retomada após uma interrupção local de rede. |
| Foco | Maturidade e tolerância a falhas. |
| Ponto de vista | Usuários finais e equipe de avaliação. |
| Contexto | Execuções repetidas de tarefas de leitura e, quando viável, desconexão temporária apenas do dispositivo utilizado nos testes. |
| Relação com a Fase 1 | Confiabilidade, ênfase 4. |

[Q3](questoes-hipoteses.md#q3) aborda a ocorrência de falhas em condições normais, com um resultado para cada fluxo; [Q4](questoes-hipoteses.md#q4) trata da retomada da navegação. A segunda questão observa a experiência no cliente e não mede, isoladamente, a recuperação dos servidores da Neoenergia.

## G3 — Segurança { #g3 }

Os serviços escolhidos envolvem faturas e outras informações do consumidor. A avaliação de segurança se concentrará em duas situações verificáveis pela interface: o acesso a áreas restritas depois do encerramento da sessão e a consistência de dados que deveriam permanecer iguais entre consultas próximas.

**Objetivo de medição:** avaliar os controles de acesso e a consistência das informações apresentadas pela Agência Virtual, buscando possíveis problemas de confidencialidade e indícios externos relacionados à integridade, sob a perspectiva de usuários com acesso legítimo às contas consultadas.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Páginas restritas e campos de registros estáveis exibidos em consultas autorizadas. |
| Propósito | Verificar a proteção das páginas e identificar divergências não justificadas entre consultas equivalentes. |
| Foco | Confidencialidade e integridade, esta última investigada indiretamente. |
| Ponto de vista | Usuários finais e equipe de avaliação, utilizando contas próprias ou autorizadas. |
| Contexto | Navegação autenticada, encerramento de sessão e repetição de consultas da mesma referência, sem alteração dos registros. |
| Relação com a Fase 1 | Segurança, ênfase 5. |

O controle de acesso será observado em [Q5](questoes-hipoteses.md#q5). A [Q6](questoes-hipoteses.md#q6) verifica consistência de apresentação: mesmo que não ocorram divergências, isso não permite concluir que o banco de dados esteja protegido contra alterações indevidas. A delimitação é retomada na [rastreabilidade](rastreabilidade.md).

## G4 — Eficiência de desempenho { #g4 }

O tempo de espera também interfere no uso de serviços como segunda via e histórico de consumo. Além do tempo típico de carregamento, interessa observar as respostas mais demoradas, que podem não aparecer quando se analisa somente a média ou a mediana.

**Objetivo de medição:** medir o tempo de resposta dos fluxos selecionados da Agência Virtual para localizar possíveis problemas de desempenho percebido pelos usuários, em execuções repetidas com navegador, dispositivo e conexão documentados.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Apresentação das telas e consultas disponíveis nas funcionalidades selecionadas. |
| Propósito | Identificar fluxos com respostas demoradas. |
| Foco | Eficiência de desempenho — comportamento no tempo. |
| Ponto de vista | Consumidores e equipe avaliadora. |
| Contexto | Repetições por fluxo, com critérios constantes para início e fim da medição. |
| Relação com a Fase 1 | Eficiência de desempenho, ênfase 4. |

A mediana do tempo de resposta corresponde à [Q7](questoes-hipoteses.md#q7), enquanto o percentil 90 é utilizado na [Q8](questoes-hipoteses.md#q8). Quando a etapa final de uma funcionalidade não puder ser executada, a medição ficará restrita ao trecho efetivamente percorrido.

## Desdobramento dos objetivos

As [questões e hipóteses](questoes-hipoteses.md) detalham o que será investigado. As medidas e seus limites constam em [Métricas](metricas.md), e os procedimentos de registro estão no [Protocolo de coleta](protocolo-coleta.md). A correspondência com as prioridades e funcionalidades da Fase 1 está na [matriz de rastreabilidade](rastreabilidade.md).
