import os
import pandas as pd
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain_core.documents import Document

load_dotenv()

# Pega a chave da OpenRouter do .env
openrouter_key = os.getenv("OPENROUTER_API_KEY")
openrouter_model = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")

# Instância do modelo LLM
llm = ChatOpenAI(
    openai_api_key=openrouter_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model=openrouter_model,
    temperature=0.2
)

# Instância de embeddings
embeddings = OpenAIEmbeddings(
    openai_api_key=openrouter_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model="text-embedding-ada-002"
)

def run_query(question: str, df: pd.DataFrame) -> str:
    # Reduz o dataframe para evitar excesso de tokens
    df_reduzido = df.iloc[:100] if len(df) > 100 else df
    texto_csv = df_reduzido.to_csv(index=False)

    # Transforma em documentos
    documents = [Document(page_content=texto_csv)]

    # Cria vetores e indexa com FAISS
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Busca vetores mais relevantes
    docs_similares = vectorstore.similarity_search(question, k=3)
    contexto = "\n\n".join([doc.page_content for doc in docs_similares])

    # Prompt para o modelo
    prompt = (
        "Você é um assistente que responde perguntas com base nos dados fornecidos.\n\n"
        "Contexto:\n{context}\n\n"
        "Pergunta: {question}\n"
        "Resposta:"
    )

    resposta = llm.predict(prompt.format(context=contexto, question=question))
    return resposta
