# Fase 3 — Plano de Avaliação

Na [Fase 1](fase1-requisitos.md), estabelecemos os requisitos da avaliação e, na [Fase 2](fase2-especificacao.md), especificamos as métricas (GQM) e os indicadores de gestão (PSM/CID). O objetivo desta **Fase 3: Projetar a Avaliação** é organizar a execução da Fase 4, definindo os métodos exatos, preparando os recursos e estruturando o cronograma de ação da equipe (RAMOS, 2026).

Diante do prazo restrito para a entrega do relatório final e do artigo acadêmico (22/11/2026), este documento formaliza os ajustes metodológicos necessários para viabilizar a coleta e a análise de dados sem comprometer o rigor do modelo ISO/IEC 25010:2011.

---

## 1. Atividades da Fase 3

Para que a avaliação seja projetada de forma repetível e organizada, o trabalho da Fase 3 foi dividido nas seguintes atividades:

### Atividade 1: Detalhamento do Método e Instruções (Scripts)
* **Descrição:** Traduzir o protocolo de coleta da Fase 2 em roteiros práticos e exatos (scripts de teste).
* **Responsável Principal:** Arthur.
* **Ações:** Criar o passo a passo exato para os cenários U-01 a D-03, definir a ferramenta padrão de cronometragem para M7, M8 e M14, e estruturar as planilhas onde os dados brutos e *timeouts* serão anotados.

### Atividade 2: Especificação e Preparação de Recursos
* **Descrição:** Levantar e preparar a infraestrutura humana, de software e de hardware antes da coleta.
* **Responsáveis Principais:** Arthur (Infraestrutura), Dara e Beatriz (Voluntários).
* **Ações:** Confirmar a disponibilidade de cinco voluntários sem experiência recente com a Agência Virtual; validar as credenciais da conta real; padronizar o ambiente (navegador, dispositivo e conexão) para os testes de desempenho; e preparar o repositório seguro para evidências (sem exposição de dados sensíveis).

### Atividade 3: Elaboração do Cronograma de Execução (Sprint Final)
* **Descrição:** Alocar os cenários de teste entre os 6 membros da equipe, respeitando restrições de horários de pico/fora de pico e dias distintos.
* **Responsável Principal:** Dara Maria .
* **Ações:** Definir "quem faz o que e quando" entre os dias 15/11 e 22/11, garantindo tempo hábil para a consolidação e julgamento dos dados.

### Atividade 4: Consolidação do Plano de Avaliação
* **Descrição:** Reunir o produto de todas as atividades anteriores neste documento, que servirá como guia definitivo para a Fase 4.

---

## 2. Ajustes Metodológicos (Justificativa de Prazo)

A metodologia GQM e as normas da família SQuaRE permitem a adaptação do modelo de qualidade desde que devidamente documentada e justificada em função do contexto (ISO/IEC, 2011; RAMOS, 2026). 

Para assegurar a viabilidade da entrega em 22/11/2026, aplicamos os seguintes ajustes ao [Protocolo de Coleta](fase2/protocolo-coleta.md) originalmente definido na Fase 2:

1. **Ajuste na M11 (Disponibilidade):** O protocolo exigia testes durante 7 dias com 3 verificações diárias (21 amostras). **Ajuste:** A coleta foi condensada para **5 dias (16/11 a 20/11) com 4 verificações diárias** (manhã, almoço, fim da tarde e noite). Isso garante 20 verificações por função (amostra estatisticamente comparável ao planejado) e libera o fim de semana (21 e 22) exclusivamente para a consolidação e redação do relatório.
2. **Ajuste nos Voluntários (M1, M9, M10):** As sessões de observação com os 5 voluntários foram estritamente agrupadas entre os dias **17/11 (Terça) e 19/11 (Quinta)**, evitando dependências externas nos dias finais do projeto.

---

## 3. Cronograma de Execução da Fase 4 (Sprint Final)

A tabela abaixo distribui as tarefas práticas de coleta (Fase 4), análise e redação, alinhadas aos prazos do projeto e às restrições operacionais das métricas (M12 exige dias diferentes; M14 exige pico e fora de pico).

