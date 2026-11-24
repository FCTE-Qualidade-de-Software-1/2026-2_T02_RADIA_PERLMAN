# M7 — Registros de tempo de resposta

Registros da coleta realizada em 19/11/2026 pelo avaliador Arthur, na janela de pico, nos fluxos de login, indicadores de continuidade e geração do PDF da segunda via.

## Fluxos registrados

### M7-F1 — Login

- **Evento inicial:** acionamento do botão de login (Entrar).
- **Evento final:** página inicial da Agência Virtual disponível para interação.
- **Medições:** dez durações registradas.
- **Ocorrências adicionais:** três mensagens de solicitação não concluída e três respostas HTTP 403, registradas separadamente das durações.

### M7-F2 — Indicadores de continuidade

- **Evento inicial:** acionamento da opção Indicadores de Continuidade.
- **Evento final:** resposta da página apresentada na interface.
- **Medições:** dez durações registradas.
- **Resultado observado na captura:** mensagem “Unidade sem histórico de indicadores de continuidade”.

### M7-F3 — Geração do PDF da segunda via

- **Evento inicial:** acionamento da opção para gerar ou abrir a segunda via em PDF.
- **Evento final:** PDF disponibilizado para visualização.
- **Medições:** dez durações registradas.

## Registros individuais

O arquivo `M7-registros.csv` contém as trinta durações informadas e as seis ocorrências adicionais do fluxo de login. As ocorrências sem duração não integram a lista de tempos cronometrados.

## Evidências

As capturas estão organizadas em `docs/evidencias/M7/`.

| Arquivo | Registro |
|---|---|
| `login-20261119-sucesso.png` | Login concluído e página inicial disponível |
| `login-20261119-erro-solicitacao.png` | Mensagem de solicitação não concluída |
| `login-20261119-erro-403.png` | Mensagem de erro no login com resposta HTTP 403 |
| `indicadores-continuidade-20261119-sem-historico.png` | Mensagem apresentada na página de indicadores de continuidade |
| `segundaVia-pdf-20261119.png` | PDF da segunda via disponibilizado |

As capturas dos dois tipos de erro de login representam os comportamentos observados nas seis ocorrências adicionais. Os registros individuais dessas ocorrências estão identificados no CSV.

## Ambiente de execução

| Campo | Registro |
|---|---|
| Avaliador | Arthur |
| Data da coleta | 19/11/2026 |
| Janela de coleta | Pico |
| Dispositivo | Dell Inspiron 15 3511 — Intel Core i5-1135G7 — 8 GB RAM |
| Sistema operacional | Fedora Linux 44 (Sway Spin) |
| Navegador | Mozilla Firefox, versão mais recente disponível na data da coleta |
| Conexão | Wi-Fi 5 GHz |
| VPN | Não utilizada |

## Coleta fora de pico (20/11/2026)

Registros da coleta realizada em 20/11/2026, a partir das 03:41, pelo avaliador Tiago, na janela fora de pico, nos mesmos três fluxos (M7-F1, M7-F2 e M7-F3), com os mesmos eventos inicial e final descritos acima. Foram registradas dez durações em cada fluxo, sem timeouts e sem ocorrências adicionais.

### Durações registradas (s)

| Fluxo | Durações (s) |
|---|---|
| M7-F1 — Login | 3,78; 2,57; 3,60; 2,21; 3,42; 2,34; 2,56; 2,44; 2,23; 2,29 |
| M7-F2 — Indicadores de continuidade | 3,87; 2,84; 5,70; 2,69; 7,99; 2,85; 2,29; 3,73; 3,89; 11,71 |
| M7-F3 — Geração do PDF da segunda via | 4,17; 3,24; 4,60; 2,99; 3,52; 3,49; 3,24; 4,45; 5,28; 4,32 |

### Mediana por fluxo

Com `n = 10`, a mediana corresponde à média entre o 5º e o 6º valor da série ordenada.

| Fluxo | 5º valor (s) | 6º valor (s) | Mediana (s) | Faixa (escala M7) | H7 (até 3 s) |
|---|---:|---:|---:|---|---|
| M7-F1 — Login | 2,44 | 2,56 | **2,50** | Alvo | Atendida |
| M7-F2 — Indicadores de continuidade | 3,73 | 3,87 | **3,80** | Mínimo aceitável | Não atendida |
| M7-F3 — Geração do PDF da segunda via | 3,52 | 4,17 | **3,85** | Mínimo aceitável | Não atendida |

### Registros individuais e evidências

Os 30 registros fora de pico constam no arquivo `M7-registros.csv`, com os identificadores `M7-F1-20261120-01` a `M7-F3-20261120-10`. Os horários individuais não foram registrados.

As capturas estão organizadas em `docs/evidencias/M7-M8/`:

| Arquivo | Registro |
|---|---|
| `login-20261120-fora-pico-tiago.png` | Página inicial após o login, fora de pico |
| `segundaVia-pdf-20261120-fora-pico-tiago.png` | PDF da segunda via disponibilizado fora de pico |

Não há captura do fluxo de indicadores de continuidade nesta janela. Dados pessoais foram cobertos nas imagens.

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
