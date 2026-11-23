# M8 — Registros para o percentil 90 do tempo de resposta

Este arquivo reúne os registros de tempo da M7 utilizados como base da M8. A coleta apresentada corresponde exclusivamente a um dos turnos previstos: a janela de pico realizada por Arthur em 19/11/2026. Os registros do turno fora de pico não estão incluídos.

## Fluxos registrados

| Código | Fluxo | Durações registradas |
|---|---|---:|
| F1 | Login | 10 |
| F2 | Indicadores de continuidade | 10 |
| F3 | Geração do PDF da segunda via | 10 |
| **Total** | | **30** |

## Origem dos dados

As durações foram reutilizadas dos registros individuais da M7, sem novas execuções. O arquivo `M8-registros.csv` mantém o identificador correspondente da observação de origem (`id_origem_m7`), a data, o horário, o avaliador, o fluxo, o tempo em segundos e as condições do ambiente.

As seis ocorrências adicionais de erro do login registradas na M7 também constam no CSV, separadas das durações concluídas e sem valor de tempo. Elas não integram a série de durações utilizada para o percentil 90.

## Escopo desta coleta

Os registros deste arquivo representam somente a coleta de Arthur na janela de pico. Não incluem as medições realizadas por outro avaliador no turno fora de pico e não constituem a consolidação de todos os turnos da equipe.

## Evidências

As evidências são as mesmas vinculadas às observações de origem da M7 e permanecem armazenadas em `docs/evidencias/M7/`.

| Arquivo | Registro |
|---|---|
| `login-20261119-sucesso.png` | Login concluído |
| `login-20261119-erro-solicitacao.png` | Mensagem de solicitação não concluída |
| `login-20261119-erro-403.png` | Erro no login com resposta HTTP 403 |
| `login-20261119-captura-complementar.png` | Captura complementar do fluxo de login |
| `indicadores-continuidade-20261119-sem-historico.png` | Resposta apresentada na página de indicadores de continuidade |
| `segundaVia-pdf-20261119.png` | PDF da segunda via disponibilizado |

## Ambiente de execução

| Campo | Registro |
|---|---|
| Avaliador | Arthur |
| Data da coleta | 19/11/2026 |
| Turno registrado | Janela de pico |
| Dispositivo | Dell Inspiron 15 3511 — Intel Core i5-1135G7 — 8 GB RAM |
| Sistema operacional | Fedora Linux 44 (Sway Spin) |
| Navegador | Mozilla Firefox, versão mais recente disponível na data da coleta |
| Conexão | Wi-Fi 5 GHz |
| VPN | Não utilizada |

## Coleta fora de pico (20/11/2026)

Os registros de tempo da M7 coletados por Tiago em 20/11/2026, na janela fora de pico, também são a base da M8. Foram reutilizadas as 30 durações (dez por fluxo) dos registros individuais da M7, sem novas execuções, e o arquivo `M8-registros.csv` mantém o identificador de origem (`id_origem_m7`) de cada uma. Os registros deste turno são apresentados separadamente dos de 19/11/2026.

### Percentil 90 por fluxo

Método do posto mais próximo: `posto = ceil(0,90 × n) = ceil(0,90 × 10) = 9`. O P90 é o nono valor da lista ordenada.

| Fluxo | Valores em ordem crescente (s) | P90 (s) | Faixa (escala M8) | H8 (até 5 s) |
|---|---|---:|---|---|
| F1 — Login | 2,21; 2,23; 2,29; 2,34; 2,44; 2,56; 2,57; 3,42; 3,60; 3,78 | **3,60** | Alvo | Atendida |
| F2 — Indicadores de continuidade | 2,29; 2,69; 2,84; 2,85; 3,73; 3,87; 3,89; 5,70; 7,99; 11,71 | **7,99** | Mínimo aceitável | Não atendida |
| F3 — PDF da segunda via | 2,99; 3,24; 3,24; 3,49; 3,52; 4,17; 4,32; 4,45; 4,60; 5,28 | **4,60** | Alvo | Atendida |

Com dez durações por fluxo, uma única duração alta altera o P90. Nos indicadores de continuidade, o P90 de 7,99 s fica abaixo de uma duração de 11,71 s.

### Evidências

As evidências são as mesmas da M7 fora de pico e estão em `docs/evidencias/M7-M8/`:

| Arquivo | Registro |
|---|---|
| `login-20261120-fora-pico-tiago.png` | Página inicial após o login, fora de pico |
| `segundaVia-pdf-20261120-fora-pico-tiago.png` | PDF da segunda via disponibilizado fora de pico |

### Ambiente de execução

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
