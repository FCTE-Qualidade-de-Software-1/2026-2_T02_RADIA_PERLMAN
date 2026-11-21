# M2 — Tratamento de entradas inválidas (U-02)

## 1. Objetivo e relação com o GQM

A M2 avalia se os formulários de login e cadastro da Agência Virtual da Neoenergia Brasília identificam entradas sintaticamente inválidas e apresentam orientação compreensível para que o usuário possa corrigi-las.

- **Objetivo GQM:** G1 — Capacidade de interação.
- **Questão:** Q2 — Os formulários ajudam a corrigir entradas inválidas?
- **Hipótese:** H2 — Ao menos 80% das entradas inválidas serão sinalizadas antes do envio, com orientação para a correção.
- **Métrica:** M2 — Tratamento de entradas inválidas.
- **Cenário:** U-02.

Conforme definido na Fase 2, impedir o avanço, isoladamente, não caracteriza tratamento adequado. A interface também deve sinalizar o problema e orientar a correção.

## 2. Método e condições da coleta

A coleta foi realizada em **16/11/2026**, às **18h40**, seguindo o cenário U-02 da Fase 3. Foram testados campos dos formulários de cadastro e login, com entradas inválidas previamente selecionadas. A execução foi interrompida antes de qualquer confirmação de operação.

| Campo | Registro |
|---|---|
| Avaliadora | Isabella |
| Dispositivo | Computador pessoal |
| Sistema operacional | Windows 11 |
| Navegador | Microsoft Edge |
| Conexão | Wi-Fi |
| Conta | Não aplicável às tentativas registradas |

O procedimento consistiu em inserir cada valor, observar a resposta da interface e verificar se havia sinalização do erro acompanhada de orientação compreensível. A tentativa só foi considerada adequada quando os dois requisitos foram atendidos.

## 3. Dados consolidados

A planilha de coleta apresenta onze registros (T01 a T11). O registro T09 foi marcado como **excluído** na própria ficha e, portanto, não integra o denominador. Os outros dez registros foram considerados elegíveis.

| Classificação observada | Tentativas | Registros |
|---|---:|---|
| Adequadas | 4 | T06, T07, T08 e T11 |
| Inadequadas | 6 | T01, T02, T03, T04, T05 e T10 |
| Excluídas | 1 | T09 |
| **Total registrado** | **11** | **10 elegíveis + 1 excluída** |

Entre os casos inadequados, os registros T01, T02 e T03 mostram que o campo CPF do cadastro ficou destacado em vermelho, mas sem mensagem explicativa. Em T04, o campo vazio impediu o prosseguimento, porém não apresentou orientação textual. Em T05 e T10, a resposta “Realize o procedimento de segurança” não explicou qual informação deveria ser corrigida. 

Nos registros T06, T07 e T08, o formulário de login apresentou avisos relacionados ao preenchimento do CPF/CNPJ; em T11, apresentou o aviso “Senha é obrigatória”. Esses quatro casos foram classificados como adequados na ficha de coleta.

## 4. Cálculo da M2

A fórmula estabelecida na Fase 2 é:

`M2 = 100 × V / N`

Em que:

- `V` = número de tentativas inválidas tratadas adequadamente;
- `N` = número de tentativas inválidas elegíveis.

Substituindo os valores coletados:

`M2 = 100 × 4 / 10 = 40%`

**Resultado da M2: 40%.**

## 5. Interpretação e julgamento

A escala da Fase 2 classifica resultados inferiores a 60% como **Insatisfatório**; de 60% a menos de 80% como **Mínimo aceitável**; de 80% a menos de 95% como **Alvo**; e a partir de 95% como **Excelente**.

| Referência | Critério | Resultado | Avaliação |
|---|---:|---:|---|
| Mínimo para sair de Insatisfatório | 60% | 40% | Não atingido |
| H2 | ≥ 80% | 40% | Não sustentada |
| Classificação da M2 | Faixas da Fase 2 | 40% | **Insatisfatório** |

A hipótese H2 não foi sustentada. Em seis das dez tentativas elegíveis, a interface não forneceu o conjunto de respostas esperado. Os registros indicam dois tipos principais de deficiência: campos destacados sem explicação do problema e mensagens genéricas que não identificam a informação que precisa ser corrigida.

O resultado também evidencia que a validação visual ou o bloqueio do botão, quando não acompanhados de instruções, não são suficientes para orientar o usuário. Essa distinção é central para a Q2: a avaliação não mede apenas se o sistema impede o envio, mas se ajuda o usuário a compreender e corrigir a entrada inválida.

## 6. Resposta à questão GQM

**Q2 — Os formulários ajudam a corrigir entradas inválidas?**

Parcialmente, mas o resultado geral é insatisfatório. Quatro das dez tentativas elegíveis receberam uma resposta classificada como adequada (40%). Nas demais, houve ausência de mensagem explicativa ou apresentação de mensagem genérica, sem indicação clara do campo ou dado a corrigir. Portanto, os formulários não atenderam à hipótese de que pelo menos 80% das entradas inválidas seriam sinalizadas com orientação de correção.

## 7. Oportunidades de melhoria

Com base nos casos observados, recomenda-se:

1. **Explicitar o erro junto ao campo:** substituir apenas a borda vermelha por uma mensagem textual que informe o problema, como quantidade insuficiente de dígitos ou formato inválido.
2. **Diferenciar obrigatoriedade de formato inválido:** informar “Campo obrigatório” quando estiver vazio e explicar o formato esperado quando o valor estiver preenchido incorretamente.
3. **Substituir mensagens genéricas:** revisar respostas como “Realize o procedimento de segurança” para que indiquem a ação necessária sem revelar informações sensíveis.
4. **Padronizar o feedback entre cadastro e login:** manter mensagens consistentes, específicas e compreensíveis, respeitando as regras de segurança do processo de autenticação.

Essas melhorias devem ser verificadas por uma nova rodada com entradas equivalentes às utilizadas nesta coleta, preservando o critério de sucesso definido na Fase 2.

## 8. Evidências e rastreabilidade

As evidências originais estão em `docs/evidencias/M2/`:

| Arquivo | Conteúdo |
|---|---|
| `M2-Tabela-16112026-03.png` | Ficha consolidada dos onze registros, com classificação de adequação e status de elegibilidade |
| `M2-U02-16112026-01.png` | Capturas das entradas inválidas nos formulários de cadastro e login |
| `M2-U02-16112026-02.png` | Capturas adicionais das respostas apresentadas pelo login e cadastro |

A ficha consolidada é a fonte dos numeradores, denominadores, exclusões e classificações utilizados neste resultado. As capturas de tela ilustram as respostas observadas. Os arquivos permitem rastrear o percentual calculado até os registros individuais.

## 9. Limitações

A coleta representa os campos e fluxos acessíveis nas condições observadas em 16/11/2026. Não foram realizados envios que pudessem concluir operações ou alterar dados. A métrica não avalia a implementação interna da validação, mas o feedback perceptível ao usuário. O registro T09 foi excluído conforme a ficha original; sua exclusão deve ser mantida na consolidação dos dados.

## 10. Conclusão

A M2 obteve **40%**, resultado classificado como **Insatisfatório**. A hipótese H2 não foi sustentada, pois o percentual ficou abaixo do limite de 80% e até mesmo do patamar de 60% necessário para a classificação mínima aceitável. A principal oportunidade de melhoria é tornar as mensagens de validação específicas e orientativas, sem depender apenas de destaque visual ou de mensagens genéricas.
