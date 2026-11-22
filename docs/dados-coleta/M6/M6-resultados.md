# M6 — Consistência de informações estáveis (S-02)

## 1. Objetivo e relação com o GQM

A M6 verifica se campos cadastrais e declaratórios que devem permanecer inalterados mantêm exatamente os mesmos valores em emissões consecutivas da Agência Virtual da Neoenergia Brasília, sem qualquer modificação cadastral no intervalo.

- **Objetivo GQM:** G3 — Segurança (Integridade / Não repúdio — indicador indireto).
- **Questão:** Q6 — Informações estáveis permanecem iguais em consultas consecutivas?
- **Hipótese:** H6 — Ao menos 95% das comparações de campos estáveis do Nada Consta serão consistentes.
- **Métrica:** M6 — Consistência de informações estáveis.
- **Cenário:** S-02.

Na especificação do projeto, eram previstas no mínimo 5 emissões de relatório e no mínimo 20 comparações elegíveis. Ao realizar cinco emissões consecutivas do relatório de *Nada Consta* e comparar sete campos estáveis de cada emissão subsequente contra a primeira emissão de referência, obtiveram-se **28 comparações elegíveis**, atendendo com folga a ambos os critérios mínimos.

## 2. Método e condições da coleta

As cinco emissões sucessivas da Declaração de Quitação Anual de Débitos (*Nada Consta*) foram realizadas por Henrique em **17/11/2026, entre 17h12 e 17h15**, utilizando conta própria autorizada, consolidadas no arquivo `M6-registros.csv`:

- **Ambiente de referência:** computador pessoal (desktop), sistema operacional Windows 11, navegador Microsoft Edge (`v. 157.0.4341.60`) com cache padrão habilitado e conexão cabeada (Ethernet).
- **Cronologia das emissões:** 1ª emissão às **17h12** (referência-base), 2ª e 3ª emissões às **17h14**, e 4ª e 5ª emissões às **17h15**, todas na mesma sessão autenticada e sem alterações cadastrais no intervalo.
- **Critério de comparação e privacidade:** os valores exibidos nas Emissões 2, 3, 4 e 5 foram comparados campo a campo com os da Emissão 1 (`Emissão 1 × Emissão 2`, `1 × 3`, `1 × 4` e `1 × 5`), registrando-se apenas a classificação (`Igual`, `Divergente` ou `Não comparável`) por código de campo, sem transcrever dados pessoais ou financeiros na planilha.
- **Classificação dos campos do documento:**
  - **Campos estáveis (`C01` a `C07`):** Nome do consumidor atual (`C01`), CPF/CNPJ do consumidor (`C02`), Endereço da unidade consumidora/expediente (`C03`), Município e Estado — BRASILIA/DF (`C04`), Conta Contrato (`C05`), Período de quitação — `01/01/2025 a 31/12/2025` (`C06`) e Declaração de inexistência de débitos — `2025 e anos anteriores` (`C07`).
  - **Campos dinâmicos (`D01` a `D03`):** Data e hora de emissão/impressão (`D01`), Número do pedido de serviço (`D02`) e Código de Autenticação (`D03`), excluídos das comparações de igualdade por serem gerados individualmente a cada emissão.

## 3. Resultados por campo

| Código | Campo observado no documento | Natureza | Emissão 1 × 2 | Emissão 1 × 3 | Emissão 1 × 4 | Emissão 1 × 5 | Interpretação |
|---|---|---|---|---|---|---|---|
| `C01` | Nome do consumidor atual | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — exibido sem alteração em todas as emissões |
| `C02` | CPF/CNPJ do consumidor | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — exibido sem alteração em todas as emissões |
| `C03` | Endereço da unidade consumidora/expediente | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — exibido sem alteração em todas as emissões |
| `C04` | Município e Estado (`BRASILIA` / `DF`) | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — exibido sem alteração em todas as emissões |
| `C05` | Conta Contrato | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — exibido sem alteração em todas as emissões |
| `C06` | Período de quitação (`01/01/2025 a 31/12/2025`) | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — exibido sem alteração em todas as emissões |
| `C07` | Declaração de inexistência de débitos (`2025 e anos anteriores`) | Estável | Igual | Igual | Igual | Igual | **Consistente (4/4)** — texto declaratório e exercício mantidos integralmente |
| `D01` | Data e hora de emissão/impressão | Dinâmico | Não comparável | Não comparável | Não comparável | Não comparável | **Excluído (4)** — registra o instante exato de cada emissão (`17:12` a `17:15`) |
| `D02` | Número do pedido de serviço | Dinâmico | Não comparável | Não comparável | Não comparável | Não comparável | **Excluído (4)** — identificador transacional único gerado a cada solicitação |
| `D03` | Código de Autenticação | Dinâmico | Não comparável | Não comparável | Não comparável | Não comparável | **Excluído (4)** — código verificador único gerado para cada documento emitido |

### Observações relevantes

