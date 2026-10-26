## **Produto a ser avaliado**

* **Nome e Categoria do Produto:** Agência Virtual da Neoenergia Brasília. Classifica-se como um **Software Comercial** (Pressman, 2010), organizado em uma plataforma Web para facilitar as operações comerciais, a prestação de serviços ao cliente e a descentralização do atendimento.
* **Principais tarefas e escopo de avaliação:**
    1. Login e Cadastro de Usuário
    2. Emissão de segunda via de fatura
    3. Histórico de consumo
    4. Relatório de Nada Consta
    5. Indicadores de continuidade
* **Perfil dos Usuários:** População em geral do Distrito Federal, abrangendo desde cidadãos leigos até usuários com alto conhecimento em informática. Tal heterogeneidade exige forte ênfase na Engenharia Humana e Usabilidade (Galin, 2018).

* **Descrição e Módulos do Sistema:** O escopo do sistema submetido à avaliação é composto por múltiplas funções e janelas de interação de dados, logicamente estruturadas nos seguintes módulos principais:


    1. *Módulo de Autenticação e Gestão de Perfil:* Componente responsável pelo Login e Cadastro de Usuário. Atua como a barreira de segurança primária, controlando sessões e permissões de acesso por meio de formulários de entrada de dados.
    2. *Módulo de Faturamento e Cobrança:* Engloba a Emissão de 2ª via de fatura e a geração do Relatório de Nada Consta. Caracteriza-se por interfaces de consulta transacional e exportação de relatórios em formato PDF.
    3. *Módulo de Monitoramento de Consumo e Serviços:* Contempla o Histórico de Consumo e os Indicadores de Continuidade, exigindo interfaces ricas (gráficos e tabelas) para a visualização de métricas ao longo do tempo.


* **Interfaces e Dependências:** A aplicação opera estritamente através de interfaces gráficas de usuário (GUI) baseadas na Web, exigindo como requisito de software o uso de navegadores de internet padrão (browsers). Arquiteturalmente, as operações do sistema possuem forte dependência de integração com o banco de dados corporativo da Neoenergia (back-end) para validar credenciais, recuperar históricos de medição de energia e atestar status de pagamentos em tempo real.


* **Ambiente e Massa de Dados:** Para estabelecer um ambiente de avaliação válido, serão utilizados dados reais de uma unidade consumidora localizada em Taguatinga. Esta massa de dados disponível e fidedigna é essencial para agilizar a avaliação sem causar impactos ou simular falsos positivos.


* **Perfil dos Usuários e Nível de Conhecimento:** O ambiente no qual o produto está inserido abrange a população do Distrito Federal. O sistema exige a interação de usuários com níveis altamente heterogêneos de conhecimento em informática e no domínio do serviço. Tal variação exige forte ênfase na Engenharia Humana durante a avaliação.

---


## **Referências**

* GALIN, D. *Software Quality: Concepts and Practice*. IEEE Computer Society, John Wiley & Sons, 2018.
* GARVIN, D. A. What Does "Product Quality" Really Mean?. *Sloan Management Review*, Fall 1984.
* ISO/IEC. *ISO/IEC 25010:2011 - Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. Genebra: ISO, 2011.
* ONU – Organização das Nações Unidas. *Os Objetivos de Desenvolvimento Sustentável no Brasil*. Disponível em: [https://brasil.un.org/pt-br/sdgs](https://brasil.un.org/pt-br/sdgs). Acesso em: 20 out. 2026.
* PRESSMAN, R. S. *Software Engineering: A Practitioner's Approach*, 7. ed. Nova York: McGraw Hill, 2010.
* RAMOS, C. S. *Processo de Avaliação de Produto de Software*. Material de apoio e slides da disciplina Qualidade de Software 1. Brasília: Universidade de Brasília (UnB), 2026.

---


## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 16/10/2026 | Criação do documento inicial de Fase 1 | Dara Maria Barbosa de Sousa |
| 1.1| 19/10/2026 | Descrição dos modulos do sistema| Dara Maria Barbosa de Sousa |
