# M4 — Retomada após interrupção local da conexão (R-02)

## 1. Objetivo e relação com o GQM

A M4 verifica se a navegação na Agência Virtual da Neoenergia Brasília pode ser retomada após uma interrupção breve da conexão local do dispositivo de teste durante uma consulta de leitura, sem exigir o reinício completo da jornada do usuário.

- **Objetivo GQM:** G2 — Confiabilidade.
- **Questão:** Q4 — É possível continuar a navegação após uma perda breve de conexão?
- **Hipótese:** H4 — Ao menos 80% das interrupções locais permitirão retomar o fluxo e restabelecer o estado anterior.
- **Métrica:** M4 — Retomada após interrupção local da conexão.
- **Cenário:** R-02.

A Fase 2 estabelece o mínimo de cinco tentativas seguras e independentes, aplicadas exclusivamente em consultas de leitura (sem envio de formulários, alterações cadastrais ou confirmações). A retomada é considerada adequada quando o fluxo continua ou retorna à mesma etapa em até 30 segundos após o restabelecimento da rede, admitindo-se no máximo uma ação manual de retentativa oferecida pela própria interface.

## 2. Método e condições da coleta

As cinco execuções independentes foram realizadas por Henrique em **20/11/2026, entre 19h29 e 19h36**, utilizando conta própria autorizada, consolidadas no arquivo `M4-registros.csv`:

- **Ambiente de referência:** computador pessoal (desktop), sistema operacional Windows 11, navegador Microsoft Edge (versão `157.0.4341.60`) com cache padrão habilitado e conexão cabeada (Ethernet).
- **Procedimento executado:** a partir do menu principal autenticado, acionou-se a consulta/emissão do relatório de Nada Consta (operação de leitura sem modificação de registros da conta). Durante o carregamento da requisição, a conexão Ethernet do dispositivo de teste foi interrompida localmente por **5 segundos** e, em seguida, restabelecida, cronometrando-se o comportamento da navegação dentro da janela limite de **30 segundos**, sem intervenção manual de recarregamento (F5).

## 3. Resultados por tentativa

| Identificação | Horário | Desconexão local | Ação manual | Tempo de retomada | Resultado observado | Situação | Classificação |
|---|---|---|---|---|---|---|---|
| `M4-R02-20112026-01` | 19:29 | 5 s | Nenhuma | 18 s | Navegador sinalizou falha de conexão durante o corte, retomou automaticamente após o retorno da rede e concluiu a consulta em 18 s | Elegível | **Sucesso** |
| `M4-R02-20112026-02` | 19:31 | 5 s | Nenhuma | 20 s | Navegador sinalizou falha de conexão durante o corte, retomou automaticamente após o retorno da rede e concluiu a consulta em 20 s | Elegível | **Sucesso** |
| `M4-R02-20112026-03` | 19:33 | 5 s | Nenhuma | 19 s | Navegador sinalizou falha de conexão durante o corte, retomou automaticamente após o retorno da rede e concluiu a consulta em 19 s | Elegível | **Sucesso** |
| `M4-R02-20112026-04` | 19:35 | 5 s | Nenhuma | 23 s | Navegador sinalizou falha de conexão durante o corte, retomou automaticamente após o retorno da rede e concluiu a consulta em 23 s | Elegível | **Sucesso** |
| `M4-R02-20112026-05` | 19:36 | 5 s | Nenhuma | 22 s | Navegador sinalizou falha de conexão durante o corte, retomou automaticamente após o retorno da rede e concluiu a consulta em 22 s | Elegível | **Sucesso** |

### Observações relevantes

**Retomada automática sem perda de sessão.** Nas cinco tentativas, ao desativar a interface Ethernet por 5 segundos, o Microsoft Edge exibiu imediatamente o aviso nativo de interrupção de rede; contudo, assim que a conectividade foi restabelecida, o navegador retomou a requisição pendente de forma automática, carregando o resultado esperado sem derrubar a sessão autenticada nem retornar à tela inicial.

**Comportamento temporal da recuperação.** Os tempos totais de retomada variaram entre **18 s** e **23 s** (média de **20,4 s** e mediana de **20,0 s**), permanecendo em todas as execuções abaixo do teto de **30 segundos** estipulado no protocolo.

**Dependência do navegador no ambiente cliente.** Conforme previsto na especificação da Fase 2, a recuperação observada reflete a interação entre a aplicação web e o tratamento nativo de reconexão do navegador utilizado (Microsoft Edge), não medindo isoladamente mecanismos de tolerância a falhas internas dos servidores da concessionária.