| Data | Fase | Atividades Críticas e Alocação da Equipe |
| :--- | :--- | :--- |
| **15/11 (Dom.) e 16/11 (Seg.)** | **Fechamento Fase 3** | **Arthur:** Finalizar os roteiros exatos e criar as planilhas de anotação.<br>**Dara e Beatriz:** Confirmar os 5 voluntários para os dias 17, 18 ou 19.<br>**Toda a equipe:** Iniciar as medições da **M11** (1º e 2º dia do monitoramento). |
| **16/11 (Segunda)** | **Início Fase 4 (Coleta)** | **Tiago:** Executar o Bloco de Desempenho e Maturidade (M3, M7, M8 e **M14**) no período *"Fora de Pico"* (ex: fim da noite).<br>**Henrique e Isabella:** Executar a 1ª rodada do Bloco de Segurança (M2, M4, M5, M6, M12, M13). |
| **17/11 (Terça)** | **Fase 4 (Coleta)** | **Arthur:** Executar o Bloco de Desempenho (M3, M7, M8 e **M14**) na janela de *"Pico"* (horário comercial).<br>**Henrique e Isabella:** Executar a 2ª rodada da **M12** (exigência de dias diferentes). |
| **17, 18 e 19/11** | **Fase 4 (Coleta)** | **Dara e Beatriz:** Executar as sessões de observação com os voluntários (M1, M9, M10).<br>**Qualquer membro:** Continuar as marcações diárias da **M11**. |
| **20/11 (Sexta)** | **Fim da Coleta** | Último dia de monitoramento da **M11** (5º dia do ajuste).<br>Fim absoluto de todas as coletas de dados empíricos.<br>Início da estruturação e limpeza das planilhas brutas. |
| **21/11 (Sábado)** | **Consolidação (Fase 4)** | **Toda a equipe:** Calcular os percentuais, medianas, percentil 90 e a razão pico/fora de pico. Cruzar os resultados com os "Critérios de Julgamento". *(Nota: Se M5 ou M13 falharem, já declarar insatisfatório).* |
| **22/11 (Domingo)** | **Entrega Final** | Redação do Relatório Final (Fase 4) e consolidação do Artigo Acadêmico. Verificar rodada final do script PSM/CID para capturar o esforço do fim de semana. |

---

## 4. Documentos de apoio

O plano consolidado é complementado pelos documentos operacionais abaixo:

- [Recursos e ambiente de avaliação](fase3/recursos-ambiente.md): dispositivos, navegador, conexão, ferramentas, conta autorizada, participantes e limitações. A amostra por conveniência poderá incluir familiares, amigos e conhecidos dos integrantes, desde que não façam parte da equipe e atendam aos critérios de elegibilidade.
- [Método e procedimentos de avaliação](fase3/metodo-procedimentos.md): roteiros U-01 a D-03 e instruções para obtenção das métricas M1–M14.
- [Modelo de termo de consentimento](fase3/modelo-consentimento.md): minuta para revisão da docente e uso nas sessões com participantes externos.
- [Cronograma de execução](fase3/cronograma.md): datas, responsáveis, janelas de medição e distribuição das atividades.

## 5. Entregáveis da Fase 3

Para que a **Fase 3** seja formalmente dada como concluída e a equipe autorizada a iniciar a coleta sistemática de dados (Fase 4), os seguintes artefatos devem constar no repositório:

1. **Roteiros de Avaliação (Scripts):** Documentação ou planilhas de apoio contendo o passo a passo clique-a-clique dos cenários U-01 a D-03.
2. **Inventário de Recursos:** Definição final dos voluntários, ferramentas de cronometragem e o ambiente de software padronizado para as medições.
3. **Cronograma Finalizado:** A tabela de *Sprint Final* aprovada por todos os membros.
4. **Este Documento (Plano de Avaliação):** O artefato consolidado.

## 6. Acompanhamento e Gestão (PSM/CID)

Para garantir que o indicador **PSM-3 (Razão de esforço)** reflita com precisão o alto volume de trabalho desta etapa de *Sprint Final*, todas as atividades descritas no cronograma acima devem ser transformadas em *Issues* no GitHub. 

Cada membro deve manter a estimativa na seção **Estimativa (horas)** e registrar as horas efetivamente trabalhadas na seção **Horas reais**, no corpo da Issue. A automação desenvolvida pela equipe lê esses campos do corpo das Issues; registros feitos somente nos comentários não entram no cálculo do PSM-3. A [documentação da gestão PSM/CID](./gestaoProjeto/index.md) descreve o formato esperado.

---

## Referências

* ISO/IEC. *ISO/IEC 25010:2011 — Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. Genebra: ISO, 2011.
* RAMOS, C. S. *Processo de Avaliação de Produto de Software*. Material de apoio e slides da disciplina Qualidade de Software 1. Brasília: Universidade de Brasília (UnB), 2026.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 15/11/2026 | Criação do Plano de Avaliação e cronograma ajustado | Dara Maria Barbosa de Sousa |
| 1.1 | 15/11/2026 | Correção de referências, inclusão dos documentos operacionais e explicitação das pendências de amostragem | Arthur de Lima Sobreira |
