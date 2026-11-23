# M14 — Registros de tempo entre pico e fora de pico

## C-F1 — Geração do PDF da segunda via

**Data da coleta:** 19/11/2026  
**Avaliador:** Arthur  
**Janela registrada:** Pico  
**Período:** Manhã  
**Execuções registradas:** 10

O registro corresponde às execuções do fluxo de geração do PDF da segunda via realizadas na janela de pico.

### Registros das execuções

| ID | Horário | Tempo (s) |
|---|---|---:|
| M14-CF1-20261119-01 | 09:45 | 4,11 |
| M14-CF1-20261119-02 | 09:45 | 3,70 |
| M14-CF1-20261119-03 | 09:45 | 3,65 |
| M14-CF1-20261119-04 | 09:46 | 4,18 |
| M14-CF1-20261119-05 | 09:46 | 3,73 |
| M14-CF1-20261119-06 | 09:46 | 3,99 |
| M14-CF1-20261119-07 | 09:47 | 3,71 |
| M14-CF1-20261119-08 | 09:47 | 4,26 |
| M14-CF1-20261119-09 | 09:47 | 4,32 |
| M14-CF1-20261119-10 | 09:47 | 4,04 |

### Procedimento registrado

- **Evento inicial:** acionamento da opção para gerar ou abrir a segunda via em PDF.
- **Evento final:** PDF disponibilizado para visualização.
- **Resultado observado:** PDF da segunda via disponibilizado.

### Evidência

`docs/evidencias/M14/segundaVia-pdf-pico-20261119-arthur.png`

### Ambiente de execução

| Campo | Registro |
|---|---|
| Avaliador | Arthur |
| Dispositivo | Dell Inspiron 15 3511 — Intel Core i5-1135G7 — 8 GB RAM |
| Sistema operacional | Fedora Linux 44 (Sway Spin) |
| Navegador | Mozilla Firefox, versão mais recente disponível na data da coleta; número exato não registrado |
| Conexão | Wi-Fi 5 GHz |
| VPN | Não utilizada |

O arquivo `M14-registros.csv` contém os registros individuais das dez execuções.

## C-F1 — Geração do PDF da segunda via (fora de pico)

**Data da coleta:** 20/11/2026  
**Avaliador:** Tiago  
**Janela registrada:** Fora de pico  
**Período:** Madrugada, a partir das 03:41  
**Execuções registradas:** 10

O registro corresponde às execuções do fluxo de geração do PDF da segunda via realizadas na janela fora de pico, com os mesmos eventos inicial e final da janela de pico.

### Registros das execuções

| ID | Tempo (s) |
|---|---:|
| M14-CF1-20261120-01 | 3,37 |
| M14-CF1-20261120-02 | 2,54 |
| M14-CF1-20261120-03 | 2,64 |
| M14-CF1-20261120-04 | 3,87 |
| M14-CF1-20261120-05 | 2,47 |
| M14-CF1-20261120-06 | 3,80 |
| M14-CF1-20261120-07 | 3,77 |
| M14-CF1-20261120-08 | 3,67 |
| M14-CF1-20261120-09 | 2,58 |
| M14-CF1-20261120-10 | 2,35 |

Os horários individuais não foram registrados.

### Razão entre pico e fora de pico

Série fora de pico ordenada (s): 2,35; 2,47; 2,54; 2,58; 2,64; 3,37; 3,67; 3,77; 3,80; 3,87. Com `n = 10`, a mediana é `(2,64 + 3,37) / 2 = 3,005 s`.

A mediana do pico, registrada acima, é de 4,015 s. Assim:

`M14(C-F1) = 4,015 / 3,005 ≈ 1,34`

Essa razão está na faixa Alvo da escala M14 (acima de 1,2 até 1,5) e atende o limite de H14 (até 1,5) para o C-F1. A comparação usa avaliadores e dias diferentes (Arthur em 19/11/2026 e Tiago em 20/11/2026).

### Evidência

`docs/evidencias/M7-M8/segundaVia-pdf-20261120-fora-pico-tiago.png`

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

O arquivo `M14-registros.csv` contém os registros individuais das dez execuções fora de pico.
