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

O registro consolidado de A1 a A4 informa duas rodadas realizadas em **16/11/2026, às 21h30**, e **17/11/2026, às 20h20**. O arquivo também identifica a avaliadora, o computador pessoal, Windows 11, Microsoft Edge, conexão Wi-Fi e uso de conta própria.

Para A1 e A2 foi utilizada, no máximo, uma tentativa com senha incorreta por rodada. Para A3, a sessão autenticada foi mantida sem interação por até 60 minutos. Para A4, foi observado o fluxo de cadastro sem concluir uma operação. As evidências de R1 e R2 estão em capturas separadas, cujos nomes indicam registros em 17/11 e 19/11; entretanto, esses dois itens não aparecem consolidados na tabela de resultados do arquivo de coleta.

## 3. Resultados por item

| Item | Verificação prevista | 1ª rodada | 2ª rodada | Interpretação |
|---|---|---|---|---|
| A1 | Credencial incorreta é rejeitada | Atendido | Atendido | **Atendido** — o sistema rejeitou a autenticação nas duas rodadas |
| A2 | Mensagem não indica qual credencial está incorreta | Não atendido | Não atendido | **Não atendido** — a mensagem apontou que o CPF/CNPJ informado não foi encontrado, embora a tentativa utilizasse CPF cadastrado e senha incorreta |
| A3 | Sessão expira após inatividade | Inconclusivo | Não atendido | **Inconclusivo** — na primeira rodada houve mensagem de indisponibilidade do sistema; na segunda, a sessão continuou acessível após o período observado |
| A4 | Cadastro exige comprovação de vínculo ou identidade | Atendido | Atendido | **Atendido** — o fluxo exigiu validação do código do cliente para concluir o cadastro e encaminhou e-mail para definição de senha após a aceitação dos dados |
| R1 | Sistema exibe ou notifica registro de acesso | Não consolidado | Não consolidado | **Sem classificação na ficha** — existem capturas identificadas como R1, mas não há resultado explícito por rodada no checklist |
| R2 | Emissões geram identificador ou protocolo associado ao titular | Não consolidado | Não consolidado | **Sem classificação na ficha** — as capturas mostram um campo “Protocolo” nos dados da unidade consumidora, mas não documentam que esse identificador esteja associado a uma emissão específica |

### Observações relevantes

**A2 — exposição da credencial incorreta.** Nas duas rodadas, a tentativa utilizou CPF cadastrado e senha incorreta. A mensagem observada foi “Usuário com CPF/CNPJ informado não foi encontrado.” Como a mensagem aponta o CPF/CNPJ como problema, ela não atende ao critério de não revelar qual credencial está incorreta.

**A3 — expiração da sessão.** Na primeira rodada, após o período de inatividade, a tentativa de acessar a segunda via apresentou uma mensagem de indisponibilidade do sistema. Esse comportamento não permite concluir se a sessão havia expirado, pois a própria indisponibilidade pode ter impedido o acesso. Na segunda rodada, a funcionalidade foi acessada normalmente após o período de inatividade, sem encerramento da sessão. Como os resultados das duas rodadas divergem, a regra da Fase 2 determina que A3 seja tratado como inconclusivo e retirado do denominador.

**R1 e R2 — rastreabilidade.** Há duas capturas para cada item, com datas nos nomes dos arquivos (17/11 e 19/11). A captura de R1 mostra a página inicial/menu da conta, mas não registra de forma explícita se houve procura em uma área específica de histórico ou notificação de acesso. As capturas de R2 mostram a tela de dados da unidade consumidora com um campo “Protocolo”; contudo, não demonstram que esse protocolo seja gerado por uma emissão específica ou que esteja associado ao documento emitido. Por isso, as imagens, isoladamente, não permitem atribuir resultado positivo ou negativo com segurança. É necessário completar o checklist com o resultado observado e a justificativa de cada rodada.

## 4. Cálculo e julgamento da M12

A fórmula definida na Fase 2 é:

`M12 = 100 × A / N`

Em que:

- `A` = número de itens atendidos nas duas verificações;
- `N` = número de itens elegíveis, após retirar itens inconclusivos ou sem dados suficientes para julgamento.

Com os registros consolidados disponíveis:

- A1: atendido;
- A2: não atendido;
- A3: inconclusivo e excluído do denominador;
- A4: atendido;
- R1 e R2: sem classificação consolidada, não podendo ser incluídos no cálculo sem completar os registros.

