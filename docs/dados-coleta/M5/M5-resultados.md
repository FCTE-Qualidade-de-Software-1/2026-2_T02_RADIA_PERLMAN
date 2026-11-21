# M5 — Bloqueio de acesso a páginas restritas (S-01)

## 1. Objetivo e relação com o GQM

A M5 verifica se páginas restritas da Agência Virtual da Neoenergia Brasília permanecem protegidas após o encerramento da sessão, impedindo que informações protegidas continuem utilizáveis sem autenticação.

- **Objetivo GQM:** G3 — Segurança.
- **Questão:** Q5 — Páginas restritas permanecem protegidas depois do logout?
- **Hipótese:** H5 — 100% das verificações sem sessão ativa impedirão o acesso utilizável a dados protegidos.
- **Métrica:** M5 — Bloqueio de acesso a páginas restritas.
- **Cenário:** S-01.

A Fase 2 estabelece um critério específico para esta métrica: somente 100% de bloqueios corretos sustenta H5 e recebe classificação Excelente. Qualquer acesso efetivo a informação protegida sem sessão resulta em classificação Insatisfatório.

## 2. Método e condições da coleta

A coleta foi realizada em **16/11/2026**, às **21h**, seguindo o cenário S-01 da Fase 3. Foram utilizadas páginas acessadas previamente com uma conta própria. Após o logout, foram executadas ações de retorno à página anterior, atualização e reabertura do endereço.

| Campo | Registro |
|---|---|
| Avaliadora | Isabella |
| Dispositivo | Computador pessoal |
| Sistema operacional | Windows 11 |
| Navegador | Microsoft Edge |
| Conexão | Wi-Fi |
| Conta utilizada | Conta própria |

O procedimento considerou adequado o comportamento em que, após o encerramento da sessão, o sistema permanecesse na tela de login ou exigisse nova autenticação, sem disponibilizar conteúdo protegido. A ficha distingue a navegação local do navegador do acesso utilizável à área restrita.

## 3. Dados coletados

Foram registradas cinco verificações elegíveis, distribuídas entre duas páginas restritas.

| ID | Página restrita | Ação após logout | Resultado observado | Adequada? |
|---|---|---|---|---:|
| M5-T01 | Segunda via | Botão voltar do navegador | Permaneceu na página de login, sem permitir retornar à conta | 1 |
| M5-T02 | Segunda via | Atualizar página | Permaneceu na tela de login, sem recuperar o acesso à área restrita | 1 |
| M5-T03 | Segunda via | Abrir novamente o endereço da segunda via | Permaneceu na página de login, sem permitir retornar à conta | 1 |
| M5-T04 | Histórico de consumo | Botão voltar do navegador | Permaneceu na página de login, sem retornar à área restrita | 1 |
| M5-T05 | Histórico de consumo | Reabrir o endereço | Permaneceu na tela de login, sem permitir acesso ao conteúdo protegido | 1 |
| **Total** | **Duas páginas** | **Cinco verificações** | **Nenhuma exposição observada** | **5/5** |

A quantidade mínima definida na Fase 2 e detalhada na Fase 3 é de cinco verificações, preferencialmente distribuídas entre pelo menos duas páginas restritas. A coleta atingiu essa quantidade e incluiu a segunda via e o histórico de consumo.

## 4. Cálculo da M5

A fórmula definida na Fase 2 é:

`M5 = 100 × B / N`

Em que:

- `B` = verificações sem acesso utilizável a informação protegida;
- `N` = verificações elegíveis realizadas sem sessão ativa.

Substituindo os valores coletados:

`M5 = 100 × 5 / 5 = 100%`

**Resultado da M5: 100%.**

## 5. Interpretação e julgamento

A hipótese H5 exige que todas as verificações impeçam o acesso utilizável a dados protegidos sem sessão ativa. A escala da Fase 2 não prevê níveis intermediários para M5.

| Referência | Critério | Resultado | Avaliação |
|---|---:|---:|---|
| Quantidade mínima | 5 verificações | 5 | Atingida |
| H5 | 100% | 100% | Sustentada |
| Classificação da M5 | 100% = Excelente | 100% | **Excelente** |

Nas cinco verificações, o sistema manteve a navegação na página de login e não permitiu retornar à área restrita. Não foi observada exposição utilizável de informações protegidas após o logout. Assim, dentro das páginas e condições verificadas, o comportamento observado atendeu ao critério de confidencialidade definido para a M5.

## 6. Resposta à questão GQM

**Q5 — Páginas restritas permanecem protegidas depois do logout?**

Sim, nas condições avaliadas. As cinco verificações realizadas após o encerramento da sessão impediram o retorno utilizável às páginas restritas de segunda via e histórico de consumo. O resultado foi de 100%, sustentando H5 e recebendo classificação Excelente.

## 7. Oportunidades de melhoria e recomendações

Embora a métrica tenha alcançado o resultado esperado, recomenda-se manter o comportamento observado e:

1. preservar a exigência de autenticação ao acessar diretamente endereços de páginas restritas;
2. manter o bloqueio também após ações de voltar e atualizar do navegador;
3. repetir periodicamente verificações de acesso após logout em outras funcionalidades protegidas;
4. em futuras avaliações, registrar separadamente o comportamento de conteúdo em cache e o acesso efetivo ao servidor, conforme previsto no protocolo.

Não foi identificada, nesta coleta, uma falha que justifique uma correção específica. As recomendações são preventivas e visam preservar o resultado.

## 8. Evidências e rastreabilidade

A ficha consolidada está em `docs/evidencias/M5/M5-S01-16112026-01.png`. Ela registra o ambiente, a data, as cinco tentativas, as páginas avaliadas, as ações após logout, os resultados observados e a classificação de adequação.

A ficha é a fonte dos valores utilizados no cálculo (5 verificações adequadas em 5 elegíveis). O registro permite rastrear o resultado da M5 até cada tentativa.

## 9. Limitações

O resultado se restringe às duas páginas testadas (segunda via e histórico de consumo), à conta própria utilizada e ao ambiente registrado. A avaliação não constitui auditoria de segurança, teste de invasão ou verificação de todos os endpoints da aplicação. Também não permite concluir sobre a implementação interna do controle de sessão. O julgamento deve ser entendido como evidência observacional de que, nas cinco verificações executadas, não houve acesso utilizável a conteúdo protegido sem autenticação.

## 10. Conclusão

A M5 obteve **100% (5/5)** e foi classificada como **Excelente**. A hipótese H5 foi sustentada, pois todas as verificações realizadas após o logout impediram o retorno utilizável às páginas restritas avaliadas. O resultado atende ao critério de confidencialidade definido na Fase 2, dentro do escopo e das limitações da coleta.
