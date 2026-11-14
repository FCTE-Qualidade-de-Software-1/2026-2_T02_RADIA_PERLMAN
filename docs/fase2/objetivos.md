# Objetivos de medição

Na [Fase 1](../fase1-requisitos.md), definimos que a avaliação abrangeria cinco funcionalidades da Agência Virtual da Neoenergia Brasília: login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Selecionamos usabilidade (ênfase 5), confiabilidade (4), segurança (5) e eficiência de desempenho (4), com base na ISO/IEC 25010:2011. Nosso propósito é identificar dificuldades de uso e oportunidades de melhoria nesses serviços.

Para orientar as medições, formulamos quatro objetivos pelo método *Goal–Question–Metric* (GQM). Em cada objetivo, registramos o que será examinado, por qual motivo, sob qual perspectiva e em quais condições. A observação será feita pela interface web, conforme o acesso disponível aos usuários.


**Tabela 1 —** Visão geral dos objetivos de medição
 
| Objetivo | Característica (ênfase) | Subcaracterísticas | Questões | Métricas |
|---|---|---|---|---|
| [G1](#g1) | Usabilidade (5) | Apreensibilidade, proteção contra erros, reconhecimento da adequação, operabilidade | Q1, Q2, Q9, Q10 | M1, M2, M9, M10 |
| [G2](#g2) | Confiabilidade (4) | Maturidade, disponibilidade, tolerância a falhas / recuperabilidade | Q3, Q4, Q11 | M3, M4, M11 |
| [G3](#g3) | Segurança (5) | Confidencialidade, integridade / não repúdio, autenticidade e responsabilização | Q5, Q6, Q12, Q13 | M5, M6, M12, M13 |
| [G4](#g4) | Eficiência de desempenho (4) | Comportamento temporal, capacidade | Q7, Q8, Q14 | M7, M8, M14 |
 
_Fonte: Equipe Radia Perlman, 2026._

## G1 — Usabilidade { #g1 }

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Interfaces das cinco funcionalidades selecionadas na Fase 1. |
| Propósito | Identificar dificuldades de navegação e oportunidades de melhoria nos formulários. |
| Foco | Apreensibilidade e proteção contra erros do usuário. |
| Ponto de vista | Usuários finais. |
| Contexto | Tarefas realizadas por participantes voluntários e verificação de campos com entradas inválidas, em etapas seguras da navegação. |
| Relação com a Fase 1 | Usabilidade, ênfase 5. |

**Objetivo de medição:** analisar a interface da Agência Virtual da Neoenergia Brasília para identificar dificuldades de aprendizagem e de prevenção de erros, sob a perspectiva dos usuários finais, em tarefas de navegação e preenchimento que não alterem informações da conta.

O objetivo se desdobra em [Q1](questoes-hipoteses.md#q1)(localização de funções), [Q2](questoes-hipoteses.md#q2) (erros de preenchimento), [Q9](questoes-hipoteses.md#q9) (reconhecimento da adequação) e [Q10](questoes-hipoteses.md#q10) (operação das funções).

## G2 — Confiabilidade { #g2 }

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Fluxos de navegação e consulta contemplados no escopo. |
| Propósito | Medir falhas observáveis durante o uso e a retomada após uma interrupção local de rede. |
| Foco | Maturidade e tolerância a falhas. |
| Ponto de vista | Usuários finais. |
| Contexto | Execuções repetidas de tarefas de leitura e, quando viável, desconexão temporária apenas do dispositivo utilizado nos testes. |
| Relação com a Fase 1 | Confiabilidade, ênfase 4. |

**Objetivo de medição:** analisar os fluxos de navegação e consulta da Agência Virtual quanto à ocorrência de falhas e à retomada de atividades após interrupções locais, considerando a experiência do usuário e os registros obtidos durante os testes.

[Q3](questoes-hipoteses.md#q3) aborda a ocorrência de falhas em condições normais, [Q11](questoes-hipoteses.md#q11) trata da disponibilidade e [Q4](questoes-hipoteses.md#q4) da retomada e recuperação após interrupção. Os resultados de Q4 descrevem o comportamento observado no cliente e não medem, isoladamente, a recuperação dos servidores da Neoenergia.

## G3 — Segurança { #g3 }

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Páginas restritas. |
| Propósito | Verificar a proteção das páginas e identificar divergências não justificadas entre consultas equivalentes. |
| Foco | Confidencialidade e integridade, esta última investigada indiretamente. |
| Ponto de vista | Usuários finais. |
| Contexto | Navegação autenticada, encerramento de sessão e repetição de consultas da mesma referência, sem alteração dos registros. |
| Relação com a Fase 1 | Segurança, ênfase 5. |

**Objetivo de medição:** examinar o acesso a páginas restritas e a consistência das informações exibidas pela Agência Virtual, com foco na confidencialidade e em indícios externos de integridade, em consultas realizadas por usuários autorizados.

O objetivo se desdobra em [Q12](questoes-hipoteses.md#q12) (autenticação e rastreabilidade), [Q5](questoes-hipoteses.md#q5) (proteção de acesso), [Q6](questoes-hipoteses.md#q6) (consistência de dados) e [Q13](questoes-hipoteses.md#q13) (comprovação do documento). A consistência observada em Q6 não permite concluir que o armazenamento esteja protegido contra alterações indevidas; essa delimitação é retomada na [rastreabilidade](rastreabilidade.md).

## G4 — Eficiência de desempenho { #g4 }

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Apresentação das telas e consultas disponíveis nas funcionalidades selecionadas. |
| Propósito | Identificar fluxos com respostas demoradas. |
| Foco | Eficiência de desempenho — comportamento no tempo. |
| Ponto de vista | Usuários finais. |
| Contexto | Repetições por fluxo, com critérios constantes para início e fim da medição. |
| Relação com a Fase 1 | Eficiência de desempenho, ênfase 4. |

**Objetivo de medição:** medir o tempo de resposta dos fluxos selecionados da Agência Virtual para localizar possíveis problemas de desempenho percebido pelos usuários, em execuções repetidas com navegador, dispositivo e conexão documentados.

A mediana do tempo de resposta corresponde à [Q7](questoes-hipoteses.md#q7), enquanto o percentil 90 é utilizado na [Q8](questoes-hipoteses.md#q8) e a comparação entre pico e fora de pico à [Q14](questoes-hipoteses.md#q14). Quando a etapa final de uma funcionalidade não puder ser executada, a medição ficará restrita ao trecho efetivamente percorrido.

## Desdobramento dos objetivos

As [questões e hipóteses](questoes-hipoteses.md) detalham o que será investigado. As medidas e seus limites constam em [Métricas](metricas.md), e os procedimentos de registro estão no [Protocolo de coleta](protocolo-coleta.md). A correspondência com as prioridades e funcionalidades da Fase 1 está na [matriz de rastreabilidade](rastreabilidade.md).

## Referências
 
* BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Nova York: John Wiley & Sons, 1994.
* ISO/IEC. *ISO/IEC 25010:2011 — Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. Genebra: ISO, 2011.
* SILVA, C. V. P. da; MOURA, D. C. de; CAMPOS, D. de C.; NERY, P. *GQM – Goal-Question-Metric*. 2009.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 14/10/2026 | Criação do documento dos objetivos | Beatriz Figueiredo dos Santos |
| 1.1 | 17/10/2026 | Reestruturação do documento | Arthur de Lima Sobreira |
| 1.2 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |
| 1.3 | 13/11/2026 | Alinhamento à Fase 1: inclusão de todas as subcaracterísticas do modelo adaptado, funcionalidades conforme os procedimentos da Fase 1 e objetivos no template GQM | Beatriz Figueiredo dos Santos |