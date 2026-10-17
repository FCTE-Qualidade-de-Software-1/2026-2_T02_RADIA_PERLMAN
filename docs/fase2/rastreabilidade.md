---
hide:
  - toc
---

# Rastreabilidade entre as Fases 1 e 2

O propósito estabelecido na Fase 1 é identificar oportunidades de melhoria na Agência Virtual da Neoenergia Brasília, considerando o uso do serviço pelos consumidores e as observações da equipe de avaliação. A seleção de métricas parte das quatro características priorizadas naquele documento, com base no modelo de qualidade da ISO/IEC 25010:2011.

## 1. Relação entre características, questões e métricas

| Característica | Ênfase | Subcaracterística | Objetivo | Questão e hipótese | Métrica |
|---|---:|---|---|---|---|
| Usabilidade | 5 | Apreensibilidade | [G1](objetivos.md#g1) | [Q1/H1](questoes-hipoteses.md#q1) | [M1](metricas.md#m1) — localização sem ajuda. |
| Usabilidade | 5 | Proteção contra erros | [G1](objetivos.md#g1) | [Q2/H2](questoes-hipoteses.md#q2) | [M2](metricas.md#m2) — validação de entradas inválidas. |
| Confiabilidade | 4 | Maturidade | [G2](objetivos.md#g2) | [Q3/H3](questoes-hipoteses.md#q3) | [M3](metricas.md#m3) — execuções sem falhas por fluxo. |
| Confiabilidade | 4 | Tolerância a falhas | [G2](objetivos.md#g2) | [Q4/H4](questoes-hipoteses.md#q4) | [M4](metricas.md#m4) — recuperação após desconexão local. |
| Segurança | 5 | Confidencialidade | [G3](objetivos.md#g3) | [Q5/H5](questoes-hipoteses.md#q5) | [M5](metricas.md#m5) — bloqueio integral de acesso sem sessão. |
| Segurança | 5 | Integridade | [G3](objetivos.md#g3) | [Q6/H6](questoes-hipoteses.md#q6) | [M6](metricas.md#m6) — consistência visível de dados estáveis. |
| Eficiência de desempenho | 4 | Comportamento no tempo | [G4](objetivos.md#g4) | [Q7/H7](questoes-hipoteses.md#q7) | [M7](metricas.md#m7) — tempo mediano por fluxo. |
| Eficiência de desempenho | 4 | Comportamento no tempo | [G4](objetivos.md#g4) | [Q8/H8](questoes-hipoteses.md#q8) | [M8](metricas.md#m8) — percentil 90 por fluxo. |

Usabilidade e segurança têm ênfase 5 na Fase 1; confiabilidade e eficiência de desempenho, ênfase 4. Essa diferença orientará a prioridade das recomendações, não a fórmula dos indicadores.

## 2. Aplicação das métricas às funcionalidades

A associação abaixo indica os fluxos previstos para observação. A disponibilidade real de cada etapa será confirmada no início da coleta, especialmente quando houver autenticação ou emissão de documentos.

| Funcionalidade | Métricas previstas | Condições de aplicação |
|---|---|---|
| Login e cadastro | M1, M2, M3, M7 e M8; M5 em página pós-login; M4 se viável | Testes em campos seguros, sem cadastro fictício nem alteração de conta. |
| Segunda via de fatura | M1, M3, M5, M6, M7 e M8; M4 se viável | Consultas autorizadas. O tempo de geração de PDF só será medido se a operação for efetivamente realizada. |
| Histórico de consumo | M1, M3, M5, M6, M7 e M8; M4 se viável | Comparações limitadas a períodos e referências estáveis da conta autorizada. |
| Relatório de Nada Consta | M1, M3, M5, M7 e M8; M4 se viável | Avaliação das etapas de navegação acessíveis sem modificar registros. |
| Indicadores de continuidade | M1, M3, M7 e M8; M4 se viável | Acesso, estabilidade e apresentação da tela, sem examinar os cálculos internos do indicador. |

A escolha de cada cenário deverá ser registrada antes da execução. Se uma etapa não puder ser acessada ou não fornecer observações suficientes, a métrica correspondente será apontada como inconclusiva, com justificativa.

## 3. Delimitação do escopo

Adequação funcional foi retirada da seleção de características. Assim, a avaliação não inclui indicadores específicos de completude ou correção funcional. Também ficam fora do estudo testes de carga, auditoria de código-fonte, avaliação da infraestrutura, alterações de dados de terceiros ou exploração de vulnerabilidades. As métricas adotadas trabalham com o comportamento observável no navegador.

Essa escolha decorre das condições concretas do projeto: trata-se de um serviço de terceiros, utilizado por consumidores, ao qual a equipe não possui acesso administrativo. Os resultados poderão apontar problemas percebidos no uso, mas não representarão uma análise de todos os componentes da plataforma.

## 4. Correspondência conceitual com a Fase 1

Dois exemplos citados na definição inicial do escopo exigem uma distinção na hora de medir:

- **Dados inválidos e tolerância a falhas.** A reação a um campo preenchido incorretamente será tratada em M2, vinculada à proteção contra erros do usuário. Para tolerância a falhas, a M4 observa especificamente uma interrupção breve da conexão local, durante navegação de leitura.
- **Bloqueio após senhas incorretas e integridade.** O bloqueio de tentativas de autenticação é um mecanismo mais diretamente ligado ao controle de acesso. A confidencialidade será examinada em M5; a subcaracterística integridade permanece representada em M6 por uma verificação indireta de consistência entre consultas.

A M6 não testa resistência a modificações não autorizadas nem integridade de armazenamento. A redação da Fase 1 e a interpretação dos resultados devem manter essa distinção para que as conclusões não ultrapassem as evidências disponíveis.

Na M3, cada fluxo terá uma taxa própria e o pior resultado será usado em G2; na M5, qualquer exposição efetiva de dados protegidos sem sessão levará à classificação insatisfatória de G3. Essas regras evitam que valores consolidados ocultem falhas relevantes. O [gráfico GQM](grafico-gqm.md) apresenta a hierarquia de objetivos, questões e métricas. Os [Critérios de julgamento](criterios-julgamento.md) detalham as decisões de classificação. O [PSM/CID](gestao-psm.md) acompanha a execução do projeto separadamente, sem integrar os resultados de qualidade do produto.
