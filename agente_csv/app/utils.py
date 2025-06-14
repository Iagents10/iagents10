import os
import zipfile
import pandas as pd

def unzip_file(zip_path, extract_to="extracted"):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def load_csvs(folder="extracted"):
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            return pd.read_csv(os.path.join(folder, file))
    return None
