<p align="center">
  <img src="assets/logo-neoenergia.svg" alt="Logo da Neoenergia Brasília" width="250">
</p>

# Visão Geral do Projeto

Este site reúne a documentação do projeto prático da disciplina de Qualidade de Software, do curso de Engenharia de Software da Universidade de Brasília (UnB), ministrada pela professora Cristiane Soares Ramos. 

O objeto de estudo deste projeto é a **Agência Virtual da Neoenergia Brasília**, um software comercial submetido a um processo sistemático de avaliação da qualidade de produto.

!!! success "Artigo Técnico-Acadêmico (Versão Final)"
    Toda a documentação, os protocolos de coleta, os dados brutos anonimizados e as evidências levantadas ao longo das quatro fases detalhadas neste site fundamentam o **Artigo Científico** final da equipe, que consolida o julgamento da qualidade e a validação da ação de melhoria proposta.
    
    * [Acessar a Versão Final do Artigo (Fases 1 a 4)](./artigo/QSW1_2026_2_T02___Equipe_Radia_Perlman.pdf)
    * [Acessar a 1ª Versão do Artigo (Fases 1 e 2)](./artigo/QSW1_2026_2_T02_Equipe_Radia_Perlman_v1.pdf)

## Fundamentação Teórica

A Engenharia de Software é definida como a aplicação de uma abordagem sistemática, disciplinada e quantificável para o desenvolvimento, operação e manutenção de software. Dentro dessa disciplina, a qualidade de software é um conceito complexo e altamente dependente do contexto, podendo ser percebida de diferentes maneiras.

Segundo Garvin (1984), a qualidade pode ser analisada através de cinco visões principais: transcendental, do usuário, da manufatura, do produto e baseada em valor. Este projeto norteia-se primordialmente pelas seguintes perspectivas:

* **Visão do Usuário:** Avalia o grau em que o produto atende às necessidades e expectativas dos usuários, abrangendo elementos como a capacidade de interação.
* **Visão do Produto:** Explora as relações causais entre propriedades internas e externas, assumindo que a qualidade pode ser avaliada de maneira objetiva por meio de atributos mensuráveis.

Para padronizar a avaliação, o projeto adota a família de normas **SQuaRE (*Systems and Software Quality Requirements and Evaluation*)**. Utiliza-se o modelo de qualidade de produto **ISO/IEC 25010** (incluindo a terminologia atualizada da revisão de 2023) e o processo de avaliação **ISO/IEC 25040**, categorizando as propriedades externas observáveis em caixa-preta em quatro características priorizadas: **Capacidade de Interação**, **Confiabilidade**, **Segurança** e **Eficiência de Desempenho**, desdobradas pelo método **Goal-Question-Metric (GQM)**.

## O Processo de Avaliação

Para que a qualidade do produto seja mensurada de forma sistemática e repetível, o projeto seguiu o Processo de Avaliação de Produto de Software estruturado em quatro fases fundamentais:

1. **[Fase 1 - Estabelecer requisitos de avaliação:](fase1-requisitos.md)** Definição do propósito da avaliação, delimitação das cinco funcionalidades avaliadas, justificativa das características da ISO/IEC 25010 (ênfases de 1 a 5) e alinhamento aos ODS 7, 12 e 16.
2. **[Fase 2 - Especificar a avaliação:](fase2-especificacao.md)** Desdobramento GQM em 4 objetivos (`G1`–`G4`), 14 questões (`Q1`–`Q14`), 14 hipóteses (`H1`–`H14`) e 14 métricas (`M1`–`M14`), com níveis de pontuação e critérios de julgamento.
3. **[Fase 3 - Projetar a avaliação:](fase3-plano-avaliacao.md)** Consolidação dos 14 roteiros de medição (`U-01` a `D-03`), protocolo com cinco voluntários (`P01`–`P05`), definição de ambiente, limitações e cronograma de execução.
4. **[Fase 4 - Executar a avaliação:](fase4-execucao.md)** Coleta das medidas em produção, auditoria dos registros, julgamento final da qualidade do software, recomendações priorizadas (`AM-01` a `AM-08`) e validação de protótipo funcional como ação de melhoria.

## Síntese dos Resultados e Ação de Melhoria

A coleta empírica ocorreu entre **16 e 20/11/2026**, com auditoria e consolidação entre **21 e 23/11/2026**. Das 14 hipóteses estabelecidas, **7 foram sustentadas**, **5 não foram sustentadas** e **2 ficaram inconclusivas**:

