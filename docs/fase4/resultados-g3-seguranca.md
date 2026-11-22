# Resultados de G3 — Segurança

Esta página apresenta os resultados do objetivo G3, que avalia a autenticação no login e no cadastro, a proteção das páginas restritas após o logout e a consistência e a autenticidade do relatório de Nada Consta.

As fórmulas, as faixas de pontuação e as quantidades mínimas são as definidas em [Métricas](../fase2/metricas.md) e nos [Critérios de julgamento](../fase2/criterios-julgamento.md). Os dados brutos estão relacionados em [Dados brutos e evidências](dados-brutos.md).

## M6 — Consistência de informações estáveis

As medições da M6, vinculadas ao cenário S-02, foram realizadas em 17/11/2026, entre 17h12 e 17h15. Foram emitidas cinco vias consecutivas da Declaração de Quitação Anual de Débitos (Nada Consta) na mesma sessão autenticada, sem alterações cadastrais no intervalo. Sete campos estáveis (`C01` a `C07`) das Emissões 2, 3, 4 e 5 foram comparados com a Emissão 1 de referência, totalizando 28 comparações elegíveis, além de três campos dinâmicos (`D01` a `D03`) excluídos por variarem a cada documento gerado.

**Tabela 1 — Resultados por campo observado no Nada Consta**

| Código | Campo observado | Natureza | Consistentes (C) | Elegíveis (N) | M6 = 100 × C/N | Interpretação |
|---|---|---|---:|---:|---:|---|
| `C01` | Nome do consumidor atual | Estável | 4 | 4 | 100% | Consistente |
| `C02` | CPF/CNPJ do consumidor | Estável | 4 | 4 | 100% | Consistente |
| `C03` | Endereço da unidade consumidora/expediente | Estável | 4 | 4 | 100% | Consistente |
| `C04` | Município e Estado (`BRASILIA` / `DF`) | Estável | 4 | 4 | 100% | Consistente |
| `C05` | Conta Contrato | Estável | 4 | 4 | 100% | Consistente |
| `C06` | Período de quitação (`01/01/2025 a 31/12/2025`) | Estável | 4 | 4 | 100% | Consistente |
| `C07` | Declaração de inexistência de débitos (`2025 e anos anteriores`) | Estável | 4 | 4 | 100% | Consistente |
| `D01`–`D03` | Data/hora de emissão, nº do pedido e código de autenticação | Dinâmico | — | — | — | Excluídos (12 registros) |

_Fonte: [M6-registros.csv](../dados-coleta/M6/M6-registros.csv), Equipe Radia Perlman, 2026._

Todos os sete campos cadastrais e declaratórios estáveis mantiveram valores idênticos entre a emissão de referência e as quatro emissões subsequentes, sem perda de formatação ou divergência de conteúdo. Os campos transacionais dinâmicos (`D01` a `D03`) foram registrados como não comparáveis e excluídos do denominador com justificativa.

O cálculo da métrica considerou todas as 28 comparações elegíveis:

- **M6:** `M6 = 100 × C / N = 100 × 28 / 28 = 100%`.

A classificação consolidada da M6 é **Excelente** (`100%` na escala específica da métrica). A hipótese H6, que exige pelo menos 95% de comparações consistentes nos campos estáveis do Nada Consta, foi **sustentada**.

### Ambiente e evidências

A coleta foi realizada em um computador pessoal (desktop), sistema operacional Windows 11, navegador Microsoft Edge (versão `157.0.4341.60`, com cache padrão habilitado) e conexão cabeada (Ethernet), utilizando conta própria autorizada.

Os registros visuais incluem as capturas anonimizadas das cinco emissões consecutivas ([emissão 01](../evidencias/M6/M6-17112026-01.png), [emissão 02](../evidencias/M6/M6-17112026-02.png), [emissão 03](../evidencias/M6/M6-17112026-03.png), [emissão 04](../evidencias/M6/M6-17112026-04.png) e [emissão 05](../evidencias/M6/M6-17112026-05.png)). O detalhamento completo está disponível na [documentação de coleta da M6](../dados-coleta/M6/M6-resultados.md).

A consistência observada na M6 refere-se exclusivamente à estabilidade visual dos dados apresentados pela interface web, não comprovando isoladamente a integridade do armazenamento interno.

## M12 — Itens de autenticidade e responsabilização atendidos

As medições da M12, vinculadas ao cenário S-03, foram executadas em duas rodadas por item em dias distintos: os itens `A1` a `A4` foram verificados em 16/11/2026 (21h30) e 17/11/2026 (20h20), enquanto os itens `R1` e `R2` foram verificados em 17/11/2026 (16h50–16h54) e 19/11/2026 (14h44–14h47).

**Tabela 2 — Resultados por item de verificação**

| Item | Verificação prevista | 1ª rodada | 2ª rodada | Resultado consolidado | Situação |
|---|---|---|---|---|---|
| `A1` | Credencial incorreta é rejeitada | Atendido | Atendido | Atendido | Elegível |
| `A2` | Mensagem não indica qual credencial está incorreta | Não atendido | Não atendido | Não atendido | Elegível |
| `A3` | Sessão expira após inatividade | Inconclusivo | Não atendido | Inconclusivo | Excluído |
| `A4` | Cadastro exige comprovação de vínculo ou identidade | Atendido  | Atendido  | Atendido | Elegível |
| `R1` | Sistema exibe ou notifica registro de acesso | Não atendido | Não atendido | Não atendido | Elegível |
| `R2` | Emissões geram identificador ou protocolo associado ao titular | Atendido  | Atendido  | Atendido | Elegível |

_Fonte: [M12-registros.csv](../dados-coleta/M12/M12-registros.csv), Equipe Radia Perlman, 2026._

