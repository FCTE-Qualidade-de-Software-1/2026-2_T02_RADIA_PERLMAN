# M3 — Execuções sem falhas observáveis (R-01)

A coleta da M3 foi realizada em 19/11/2026, em dois períodos: manhã e tarde. Foram avaliados dois fluxos da Agência Virtual da Neoenergia Brasília: a abertura do Histórico de Consumo e a emissão de segunda via a partir do histórico.

## 1. Fluxos avaliados

### R01-F1 — Abertura do Histórico de Consumo

- **Condição inicial:** sessão autenticada na página inicial da Agência Virtual.
- **Ação:** acessar a opção “Histórico de Consumo”.
- **Resultado esperado:** apresentação da tabela de faturas para consulta.
- **Resultado obtido:** a tabela foi apresentada nas dez execuções, sem falhas observáveis.

### R01-F2 — Emissão de segunda via a partir do Histórico de Consumo

- **Condição inicial:** sessão autenticada, com a tabela do Histórico de Consumo aberta.
- **Ação:** selecionar a opção de segunda via de uma fatura.
- **Resultado esperado:** geração e disponibilização da segunda via para visualização.
- **Resultado obtido:** nove execuções foram concluídas. Em uma tentativa, às 08:46, a interface apresentou a mensagem “Nosso sistema está indisponível no momento” e a emissão não foi concluída.

## 2. Resultados

| Fluxo | Período | Execuções | Sem falha | Com falha |
|---|---|---:|---:|---:|
| R01-F1 — Abertura do Histórico de Consumo | Manhã | 5 | 5 | 0 |
| R01-F1 — Abertura do Histórico de Consumo | Tarde | 5 | 5 | 0 |
| **R01-F1 — Total** | **Manhã e tarde** | **10** | **10** | **0** |
| R01-F2 — Emissão de segunda via | Manhã | 5 | 4 | 1 |
| R01-F2 — Emissão de segunda via | Tarde | 5 | 5 | 0 |
| **R01-F2 — Total** | **Manhã e tarde** | **10** | **9** | **1** |

## 3. Cálculo da M3

A métrica é calculada separadamente para cada fluxo:

`M3(f) = 100 × E(f) / N(f)`

Em que:

- `E(f)` corresponde ao número de execuções sem falha observável no fluxo;
- `N(f)` corresponde ao total de execuções elegíveis do mesmo fluxo.

**R01-F1 — Abertura do Histórico de Consumo**

`M3(F1) = 100 × 10 / 10 = 100%`

**R01-F2 — Emissão de segunda via**

`M3(F2) = 100 × 9 / 10 = 90%`

Os resultados são mantidos separados por fluxo, sem agrupamento das duas funcionalidades em um único percentual. Considerando o critério de H3 definido na Fase 2 (M3(f) ≥ 80% para cada fluxo elegível com amostra mínima), os dois fluxos atingiram o limite estabelecido.

## 4. Registro das execuções e evidências

As vinte execuções estão registradas individualmente no arquivo `M3-resultados.csv`, com data, horário, avaliador, fluxo, período, condições iniciais, ação executada, resultado esperado, resultado observado e evidência correspondente.

As capturas estão organizadas em `docs/evidencias/M3/`:

| Arquivo | Registro |
|---|---|
| `historicoConsumo-19112026-manha-arthur.png` | Abertura do Histórico de Consumo no período da manhã |
| `historicoConsumo-19112026-tarde-arthur.png` | Abertura do Histórico de Consumo no período da tarde |
| `segundaVia-19112026-manha-arthur.png` | Emissão de segunda via no período da manhã |
| `segundaVia-19112026-tarde-arthur.png` | Emissão de segunda via no período da tarde |
| `segundaVia-19112026-erro-01-arthur.png` | Mensagem de indisponibilidade apresentada às 08:46 |

As capturas de sucesso registram o comportamento observado em cada fluxo e período. A captura da mensagem de indisponibilidade documenta a falha registrada na quinta tentativa do fluxo R01-F2.

## 5. Ambiente de execução

| Campo | Registro |
|---|---|
| Avaliador | Arthur |
| Data da coleta | 19/11/2026 |
| Dispositivo | Dell Inspiron 15 3511 — Intel Core i5-1135G7 — 8 GB RAM |
| Sistema operacional | Fedora Linux 44 (Sway Spin) |
| Navegador | Mozilla Firefox, versão mais recente disponível na data da coleta |
| Conexão | Wi-Fi 5 GHz |
| Condição da conexão | Estável, conforme informado pelo avaliador |
| VPN | Não utilizada |

## 6. Execuções fora de pico (20/11/2026)

As mesmas execuções de R-01 foram realizadas por Tiago na janela fora de pico, em 20/11/2026, a partir das 03:41. Foram avaliados os dois fluxos da seção 1, com dez execuções por fluxo e as mesmas condições iniciais, ações e resultados esperados. Os horários individuais das execuções não foram registrados.

### 6.1 Resultados

| Fluxo | Período | Execuções | Sem falha | Com falha |
|---|---|---:|---:|---:|
| R01-F1 — Abertura do Histórico de Consumo | Madrugada | 10 | 10 | 0 |
| R01-F2 — Emissão de segunda via | Madrugada | 10 | 10 | 0 |

### 6.2 Cálculo da M3 fora de pico

**R01-F1 — Abertura do Histórico de Consumo**

`M3(F1) = 100 × 10 / 10 = 100%`

**R01-F2 — Emissão de segunda via**

`M3(F2) = 100 × 10 / 10 = 100%`

Os resultados fora de pico são mantidos separados dos resultados de 19/11/2026 e por fluxo. Em ambos os fluxos, o critério de H3 (M3(f) ≥ 80%) foi atendido nesta janela. A falha registrada às 08:46 de 19/11/2026 não se repetiu.

### 6.3 Registro das execuções e evidências

As vinte execuções fora de pico estão registradas individualmente no arquivo `M3-resultados.csv`, com os identificadores `M3-R01-F1-20261120-01` a `M3-R01-F2-20261120-10`.

As capturas estão organizadas em `docs/evidencias/M3/`:

| Arquivo | Registro |
|---|---|
| `historicoConsumo-20112026-01-tiago.png` | Tabela do Histórico de Consumo fora de pico |
| `segundaVia-20112026-01-tiago.png` | Segunda via emitida fora de pico |

As capturas são representativas das execuções, e não existe uma captura para cada execução. Dados pessoais foram cobertos nas imagens.

### 6.4 Ambiente de execução

| Campo | Registro |
|---|---|
| Avaliador | Tiago |
| Data da coleta | 20/11/2026, a partir das 03:41 |
| Janela de coleta | Fora de pico |
| Dispositivo | Predator Helios Neo 16 — Intel Core Ultra 9 — 32 GB RAM |
| Sistema operacional | Windows 11 |
| Navegador | Google Chrome, versão mais recente disponível na data da coleta; número exato não registrado |
| Conexão | Wi-Fi 5 GHz |
| VPN | Não utilizada |
