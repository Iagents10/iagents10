import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain_core.documents import Document

load_dotenv()  # Carrega as variáveis de ambiente

# Pegando a chave da OpenAI direto do .env
openai_key = os.getenv("OPENAI_API_KEY")

# Configura o modelo LLM usando a API oficial da OpenAI
llm = ChatOpenAI(
    openai_api_key=openai_key,
    model="gpt-3.5-turbo"
)

# Configura os embeddings da OpenAI
embeddings = OpenAIEmbeddings(
    openai_api_key=openai_key
)

def run_query(question, documents):
    # Garante que documentos são instâncias de Document
    docs = [Document(page_content=text) if isinstance(text, str) else text for text in documents]

    texts = [doc.page_content for doc in docs]
    metadatas = [doc.metadata if hasattr(doc, "metadata") else {} for doc in docs]

    # Indexa os documentos
    vectorstore = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    # Recupera os mais relevantes
    relevant_docs = vectorstore.similarity_search(question, k=4)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    prompt = (
        "Você é um assistente que responde perguntas com base nos dados fornecidos.\n\n"
        "Contexto:\n{context}\n\n"
        "Pergunta: {question}\n"
        "Resposta:"
    )

    response = llm.predict(prompt.format(context=context, question=question))
    return response
