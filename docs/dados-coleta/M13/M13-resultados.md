# M13 — Documentos com autenticidade verificável (S-04)

## 1. Objetivo e relação com o GQM

A M13 avalia se o relatório de *Nada Consta* (Declaração de Quitação Anual de Débitos) emitido pela Agência Virtual da Neoenergia Brasília dispõe de mecanismos eficazes para comprovar sua emissão e prevenir modificações não autorizadas, permitindo que terceiros verifiquem sua autenticidade no canal oficial indicado.

- **Objetivo GQM:** G3 — Segurança (Integridade / Não repúdio).
- **Questão:** Q13 — O relatório de Nada Consta pode ter sua autenticidade e sua emissão comprovadas?
- **Hipótese:** H13 — 100% dos relatórios de Nada Consta emitidos terão autenticidade verificável.
- **Métrica:** M13 — Documentos com autenticidade verificável.
- **Cenário:** S-04.

A Fase 2 estabelece a quantidade mínima de cinco documentos emitidos e elegíveis, reutilizando as emissões geradas na M6. Um documento só é considerado adequado quando atende simultaneamente a dois critérios: **(a)** possuir mecanismo de comprovação (como código de autenticação, QR Code ou assinatura digital) e **(b)** esse mecanismo confirmar a autenticidade e os mesmos dados do documento no canal oficial indicado ou no leitor de PDF. O julgamento da M13 é binário: apenas `100%` sustenta a hipótese H13 e recebe classificação **Excelente**; qualquer resultado inferior recebe classificação **Insatisfatório**.

## 2. Método e condições da coleta

As cinco verificações foram conduzidas por Henrique em **17/11/2026, às 17h23**, reutilizando os cinco relatórios de *Nada Consta* emitidos na M6 com conta própria autorizada, consolidadas no arquivo `M13-registros.csv`:

