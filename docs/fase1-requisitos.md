# Fase 1: Requisitos de Avaliação

## 1. Propósito da avaliação
O propósito desta avaliação é analisar a qualidade do software "Agência Virtual da Neoenergia Brasília", com o objetivo de indicar pontos para melhoria no produto e compreender o seu comportamento diante de cenários práticos de uso. Do ponto de vista dos usuários finais e da equipe de avaliação (alunos de Engenharia de Software), a análise será focada nas visões de qualidade do usuário e do produto, conforme definidas por Garvin (1984). A visão do usuário considera a adequação ao uso, enquanto a visão do produto foca nos atributos e propriedades internas que resultam na qualidade externa.

## 2. Produto avaliado
* **Nome do produto:** Agência Virtual da Neoenergia Brasília.
* **Descrição e Categoria:** O sistema enquadra-se na categoria de **Software Comercial** (Pressman, 2010), organizado de forma a facilitar operações financeiras e de prestação de serviços para clientes corporativos e residenciais.
* **Principais tarefas e escopo de avaliação:**
    1. Login e Cadastro de Usuário
    2. Emissão de segunda via de fatura
    3. Histórico de consumo
    4. Relatório de Nada Consta
    5. Indicadores de continuidade
* **Perfil dos Usuários:** População em geral do Distrito Federal, abrangendo desde cidadãos leigos até usuários com alto conhecimento em informática. Tal heterogeneidade exige forte ênfase na Engenharia Humana e Usabilidade (Galin, 2018).

## 3. Modelos de qualidade
A avaliação baseia se na família de normas **SQuaRE (Software product Quality Requirements and Evaluation)**, especificamente a **ISO/IEC 25010** (Modelo de Qualidade de Produto).

 Detalhamos abaixo as características e subcaracterísticas escolhidas. Cada uma recebeu uma nota de "ênfase" (em uma escala de 1 a 5, onde 1 significa nenhum interesse e 5 representa grande interesse para a avaliação):

* **Usabilidade (Ênfase 5):** A usabilidade mede o quão fácil e intuitivo é utilizar o sistema. Como a Agência Virtual atende a toda a população (desde pessoas com muita facilidade com tecnologia até pessoas com nenhuma), este é um ponto crucial.
    * *Apreensibilidade (Learnability):* Avalia se um usuário iniciante consegue aprender rapidamente a usar as funções básicas, como emitir uma segunda via ou consultar um histórico, sem precisar de manuais.
    * *Proteção contra erros do usuário (User error protection):* Verifica se o sistema ajuda o usuário a não cometer erros ou a corrigi-los facilmente. Por exemplo, se o usuário digitar um CPF incompleto ou com letras, o sistema deve avisar claramente o que está errado, em vez de simplesmente travar (ISO/IEC 25010; Galin, 2018).

* **Confiabilidade (Ênfase 4):** A confiabilidade diz respeito à capacidade do sistema de se manter funcionando de forma correta e estável, sem apresentar falhas inesperadas durante o uso.
    * *Maturidade:* Avalia a frequência com que o sistema apresenta defeitos visíveis no dia a dia.
    * *Tolerância a falhas:* Mede como o sistema reage quando algo dá errado (como a inserção de dados inválidos ou uma pequena falha de rede). Realizaremos testes simulando ações atípicas do usuário para garantir que o sistema lide com essas situações de forma "elegante", exibindo mensagens de erro amigáveis sem interromper totalmente o serviço (ISO/IEC 25010; Galin, 2018).

* **Segurança (Ênfase 5):** Como a Agência Virtual lida com dados pessoais e informações financeiras (faturas, endereço, histórico de consumo), a segurança é a capacidade do software de proteger essas informações contra acessos de terceiros.
    * *Confidencialidade:* Garante que os dados do cliente só sejam acessíveis pela pessoa que possui a autorização e as credenciais corretas para vê-los.
    * *Integridade:* Garante que os dados não possam ser alterados indevidamente. Avaliaremos, por exemplo, os mecanismos de bloqueio da plataforma após múltiplas tentativas de login com senha incorreta, atestando a proteção da conta (ISO/IEC 25010).

* **Eficiência de Desempenho (Ênfase 4):** Esta característica mede a agilidade do sistema e o tempo que o usuário precisa esperar para que uma tarefa seja concluída.
    * *Comportamento no tempo (Time behavior):* Avalia especificamente o tempo de resposta da plataforma. Vamos testar e observar, por exemplo, quanto tempo o sistema demora para processar o login, gerar o PDF da segunda via da fatura para download ou carregar os gráficos da tela de histórico de consumo (ISO/IEC 25010).

---

## Referências Bibliográficas
* GALIN, D. *Software Quality: Concepts and Practice*. IEEE Computer Society, John Wiley & Sons, 2018.
* GARVIN, D. A. *What Does "Product Quality" Really Mean?*. Sloan Management Review, Fall 1984.
* ISO/IEC 25010:2011. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*.
* PRESSMAN, R. S. *Software Engineering: A Practitioner's Approach*, 7 ed., McGraw Hill, 2010.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 16/10/2026 | Criação do documento inicial de Fase 1 | Dara Maria Barbosa de Sousa |
| 1.1 | 16/10/2026 | Remoção de Mitigação de Riscos e refatoração de formatação | Dara Maria Barbosa de Sousa |