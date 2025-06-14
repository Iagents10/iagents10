# Agente CSV ZIP

Este projeto é um agente que responde perguntas sobre arquivos CSV contidos em arquivos ZIP, usando LLM via OpenRouter.

## Como usar (Linux Mint)
```bash
# Requisitos
sudo apt install python3-pip unzip -y

# Clone e entre no projeto
git clone https://github.com/Iagents10/iagents10
cd iagents10

# Instale dependências
pip install -r requirements.txt

# Copie e edite o .env
cp app/.env.example app/.env
nano app/.env  # coloque sua chave OpenRouter

# Rode a aplicação
uvicorn app.main:app --reload
```

Depois acesse: http://localhost:8000/docs para usar a interface interativa da API.

## Estrutura
- Recebe .zip via upload
- Descompacta e lê o CSV
- Gera resposta com base na pergunta do usuário e os dados

## Exemplo de perguntas
- Qual fornecedor recebeu o maior valor?
- Qual item teve maior volume entregue?
- Qual foi a data de maior faturamento?
- Quem comprou mais de 10 unidades?
