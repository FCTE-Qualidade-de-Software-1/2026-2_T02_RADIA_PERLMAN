---
hide:
  - toc
---

# Rastreabilidade entre as Fases 1 e 2

Na Fase 1, definimos como propósito identificar oportunidades de melhoria na Agência Virtual da Neoenergia Brasília, considerando as necessidades dos consumidores. As quatro características priorizadas com base na ISO/IEC 25010:2011 serviram de referência para a escolha das métricas apresentadas nesta fase.

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

A tabela indica em quais funcionalidades pretendemos aplicar cada métrica. Antes dos testes, verificaremos quais etapas estão acessíveis, especialmente nos serviços que exigem autenticação ou emissão de documentos.

| Funcionalidade | Métricas previstas | Condições de aplicação |
|---|---|---|
| Login e cadastro | M1, M2, M3, M7 e M8; M5 em página pós-login; M4 se viável | Testes em campos seguros, sem cadastro fictício nem alteração de conta. |
| Segunda via de fatura | M1, M3, M5, M6, M7 e M8; M4 se viável | Consultas autorizadas. O tempo de geração de PDF só será medido se a operação for efetivamente realizada. |
| Histórico de consumo | M1, M3, M5, M6, M7 e M8; M4 se viável | Comparações limitadas a períodos e referências estáveis da conta autorizada. |
| Relatório de Nada Consta | M1, M3, M5, M7 e M8; M4 se viável | Avaliação das etapas de navegação acessíveis sem modificar registros. |
| Indicadores de continuidade | M1, M3, M7 e M8; M4 se viável | Acesso, estabilidade e apresentação da tela, sem examinar os cálculos internos do indicador. |

Registraremos os cenários escolhidos antes de começar. Se não houver acesso a alguma etapa ou não conseguirmos reunir observações suficientes, o resultado correspondente ficará inconclusivo, com a justificativa documentada.

## 3. Delimitação do escopo

Retiramos a adequação funcional do escopo e, por isso, não definimos indicadores de completude ou correção funcional. Também não incluímos testes de carga, auditoria de código-fonte ou avaliações da infraestrutura. As métricas escolhidas se concentram no comportamento que conseguimos observar pela interface.

Esse recorte considera as condições de acesso ao sistema. Como estamos avaliando um serviço de terceiros sem privilégios administrativos, nossas conclusões ficarão limitadas aos fluxos executados e às evidências obtidas durante os testes.

## 4. Correspondência conceitual com a Fase 1

Dois exemplos citados na definição inicial do escopo exigem uma distinção na hora de medir:

- **Dados inválidos e tolerância a falhas.** A reação a um campo preenchido incorretamente será tratada em M2, vinculada à proteção contra erros do usuário. Para tolerância a falhas, a M4 observa especificamente uma interrupção breve da conexão local, durante navegação de leitura.
- **Bloqueio após senhas incorretas e integridade.** O bloqueio de tentativas de autenticação é um mecanismo mais diretamente ligado ao controle de acesso. A confidencialidade será examinada em M5; a subcaracterística integridade permanece representada em M6 por uma verificação indireta de consistência entre consultas.

A M6 não permite verificar a integridade do armazenamento ou a resistência a alterações indevidas. Ao apresentar os resultados, manteremos essa distinção entre a consistência observada na interface e os mecanismos internos de proteção.

Em M3, a taxa será calculada separadamente para cada fluxo; em M5, qualquer exposição de dados protegidos sem autenticação resultará em classificação insatisfatória. Essa opção evita que resultados agregados ocultem problemas relevantes. O [gráfico GQM](grafico-gqm.md) apresenta as ligações entre objetivos, questões e métricas, e os [critérios de julgamento](criterios-julgamento.md) explicam a classificação. O acompanhamento do trabalho pelo [PSM/CID](gestao-psm.md) permanece separado das medidas de qualidade do produto.

## Histórico de Versões

| Versão | Data | Descrição da Alteração | Autor(a) |
|---|---|---|---|
| 1.0 | 17/10/2026 | Criação do documento da rastreabilidade| Arthur de Lima Sobreira |
| 1.1 | 20/10/2026 | Revisão e versionamento | Henrique Martins Alencar |