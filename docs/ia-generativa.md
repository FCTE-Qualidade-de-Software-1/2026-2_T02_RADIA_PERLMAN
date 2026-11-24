# Declaração de Uso de Inteligência Artificial Generativa

Esta página registra, de forma transparente, como a equipe utilizou ferramentas de Inteligência Artificial (IA) generativa ao longo do desenvolvimento do projeto de avaliação da **Agência Virtual da Neoenergia Brasília** (Fases 1 a 4, documentação no MkDocs e artigo técnico-acadêmico).

## 1. Diretrizes Gerais da Equipe

O uso de ferramentas de IA generativa neste projeto seguiu princípios de integridade acadêmica, rastreabilidade e proteção de dados:

* **Papel de apoio:** as ferramentas foram empregadas exclusivamente como suporte para revisão textual, estruturação de documentos em Markdown/LaTeX, organização de tabelas e diagramas, apoio na prototipação visual e revisão de consistência entre artefatos.
* **Autoria e validação humana:** todo o planejamento metodológico (GQM), a execução presencial e remota dos cenários de teste, a coleta de tempos e evidências, os cálculos estatísticos e o julgamento crítico da qualidade do produto foram conduzidos, conferidos e validados manualmente pelos integrantes da equipe.
* **Privacidade e segurança:** nenhum dado sensível de consumidores (CPF, número de unidade consumidora, senhas, tokens, faturas ou documentos de Nada Consta) nem dados pessoais dos voluntários (nomes, contatos ou termos assinados) foram inseridos em ferramentas de IA.

## 2. Quadro Resumo por Integrante

| Integrante | Ferramentas Utilizadas | Principais Finalidades | Fases / Artefatos |
|---|---|---|---|
| **Arthur de Lima Sobreira** | *A preencher* | *A preencher* | *A preencher* |
| **Beatriz Figueiredo dos Santos** | Claude (Anthropic) | Apoio na redação e estruturação de documentos (GitHub Pages e artigo no Overleaf), revisão de documentação e implementação do protótipo da ação de melhoria a partir das análises e decisões de design próprias | Fases 2 e 4, roteiro de coleta com voluntários, protótipo, GitHub Pages e Artigo |
| **Dara Maria Barbosa de Sousa** | Google Gemini | Revisão textual, padronização Markdown/Mermaid, verificação de consistência entre fases e apoio na consolidação de relatórios e Git | Fases 1, 2, 3, 4 e MkDocs |
| **Henrique Martins Alencar** | Google Gemini | Revisão textual, padronização, organização, apoio no LaTeX e apoio no registro de resultados. | Fases 2, 4 e Artigo |
| **Isabella Mendes Choukaira** | *A preencher* | *A preencher* | *A preencher* |
| **Tiago Scherrer Tavares de Lyra** | *A preencher* | *A preencher* | *A preencher* |

## 3. Declarações Individuais

### 3.1. Arthur de Lima Sobreira

* **Ferramentas utilizadas:** *(informar nome e versão/modelo, ou registrar "Não utilizou")*
* **Fases e artefatos apoiados:** *(ex.: Fase 2, Fase 3, Fase 4 — resultados de G2/G4)*
* **Finalidade do uso:** *(descrever como a ferramenta foi usada: revisão de texto, formatação, apoio em scripts, etc.)*
* **Validação humana:** *(descrever como os dados, cálculos e textos gerados foram revisados pelo integrante)*

---

### 3.2. Beatriz Figueiredo dos Santos

* **Ferramentas utilizadas:** Claude (Anthropic).
* **Fases e artefatos apoiados:** Fase 2; Fase 4 (roteiro de coleta das métricas de capacidade de interação com voluntários, resultados de G1, protótipo funcional da tela de Indicadores de Continuidade, plano de validação e análise dos resultados da validação); documentação no GitHub Pages (MkDocs); e Artigo (Overleaf).
* **Finalidade do uso:**    
    * **Redação e estruturação de documentos:** utilizei a ferramenta como apoio na organização das páginas do MkDocs e do artigo no Overleaf, na estruturação de seções e tabelas em Markdown e na redação de textos a partir dos dados, das análises e das decisões que tomei.
    * **Revisão de documentação:** usei a ferramenta para revisão ortográfica e de clareza, para verificar a consistência entre páginas (por exemplo, entre os resultados de G1, a justificativa da ação de melhoria e o plano de validação) e para corrigir numeração, links e referências.
    * **Elaboração do protótipo:** defini o problema, a análise das telas atuais e a visão da solução (layout, textos, comportamento do gráfico e ajustes visuais), e a ferramenta implementou essas definições em HTML, CSS e JavaScript. Revisei cada versão e propus novos ajustes com base em análise própria e nos resultados das sessões com voluntários.
