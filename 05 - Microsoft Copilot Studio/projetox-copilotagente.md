# 🧠 Projeto Copilot Studio - Criação de Agente Inteligente

## 🎯 Objetivo

Criar um agente personalizado no Copilot Studio que atue como assistente oficial da plataforma DIO, retornando respostas da documentação oficial da Microsoft (Microsoft Learn), com foco em Copilot Studio, Power Platform e AI Builder.

---

## ✅ Etapa 01 - Criar o Agente

### Nome do Agente:

**Agent da DIO | Projeto X**

### Descrição:

> Agente responsável por buscar conteúdos de Copilot Studio dentro da documentação oficial da Microsoft, sendo que toda a atuação dele será como o "Agente da DIO".

### Instruções do Agente:

```
Você é o agente chamado "Agente da Dio", e vai agir em tom formal com o idioma em português, para retornar informações relevantes da documentação oficial da Microsoft, o Microsoft Learn.
Ao retornar uma resposta para a pergunta do usuário você deve considerar:
- Buscar a melhor resposta na documentação
- Retornar a resposta apropriada e amigável, em tom formal
- Retornar uma ou mais citações da documentação
```

---

## ✅ Etapa 02 - Customizar um Tópico

### Criar um novo tópico:

- **Clique em "Tópicos" > "Adicionar tópico em branco"**

### Frases de gatilho (phrases):

- "Buscar informações de AI Builder"
- "O que é AI Builder"
- "Onde encontro informações da ferramenta de AI da Power Platform"

### Ação seguinte:

- Clique em **"Criar respostas com IA"** (Create with Copilot / Generate Answers)
- A IA irá sugerir respostas com base nas frases de gatilho.

---

## ✅ Etapa 03 - Personalizar mensagem de erro (Fallback)

### Personalizando a mensagem de erro:

1. Acesse o **"Bot de Conversação"** no menu principal.
2. Vá até a seção **"Fallback (quando o bot não entende)"**.
3. Edite a mensagem padrão com algo mais personalizado, por exemplo:

```
Desculpe, ainda não tenho uma resposta para isso com base na documentação da Microsoft. Por favor, tente reformular sua pergunta ou pergunte algo relacionado ao Copilot Studio ou Power Platform.
```

---

## ✅ Etapa 04 - Ajustar qualidade da resposta com GenAI

No editor de respostas do tópico:

1. Clique na **resposta gerada automaticamente pela IA**.
2. Use os botões:
   - 🔽 **“Menos criativa” (Make less creative)**: para uma resposta mais direta, técnica e próxima do conteúdo original.
   - 🔼 **“Mais criativa” (Make more creative)**: para respostas com linguagem mais natural, mais adaptada à conversa.

> ⚠️ Ajustar a criatividade afeta o tom e a forma da resposta, mas sempre mantenha a fidelidade à fonte oficial.

---

## 📁 Materiais relacionados

- [Documentação Microsoft Learn](https://learn.microsoft.com/pt-br/)
- [Copilot Studio - Introdução](https://learn.microsoft.com/pt-br/copilot-studio/overview)
- [AI Builder](https://learn.microsoft.com/pt-br/ai-builder/)

---

**Desenvolvido por:** Agatha Ruiz  
**Curso:** Projeto prático com Copilot Studio — DIO
