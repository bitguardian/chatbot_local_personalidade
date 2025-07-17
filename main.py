import gradio as gr
import openai
import os
from chatbot import carregar_memoria, salvar_memoria, montar_prompt

# Configuração Ollama
openai.api_base = "http://localhost:11434/v1"
openai.api_key = "fake" 
modelo = "zephyr"        # Ou mistral, llama2 etc.

memoria = carregar_memoria()

# Conversa IA
def conversar(mensagem, estilo, chat_hist):
    prompt = montar_prompt(estilo, memoria, mensagem)

    resposta = openai.ChatCompletion.create(
        model=modelo,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=300
    )["choices"][0]["message"]["content"]

    # Atualiza memória local
    memoria.append({"usuario": mensagem, "ia": resposta})
    salvar_memoria(memoria)

    # Adiciona ao histórico visual
    chat_hist.append({"role": "user", "content": mensagem.strip()})
    chat_hist.append({"role": "assistant", "content": resposta.strip()})
    return "", chat_hist

# UI com gradio
with gr.Blocks(title="Chatbot Local com Personalidade") as app:
    gr.Markdown("# 🤖 Chatbot Local com Personalidade")
    
    with gr.Row():
        estilo = gr.Radio(
            ["friendly", "formal", "sarcastic"],
            value="friendly",
            label="Escolha a personalidade da IA",
            interactive=True
        )

    chat_hist = gr.Chatbot(label="Histórico de Conversa", height=500, type="messages", value=[])
    msg = gr.Textbox(label="Digite sua mensagem", placeholder="Escreva aqui e pressione Enter...")

    def ao_enviar(m, e):
        return conversar(m, e, chat_hist.value)

    msg.submit(ao_enviar, [msg, estilo], [msg, chat_hist])

app.launch()
