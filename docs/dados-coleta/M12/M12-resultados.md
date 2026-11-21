# M12 — Itens de autenticidade e responsabilização atendidos (S-03)

## 1. Objetivo e relação com o GQM

A M12 verifica, por meio de comportamentos observáveis pelo usuário, se a Agência Virtual da Neoenergia Brasília rejeita credenciais incorretas, evita revelar qual credencial está errada, encerra sessões inativas, exige comprovação de vínculo no cadastro e apresenta elementos de rastreabilidade de acesso e de emissão.

- **Objetivo GQM:** G3 — Segurança.
- **Questão:** Q12 — O sistema comprova a identidade do usuário e associa as ações a ele?
- **Hipótese:** H12 — Ao menos 80% dos itens de verificação de autenticidade e responsabilização serão atendidos.
- **Métrica:** M12 — Itens de autenticidade e responsabilização atendidos.
- **Cenário:** S-03.

A Fase 2 define seis itens (A1, A2, A3, A4, R1 e R2). Cada item deve ser verificado duas vezes, em dias diferentes. Um item só é considerado atendido quando as duas verificações são positivas. Quando os resultados divergem, o item é inconclusivo e sai do denominador, com justificativa. A métrica exige pelo menos cinco itens elegíveis.

## 2. Método e condições da coleta

As verificações foram executadas em duas frentes complementares utilizando conta própria autorizada, em computador pessoal com Windows 11 e navegador Microsoft Edge, consolidadas no arquivo `M12-registros.csv`:

- **Itens A1 a A4 (Autenticação e cadastro):** coletados por Isabella em **16/11/2026, às 21h30** (1ª rodada), e **17/11/2026, às 20h20** (2ª rodada), em conexão Wi-Fi. Para A1 e A2 utilizou-se apenas uma tentativa com senha incorreta por rodada; para A3 manteve-se a sessão autenticada sem interação por até 60 minutos; para A4 observou-se o fluxo de cadastro sem concluir uma operação.
- **Itens R1 e R2 (Rastreabilidade e responsabilização):** coletados por Henrique em **17/11/2026, entre 16h50 e 16h54** (1ª rodada), e **19/11/2026, entre 14h44 e 14h47** (2ª rodada), em conexão Ethernet. Para R1 verificou-se a exibição ou notificação de registro de acesso após login; para R2 verificou-se a geração de número de protocolo associado ao titular durante a emissão de 2ª via.

## 3. Resultados por item

| Item | Verificação prevista | 1ª rodada | 2ª rodada | Interpretação |
|---|---|---|---|---|
| A1 | Credencial incorreta é rejeitada | Atendido | Atendido | **Atendido** — o sistema rejeitou a autenticação nas duas rodadas |
| A2 | Mensagem não indica qual credencial está incorreta | Não atendido | Não atendido | **Não atendido** — a mensagem apontou que o CPF/CNPJ informado não foi encontrado, embora a tentativa utilizasse CPF cadastrado e senha incorreta |
| A3 | Sessão expira após inatividade | Inconclusivo | Não atendido | **Inconclusivo** — na primeira rodada houve mensagem de indisponibilidade do sistema; na segunda, a sessão continuou acessível após o período observado |
| A4 | Cadastro exige comprovação de vínculo ou identidade | Atendido | Atendido | **Atendido** — o fluxo exigiu validação do código do cliente para concluir o cadastro e encaminhou e-mail para definição de senha após a aceitação dos dados |
| R1 | Sistema exibe ou notifica registro de acesso | Não atendido | Não atendido | **Não atendido** — em ambas as rodadas, o portal não exibiu data/hora de último acesso nem enviou notificação de início de nova sessão |
| R2 | Emissões geram identificador ou protocolo associado ao titular | Atendido | Atendido | **Atendido** — em ambas as rodadas, ao emitir a 2ª via, o sistema gerou um número de protocolo único associado à sessão e ao titular |

### Observações relevantes

**A2 — exposição da credencial incorreta.** Nas duas rodadas, a tentativa utilizou CPF cadastrado e senha incorreta. A mensagem observada foi “Usuário com CPF/CNPJ informado não foi encontrado.” Como a mensagem aponta o CPF/CNPJ como problema, ela não atende ao critério de não revelar qual credencial está incorreta.

**A3 — expiração da sessão.** Na primeira rodada, após o período de inatividade, a tentativa de acessar a segunda via apresentou uma mensagem de indisponibilidade do sistema. Esse comportamento não permite concluir se a sessão havia expirado, pois a própria indisponibilidade pode ter impedido o acesso. Na segunda rodada, a funcionalidade foi acessada normalmente após o período de inatividade, sem encerramento da sessão. Como os resultados das duas rodadas divergem, a regra da Fase 2 determina que A3 seja tratado como inconclusivo e retirado do denominador.

