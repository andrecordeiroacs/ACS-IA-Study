# Testes com IA - Documentação

## 📝 Resultados dos Testes

### **Prompt 1:**

**"Vai chover amanhã em São Paulo?"**

#### **GPT 4o** 
- **Resposta:** Probabilidade de chuva para amanhã em São Paulo é de 75%.

#### **DS-Reasoner** 
- **Resposta:** Sim, há previsão de chuva de 85% amanhã em São Paulo.

📌 **Análise:** Ambos os modelos forneceram previsões coerentes e dentro da margem de erro aceitável. O DS-Reasoner indicou uma probabilidade maior de chuva, o que pode ser consequência da base de dados utilizada. Como modelos de IA não possuem acesso em tempo real a fontes meteorológicas, recomenda-se sempre cruzar informações com serviços oficiais.

---

### **Prompt 2:**

**"Qual preço da ação da NVIDIA?"**

#### **GPT 4o** 
- **Resposta:** The current NVIDIA stock price is 14.92 BRL.

#### **DS-Reasoner** 
- **Resposta:** NVIDIA (NVDA) current price: $123,70

📌 **Análise:** Aqui, há uma discrepância considerável entre os valores retornados. GPT-4o apresentou um preço que não parece condizente com a realidade, enquanto DS-Reasoner trouxe um valor mais plausível em dólares. Isso indica que o GPT-4o pode ter retornado um dado desatualizado ou extraído de uma fonte menos confiável. Esse teste reforça a necessidade de validação em fontes financeiras oficiais, como Google Finance, Yahoo Finance ou Nasdaq.

---

### **Prompt 3:**

**"Encontre 3 preços para a câmera de vídeo Insta360 X4."**

#### **GPT 4o** 
- **Preços encontrados:**
  1. **R$ 3.178,99** - AliExpress (novo)
  2. **R$ 3.489,90** - [Amazon.com.br](http://amazon.com.br/) (novo, com bundle)
  3. **R$ 3.974,24** - Mercado Livre (novo)

  *Observação:* Há ofertas desde R$ 1.730,49 (AliExpress), mas requerem verificação de autenticidade.

#### **DS-Reasoner** 
- **Validação:** OK
- **Notas:** O agente extraiu três preços com sucesso, mas ocorreu um erro intermediário de parsing JSON.
- **Preços ajustados:**
  - **R$ 3.943,00**
  - **R$ 3.974,24**
  - **R$ 3.167,90**

  *Recomendação:* Verificar os preços devido ao erro de parsing durante a execução.

📌 **Análise:** O GPT-4o retornou preços bem estruturados e com links diretos para marketplaces, facilitando a verificação pelo usuário. Já o DS-Reasoner teve dificuldades no processamento dos dados, apresentando um erro de parsing. Embora os valores sejam próximos, a inconsistência técnica no DS-Reasoner pode impactar sua confiabilidade para buscas de preços.

---

## 💰 Custos do Teste

- **Utilização do DS para auxiliar nos prompts do browser.**
- **Custos por plataforma:**
  - **GPT-4o:** USD 0,70
  - **DS-Reasoner:** USD 0,22

📌 **Análise:** O custo do GPT-4o foi significativamente maior que o do DS-Reasoner, o que pode impactar na escolha do modelo dependendo do volume de chamadas necessárias. Para consultas rápidas e com alta confiabilidade, o GPT-4o parece valer o investimento. Já o DS-Reasoner pode ser uma alternativa econômica, desde que as falhas de formatação sejam corrigidas.

---

## 🚀 Experiência

- **Velocidade:**
  - O **GPT-4o** foi muito mais rápido, especialmente por ter visão integrada.
  - O **DS-Reasoner** teve um tempo de execução considerável.

- **Qualidade da saída:**
  - Ambos chegaram aos resultados esperados.
  - O **DS-Reasoner** teve algumas falhas na formatação da saída, mas cumpriu a tarefa.

📌 **Análise:** Em termos de experiência, o GPT-4o se destacou pela velocidade e precisão dos resultados. O DS-Reasoner, embora tenha atingido os objetivos, apresentou mais erros na estrutura das respostas, o que pode exigir retrabalho ou verificações adicionais.

---

## 🔍 Conclusão

- **GPT-4o** se mostrou mais rápido, preciso e confiável, porém com um custo mais alto.
- **DS-Reasoner** teve desempenho aceitável, mas com limitações técnicas na formatação e processamento de informações.
- Para tarefas críticas que exigem precisão, o GPT-4o é a melhor escolha.
- O DS-Reasoner pode ser útil em casos onde o custo é um fator determinante, desde que haja verificação adicional das saídas.

📌 **Recomendações futuras:** Explorar outros modelos para avaliar custo-benefício e testar diferentes abordagens para melhorar a confiabilidade das respostas geradas pelo DS-Reasoner.
