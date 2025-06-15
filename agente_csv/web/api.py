import argparse
import zipfile
import os
import pandas as pd
from backend.query_engine import perguntar
from backend.data_loader import carregar_csvs


def extrair_zip(zip_path, extract_to="temp_extracao"):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to


def main():
    parser = argparse.ArgumentParser(description="Agente para perguntas sobre CSVs em ZIP")
    parser.add_argument("--question", type=str, required=True, help="Pergunta a ser respondida")
    parser.add_argument("--zip_path", type=str, required=True, help="Caminho para o arquivo ZIP")
    args = parser.parse_args()

    pasta_extraida = extrair_zip(args.zip_path)
    dados = carregar_csvs(pasta_extraida)

    resposta = perguntar(dados, args.question)
    print(resposta)


if __name__ == "__main__":
    main()
