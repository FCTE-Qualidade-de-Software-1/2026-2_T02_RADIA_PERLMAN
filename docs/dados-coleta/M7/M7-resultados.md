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

As capturas estão organizadas em `docs/evidencias/M7-M8/`.

| Arquivo | Registro |
|---|---|
| `login-20261119-sucesso.jpeg` | Login concluído e página inicial disponível |
| `login-20261119-erro-solicitacao.jpeg` | Mensagem de solicitação não concluída |
| `login-20261119-erro-403.jpeg` | Mensagem de erro no login com resposta HTTP 403 |
| `indicadores-continuidade-20261119-sem-historico.jpeg` | Mensagem apresentada na página de indicadores de continuidade |
| `segundaVia-pdf-20261119.jpeg` | PDF da segunda via disponibilizado |

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
