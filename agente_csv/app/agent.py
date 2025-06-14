import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent

def criar_agente(df):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )
    return create_pandas_dataframe_agent(llm, df, verbose=False)