| Objetivo | Característica (Ênfase) | Nível Obtido | Síntese dos Resultados |
| :--- | :--- | :--- | :--- |
| **G1** | Capacidade de Interação (5) | **Insatisfatório** | Localização sem ajuda atingiu 100% (**M1**), mas apenas 4 de 10 entradas inválidas orientaram a correção (**M2**: 40%). Reconhecimento atingiu 80% (**M9**), e a operação ficou inconclusiva após exclusão do gráfico inexistente (**M10**). |
| **G2** | Confiabilidade (4) | **Mínimo aceitável** | Alta estabilidade nos fluxos (**M3**: Alvo) e 100% de retomada após queda breve de rede (**M4**), porém impactada por quatro indisponibilidades em 17/11 (**M11**: 87,5%). |
| **G3** | Segurança (5) | **Insatisfatório** | Bloqueio pós-logout (**M5**: 100%) e consistência de dados (**M6**: 100%) atendidos, mas nenhum dos 5 comprovantes de Nada Consta pôde ser validado no portal ou via assinatura digital (**M13**: 0%, tolerância zero). |
| **G4** | Eficiência de Desempenho (4) | **Inconclusivo** | Percentil 90 dentro do alvo no login e nos indicadores (**M8**), mediana do login em 3,425 s (**M7**: Mínimo aceitável) e descarte auditado da série fora de pico (**M14**: inconclusiva). |

* **Julgamento Global:** **Necessidade de melhorias prioritárias** (determinado pelos níveis *Insatisfatório* em G1 e G3, com registro explícito das métricas inconclusivas M10 e M14).
* **Ação de Melhoria (`OM-01` / `AM-03`):** Desenvolvimento e validação (em 23/11/2026) de um **protótipo funcional** em página única para os **Indicadores de Continuidade** (WCAG 2.2 nível AA), resolvendo a ambiguidade da tela menos reconhecida na avaliação.

---

## *Equipe de Avaliação*

Abaixo estão os integrantes responsáveis por conduzir este processo de avaliação de qualidade de software:

| Foto | Nome | GitHub |
|:---:|---|---|
| <img src="https://github.com/arthor13.png" alt="Foto de Arthur de Lima Sobreira" width="50" style="border-radius: 50%;"> | Arthur de Lima Sobreira | [@arthor13](https://github.com/arthor13) |
| <img src="https://github.com/BeatrizSants.png" alt="Foto de Beatriz Figueiredo dos Santos" width="50" style="border-radius: 50%;"> | Beatriz Figueiredo dos Santos | [@BeatrizSants](https://github.com/BeatrizSants) |
| <img src="https://github.com/daramariabs.png" alt="Foto de Dara Maria Barbosa de Sousa" width="50" style="border-radius: 50%;"> | Dara Maria Barbosa de Sousa | [@daramariabs](https://github.com/daramariabs) |
| <img src="https://github.com/henryqma.png" alt="Foto de Henrique Martins Alencar" width="50" style="border-radius: 50%;"> | Henrique Martins Alencar | [@henryqma](https://github.com/henryqma) |
| <img src="https://github.com/isabellachoukaira.png" alt="Foto de Isabella Mendes Choukaira" width="50" style="border-radius: 50%;"> | Isabella Mendes Choukaira | [@isabellachoukaira](https://github.com/isabellachoukaira) |
| <img src="https://github.com/TiagoSTdeLyra.png" alt="Foto de Tiago Scherrer Tavares de Lyra" width="50" style="border-radius: 50%;"> | Tiago Scherrer Tavares de Lyra | [@TiagoSTdeLyra](https://github.com/TiagoSTdeLyra) |

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|:---:|:---:|---|---|
| 1.0 | 16/10/2026 | Criação da visão geral do projeto | Dara Maria Barbosa de Sousa |
| 1.1 | 26/10/2026 | Inclusão do Artigo Acadêmico como escopo final e revisão textual | Dara Maria Barbosa de Sousa |
| 1.2 | 21/11/2026 | Correção do link da Fase 3, inclusão de texto alternativo nas fotos da equipe e limpeza de comentários | Dara Maria Barbosa de Sousa |
| 1.3 | 24/11/2026 | Atualização para a entrega final, com link do artigo e síntese de resultados  | Henrique Martins Alencar |

---