* **Validação humana:**  Realizei a coleta com os voluntários, o registro das fichas, os tempos e os códigos de resultado sem uso de IA. Além do protótipo, revisei manualmente todos os textos redigidos com apoio da ferramenta e conferi as análises com as fichas e os dados coletados antes da publicação. Testei o protótipo a cada versão e decidi o que manter, remover ou alterar. Não inseri na ferramenta dados pessoais dos voluntários nem dados sensíveis da unidade consumidora; as capturas de tela utilizadas tiveram esses dados ocultados.

---

### 3.3. Dara Maria Barbosa de Sousa

* **Ferramentas utilizadas:** Google Gemini.
* **Fases e artefatos apoiados:** Fase 1 (`produto-avaliado.md`, `modelo-qualidade.md`, `alinhamento-ods.md`), Fase 2 (`metricas.md`, `protocolo-coleta.md`), Fase 3 (`cronograma.md`, `metodo-procedimentos.md`, `recursos-ambiente.md`, `modelo-consentimento.md`), Fase 4 (`fase4-execucao.md`, `obtencao-medidas.md`, `resultados-g2-confiabilidade.md`, `julgamento-conclusoes.md`) e configuração do site (`index.md`, `mkdocs.yml`).
* **Finalidade do uso:** Revisão ortográfica e de clareza textual, padronização de tabelas Markdown e diagramas Mermaid, verificação cruzada de consistência amostral entre as Fases 2 e 3, consolidação das tabelas de resultados.
* **Validação humana:** Todas as verificações práticas coletadas, os cálculos das métricas, a auditoria dos registros brutos e as decisões metodológicas foram executados e conferidos manualmente antes da publicação no repositório.

---

### 3.4. Henrique Martins Alencar

* **Ferramentas utilizadas:** Google Gemini
* **Fases e artefatos apoiados:** Fase 2 (`objetivos.md`, `questoes-hipoteses.md`, `metricas.md`, `criterios-julgamento.md`), Fase 4 (`resultados-g2-confiabilidade.md`, `resultados-g3-seguranca.md`, `M4-resultados.md`, `M6-resultados.md`, `M12-resultados.md`, `M13-resultados.md`, `M6-registros.csv`) e Artigo.
* **Finalidade do uso:** Revisão ortográfica, revisão de formato, padronização e estruturação de documentos, verificação de consistência, apoio em linguagem LaTeX e preenchimento de planilha de registros extensa (`M6-registros.csv`).
* **Validação humana:** Todas as sugestões da IA foram revisadas manualmente e utilizadas como oportunidade de melhoria antes da publicação no repositório.

---

### 3.5. Isabella Mendes Choukaira

* **Ferramentas utilizadas:** *(informar nome e versão/modelo, ou registrar "Não utilizou")*
* **Fases e artefatos apoiados:** *(ex.: Fase 2, Fase 4 — resultados de M2, M5 e M12)*
* **Finalidade do uso:** *(descrever como a ferramenta foi usada: revisão de texto, formatação de tabelas, etc.)*
* **Validação humana:** *(descrever como os registros de coleta e textos foram revisados pela integrante)*

---

### 3.6. Tiago Scherrer Tavares de Lyra

* **Ferramentas utilizadas:** *(informar nome e versão/modelo, ou registrar "Não utilizou")*
* **Fases e artefatos apoiados:** *(informar fases/artefatos em que atuou)*
* **Finalidade do uso:** *(descrever como a ferramenta foi usada, ou registrar "Não utilizou")*
* **Validação humana:** *(descrever como os conteúdos produzidos foram revisados pelo integrante)*

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da página | Beatriz Figueiredo dos Santos |
| 1.1 | 24/11/2026 | Estruturação das diretrizes gerais, quadro resumo e seções de declaração individual por integrante | Dara Maria Barbosa de Sousa |
| 1.2 | 24/11/2026 | Declaração individual de uso de IA | Henrique Martins Alencar |
| 1.3 | 24/11/2026 | Correção de texto | Henrique Martins Alencar |
| 1.4 | 24/11/2026 | Declaração individual de uso de IA | Beatriz Figueiredo dos Santos |