import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

llm = ChatOpenAI(openai_api_key=os.getenv("OPENROUTER_API_KEY"), temperature=0.1)

def run_query(question, dataframe):
    context = dataframe.head(100).to_csv(index=False)
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Você é um analista de dados. Com base nos dados abaixo (em CSV), responda com clareza a pergunta do usuário.

Dados:
{context}

Pergunta:
{question}
        """,
    )
    response = llm.predict(prompt.format(context=context, question=question))
    return response.strip()