Dos seis itens previstos, três foram atendidos nas duas rodadas (`A1`, `A4` e `R2`). O item `A2` falhou por exibir a mensagem *“Usuário com CPF/CNPJ informado não foi encontrado”* mesmo diante de CPF cadastrado e senha incorreta, revelando qual credencial falhou. O item `R1` falhou por não apresentar registro de último acesso nem notificação de novo login. Já o item `A3` foi retirado do denominador como inconclusivo devido à mensagem de indisponibilidade do portal na primeira rodada, divergindo da permanência da sessão observada após 60 minutos na segunda rodada.

Com cinco itens elegíveis (`N = 5`), atingindo o mínimo exigido pela Fase 2, o cálculo da métrica foi:

- **M12:** `M12 = 100 × A / N = 100 × 3 / 5 = 60%`.

A classificação consolidada da M12 é **Mínimo aceitável** (faixa de 60% a menos de 80%). A hipótese H12, que exige pelo menos 80% dos itens elegíveis atendidos, **não foi sustentada**.

### Ambiente e evidências

A coleta foi realizada em computadores pessoais com sistema operacional Windows 11, navegador Microsoft Edge e conta própria autorizada, utilizando conexão Wi-Fi nas verificações de `A1` a `A4` e conexão cabeada (Ethernet) nas verificações de `R1` e `R2`.

Os registros visuais e documentais incluem a [ficha consolidada de A1 a A4](../evidencias/M12/M12-A1-A4-17112026-01.pdf), a [captura de erro de login (A1/A2)](../evidencias/M12/M12-A1-A2-17112026-02.png), os registros de ausência de aviso de acesso em R1 ([1ª rodada](../evidencias/M12/M12-R1-17112026-01.png) e [2ª rodada](../evidencias/M12/M12-R1-19112026-02.png)) e as capturas de geração de protocolo em R2 ([1ª rodada](../evidencias/M12/M12-R2-17112026-01.png) e [2ª rodada](../evidencias/M12/M12-R2-19112026-02.png)). A análise detalhada consta na [documentação de coleta da M12](../dados-coleta/M12/M12-resultados.md).

## M13 — Documentos com autenticidade verificável

As medições da M13, vinculadas ao cenário S-04, foram realizadas em 17/11/2026, às 17h23, reutilizando os cinco relatórios de Nada Consta emitidos na M6. Para cada documento, verificou-se a existência de mecanismo de comprovação (critério `a`) e a possibilidade de confirmar a autenticidade no canal oficial indicado no próprio relatório (critério `b`).

**Tabela 3 — Resultados da verificação de autenticidade por documento**

| Identificação | Documento avaliado | Critério (a): Mecanismo | Critério (b): Verificação no canal oficial | Classificação | Situação |
|---|---|---|---|---|---|
| `M13-S04-17112026-01` | Emissão 1 (reutilizada da M6) | Sim (código + conta contrato) | Não (validador inexistente no site indicado) | Falha | Elegível |
| `M13-S04-17112026-02` | Emissão 2 (reutilizada da M6) | Sim (código + conta contrato) | Não (validador inexistente no site indicado) | Falha | Elegível |
| `M13-S04-17112026-03` | Emissão 3 (reutilizada da M6) | Sim (código + conta contrato) | Não (validador inexistente no site indicado) | Falha | Elegível |
| `M13-S04-17112026-04` | Emissão 4 (reutilizada da M6) | Sim (código + conta contrato) | Não (validador inexistente no site indicado) | Falha | Elegível |
| `M13-S04-17112026-05` | Emissão 5 (reutilizada da M6) | Sim (código + conta contrato) | Não (validador inexistente no site indicado) | Falha | Elegível |

_Fonte: [M13-registros.csv](../dados-coleta/M13/M13-registros.csv), Equipe Radia Perlman, 2026._

Embora os cinco documentos apresentem um código de autenticação e instruam o usuário a acessar `https://www.neoenergia.com/brasilia` com o número da conta contrato para validar o comprovante, o portal oficial indicado não disponibiliza ferramenta de consulta ou validação para esse documento, nem o PDF possui assinatura digital verificável em leitor padrão.

O cálculo da métrica considerou os cinco documentos emitidos elegíveis:

- **M13:** `M13 = 100 × W / N = 100 × 0 / 5 = 0%`.

Pela regra binária estabelecida nos critérios de julgamento, a classificação da M13 é **Insatisfatório** (qualquer valor abaixo de 100%). A hipótese H13, que exige 100% dos relatórios com autenticidade verificável, **não foi sustentada**.

### Ambiente e evidências

A verificação foi conduzida em um computador pessoal (desktop), sistema operacional Windows 11, navegador Microsoft Edge (versão `157.0.4341.60`) e conexão cabeada (Ethernet), preservando o sigilo dos PDFs originais e dos códigos de autenticação.

Os registros visuais incluem a [página inicial indicada no link](../evidencias/M13/M13-17112026-01.png) e a [navegação pelas seções de serviços e login do portal](../evidencias/M13/M13-17112026-02.png) (demonstrando a ausência do validador), além das capturas anonimizadas das cinco emissões do Nada Consta ([01](../evidencias/M6/M6-17112026-01.png), [02](../evidencias/M6/M6-17112026-02.png), [03](../evidencias/M6/M6-17112026-03.png), [04](../evidencias/M6/M6-17112026-04.png) e [05](../evidencias/M6/M6-17112026-05.png)). O detalhamento completo consta na [documentação de coleta da M13](../dados-coleta/M13/M13-resultados.md).


## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da estrutura da página | Beatriz |
| 1.1 | 22/11/2026 | Inclusão dos cálculos e resultados de M6, M12 e M13 | Henrique |