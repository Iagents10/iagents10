import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "https://github.com/Iagents10",  # personalize com seu site ou GitHub
    "X-Title": "AgenteCSV"
}

data = {
    "model": "openai/gpt-3.5-turbo",  # ou qualquer modelo listado em https://openrouter.ai/models
    "messages": [
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Qual a capital do Brasil?"}
    ]
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
)

print("Status:", response.status_code)
print("Resposta:")
print(response.json())
