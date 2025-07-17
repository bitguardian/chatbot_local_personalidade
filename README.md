
# 🤖 Chatbot Local com Personalidade

Um chatbot inteligente, 100% **offline**, alimentado por modelos de linguagem locais como **Zephyr**, **Mistral**, **LLaMA 2** e outros via [Ollama](https://ollama.com/). O projeto foi desenvolvido em **Python 3.10** e oferece memória persistente, estilos de resposta personalizáveis e interface moderna com **Gradio**.

---

## 📚 Como funciona?

Este chatbot utiliza modelos LLM rodando localmente via Ollama, sem necessidade de conexão com a nuvem. A aplicação mantém um histórico das conversas (memória), permitindo respostas contextualizadas e personalizadas conforme o estilo escolhido pelo usuário:

- **Amigável**: Respostas acolhedoras e descontraídas.
- **Formal**: Respostas educadas e profissionais.
- **Sarcástico**: Respostas irônicas e bem-humoradas.

O usuário interage via uma interface web (Gradio), seleciona o estilo desejado e conversa normalmente. Todo o histórico é salvo localmente, garantindo privacidade e funcionamento offline.

---

## 🗂️ Estrutura do Projeto

```
chatbot_local_personalidade/
├── chatbot.py                 # Funções de memória, montagem de prompt e personalidades
├── main.py                    # Interface Gradio e integração com Ollama
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
├── memory/
│   └── session_log.json       # Histórico persistente das conversas
├── personality_prompts/
│   ├── friendly.txt           # Prompt para personalidade amigável
│   ├── formal.txt             # Prompt para personalidade formal
│   └── sarcastic.txt          # Prompt para personalidade sarcástica
```

---

## 🧠 Funcionalidades

- **LLM local** via Ollama (Zephyr, Mistral, LLaMA 2, etc)
- **Rodando 100% offline** (sem nuvem)
- **Memória persistente**: histórico salvo em `memory/session_log.json`
- **Personalidades customizáveis**: escolha entre amigável, formal ou sarcástico
- **Interface moderna**: chat web com Gradio
- **Fácil expansão**: adicione novos estilos criando arquivos em `personality_prompts/`

---

## 🛠️ Requisitos

- **Python 3.10** (recomendado)
- [Ollama instalado e funcionando](https://ollama.com)
- Modelo LLM já baixado (ex: `ollama run zephyr`)
- Bibliotecas Python (veja `requirements.txt`)

---

## 🚀 Como rodar o projeto

```bash
# 1. Clone o repositório
git clone https://github.com/bitguardian/chatbot_local_personalidade.git
cd chatbot-local-personalidade

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie o modelo local (Zephyr, Mistral, etc)
ollama run zephyr

# 4. Execute o chatbot
python main.py
```

---

## 💡 Personalidades

Os estilos de resposta são definidos por arquivos em `personality_prompts/`. Para criar novos estilos, basta adicionar um novo arquivo `.txt` com instruções para o modelo.

---

## 📝 Memória de Conversa

O histórico das conversas é salvo em `memory/session_log.json`, permitindo que o chatbot lembre interações anteriores e responda de forma mais contextualizada.

---

## 📄 Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).
