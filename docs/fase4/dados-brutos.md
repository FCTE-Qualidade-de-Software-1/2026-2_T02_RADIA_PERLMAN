# Dados brutos e evidências

Esta página relaciona cada métrica aos arquivos de dados e às evidências da coleta, para que qualquer resultado possa ser conferido a partir do dado bruto, como prevê o [Protocolo de coleta](../fase2/protocolo-coleta.md).

## 1. Arquivos por métrica

**Tabela 1 —** Localização dos dados brutos

| Objetivo | Métrica | Cenário | Arquivo de dados | Evidências | Página de resultados |
|---|---|---|---|---|---|
| G1 | M1, M9, M10 | U-01, U-03, U-04 | Roteiro de coleta de capacidade de interação com voluntários (fichas P01 a P05) | [Fichas anonimizadas](../evidencias/M1-M9-M10/Coleta-das-métricas-com-voluntários.pdf) | [G1 — Capacidade de Interação](resultados-g1-capacidade-interacao.md) |
| G1 | M2 | U-02 | [CSV](../dados-coleta/M2/M2-registros.csv) · [registro da coleta](../dados-coleta/M2/M2-resultados.md) | [Ficha consolidada](../evidencias/M2/M2-Tabela-16112026-03.png) · [capturas 1](../evidencias/M2/M2-U02-16112026-01.png) · [capturas 2](../evidencias/M2/M2-U02-16112026-02.png) | [G1 — Capacidade de Interação](resultados-g1-capacidade-interacao.md) |
| G2 | M3 | R-01 | [CSV](../dados-coleta/M3/M3-resultados.csv) · [registro da coleta](../dados-coleta/M3/M3-resultados.md) | [Capturas M3](../evidencias/M3/historicoConsumo-19112026-01-arthur.jpeg) · [falha observada](../evidencias/M3/segundaVia-19112026-erro-01-arthur.jpeg) | [G2 — Confiabilidade](resultados-g2-confiabilidade.md) |
| G2 | M4 | R-02 | [CSV](../dados-coleta/M4/M4-registros.csv) · [Registro da coleta](../dados-coleta/M4/M4-resultados.md) | [Retomada após interrupção](../evidencias/M4/M4-R02-20112026-01.png) | [G2 — Confiabilidade](resultados-g2-confiabilidade.md) |
| G2 | M11 | R-03 | [CSV](../dados-coleta/M11/M11-registros.csv) | [Captura operacional 17/11](../evidencias/M11/segundavia-1711-01-dara.png) · [erro 17/11 (tarde)](../evidencias/M11/indisponivel-1711-03-dara.png) · [erro 17/11 (noite)](../evidencias/M11/tela_erro-1711-04-dara.png) *(32 capturas em `docs/evidencias/M11/`)* | [G2 — Confiabilidade](resultados-g2-confiabilidade.md) |
| G3 | M5 | S-01 | [CSV](../dados-coleta/M5/M5-registros.csv) · [registro da coleta](../dados-coleta/M5/M5-resultados.md) | [Ficha consolidada](../evidencias/M5/M5-S01-16112026-01.png) | [G3 — Segurança](resultados-g3-seguranca.md) |
| G3 | M6 | S-02 | [CSV](../dados-coleta/M6/M6-registros.csv) · [Registro da coleta](../dados-coleta/M6/M6-resultados.md) | [Relatórios Nada Consta](../evidencias/M6/M6-17112026-01.png) | [G3 — Segurança](resultados-g3-seguranca.md) |
| G3 | M12 | S-03 | [CSV](../dados-coleta/M12/M12-registros.csv) · [Registro da coleta](../dados-coleta/M12/M12-resultados.md) | [Ficha A1 - A4](../evidencias/M12/M12-A1-A4-17112026-01.pdf) · [Tentativa de Login](../evidencias/M12/M12-A1-A2-17112026-02.png) · [Página inicial](../evidencias/M12/M12-R1-17112026-01.png) · [Protocolo](../evidencias/M12/M12-R2-17112026-01.png) | [G3 — Segurança](resultados-g3-seguranca.md) |
| G3 | M13 | S-04 | [CSV](../dados-coleta/M13/M13-registros.csv) · [Registro da coleta](../dados-coleta/M13/M13-resultados.md) | [Link indicado](../evidencias/M13/M13-17112026-01.png) · [Menu de serviços](../evidencias/M13/M13-17112026-02.png) | [G3 — Segurança](resultados-g3-seguranca.md) |
| G4 | M7, M8 | D-01, D-02 | [CSV M7](../dados-coleta/M7/M7-registros.csv) · [CSV M8](../dados-coleta/M8/M8-registros.csv) | [Login](../evidencias/M7-M8/login-20261119-sucesso.jpeg) · [erro HTTP 403](../evidencias/M7-M8/WhatsApp%20Image%202026-11-19%20at%2009.14.28.jpeg) · [indicadores](../evidencias/M7-M8/indicadores-continuidade-20261119-sem-historico.jpeg) · [PDF](../evidencias/M7-M8/segundaVia-pdf-20261119.jpeg) | [G4 — Eficiência de desempenho](resultados-g4-desempenho.md) |
| G4 | M14 | D-03 | [CSV do pico](../dados-coleta/M14/M14-registros.csv) · [registro da coleta](../dados-coleta/M14/M14-resultados.md) | [PDF, janela de pico](../evidencias/M14/segundaVia-pdf-pico-20261119-arthur.jpeg) | [G4 — Eficiência de desempenho](resultados-g4-desempenho.md) |

_Fonte: Equipe Radia Perlman, 2026._

## 2. Dados que não são publicados

Conforme [Recursos e ambiente](../fase3/recursos-ambiente.md) e o [modelo de termo de consentimento](../fase3/modelo-consentimento.md), os itens abaixo não são publicados no repositório:

- termos de consentimento assinados e a relação entre códigos e identidades dos participantes;
- documentos emitidos (2ª via e Nada Consta) e seus códigos de autenticação;
- senhas, tokens e outras credenciais;
- registros submetidos para a janela fora de pico (Bloco 3), descartados na auditoria interna por inconsistência e ausência de rastreabilidade, conforme documentado em [Obtenção das medidas](obtencao-medidas.md).

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da estrutura da página | Beatriz |
| 1.1 | 22/11/2026 | Inclusão dos vínculos de dados e evidências de M3, M7, M8 e M14 | Arthur de Lima Sobreira |
| 1.2 | 22/11/2026 | Inclusão dos vínculos de dados e evidências de M4, M6, M12 e M13 | Henrique |
| 1.3 | 22/11/2026 | Inclusão dos vínculos de dados e evidências de M2, M5 | Isabella |
| 1.4 | 22/11/2026 | Inclusão dos vínculos de dados e evidências de M1, M9 e M10 | Beatriz |
| 1.5 | 23/11/2026 | Inclusão dos vínculos de dados e evidências da M11 | Dara Maria Barbosa de Sousa |
| 1.6 | 24/11/2026 | Padronização do caminho de evidências da M11 e registro do descarte do Bloco 3 nos itens não publicados | Dara Maria Barbosa de Sousa |