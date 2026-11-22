# Ação de melhoria
 
> **Projeto:** Avaliação de Qualidade de Software — Agência Virtual Neoenergia Brasília  
> **Origem:** [Resultados de G1 — Capacidade de Interação](./resultados-g1-capacidade-interacao.md), oportunidade **OM-01**  
> **Funcionalidade-alvo:** Indicadores de Continuidade (DIC, FIC e DMIC)    
> **Tipo de ação escolhida:** Protótipo de alta fidelidade
 
## 1. Origem da ação
 
Esta página desenvolve a oportunidade **OM-01**, priorizada na seção [Oportunidades de melhoria](./resultados-g1-capacidade-interacao.md#5-oportunidades-de-melhoria) dos Resultados de G1. A análise dos dados está naquela página. Aqui ficam apenas os pontos que orientam o que será criado:
 
- M9 ficou em 80%, no limite da meta, e **toda a perda veio da tela de Indicadores de Continuidade**, reconhecida por 3 de 5 participantes.
- Os dois erros escolheram a mesma alternativa, **"histórico de consumo"**. A nova tela precisa deixar explícito o que ela mostra **e o que não mostra**.
- Dois dos três acertos vieram com hesitação. A tela precisa ser entendida **sem depender de comparação entre alternativas**.
- Erraram participantes de familiaridade baixa e alta. A solução precisa servir **a todos os perfis**.


## 2. Justificativa da escolha
 
O problema é de **interface, linguagem e fluxo de navegação**, e não técnico: não houve falha do sistema (FS) em nenhuma sessão. Por isso a ação escolhida é um **protótipo de alta fidelidade**, pelos seguintes motivos:
 
1. **Ponto mais frágil da avaliação:** com mais um erro na Tela B, M9 cairia para 70% e H9 não seria sustentada.
2. **Erro induzido pela tela:** a confusão sempre com o histórico de consumo indica que o layout (tabela de Mês/Ano) e o texto ("detalhar seu histórico") levam a essa leitura. Isso se corrige no desenho da tela.
3. **Operação que não pôde ser medida:** a tarefa T4 (alterar o período do gráfico) foi excluída porque a interface atual é uma tabela estática. O protótipo cria essa interação e permite medi-la.
4. **Validação antes do código:** o protótipo permite repetir o cenário U-03 com o mesmo protocolo, sem depender de acesso ao código da Neoenergia.

 
## 4. O que será criado
 
### 4.1 Conceito
 
Centralizar as duas telas em **uma única página, "Qualidade do fornecimento de energia"**, que responda em poucos segundos as três perguntas do usuário:
 
1. **Para que serve esta página?** Subtítulo em linguagem simples.
2. **Está tudo bem com a minha energia?** Cartões de situação com ícone, texto e cor.
3. **Quando e quanto fiquei sem energia?** Gráfico dinâmico por mês, com o limite permitido e o detalhe na mesma tela.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 21/11/2026 | Criação da página | Beatriz |
| 1.1 | 22/11/2026 | Proposta inicial da ação de melhoria para a funcionalidade Indicadores de Continuidade | Beatriz |