# Teste Browser-use

**Resumo Executivo dos Testes**

Analisando a performance e os resultados dos modelos **GPT 4o** e **DS-Reasoner** em três cenários específicos de extração e validação de informações. Abaixo estão os principais pontos avaliados:

---

### **Cenário 1: Previsão do tempo para São Paulo - SP**

- **GPT 4o**: Apresentou a temperatura (26°C) e a condição climática (tempestade intensa) para o dia seguinte de maneira clara, precisa e sem artefatos de automação.
- **DS-Reasoner**: Gerou resultados semelhantes, com formato limpo e dados consistentes, também sem sinais de automação no texto final.

---

### **Cenário 2: Obtenção do preço da ação da NVIDIA**

- **GPT 4o**: Informou o preço da ação como $142,62 (fechamento) e confirmou o salvamento em arquivo de texto. A execução foi rápida e eficiente.
- **DS-Reasoner**: Apesar de capturar o preço ($142,62), houve inconsistências:
    - Utilizou vírgula como separador decimal, contrariando o formato padrão dos EUA.
    - Incluiu artefatos de automação no resultado (e.g., "Navigated to URL").
    - Não confirmou a criação do arquivo de texto, limitando o cumprimento da tarefa.

---

### **Cenário 3: Comparação de preços da câmera Insta360 X4**

- **GPT 4o**: Apresentou os preços de maneira organizada e coletou informações de múltiplas plataformas (Google Shopping, Amazon Brasil, Mercado Livre). Valores específicos foram destacados:
    - Mercado Livre: R$ 4.034, R$ 4.389, R$ 4.689.
- **DS-Reasoner**: Conseguiu coletar preços semelhantes, mas enfrentou limitações:
    - Formato final incluiu inconsistências de automação.
    - Um erro de contexto no modelo foi reportado, impactando o processamento da tarefa.

---

### **Custos e Experiência**

- Custos totais:
    - **GPT 4o**: USD 0,70
    - **DS-Reasoner**: USD 0,22
- Velocidade:
    - **GPT 4o** foi significativamente mais rápido, beneficiando-se de capacidades avançadas como visão.
    - **DS-Reasoner** apresentou maior tempo de execução, além de erros pontuais no processo de validação.
- Consideração: Apesar dos erros no **DS-Reasoner**, ajustes no processo de validação podem tornar o modelo mais robusto e eficiente.

---

### **Conclusão**

O **GPT 4o** mostrou-se superior em precisão, clareza e tempo de execução, especialmente em cenários mais complexos. No entanto, o **DS-Reasoner** oferece uma alternativa mais econômica, com potencial de melhoria em validação e formatação dos resultados. A escolha entre os modelos dependerá do balanço entre custo e desempenho desejado.

---

# Apêndice, resultados e anotações feitas durante os testes:

## **Prompt 1:**

**"what's the weather for São Paulo - SP for tomorrow?"**

**GPT 4o** 

The result directly answers with tomorrow's temperature (26°C) and condition (intense thunderstorm) for São Paulo - SP. Values are reasonable, and the final output avoids browser automation artifacts, focusing on relevant weather data.

**DS-Reasoner** 

Notes: The result directly provides tomorrow's temperature (26°C) and condition for São Paulo - SP. Values are plausible, and the format is clean without browser automation steps (e.g., "Navigated to..." or "Sent keys") in the final answer.

---

## **Prompt 2:**

**"Get NVIDIA's stock price and save it to a text file."**

**GPT 4o** 

{'text': "The NVIDIA stock price is mentioned as 142.62 (closing) in the extracted content. Saving this value into the file 'nvidia_stock_price.txt'."}}])

**DS-Reasoner** 

AgentHistoryList(all_results=[ActionResult(is_done=False, extracted_content='🔗  Navigated to https://www.google.com/finance/quote/NVDA:NASDAQ', error=None, include_in_memory=True), ActionResult(is_done=True, extracted_content='NVDA stock price: $142,62 (as of 2025-01-26 19:21)', error=None, include_in_memory=False)], all_model_outputs=[{'go_to_url': {'url': 'https://www.google.com/finance/quote/NVDA:NASDAQ'}}, {'done': {'text': 'NVDA stock price: $142,62 (as of 2025-01-26 19:21)'}}])

🔍 Quality Check:

Validation: ERROR

Notes: The stock price uses a comma as a decimal separator ($142,62), which is inconsistent with standard US formatting. The date (2025-01-26) is in the future, suggesting invalid or test data. The automation artifacts (e.g., "Navigated to URL") are included, and saving to a text file is not confirmed.

---

## **Prompt 3:**

**"Encontre 3 preços para a camera de vídeo Insta360 X4."**

**GPT 4o** 

Result: Successfully collected the prices for Insta360 X4 from multiple platforms:

1. ****Google Shopping****

- Prices for multiple listings were extracted but are not displayed here for privacy.

2. ****Amazon Brazil****

- Prices were extracted for 'Insta360 X4', but specific values are not disclosed.

3. ****Mercado Livre****

- First product: R$ 4.034

- Second product option: R$ 4.389

- Third product: R$ 4.689

**DS-Reasoner** 

:{"text":"Price comparison complete:\n- Preço 1 (Google Shhopping): R$4.034,00\n- Preço 2 (Amazon): R$4.399,00\n- Preço 3 (Mercado Livre): R$4.034"}}

INFO     [agent] 📄 Result: Price comparison complete:

- Preço 1 (Google Shopping): R$4.034,00
- Preço 2 (Amazon): R$4.399,00
- Preço 3 (Mercado Livre): R$4.034

INFO     [agent] ✅ Task completed successfully

WARNING  [agent] No history or first screenshot to create GIF from

❌ Error: Error code: 400 - {'error': {'message': "This model's maximum context length is 65536 tokens. However, you requested 96438 tokens (96438 in the messages, 0 in the completion). Please reduce the length of the messages or completion.", 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_request_error'}}

---

## Gastos no dia:

Usei DS em todos os testes pra pensar no prompt do browser

Custos por plataforma:

GPT - USD 0,70

DS - USD 0,22

---

## Experiência:

Na experiência, GPT4o por ter visão, foi mega rápido, enquanto o DS teve um tempo considerável de execução.

Ambos chegaram nos resultados, o DS teve o Validation retornando erro, porém o valor foi capturado e estava no text, acho que cabe um ajuste no validation e funcionará normal
