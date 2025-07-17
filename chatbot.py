import json
import os

MEMORY_DIR = "memory"
MEMORY_FILE = os.path.join(MEMORY_DIR, "session_log.json")

# Garante que a pasta memory/ exista
os.makedirs(MEMORY_DIR, exist_ok=True)

def carregar_memoria():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Se o arquivo estiver corrompido ou mal formado
        return []

def salvar_memoria(memoria):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)

def montar_prompt(personalidade, historico, pergunta):
    try:
        with open(f"personality_prompts/{personalidade}.txt", "r", encoding="utf-8") as f:
            estilo = f.read().strip()
    except FileNotFoundError:
        estilo = "Você é um assistente neutro. Responda com clareza."

    contexto = "\n".join([f"Usuário: {h['usuario']}\nIA: {h['ia']}" for h in historico[-5:]])
    prompt = f"{estilo}\n\n{contexto}\nUsuário: {pergunta}\nIA:"
    return prompt