- **Ambiente de referência:** computador pessoal (desktop), sistema operacional Windows 11, navegador Microsoft Edge (`v. 157.0.4341.60`) com cache padrão habilitado e conexão cabeada (Ethernet).
- **Procedimento executado:**
  1. Inspecionou-se cada um dos cinco relatórios emitidos para verificar a presença de mecanismo de comprovação de autenticidade — critério **(a)**.
  2. Seguiu-se a instrução impressa no rodapé dos próprios documentos (*"Utilize o código de autenticação mais o número da conta contrato e acesse o site www.neoenergia.com/brasilia para validar a autenticidade deste documento"*), acessando [https://www.neoenergia.com/brasilia](https://www.neoenergia.com/brasilia) e navegando pelas seções de serviços e login do portal oficial para localizar a ferramenta de validação — critério **(b)**.
- **Sigilo e privacidade:** em conformidade com o protocolo de coleta, os PDFs originais e os valores do código de autenticação e da conta contrato não foram publicados no repositório.

## 3. Resultados por documento

| Identificação | Documento avaliado | Critério (a): Mecanismo presente | Canal indicado no documento | Critério (b): Autenticidade confirmada | Classificação | Situação |
|---|---|---|---|---|---|---|
| `M13-S04-17112026-01` | Emissão 1 (reutilizada da M6) | **Sim** (código de autenticação + conta contrato) | `https://www.neoenergia.com/brasilia` | **Não** (validador inexistente no portal indicado) | **Falha** | Elegível |
| `M13-S04-17112026-02` | Emissão 2 (reutilizada da M6) | **Sim** (código de autenticação + conta contrato) | `https://www.neoenergia.com/brasilia` | **Não** (validador inexistente no portal indicado) | **Falha** | Elegível |
| `M13-S04-17112026-03` | Emissão 3 (reutilizada da M6) | **Sim** (código de autenticação + conta contrato) | `https://www.neoenergia.com/brasilia` | **Não** (validador inexistente no portal indicado) | **Falha** | Elegível |
| `M13-S04-17112026-04` | Emissão 4 (reutilizada da M6) | **Sim** (código de autenticação + conta contrato) | `https://www.neoenergia.com/brasilia` | **Não** (validador inexistente no portal indicado) | **Falha** | Elegível |
| `M13-S04-17112026-05` | Emissão 5 (reutilizada da M6) | **Sim** (código de autenticação + conta contrato) | `https://www.neoenergia.com/brasilia` | **Não** (validador inexistente no portal indicado) | **Falha** | Elegível |

### Observações relevantes

- **Atendimento apenas parcial (critério a vs. critério b).** Todos os cinco relatórios emitidos exibem um código alfanumérico de autenticação e a instrução explícita para validá-lo juntamente com o número da conta contrato no endereço `www.neoenergia.com/brasilia`, atendendo ao critério **(a)**. Contudo, ao acessar o endereço indicado, o portal direciona apenas para a página institucional inicial, sem apresentar formulário, link ou seção para validação do documento.

- **Inexistência de ferramenta de validação na navegação do portal.** Além da página inicial indicada no link (`M13-17112026-01.png`), foi realizada navegação pelas demais áreas de atendimento, serviços e tela de login do site (`M13-17112026-02.png`), não sendo localizada nenhuma funcionalidade que aceite o código de autenticação e a conta contrato para conferir a autenticidade da Declaração de Quitação Anual de Débitos.

- **Ausência de assinatura digital verificável em leitor de PDF.** Os arquivos gerados também não contêm certificado digital ICP-Brasil incorporado que permita validar sua integridade diretamente em leitores de PDF padrão, tornando impossível comprovar a autenticidade do documento por qualquer meio oficial.

## 4. Cálculo e julgamento da M13

A fórmula definida na Fase 2 é:

`M13 = 100 × W / N`

Em que:

- `W` = número de documentos com autenticidade verificada nos critérios (a) e (b);
- `N` = número de documentos emitidos elegíveis.

Consolidando os registros de `M13-registros.csv`:

- **Documentos emitidos elegíveis (`N = 5`):** `M13-S04-17112026-01` a `M13-S04-17112026-05` (amostra mínima de 5 documentos atingida, sem exclusões);
- **Documentos com autenticidade verificada (`W = 0`):** nenhum dos cinco relatórios pôde ser validado no canal oficial indicado.

Aplicando a fórmula:

`M13 = 100 × 0 / 5 = 0%`

- **Classificação da métrica:** **Insatisfatório** (regra binária: qualquer resultado abaixo de `100%` é insatisfatório).
- **Julgamento da hipótese H13 (`M13 = 100%`):** **Não sustentada**.

## 5. Resposta à questão GQM

**Q13 — O relatório de Nada Consta pode ter sua autenticidade e sua emissão comprovadas?**

Não. Embora o relatório de *Nada Consta* informe um código de autenticação e instrua o cidadão ou terceiro interessado a validá-lo em `www.neoenergia.com/brasilia`, o site oficial indicado não disponibiliza nenhuma interface ou funcionalidade para realizar essa verificação, nem o arquivo possui assinatura digital validável em leitor de PDF. Com **0% (`0/5`)** de documentos verificáveis, a métrica recebeu classificação **Insatisfatório** e a hipótese **H13** não foi sustentada.

## 6. Oportunidades de melhoria

1. **Disponibilizar página pública de validação no portal indicado:** implementar e publicar em `www.neoenergia.com/brasilia` (com link direto visível no menu de serviços e na tela de acesso) o formulário de consulta que receba o **código de autenticação** e o **número da conta contrato**, retornando a confirmação da emissão e os dados essenciais da declaração para conferência.
2. **Incorporar QR Code com URL direta de verificação:** incluir no documento emitido um QR Code que aponte diretamente para a página do validador oficial, reduzindo erros de digitação e agilizando a conferência por terceiros.
3. **Adotar assinatura digital verificável no PDF (opcional/complementar):** assinar eletronicamente o PDF gerado com certificado digital institucional, permitindo validação offline de integridade e autoria em leitores de PDF convencionais.

## 7. Evidências e rastreabilidade

Os dados brutos e as capturas anonimizadas que comprovam tanto a presença da instrução no documento quanto a ausência da ferramenta de validação no portal estão organizados em `docs/evidencias/`:

| Arquivo | Registro |
|---|---|
| [`M13-17112026-01.png`](../../evidencias/M13/M13-17112026-01.png) | Captura da página inicial da Neoenergia Brasília (`www.neoenergia.com/brasilia`) indicada no documento, sem ferramenta de validação |
| [`M13-17112026-02.png`](../../evidencias/M13/M13-17112026-02.png) | Captura da navegação pelas seções de serviços e login do portal, confirmando a inexistência de validador para o relatório |
| [`M6-17112026-01.png`](../../evidencias/M6/M6-17112026-01.png) | Captura anonimizada da 1ª emissão do relatório de Nada Consta exibindo o código de autenticação e a instrução de validação no rodapé |
| [`M6-17112026-02.png`](../../evidencias/M6/M6-17112026-02.png) | Captura anonimizada da 2ª emissão do relatório de Nada Consta exibindo o código de autenticação e a instrução de validação no rodapé |
| [`M6-17112026-03.png`](../../evidencias/M6/M6-17112026-03.png) | Captura anonimizada da 3ª emissão do relatório de Nada Consta exibindo o código de autenticação e a instrução de validação no rodapé |
| [`M6-17112026-04.png`](../../evidencias/M6/M6-17112026-04.png) | Captura anonimizada da 4ª emissão do relatório de Nada Consta exibindo o código de autenticação e a instrução de validação no rodapé |
| [`M6-17112026-05.png`](../../evidencias/M6/M6-17112026-05.png) | Captura anonimizada da 5ª emissão do relatório de Nada Consta exibindo o código de autenticação e a instrução de validação no rodapé |

## 8. Limitações e pendências de consistência

1. **Restrição de publicação dos documentos originais:** conforme determinado no plano de recursos e ambiente, os PDFs completos do relatório de *Nada Consta* e os valores numéricos dos códigos de autenticação não foram anexados ao repositório público, sendo substituídos pelas capturas anonimizadas das emissões reutilizadas da M6.
2. **Impacto na consolidação do objetivo G3:** pelos critérios de julgamento da Fase 2, a classificação de cada objetivo GQM corresponde à menor classificação obtida entre suas métricas associadas (`M5`, `M6`, `M12` e `M13`). Assim, o resultado **Insatisfatório** da M13 determina diretamente o julgamento **Insatisfatório** para o objetivo **G3 (Segurança)** na síntese final da avaliação.

## 9. Conclusão

A métrica **M13** obteve **0% (`0/5` documentos com autenticidade verificável)**, recebendo classificação **Insatisfatório** e tornando a hipótese **H13 não sustentada**. Embora o comprovante emitido pela Agência Virtual apresente um código de autenticação e indique o portal `www.neoenergia.com/brasilia` para conferência, a ausência efetiva de uma ferramenta de validação no site impede que usuários ou terceiros comprovem a autenticidade e a integridade do documento.