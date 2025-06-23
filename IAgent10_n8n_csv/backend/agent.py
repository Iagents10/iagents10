import pandas as pd
from supabase import create_client
from .query_engine import run_query
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_data_from_supabase(table: str = "nota_fiscal") -> pd.DataFrame:
    response = supabase.table(table).select("*").execute()
    data = response.data
    return pd.DataFrame(data)

def process_question(zip_path, question):
    from .query_engine import run_query
    from .supabase_connector import get_data_from_supabase  # ou outro nome

    df = get_data_from_supabase()
    if df.empty:
        return "Nenhum dado encontrado no Supabase."
    return run_query(question, df)

def process_question_from_supabase(question: str) -> str:
    df = get_data_from_supabase("nota_fiscal")
    if df.empty:
        return "Nenhum dado disponível no Supabase."
    return run_query(question, df)


