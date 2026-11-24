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

As evidências são as mesmas vinculadas às observações de origem da M7 e permanecem armazenadas em `docs/evidencias/M7-M8/`.

| Arquivo | Registro |
|---|---|
| `login-20261119-sucesso.jpeg` | Login concluído |
| `login-20261119-erro-solicitacao.jpeg` | Mensagem de solicitação não concluída |
| `login-20261119-erro-403.jpeg` | Erro no login com resposta HTTP 403 |
| `login-20261119-captura-complementar.jpeg` | Captura complementar do fluxo de login |
| `indicadores-continuidade-20261119-sem-historico.jpeg` | Resposta apresentada na página de indicadores de continuidade |
| `segundaVia-pdf-20261119.jpeg` | PDF da segunda via disponibilizado |

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
