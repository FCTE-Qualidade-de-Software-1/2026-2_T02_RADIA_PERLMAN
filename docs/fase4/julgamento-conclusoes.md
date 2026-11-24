# Julgamento e conclusões

Esta página reúne o julgamento final da qualidade da Agência Virtual da Neoenergia Brasília, a partir dos resultados de G1 a G4 e das regras dos [Critérios de julgamento](../fase2/criterios-julgamento.md).

## 1. Resultado por objetivo

Conforme os critérios da Fase 2, cada objetivo recebe o menor nível entre suas métricas, e os objetivos são apresentados separadamente, sem média geral.

**Tabela 1 —** Síntese dos objetivos GQM

| Objetivo | Característica (ênfase) | Métricas | Nível | Hipóteses sustentadas | Página |
|---|---|---|---|---|---|
| G1 | Usabilidade (5) | M1, M2, M9, M10 | **Insatisfatório** | H1 e H9 | [G1](resultados-g1-capacidade-interacao.md) |
| G2 | Confiabilidade (4) | M3, M4, M11 | **Mínimo aceitável** | H3 e H4 | [G2](resultados-g2-confiabilidade.md) |
| G3 | Segurança (5) | M5, M6, M12, M13 | **Insatisfatório** | H5 e H6 | [G3](resultados-g3-seguranca.md) |
| G4 | Eficiência de desempenho (4) | M7, M8, M14 | **Inconclusivo** | H8 | [G4](resultados-g4-desempenho.md) |

_Fonte: Equipe Radia Perlman, 2026._

## 2. Síntese da avaliação

A avaliação empírica das 14 métricas revelou um comportamento heterogêneo entre as características da norma ISO/IEC 25010 priorizadas no estudo, sem que nenhum dos quatro objetivos GQM atingisse os níveis consolidados *Alvo* ou *Excelente*:

* **Capacidade de Interação (G1 — Insatisfatório):** embora os participantes externos tenham localizado facilmente as funcionalidades básicas (**M1 = 100%, Excelente**) e reconhecido a finalidade geral das telas no limite da meta (**M9 = 80%, Alvo**), o objetivo foi rebaixado pela baixa qualidade das mensagens de erro nos formulários de login e cadastro (**M2 = 40%, Insatisfatório**), que frequentemente destacam campos ou bloqueiam o avanço sem explicar como corrigir o preenchimento. Além disso, a ausência de gráfico interativo no Histórico de Consumo inviabilizou a tarefa T4, tornando **M10 inconclusiva** (ainda que 100% dos voluntários tenham concluído a emissão da 2ª via na tarefa T3).
* **Confiabilidade (G2 — Mínimo aceitável):** o portal demonstrou excelente capacidade de retomada automática após interrupções breves na conexão local (**M4 = 100%, Excelente**) e boa estabilidade nos fluxos do Histórico de Consumo (**M3 = Alvo**, com 100% na abertura e 90% na emissão de 2ª via). Contudo, as indisponibilidades registradas na tarde e na noite de 17/11/2026 fizeram a disponibilidade cair para **87,5%** em ambas as funções monitoradas (**M11 = Mínimo aceitável**), não sustentando H11.
* **Segurança (G3 — Insatisfatório):** o sistema protegeu adequadamente as páginas restritas após o encerramento da sessão (**M5 = 100%, Excelente**) e manteve total consistência visual entre emissões consecutivas do relatório de Nada Consta (**M6 = 100%, Excelente**). Porém, o objetivo foi classificado como **Insatisfatório** porque nenhum dos cinco relatórios emitidos pôde ter sua autenticidade verificada no endereço oficial indicado no próprio documento (**M13 = 0%, Insatisfatório**), somado à exposição de qual credencial estava incorreta durante falhas de login e à ausência de notificações de acesso (**M12 = 60%, Mínimo aceitável**).
* **Eficiência de Desempenho (G4 — Inconclusivo):** nas medições auditadas em horário de pico, os tempos de resposta mantiveram o percentil 90 dentro da meta nos fluxos da Fase 2 (**M8 = Alvo**, com P90 de 4,36 s no login e 4,06 s nos indicadores), mas a mediana do login ficou ligeiramente acima do limite de 3 segundos (**M7 = 3,425 s, Mínimo aceitável**), acompanhada de seis ocorrências sem conclusão (erros HTTP 403 e falhas de solicitação). Como a coleta fora de pico foi invalidada na auditoria interna, não foi possível calcular a razão da **M14**, encerrando o julgamento de G4 como **Inconclusivo**.