## 4. Cálculo e julgamento da M4

A fórmula definida na Fase 2 é:

`M4 = 100 × R / N`

Em que:

- `R` = número de tentativas em que a navegação foi retomada conforme o critério;
- `N` = número de interrupções locais elegíveis.

Consolidando os registros de `M4-registros.csv`:

- **Tentativas elegíveis (`N = 5`):** `M4-R02-20112026-01` a `M4-R02-20112026-05` (amostra mínima atingida, sem exclusões);
- **Tentativas retomadas com sucesso (`R = 5`):** todas as cinco execuções concluíram o carregamento dentro de 30 segundos, sem ação manual.

Aplicando a fórmula:

`M4 = 100 × 5 / 5 = 100%`

- **Classificação da métrica:** **Excelente** (faixa de `95%` ou mais).
- **Julgamento da hipótese H4 (`M4 ≥ 80%`):** **Sustentada**.

## 5. Resposta à questão GQM

**Q4 — É possível continuar a navegação após uma perda breve de conexão?**

Sim. Nas cinco interrupções locais de 5 segundos avaliadas no ambiente de referência (Microsoft Edge em Windows 11), a navegação foi retomada automaticamente após o restabelecimento da rede em até **23 segundos** (limite de 30 segundos), mantendo a sessão autenticada ativa e concluindo a consulta sem reiniciar a jornada do usuário. Com **100%** de retomada, a hipótese **H4** foi sustentada.

## 6. Oportunidades de melhoria

1. **Feedback visual próprio da aplicação durante quedas de rede:** embora a retomada tenha ocorrido com sucesso no navegador de referência, a Agência Virtual delega integralmente o aviso de desconexão à página nativa de erro do navegador. Exibir um indicador interno de status de conexão ou botão próprio de *"Tentar novamente"* na interface tornaria a recuperação uniforme mesmo em navegadores que não realizam recarregamento automático após queda de rede.

## 7. Evidências e rastreabilidade

Os dados brutos e as capturas anonimizadas estão organizados em `docs/evidencias/M4/`:

| Arquivo | Registro |
|---|---|
| [`M4-R02-20112026-01.png`](../../evidencias/M4/M4-R02-20112026-01.png) | Captura anonimizada da retomada concluída na 1ª tentativa (19h29, retomada em 18 s) |
| [`M4-R02-20112026-02.png`](../../evidencias/M4/M4-R02-20112026-02.png) | Captura anonimizada da retomada concluída na 2ª tentativa (19h31, retomada em 20 s) |
| [`M4-R02-20112026-03.png`](../../evidencias/M4/M4-R02-20112026-03.png) | Captura anonimizada da retomada concluída na 3ª tentativa (19h33, retomada em 19 s) |
| [`M4-R02-20112026-04.png`](../../evidencias/M4/M4-R02-20112026-04.png) | Captura anonimizada da retomada concluída na 4ª tentativa (19h35, retomada em 23 s) |
| [`M4-R02-20112026-05.png`](../../evidencias/M4/M4-R02-20112026-05.png) | Captura anonimizada da retomada concluída na 5ª tentativa (19h36, retomada em 22 s) |

## 8. Limitações e pendências de consistência

1. **Escopo funcional adaptado:** na Fase 2, o cenário R-02 previa a interrupção durante o carregamento de gráfico no *Histórico de consumo*; na execução real, aplicou-se o procedimento na consulta/emissão do relatório de *Nada Consta*, mantendo integralmente o critério metodológico de consulta de leitura sem alteração de dados cadastrais.
2. **Escopo arquitetural da medição:** os resultados avaliam a tolerância a falhas e a recuperabilidade observadas no ambiente cliente (navegador Microsoft Edge e rede local do dispositivo de teste), não representando teste de recuperação dos servidores ou da infraestrutura interna da Neoenergia Brasília.

## 9. Conclusão

A métrica **M4** alcançou **100% (`5/5` tentativas retomadas com sucesso)**, obtendo classificação **Excelente** e sustentando a hipótese **H4**. O sistema demonstrou capacidade de preservar o estado da sessão e concluir a consulta após interrupções locais breves de conectividade dentro do limite de 30 segundos, ainda que a experiência de aviso e reconexão dependa diretamente do comportamento do navegador utilizado.