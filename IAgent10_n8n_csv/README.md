# IAgent10 - Consulta Inteligente de Notas Fiscais via n8n e LLM

Este projeto implementa um agente inteligente para consulta de dados de notas fiscais a partir de arquivos CSV, orquestrado via **n8n** e integrado a modelos de linguagem (LLM) como o GPT-4o. O fluxo automatiza desde a ingestão dos dados até a interpretação de perguntas em linguagem natural, tudo com suporte a interfaces modernas como **Streamlit** e conteinerização via **Docker**.

## 🌐 Repositório

Este projeto está contido na pasta:

```
https://github.com/Iagents10/iagents10/IAgent10_n8n_csv
```

## 🔧 Tecnologias Utilizadas

- [n8n](https://n8n.io/) para orquestração do fluxo
- [LangChain](https://www.langchain.com/) com modelo OpenAI (GPT-4o-mini)
- [Supabase](https://supabase.com/) para banco de dados
- [Google Drive API](https://developers.google.com/drive) para ingestão dos arquivos
- [Streamlit](https://streamlit.io/) para interface web
- [Docker](https://www.docker.com/) para conteinerização do ambiente

---

## 📁 Estrutura do Projeto

```
IAgent10_n8n_csv/
├── README.md
├── workflow/
│   └── AIgent10_n8n.json   # Fluxo n8n completo exportado
├── streamlit_app/
│   ├── app.py                # Interface web para perguntas
│   └── requirements.txt      # Dependências do Streamlit
├── docker-compose.yml       # Orquestração do ambiente
└── .env                     # Variáveis de ambiente (chaves e configs)
```

---

## ▶️ Como Executar

### 1. Clone o Repositório

```bash
git clone https://github.com/Iagents10/iagents10.git
cd iagents10/IAgent10_n8n_csv
```

### 2. Configure o Arquivo `.env`

Crie um arquivo `.env` com as seguintes variáveis:

```env
OPENAI_API_KEY=your_openai_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

### 3. Execute com Docker Compose

```bash
docker-compose up --build
```

Isso iniciará:
- O n8n na porta `5678`
- A interface Streamlit na porta `8501`

Acesse via:
```
http://localhost:8501
```

---

## 💬 Utilização via Interface

- Faça uma pergunta como:
  - "Qual o fornecedor com maior montante recebido?"
  - "Qual item teve maior volume entregue?"
- O agente usa a LLM para interpretar, consulta os dados no Supabase/PostgreSQL e retorna a resposta na interface.

---

## 📦 Importação do Fluxo n8n

1. Acesse `http://localhost:5678`
2. Importe o arquivo `workflow/desafio_2_copy.json`
3. Configure as credenciais (Google Drive, Supabase, OpenAI)
4. Execute o fluxo

---

## 🚀 Possíveis Melhorias Futuras

- Cache local de respostas
- Geração automática de dashboards com Streamlit
- Histórico de perguntas
- Upload manual de arquivos CSV pela interface

---

## 📄 Licença

MIT License © [Alexsandro Nepunuceno](https://github.com/alexsandrocn)