**Estabilidade integral dos dados cadastrais e declaratórios (`C01` a `C07`).** Em todos os pares comparados contra a primeira emissão, os sete campos estáveis mantiveram exatamente o mesmo conteúdo, sem truncamento, perda de formatação ou variação entre consultas realizadas em sequência.

**Separação entre campos estáveis e metadados transacionais (`D01` a `D03`).** Conforme previsto na regra de exclusão da Fase 2, o carimbo de data/hora, o número do pedido de serviço e o código de autenticação variam legitimamente a cada documento gerado, sendo registrados como *Não comparável* (`Excluída`) para não distorcer o denominador da métrica.

**Limite de interpretação da consistência visual.** A coincidência de 100% entre as emissões demonstra estabilidade na apresentação das informações pela interface web, mas não comprova isoladamente os mecanismos internos de proteção do banco de dados contra alterações não autorizadas.

## 4. Cálculo e julgamento da M6

A fórmula definida na Fase 2 é:

`M6 = 100 × C / N`

Em que:

- `C` = número de comparações consistentes;
- `N` = número de comparações elegíveis da mesma referência.

Consolidando os 40 registros documentados em `M6-registros.csv`:

- **Comparações elegíveis (`N = 28`):** `7` campos estáveis (`C01` a `C07`) × `4` pares de comparação contra a Emissão 1 (atendendo aos mínimos de 5 e 20 comparações da documentação);
- **Registros excluídos (`12`):** `3` campos dinâmicos (`D01` a `D03`) × `4` pares de comparação, excluídos com justificativa por serem variáveis por natureza;
- **Comparações consistentes (`C = 28`):** todos os 28 pares elegíveis apresentaram valores idênticos.

Aplicando a fórmula:

`M6 = 100 × 28 / 28 = 100%`

- **Classificação da métrica:** **Excelente** (`100%` na escala específica da M6).
- **Julgamento da hipótese H6 (`M6 ≥ 95%`):** **Sustentada**.

## 5. Resposta à questão GQM

**Q6 — Informações estáveis permanecem iguais em consultas consecutivas?**

Sim. Nas 28 comparações realizadas sobre os sete campos estáveis da Declaração de Quitação Anual de Débitos (*Nada Consta*), **100%** dos valores permaneceram idênticos entre a emissão de referência e as quatro emissões consecutivas realizadas na mesma sessão. Com classificação **Excelente**, a hipótese **H6** foi sustentada dentro do escopo observável na interface da Agência Virtual.

## 6. Oportunidades de melhoria

1. **Revisão ortográfica no cabeçalho do comprovante:** no topo do documento emitido consta o texto *"Pedido de serviço para Declaração de Quitação Anual de Débitoss"* (com consoante duplicada ao final de *"Débitos"*), cuja correção aprimora a apresentação formal do relatório.
2. **Inclusão de QR Code para validação rápida:** embora o rodapé informe o código de autenticação e o número da conta contrato para validação no site da Neoenergia Brasília, adicionar um QR Code direto para o endereço de verificação facilitaria a conferência de autenticidade por terceiros (aspecto avaliado na M13).

## 7. Evidências e rastreabilidade

Os dados brutos e as capturas anonimizadas das cinco emissões estão organizados em `docs/evidencias/M6/`:

| Arquivo | Registro |
|---|---|
| [`M6-17112026-01.png`](../../evidencias/M6/M6-17112026-01.png) | Captura anonimizada da 1ª emissão do relatório de Nada Consta (17h12 — emissão de referência) |
| [`M6-17112026-02.png`](../../evidencias/M6/M6-17112026-02.png) | Captura anonimizada da 2ª emissão do relatório de Nada Consta (17h14) |
| [`M6-17112026-03.png`](../../evidencias/M6/M6-17112026-03.png) | Captura anonimizada da 3ª emissão do relatório de Nada Consta (17h14) |
| [`M6-17112026-04.png`](../../evidencias/M6/M6-17112026-04.png) | Captura anonimizada da 4ª emissão do relatório de Nada Consta (17h15) |
| [`M6-17112026-05.png`](../../evidencias/M6/M6-17112026-05.png) | Captura anonimizada da 5ª emissão do relatório de Nada Consta (17h15) |

## 8. Limitações e pendências de consistência

1. **Alcance da evidência de integridade:** conforme delimitado na Fase 2 e na Fase 3, a consistência observada na M6 refere-se exclusivamente à estabilidade da apresentação dos dados em consultas próximas, não comprovando a proteção do armazenamento interno contra modificações indevidas.
2. **Reutilização das emissões na M13:** conforme previsto no plano de coleta, os cinco documentos emitidos nesta etapa são reutilizados como amostra documental para a verificação de autenticidade no canal oficial da concessionária na métrica M13.

## 9. Conclusão

A métrica **M6** atingiu **100% (`28/28` comparações elegíveis consistentes)**, recebendo classificação **Excelente** e sustentando a hipótese **H6**. A Agência Virtual manteve todos os campos cadastrais e declaratórios do relatório de *Nada Consta* perfeitamente íntegros e uniformes ao longo das cinco emissões consecutivas avaliadas.