**R1 — ausência de registro ou alerta de acesso.** Nas duas datas observadas (17/11 e 19/11), após a autenticação na conta autorizada, a interface inicial  não exibiu informações sobre último acesso nem disparou aviso de novo login, resultando em não atendimento do item. Também não havia um menu do usuário onde poderia ter essa informação.

## 4. Cálculo e julgamento da M12

A fórmula definida na Fase 2 é:

`M12 = 100 × A / N`

Em que:

- `A` = número de itens atendidos nas duas verificações;
- `N` = número de itens elegíveis, após retirar itens inconclusivos ou sem dados suficientes para julgamento.

Consolidando os seis itens verificados:

- **Itens elegíveis (`N = 5`):** A1, A2, A4, R1 e R2 (atingindo a amostra mínima de cinco itens exigida pela Fase 2);
- **Item excluído (`1`):** A3 (inconclusivo devido à indisponibilidade do sistema na 1ª rodada e divergência em relação à 2ª);
- **Itens atendidos (`A = 3`):** A1, A4 e R2.

Aplicando a fórmula:

`M12 = 100 × 3 / 5 = 60%`

- **Classificação da métrica:** **Mínimo aceitável** (faixa de `60%` a menos de `80%`).
- **Julgamento da hipótese H12 (`M12 ≥ 80%`):** **Não sustentada**.


## 5. Resposta à questão GQM

**Q12 — O sistema comprova a identidade do usuário e associa as ações a ele?**

Parcialmente. A Agência Virtual atendeu a **60%** dos itens elegíveis (**Mínimo aceitável**): o portal rejeita credenciais inválidas (A1), exige comprovação de vínculo com a unidade consumidora por meio do código do cliente e confirmação por e-mail no cadastro (A4) e gera protocolo único associado ao titular nas emissões (R2). Por outro lado, o sistema expõe qual credencial está incorreta na mensagem de erro de login (A2), não exibe nem notifica o histórico de acessos ao titular (R1) e apresentou falha de encerramento de sessão por inatividade na rodada válida observada (A3). Dessa forma, a hipótese **H12** não foi sustentada.

## 6. Oportunidades de melhoria e complementação da coleta

1. **Neutralizar a mensagem de falha de autenticação (A2):** substituir a mensagem *"Usuário com CPF/CNPJ informado não foi encontrado"* por uma resposta genérica (por exemplo, *"CPF/CNPJ ou senha inválidos"*), evitando confirmar a existência ou inexistência de cadastros.
2. **Exibir registro ou alerta de acesso ao usuário (R1):** incluir na área logada a data e hora do último acesso ou enviar notificação por e-mail a cada novo login realizado na conta.
3. **Garantir expiração de sessão por inatividade (A3):** configurar timeout explícito de sessão após período de ociosidade, exigindo nova autenticação para acessar áreas restritas como a emissão de segunda via.


## 7. Evidências e rastreabilidade

As evidências estão organizadas em `docs/evidencias/M12/`:

| Arquivo | Registro |
|---|---|
| `M12-A1-A4-17112026-01.pdf` | Ficha consolidada de A1 a A4, com ambiente, duas rodadas, entradas, resultados observados e justificativas |
| `M12-A1-A2-17112026-02.png` | Captura da tentativa de login com credenciais incorretas e mensagem apresentada pelo sistema |
| `M12-R1-17112026-01.png` | Captura da página inicial/menu utilizada como evidência de R1 |
| `M12-R1-19112026-02.png` | Segunda captura de R1, identificada pelo nome do arquivo como 19/11 |
| `M12-R2-17112026-01.png` | Captura da tela de dados da unidade consumidora com campo “Protocolo” |
| `M12-R2-19112026-02.png` | Segunda captura de R2, identificada pelo nome do arquivo como 19/11 |

## 8. Limitações e pendências de consistência

1. As rodadas de A1 a A4 (16/11 e 17/11, via Wi-Fi) e de R1 e R2 (17/11 e 19/11, via Ethernet) foram conduzidas por dois avaliadores em datas distintas, respeitando integralmente o critério de duas verificações em dias diferentes por item.
2. A primeira verificação de A3 foi afetada por mensagem de indisponibilidade do portal, impedindo atribuir o bloqueio exclusivamente ao controle de expiração de sessão e motivando sua exclusão do denominador.

## 9. Conclusão

A métrica **M12** obteve o valor de **60% (`3/5` itens elegíveis atendidos)**, recebendo classificação **Mínimo aceitável** e tornando a hipótese **H12 não sustentada**. O sistema demonstra controles adequados na rejeição de login inválido (A1), na validação de vínculo cadastral (A4) e na emissão de protocolos de atendimento (R2), mas precisa evoluir na neutralidade das mensagens de erro de autenticação (A2), na visibilidade do histórico de acessos (R1) e na expiração de sessões inativas (A3).
