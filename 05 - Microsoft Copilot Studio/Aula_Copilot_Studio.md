
# 🤖 Aula: Trabalhando com Tópicos no Microsoft Copilot Studio

## 🎯 Objetivo da Aula
Explorar o funcionamento dos **tópicos** no Copilot Studio, aprender a criar fluxos inteligentes com gatilhos, ações, ramificações, uso de entidades e fallback inteligente para melhorar a experiência do usuário.

---

## 🧠 O que são Tópicos?

Tópicos são blocos de conversa que respondem a **intuições específicas do usuário**. Cada tópico tem:

- **Gatilhos**: frases que iniciam o tópico.
- **Ações**: o que o bot executa quando o tópico é acionado.

Eles permitem modularizar o comportamento do bot e criar fluxos lógicos reutilizáveis e claros.

---

## 🏗️ Tipos de Tópicos

### 🔹 Tópicos do Sistema
- Predefinidos pela plataforma.
- Lidam com interações padrão como:
  - Saudação (OnStartConversation)
  - Encerramento
  - Falhas de entendimento (Fallback)

### 🔸 Tópicos Personalizados
- Criados pelo usuário para atender objetivos específicos.
- Ex: “Consultar boleto”, “Dicas de viagem”, “Agendar atendimento”.

---

## 🧲 Gatilhos

Gatilhos são frases ou intenções que ativam o tópico. São analisadas com NLP e podem ser:

- Frases completas ("quero viajar")
- Expressões curtas ("viagem")
- Variantes de intenção ("obrigado", "valeu", "agradeço")

---

## ⚙️ Ações

Após o gatilho, o tópico executa **ações**, como:

- `SendActivity` → responde com uma mensagem.
- `Ask a question` → coleta dados do usuário.
- `BeginDialog` → chama outro tópico.
- `SetVariable`, `Condition` → lógica interna.

---

## 🧭 Interface do Copilot Studio

### ✏️ Topic Details
- Nome, descrição, status (ativo/inativo), prioridade.

### 🔍 Input
- Lista de gatilhos de texto.

### 📤 Output
- Fluxos de ações, variáveis, redirecionamentos.

---

## 🛠️ Exemplo de Tópico Criado

### 🔖 Nome do Tópico
**Dicas de viagem**

### 📌 Prompt
```
Por favor busque para mim [Numero] de opções de atividades no [Destino] para pessoas que estão conhecendo pela primeira vez. Por favor retorne uma lista enumerada com emojis no nome de atividade e uma breve descrição.
```

### ✅ Resposta Esperada
```
Claro! Aqui estão 3 sugestões de atividades em Lisboa para quem está visitando pela primeira vez:

1. 🏰 Castelo de São Jorge – Uma fortaleza histórica com vistas panorâmicas da cidade.
2. 🚋 Passeio no Elétrico 28 – Um clássico bonde amarelo que percorre os principais bairros históricos.
3. 🌊 Visita ao Oceanário – Um dos maiores aquários da Europa, ideal para todas as idades.

Aproveite sua viagem! 🌍✈️
```

---

## 🌿 Ramificações em Tópicos

Ramificações permitem criar **caminhos alternativos** dentro do fluxo de um tópico, com base em:

- Condições (`If/Else`)
- Respostas do usuário
- Valor de variáveis

### ✨ O que você pode fazer:
- **Redirecionar** para um passo específico
- **Transferir controle** para outro tópico (`BeginDialog`)
- **Encerrar** a conversa ou o tópico atual (`EndDialog`)

💡 Exemplo:
```yaml
- kind: IfCondition
  condition: =destination == 'Lisboa'
  actions:
    - kind: SendActivity
      activity: "Você escolheu Lisboa! Aqui vão algumas dicas locais."
```

---

## 🔄 Tópicos de Fallback do Sistema

### ❓ O que é Fallback?

É o comportamento padrão quando o bot **não entende a intenção do usuário**. No Microsoft Copilot Studio, o tópico de fallback é chamado:

```yaml
OnUnrecognizedIntent
```

### ⚙️ Como configurar:
1. Vá em **System Topics**
2. Selecione **OnUnrecognizedIntent**
3. Customize a resposta com `SendActivity`, redirecione ou logue a falha.

💡 Dica:
Você pode criar **uma lista de perguntas de acompanhamento**, ou até mesmo **transferir o controle para um atendente humano**.

---

## 🧩 Entidades e Variáveis no Microsoft Copilot Studio

### 📦 O que são Entidades?

Entidades são **tipos de dados estruturados** que o bot consegue extrair das respostas dos usuários. Exemplos:

- Número (`Number`)
- Localização (`Location`)
- Data (`Date`)
- Personalizadas (ex: `TipoDeViagem`)

### 🧮 O que são Variáveis?

Variáveis armazenam **valores temporários** coletados durante a conversa. São úteis para manter o contexto e controlar decisões.

### 🧠 Preenchimento de Slot

É a técnica de **fazer perguntas sequenciais** até que todas as entidades necessárias estejam preenchidas.

💬 Exemplo:
```
Bot: Qual destino deseja visitar?
Usuário: Lisboa
→ destino = Lisboa

Bot: Quantas atividades você deseja?
Usuário: 3
→ numero = 3
```

### Exemplo com Slots:

```yaml
- kind: AskQuestion
  property: destino
  question: Qual é o destino desejado?

- kind: AskQuestion
  property: numero
  question: Quantas atividades você gostaria de receber?
```

---

## 📚 Modelos de Prompts para Criação de Tópicos

A Microsoft oferece uma galeria com **prompts prontos** no site:

🔗 [https://aka.ms/power-prompts](https://aka.ms/power-prompts)

### Exemplos de Prompts:

- 🧠 **Explicação simples**  
  "Explique esse conceito como se fosse para uma criança."

- 🔍 **Resumo de texto**  
  "Leia o conteúdo abaixo e me dê um resumo em 3 frases."

- 📊 **Análise de sentimento**  
  "Esse texto é positivo, negativo ou neutro?"

- 🧾 **Extração de dados**  
  "Liste todos os produtos com nome e preço no texto abaixo."

---

## ✅ Conclusão

Compreender tópicos, gatilhos, ações, fallback, entidades e variáveis é essencial para construir bots úteis e eficientes no **Microsoft Copilot Studio**. A prática com prompts e ramificações permite maior personalização e escalabilidade nas conversas.

Explore, crie, teste e otimize! 🚀🤖
