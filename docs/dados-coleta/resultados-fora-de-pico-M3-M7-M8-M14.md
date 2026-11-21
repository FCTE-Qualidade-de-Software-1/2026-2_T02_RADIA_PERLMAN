# Resultados da coleta fora de pico — M3, M7, M8 e M14

Coleta realizada em **20/11/2026**, a partir das **03:41**, pelo avaliador **Tiago**, na janela **fora de pico**. Os fluxos e os eventos de início e fim seguem os mesmos da coleta de pico de Arthur (19/11/2026), para que as duas janelas sejam comparáveis.



## 1. M3 — Execuções sem falhas observáveis (R-01)

| Fluxo | Execuções | Sem falha | Com falha | M3 |
|---|---:|---:|---:|---:|
| R01-F1 — Abertura do Histórico de Consumo | 10 | 10 | 0 | 100% |
| R01-F2 — Emissão de segunda via a partir do Histórico de Consumo | 10 | 10 | 0 | 100% |

`M3(f) = 100 × E(f) / N(f)`

- `M3(F1) = 100 × 10 / 10 = 100%`
- `M3(F2) = 100 × 10 / 10 = 100%`

**Julgamento:** a H3 (M3(f) ≥ 80% em cada fluxo) foi atendida nos dois fluxos, nesta janela. A tentativa com falha da coleta de pico (08:46) não se repetiu fora de pico.

## 2. M7 — Mediana do tempo de resposta

Dez durações válidas por fluxo, em segundos, na ordem de coleta.

| Fluxo | Durações (s) | Mediana (s) |
|---|---|---:|
| M7-F1 — Login | 3,78; 2,57; 3,60; 2,21; 3,42; 2,34; 2,56; 2,44; 2,23; 2,29 | **2,50** |
| M7-F2 — Indicadores de continuidade | 3,87; 2,84; 5,70; 2,69; 7,99; 2,85; 2,29; 3,73; 3,89; 11,71 | **3,80** |
| M7-F3 — Geração do PDF da segunda via | 4,17; 3,24; 4,60; 2,99; 3,52; 3,49; 3,24; 4,45; 5,28; 4,32 | **3,85** |

Mediana calculada com n = 10, como a média dos 5º e 6º valores ordenados. Não houve timeouts nem falhas nas durações registradas.

| Fluxo | Mediana (s) | Faixa (escala M7) | H7 (≤ 3 s) |
|---|---:|---|---|
| Login | 2,50 | Alvo (> 2 s até 3 s) | Atendida |
| Indicadores de continuidade | 3,80 | Mínimo aceitável (> 3 s até 5 s) | Não atendida |
| PDF da segunda via | 3,85 | Mínimo aceitável (> 3 s até 5 s) | Não atendida |

A H7 exige mediana ≤ 3 s em todos os fluxos. O login a atendeu, mas os indicadores e o PDF da segunda via não, então a H7 não é sustentada nesta janela.

## 3. M8 — Percentil 90 do tempo de resposta

Método do posto mais próximo: `posição = ⌈0,9 × n⌉ = ⌈0,9 × 10⌉ = 9`. O P90 é o 9º menor valor de cada série.

| Fluxo | 9º menor valor = P90 (s) | Faixa (escala M8) | H8 (≤ 5 s) |
|---|---:|---|---|
| Login | **3,60** | Alvo (> 3 s até 5 s) | Atendida |
| Indicadores de continuidade | **7,99** | Mínimo aceitável (> 5 s até 8 s) | Não atendida |
| PDF da segunda via | **4,60** | Alvo (> 3 s até 5 s) | Atendida |

A H8 exige P90 ≤ 5 s em todos os fluxos. Login e PDF da segunda via a atenderam; os indicadores não, então a H8 não é sustentada nesta janela. Com 10 observações, um único valor alto muda o P90: nos indicadores, o P90 é 7,99 s, mas existe uma duração de 11,71 s acima dele.

## 4. M14 — Razão entre pico e fora de pico

`M14(f) = mediana no pico / mediana fora do pico`

### C-F1 — Geração do PDF da segunda via

| Janela | Data | Avaliador | Execuções | Mediana (s) |
|---|---|---|---:|---:|
| Pico (manhã) | 19/11/2026 | Arthur | 10 | 4,015 |
| Fora de pico (madrugada) | 20/11/2026 | Tiago | 10 | 3,005 |

Durações fora de pico (s): 3,37; 2,54; 2,64; 3,87; 2,47; 3,80; 3,77; 3,67; 2,58; 2,35.

`M14(C-F1) = 4,015 / 3,005 ≈ 1,34`

**Julgamento:** 1,34 está na faixa **Alvo** (> 1,2 até 1,5), com a H14 atendida para o C-F1 (≤ 1,5). Isso corresponde a cerca de 34% de degradação no pico.


## 5. Observações

- A M7 e a M8 usam as mesmas durações, como previsto no protocolo.
- A comparação de M14 mistura avaliadores, dias e dispositivos diferentes. Isso é uma limitação a registrar no relatório.

## 6. Ambiente de execução

| Campo | Registro |
|---|---|
| Avaliador | Tiago |
| Data da coleta | 20/11/2026, a partir das 03:41 |
| Janela de coleta | Fora de pico |
| Dispositivo | Predator Helios Neo 16 Intel(R) Core(TM) Ultra 9  32 GB RAM |
| Sistema operacional | Windows 11 |
| Navegador e versão | Google Chrome, versão mais recente disponível na data da coleta; número exato não registrado |
| Conexão | Wi-Fi 5 GHz |
| VPN | Não utilizado  |
