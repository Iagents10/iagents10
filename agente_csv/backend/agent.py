import zipfile
import os
import pandas as pd
from .query_engine import run_query

def extract_zip(file_path, extract_to="temp"):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    csv_files = [os.path.join(extract_to, f) for f in os.listdir(extract_to) if f.endswith('.csv')]
    return csv_files

def load_csv_files(file_paths):
    dataframes = []
    for file in file_paths:
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            print(f"Erro ao carregar {file}: {e}")
    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        return pd.DataFrame()

def process_question(zip_path, question):
    csv_files = extract_zip(zip_path)
    df = load_csv_files(csv_files)
    if df.empty:
        return "Nenhum dado CSV válido encontrado no arquivo ZIP."
    return run_query(question, df)