## 3. Relação com o propósito da Fase 1

Na [Fase 1](../fase1-requisitos.md), estabeleceu-se como propósito avaliar, sob a perspectiva do cidadão do Distrito Federal, se a Agência Virtual da Neoenergia Brasília oferece um canal digital acessível, confiável, seguro e ágil para o autoatendimento de serviços essenciais, reduzindo a dependência do atendimento presencial e apoiando as metas de acesso moderno à energia (ODS 7), consumo consciente (ODS 12) e transparência institucional (ODS 16).

Os resultados obtidos mostram que, quando o portal está operacional, o usuário consegue cumprir jornadas transacionais essenciais — como localizar e baixar a segunda via da fatura — e conta com proteção básica contra acesso não autorizado após o logout. Entretanto, foram evidenciadas barreiras relevantes que comprometem o propósito de atendimento inclusivo e transparente:

1. **Barreiras para usuários com baixa familiaridade digital:** a ausência de instruções claras de correção em formulários (M2), a presença de botões sem rótulo textual (como o ícone de impressão da 2ª via) e a ambiguidade da tela de *Indicadores de Continuidade* (frequentemente confundida com o histórico de consumo na M9) dificultam a autonomia do cidadão leigo. Para responder diretamente a esse achado, a equipe projetou e validou um protótipo funcional de melhoria (OM-01), documentado em [Ação de melhoria](acao-melhoria.md) e [Plano de validação](plano-validacao.md).
2. **Lacuna de transparência e fé pública documental:** a inexistência de um validador ativo no portal institucional para conferir o código de autenticação impresso no *Relatório de Nada Consta* (M13) enfraquece a garantia de não repúdio exigida de uma concessionária de serviço público (ODS 16).
3. **Instabilidades em horários críticos:** as falhas de acesso e erros HTTP 403 observados em horário comercial e noturno (M7 e M11) indicam que o autoatendimento ainda está sujeito a interrupções que podem obrigar o consumidor a buscar canais presenciais ou telefônicos.

## 4. Limitações da avaliação

* **Amostras pequenas e por conveniência:** os resultados descrevem as condições, os dispositivos e os participantes observados durante a janela de execução (16/11 a 20/11/2026), não permitindo generalização estatística para toda a base de consumidores do Distrito Federal.
* **Ausência de gráfico interativo no Histórico de Consumo:** a interface real do portal apresenta apenas uma tabela estática de leituras e valores, sem gráfico ou seletor de período. Essa característica inviabilizou a execução da tarefa T4 (reduzindo a amostra elegível de M10 para 5 tarefas e tornando M10/H10 inconclusivas) e impediu a coleta do fluxo C-F2 na métrica M14.
* **Descarte dos registros fora de pico (Bloco 3):** os dados submetidos para a janela fora de pico foram invalidados na auditoria interna da equipe por inconsistência e ausência de rastreabilidade, restringindo a análise de desempenho à janela de pico e tornando M14 e G4 inconclusivos.
* **Abordagem estritamente de caixa-preta:** sem acesso ao código-fonte, aos logs internos ou à infraestrutura da concessionária, as conclusões limitam-se ao comportamento observável pela interface web em uma única unidade consumidora autorizada.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da estrutura da página com os resultados parciais de G1 | Beatriz |
| 1.1 | 22/11/2026 | Atualiza G1 e G3 | Isabella |
| 1.2 | 23/11/2026 | Inclusão do julgamento final de G2 (Mínimo aceitável), ajuste de H10 em G1 e registro da limitação do Histórico de Consumo | Dara Maria Barbosa de Sousa |
| 1.3 | 24/11/2026 | Consolidação do julgamento de G4 (Inconclusivo), redação da síntese da avaliação, relação com a Fase 1 e registro do descarte do Bloco 3 nas limitações | Dara Maria Barbosa de Sousa |