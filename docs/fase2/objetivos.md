# Objetivos de medição

Na [Fase 1](../fase1-requisitos.md), definimos que a avaliação abrangeria cinco funcionalidades da Agência Virtual da Neoenergia Brasília: login e cadastro, segunda via de fatura, histórico de consumo, relatório de Nada Consta e indicadores de continuidade. Selecionamos usabilidade (ênfase 5), confiabilidade (4), segurança (5) e eficiência de desempenho (4), com base na ISO/IEC 25010:2011. Nosso propósito é identificar dificuldades de uso e oportunidades de melhoria nesses serviços.

Para orientar as medições, formulamos quatro objetivos pelo método *Goal–Question–Metric* (GQM). Cada objetivo é descrito com o *template* do GQM (BASILI; CALDIERA; ROMBACH, 1994): objeto de análise, propósito, foco de qualidade, ponto de vista e contexto. Em seguida, indicamos as funcionalidades e tarefas observadas, a origem de cada elemento na Fase 1 e o *abstraction sheet* do objetivo. A observação será feita pela interface web, conforme o acesso disponível aos usuários.


**Tabela 1 —** Visão geral dos objetivos de medição
 
| Objetivo | Característica (ênfase) | Subcaracterísticas | Questões | Métricas |
|---|---|---|---|---|
| [G1](#g1) | Usabilidade (5) | Apreensibilidade, proteção contra erros, reconhecimento da adequação, operabilidade | Q1, Q2, Q9, Q10 | M1, M2, M9, M10 |
| [G2](#g2) | Confiabilidade (4) | Maturidade, disponibilidade, tolerância a falhas / recuperabilidade | Q3, Q4, Q11 | M3, M4, M11 |
| [G3](#g3) | Segurança (5) | Confidencialidade, integridade / não repúdio, autenticidade e responsabilização | Q5, Q6, Q12, Q13 | M5, M6, M12, M13 |
| [G4](#g4) | Eficiência de desempenho (4) | Comportamento temporal, capacidade | Q7, Q8, Q14 | M7, M8, M14 |
 
_Fonte: Equipe Radia Perlman, 2026._

## G1 — Usabilidade { #g1 }

| Campo | Descrição |
|---|---|
| **Analisar** | a Agência Virtual da Neoenergia Brasília |
| **Com o propósito de** | avaliar |
| **Com respeito a** | usabilidade: apreensibilidade, proteção contra erros do usuário, reconhecimento da adequação e operabilidade |
| **Do ponto de vista de** | usuários finais: clientes residenciais e corporativos do Distrito Federal, de cidadãos leigos a pessoas com alto conhecimento em informática |
| **No contexto de** | uso da Agência Virtual em produção, pelo navegador web, por cidadãos com níveis muito diferentes de conhecimento em informática, que precisam resolver seus serviços de energia sem auxílio externo. Nos testes, esse contexto é reproduzido com participantes voluntários sem experiência recente com o serviço, que usam a conta autorizada de uma unidade consumidora de Taguatinga, sem ajuda do avaliador e sem alterar informações da conta |
 
**Funcionalidades e tarefas:** login e cadastro (entradas inválidas nos formulários); segunda via de fatura e histórico de consumo (localizar a função, emitir a 2ª via e alterar o período do gráfico); relatório de Nada Consta e indicadores de continuidade (reconhecer a finalidade da tela). A distribuição segue os procedimentos de avaliação do [modelo de qualidade](../fase1/modelo-qualidade.md) da Fase 1.

O objetivo se desdobra em [Q1](questoes-hipoteses.md#q1)(localização de funções), [Q2](questoes-hipoteses.md#q2) (erros de preenchimento), [Q9](questoes-hipoteses.md#q9) (reconhecimento da adequação) e [Q10](questoes-hipoteses.md#q10) (operação das funções).

### Ligação com a Fase 1
 
| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (quatro subcaracterísticas de usabilidade) | Ramo “Usabilidade” do modelo adaptado ([modelo de qualidade](../fase1/modelo-qualidade.md)) |
| Funcionalidades e tarefas | Procedimentos de avaliação: proteção contra erros no Login/Cadastro; operabilidade e apreensibilidade na Emissão de 2ª via e no Histórico de Consumo; reconhecimento da adequação no Relatório de Nada Consta e nos Indicadores de Continuidade |
| Ponto de vista | Parte interessada “usuários finais” ([requisitos de avaliação](../fase1-requisitos.md)) e perfil dos usuários ([produto avaliado](../fase1/produto-avaliado.md)) |
| Contexto (uso sem auxílio, conhecimento heterogêneo, navegador, conta de Taguatinga) | Justificativa da ênfase da usabilidade; interfaces e dependências; ambiente e massa de dados |
| Propósito (avaliar) | Propósito da avaliação: identificar pontos de melhoria do portal |
| Prioridade | Ênfase 5 (máxima) na seleção e priorização das características |
| ODS | ODS 7 (usabilidade no Login e na 2ª via), ODS 12 (apreensibilidade no Histórico de Consumo) e ODS 16 (reconhecimento da adequação no Nada Consta e nos Indicadores de Continuidade), conforme o [alinhamento aos ODS](../fase1/alinhamento-ods.md) |
 
### Abstraction sheet
 
| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Agência Virtual (5 funcionalidades) | Avaliar | Usabilidade (quatro subcaracterísticas) | Usuários finais |

## G2 — Confiabilidade { #g2 }

| Campo | Descrição |
|---|---|
| **Analisar** | a Agência Virtual da Neoenergia Brasília |
| **Com o propósito de** | avaliar |
| **Com respeito a** | confiabilidade: maturidade, disponibilidade e tolerância a falhas / recuperabilidade |
| **Do ponto de vista de** | usuários finais: clientes residenciais e corporativos do Distrito Federal |
| **No contexto de** | uso da Agência Virtual em produção, em dias e horários variados, por clientes que precisam pagar contas no prazo e comprovar adimplência, com conexões sujeitas a quedas breves. Nos testes, esse contexto é reproduzido por execuções repetidas dos fluxos do histórico de consumo, por verificações agendadas da 2ª via e do Nada Consta durante sete dias e pela interrupção breve da rede, apenas no dispositivo de teste, durante o carregamento do gráfico de consumo |
 
**Funcionalidades e tarefas:** histórico de consumo (execuções repetidas dos fluxos e interrupção da rede durante o carregamento do gráfico); segunda via de fatura e relatório de Nada Consta (verificações agendadas de disponibilidade). Login e cadastro e indicadores de continuidade não são foco das medidas de confiabilidade, conforme a nota de escopo do [modelo de qualidade](../fase1/modelo-qualidade.md) da Fase 1.

[Q3](questoes-hipoteses.md#q3) aborda a ocorrência de falhas em condições normais, [Q11](questoes-hipoteses.md#q11) trata da disponibilidade e [Q4](questoes-hipoteses.md#q4) da retomada e recuperação após interrupção. Os resultados de Q4 descrevem o comportamento observado no cliente e não medem, isoladamente, a recuperação dos servidores da Neoenergia.


### Ligação com a Fase 1
 
| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (três subcaracterísticas de confiabilidade) | Ramo “Confiabilidade” do modelo adaptado ([modelo de qualidade](../fase1/modelo-qualidade.md)) |
| Funcionalidades e tarefas | Procedimentos de avaliação: disponibilidade na Emissão de 2ª via e no Relatório de Nada Consta; maturidade, tolerância a falhas e recuperabilidade no Histórico de Consumo; nota de escopo que retira Login/Cadastro e Indicadores de Continuidade |
| Ponto de vista | Parte interessada “usuários finais” ([requisitos de avaliação](../fase1-requisitos.md)) |
| Contexto (pagar no prazo, comprovar adimplência, erro de comunicação) | Justificativa da ênfase da confiabilidade e nota de escopo dos procedimentos |
| Propósito (avaliar) | Propósito da avaliação: identificar pontos de melhoria e compreender o comportamento do sistema em cenários reais de uso |
| Prioridade | Ênfase 4 (alta) na seleção e priorização das características |
| ODS | ODS 7 (disponibilidade na 2ª via), conforme o [alinhamento aos ODS](../fase1/alinhamento-ods.md) |
 
### Abstraction sheet
 
| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Agência Virtual (3 funcionalidades) | Avaliar | Confiabilidade (três subcaracterísticas) | Usuários finais |

## G3 — Segurança { #g3 }

| Campo | Descrição |
|---|---|
| **Analisar** | a Agência Virtual da Neoenergia Brasília |
| **Com o propósito de** | avaliar |
| **Com respeito a** | segurança: confidencialidade, integridade / não repúdio, autenticidade e responsabilização |
| **Do ponto de vista de** | usuários finais: clientes residenciais e corporativos do Distrito Federal |
| **No contexto de** | uso autenticado da Agência Virtual em produção, com acesso a dados cadastrais e financeiros e emissão de documentos comprobatórios, observado apenas pelos recursos disponíveis ao usuário comum. Nos testes, esse contexto é reproduzido com a conta autorizada da unidade consumidora de Taguatinga: verificação do login e do cadastro, encerramento de sessão seguido de nova tentativa de acesso e emissão repetida do relatório de Nada Consta, sem testes de invasão, uso de contas de terceiros ou alteração de registros |
 
**Funcionalidades e tarefas:** login e cadastro (itens de autenticidade e responsabilização); segunda via de fatura e histórico de consumo (acesso após o logout); relatório de Nada Consta (consistência entre emissões e comprovação de autenticidade). Os indicadores de continuidade ficam fora deste objetivo, por serem dados de transparência pública, conforme a nota de escopo do [modelo de qualidade](../fase1/modelo-qualidade.md) da Fase 1.

O objetivo se desdobra em [Q12](questoes-hipoteses.md#q12) (autenticação e rastreabilidade), [Q5](questoes-hipoteses.md#q5) (proteção de acesso), [Q6](questoes-hipoteses.md#q6) (consistência de dados) e [Q13](questoes-hipoteses.md#q13) (comprovação do documento). A consistência observada em Q6 não permite concluir que o armazenamento esteja protegido contra alterações indevidas; essa delimitação é retomada na [rastreabilidade](rastreabilidade.md).


### Ligação com a Fase 1
 
| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (três subcaracterísticas de segurança) | Ramo “Segurança” do modelo adaptado ([modelo de qualidade](../fase1/modelo-qualidade.md)) |
| Funcionalidades e tarefas | Procedimentos de avaliação: autenticidade e responsabilização no Login/Cadastro; confidencialidade na Emissão de 2ª via e no Histórico de Consumo; integridade e não repúdio no Relatório de Nada Consta; nota de escopo que retira os Indicadores de Continuidade |
| Ponto de vista | Parte interessada “usuários finais”, que exige uma interface segura ([requisitos de avaliação](../fase1-requisitos.md)) |
| Contexto (dados sensíveis e financeiros, observação externa, conta de Taguatinga) | Justificativa da ênfase da segurança; justificativa da adaptação do modelo (testes de caixa-preta em produção); ambiente e massa de dados |
| Propósito (avaliar) | Propósito da avaliação: identificar pontos de melhoria do portal |
| Prioridade | Ênfase 5 (máxima) na seleção e priorização das características |
| ODS | ODS 16 (integridade / não repúdio no Nada Consta), conforme o [alinhamento aos ODS](../fase1/alinhamento-ods.md) |
 
### Abstraction sheet
 
| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Agência Virtual (4 funcionalidades) | Avaliar | Segurança (três subcaracterísticas) | Usuários finais |

## G4 — Eficiência de desempenho { #g4 }


| Campo | Descrição |
|---|---|
| **Analisar** | a Agência Virtual da Neoenergia Brasília |
| **Com o propósito de** | avaliar |
| **Com respeito a** | eficiência de desempenho: comportamento temporal e capacidade |
| **Do ponto de vista de** | usuários finais: clientes residenciais e corporativos do Distrito Federal |
| **No contexto de** | uso da Agência Virtual em produção, pelo navegador web, inclusive nos períodos de maior demanda, como dias úteis em horário comercial próximos ao vencimento das faturas. Nos testes, esse contexto é reproduzido por medições repetidas de cada fluxo, com o mesmo navegador, dispositivo e conexão e critérios fixos de início e fim, em janelas de pico natural e fora de pico, sem geração de carga artificial |
 
**Funcionalidades e tarefas:** login e cadastro (envio do formulário de credenciais) e indicadores de continuidade (abertura do painel), para o tempo de resposta; segunda via de fatura (geração do PDF) e histórico de consumo (renderização do gráfico), para a comparação entre pico e fora de pico. O relatório de Nada Consta não é alvo de medição de desempenho, conforme a nota de escopo do [modelo de qualidade](../fase1/modelo-qualidade.md) da Fase 1.
 
A mediana do tempo de resposta corresponde à [Q7](questoes-hipoteses.md#q7), enquanto o percentil 90 é utilizado na [Q8](questoes-hipoteses.md#q8) e a comparação entre pico e fora de pico à [Q14](questoes-hipoteses.md#q14). Quando a etapa final de uma funcionalidade não puder ser executada, a medição ficará restrita ao trecho efetivamente percorrido.

 
### Ligação com a Fase 1
 
| Elemento do objetivo | Origem na Fase 1 |
|---|---|
| Foco (comportamento temporal e capacidade) | Ramo “Eficiência de Desempenho” do modelo adaptado ([modelo de qualidade](../fase1/modelo-qualidade.md)) |
| Funcionalidades e tarefas | Procedimentos de avaliação: comportamento temporal no Login/Cadastro e nos Indicadores de Continuidade; capacidade na Emissão de 2ª via e no Histórico de Consumo; nota de escopo que retira o Relatório de Nada Consta |
| Ponto de vista | Parte interessada “usuários finais” ([requisitos de avaliação](../fase1-requisitos.md)) |
| Contexto (períodos de pico, geração de PDF e de gráficos) | Justificativa da ênfase da eficiência de desempenho e procedimento de capacidade (resposta sob pico) |
| Propósito (avaliar) | Propósito da avaliação: identificar gargalos de desempenho |
| Prioridade | Ênfase 4 (alta) na seleção e priorização das características |
| ODS | ODS 12 (desempenho na geração do Histórico de Consumo), conforme o [alinhamento aos ODS](../fase1/alinhamento-ods.md) |
 
### Abstraction sheet
 
| Objeto | Propósito | Foco da qualidade | Ponto de vista |
|---|---|---|---|
| Agência Virtual (4 funcionalidades) | Avaliar | Comportamento temporal e capacidade | Usuários finais |

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