from .utils import unzip_files
from .data_loader import load_csv_data
from .query_engine import run_query
from dotenv import load_dotenv
load_dotenv()

def process_question(zip_path, question):
    csv_files = unzip_files(zip_path)
    if not csv_files:
        return "Nenhum arquivo CSV encontrado no ZIP."
    
    df = load_csv_data(csv_files[0])
    return run_query(question, df)