Assim, há **três itens com resultado consolidado e elegível** (A1, A2 e A4), abaixo do mínimo de cinco itens elegíveis estabelecido para a M12. Embora dois desses três itens estejam atendidos, não é metodologicamente válido apresentar `2/3` como resultado final da métrica, pois a amostra mínima não foi atingida e dois itens previstos não possuem julgamento consolidado.

**Resultado inconclusivo.**

**Não é possível calcular uma M12 final válida com a documentação disponível.** Consequentemente, H12 também permanece inconclusiva. Não se deve declarar a hipótese sustentada ou não sustentada com base apenas nos três itens consolidados.

## 5. Resposta à questão GQM

**Q12 — O sistema comprova a identidade do usuário e associa as ações a ele?**

A evidência disponível é parcial. A1 demonstrou rejeição de credencial incorreta e A4 demonstrou uma etapa de comprovação de vínculo no cadastro. Por outro lado, A2 não atendeu ao critério de mensagem neutra, pois a resposta identificou o CPF/CNPJ como problema. A3 não pôde ser julgado de forma conclusiva devido à divergência entre as rodadas. As evidências de R1 e R2 precisam de registro explícito para confirmar se há rastreabilidade de acesso e associação das emissões ao titular. Como há menos de cinco itens elegíveis consolidados, a resposta geral à Q12 permanece inconclusiva.

## 6. Oportunidades de melhoria e complementação da coleta

As evidências apontam uma oportunidade objetiva para A2: revisar a mensagem de falha de autenticação para que não revele se o CPF/CNPJ ou a senha está incorreto. A mensagem deve ser neutra, sem comprometer a segurança e sem impedir que o usuário entenda que a combinação informada não foi aceita.

Também é necessário:

1. **Completar o registro de R1:** documentar em qual área da aplicação foi procurado o histórico de acesso ou a notificação de novo login, o que foi encontrado em cada dia e qual evidência comprova o resultado.
2. **Completar o registro de R2:** verificar se o protocolo exibido pertence efetivamente à emissão da segunda via ou se identifica apenas a unidade consumidora. Registrar a relação entre o identificador, a emissão e o titular.
3. **Reavaliar A3 em condições estáveis:** repetir a verificação de expiração após inatividade, registrando o horário de início, o período efetivo sem interação, a tentativa de acesso e a resposta do sistema. A indisponibilidade observada na primeira rodada deve permanecer documentada como limitação daquela tentativa.
4. **Atualizar o checklist:** registrar os resultados de R1 e R2 por rodada e justificar formalmente qualquer item inconclusivo ou excluído.

A complementação deve respeitar a Fase 3: conta própria ou autorizada, no máximo uma tentativa incorreta por verificação de A1/A2, sem força bruta e sem uso de contas de terceiros.

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

A ficha PDF é a fonte do julgamento de A1 a A4. As capturas de R1 e R2 são evidências complementares, mas precisam ser relacionadas explicitamente a resultados por rodada antes de integrarem o denominador.

## 8. Limitações e pendências de consistência

1. A ficha PDF documenta A1 a A4, mas não apresenta uma classificação para R1 e R2, embora existam capturas correspondentes no diretório de evidências.
2. Os nomes dos arquivos de R1 e R2 indicam capturas em 17/11 e 19/11, enquanto a ficha PDF registra as duas rodadas de A1 a A4 em 16/11 e 17/11. A documentação deve explicitar se foram sessões distintas ou complementares.
3. A primeira verificação de A3 foi afetada por mensagem de indisponibilidade, o que impede atribuir o resultado exclusivamente ao controle de expiração de sessão.
4. A quantidade mínima da M12 é de cinco itens elegíveis; com apenas A1, A2 e A4 consolidados, a métrica não pode receber classificação percentual final.

## 9. Conclusão

A M12 permanece **Inconclusiva**. A coleta demonstrou resultados positivos para A1 e A4 e resultado negativo para A2; A3 foi inconclusivo devido à divergência entre as rodadas. Embora existam capturas de R1 e R2, seus resultados não foram formalmente consolidados e a relação do protocolo observado com uma emissão específica não está demonstrada. Como somente três itens possuem classificação consolidada e elegível, não foi atingido o mínimo de cinco itens exigido pela Fase 2. H12, portanto, também permanece inconclusiva até que R1 e R2 sejam documentados adequadamente e, se necessário, as verificações pendentes sejam complementadas.
