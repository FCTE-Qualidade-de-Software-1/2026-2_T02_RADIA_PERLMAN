---
hide:
  - toc
---

# Objetivos de medição

Na Fase 1, definimos que a avaliação abrangeria cinco funcionalidades da Agência Virtual da Neoenergia Brasília: login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Selecionamos usabilidade (ênfase 5), confiabilidade (4), segurança (5) e eficiência de desempenho (4), com base na ISO/IEC 25010:2011. Nosso propósito é identificar dificuldades de uso e oportunidades de melhoria nesses serviços.

Para orientar as medições, formulamos quatro objetivos pelo método *Goal–Question–Metric* (GQM). Em cada objetivo, registramos o que será examinado, por qual motivo, sob qual perspectiva e em quais condições. A observação será feita pela interface web, conforme o acesso disponível aos usuários.

## G1 — Usabilidade { #g1 }

Como a Agência Virtual é utilizada por consumidores com diferentes níveis de familiaridade digital, queremos verificar duas situações: a facilidade para encontrar um serviço pela primeira vez e a orientação oferecida quando um formulário é preenchido incorretamente.

**Objetivo de medição:** analisar a interface da Agência Virtual da Neoenergia Brasília para identificar dificuldades de aprendizagem e de prevenção de erros, sob a perspectiva dos usuários finais, em tarefas de navegação e preenchimento que não alterem informações da conta.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Interfaces das cinco funcionalidades selecionadas na Fase 1. |
| Propósito | Identificar dificuldades de navegação e oportunidades de melhoria nos formulários. |
| Foco | Apreensibilidade e proteção contra erros do usuário. |
| Ponto de vista | Usuários finais, com acompanhamento dos avaliadores durante as tarefas. |
| Contexto | Tarefas realizadas por participantes voluntários e verificação de campos com entradas inválidas, em etapas seguras da navegação. |
| Relação com a Fase 1 | Usabilidade, ênfase 5. |

O objetivo se desdobra em [Q1](questoes-hipoteses.md#q1), sobre localização de funções, e [Q2](questoes-hipoteses.md#q2), sobre tratamento de erros de preenchimento.

## G2 — Confiabilidade { #g2 }

Na confiabilidade, vamos registrar falhas que ocorram durante a navegação e verificar se é possível retomar uma consulta após uma breve interrupção da conexão local. As execuções de cada fluxo serão analisadas separadamente, para que problemas de uma funcionalidade não desapareçam em uma média geral.

**Objetivo de medição:** analisar os fluxos de navegação e consulta da Agência Virtual quanto à ocorrência de falhas e à retomada de atividades após interrupções locais, considerando a experiência do usuário e os registros obtidos durante os testes.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Fluxos de navegação e consulta contemplados no escopo. |
| Propósito | Medir falhas observáveis durante o uso e a retomada após uma interrupção local de rede. |
| Foco | Maturidade e tolerância a falhas. |
| Ponto de vista | Usuários finais e responsáveis pela avaliação. |
| Contexto | Execuções repetidas de tarefas de leitura e, quando viável, desconexão temporária apenas do dispositivo utilizado nos testes. |
| Relação com a Fase 1 | Confiabilidade, ênfase 4. |

[Q3](questoes-hipoteses.md#q3) aborda a ocorrência de falhas em condições normais, com um resultado para cada fluxo; [Q4](questoes-hipoteses.md#q4) trata da retomada da navegação. A segunda questão observa a experiência no cliente e não mede, isoladamente, a recuperação dos servidores da Neoenergia.

## G3 — Segurança { #g3 }

Em segurança, o foco estará nas informações acessíveis por uma conta autorizada. Vamos verificar se as páginas restritas permanecem protegidas após o encerramento da sessão e se determinados dados estáveis continuam iguais em consultas consecutivas.

**Objetivo de medição:** examinar o acesso a páginas restritas e a consistência das informações exibidas pela Agência Virtual, com foco na confidencialidade e em indícios externos de integridade, em consultas realizadas por usuários autorizados.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Páginas restritas e campos de registros estáveis exibidos em consultas autorizadas. |
| Propósito | Verificar a proteção das páginas e identificar divergências não justificadas entre consultas equivalentes. |
| Foco | Confidencialidade e integridade, esta última investigada indiretamente. |
| Ponto de vista | Usuários finais e avaliadores, em consultas a contas próprias ou autorizadas. |
| Contexto | Navegação autenticada, encerramento de sessão e repetição de consultas da mesma referência, sem alteração dos registros. |
| Relação com a Fase 1 | Segurança, ênfase 5. |

O controle de acesso será observado em [Q5](questoes-hipoteses.md#q5). A [Q6](questoes-hipoteses.md#q6) verifica consistência de apresentação: mesmo que não ocorram divergências, isso não permite concluir que o banco de dados esteja protegido contra alterações indevidas. A delimitação é retomada na [rastreabilidade](rastreabilidade.md).

## G4 — Eficiência de desempenho { #g4 }

Nas consultas de segunda via e histórico de consumo, por exemplo, o tempo de espera interfere diretamente na experiência de uso. Por isso, vamos medir tanto o tempo típico de resposta quanto as ocorrências mais lentas, que nem sempre aparecem na mediana.

**Objetivo de medição:** medir o tempo de resposta dos fluxos selecionados da Agência Virtual para localizar possíveis problemas de desempenho percebido pelos usuários, em execuções repetidas com navegador, dispositivo e conexão documentados.

| Elemento GQM | Definição no projeto |
|---|---|
| Objeto | Apresentação das telas e consultas disponíveis nas funcionalidades selecionadas. |
| Propósito | Identificar fluxos com respostas demoradas. |
| Foco | Eficiência de desempenho — comportamento no tempo. |
| Ponto de vista | Usuários finais e avaliadores, considerando o tempo de resposta nos fluxos selecionados. |
| Contexto | Repetições por fluxo, com critérios constantes para início e fim da medição. |
| Relação com a Fase 1 | Eficiência de desempenho, ênfase 4. |

A mediana do tempo de resposta corresponde à [Q7](questoes-hipoteses.md#q7), enquanto o percentil 90 é utilizado na [Q8](questoes-hipoteses.md#q8). Quando a etapa final de uma funcionalidade não puder ser executada, a medição ficará restrita ao trecho efetivamente percorrido.

## Desdobramento dos objetivos

As [questões e hipóteses](questoes-hipoteses.md) detalham o que será investigado. As medidas e seus limites constam em [Métricas](metricas.md), e os procedimentos de registro estão no [Protocolo de coleta](protocolo-coleta.md). A correspondência com as prioridades e funcionalidades da Fase 1 está na [matriz de rastreabilidade](rastreabilidade.md).
