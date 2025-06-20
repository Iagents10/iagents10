import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.agent import process_question

import streamlit as st
import tempfile
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

st.set_page_config(page_title="Agente CSV com LLM 🤖")
st.title("Agente CSV com LLM 🤖")
st.write("Faça upload de um arquivo `.zip` contendo arquivos CSV e pergunte algo sobre os dados.")

uploaded_file = st.file_uploader("Upload do arquivo ZIP", type="zip")

question = st.text_input("Digite sua pergunta sobre os dados")

if uploaded_file is not None and question:
    with st.spinner("Processando..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        try:
            resposta = process_question(temp_file_path, question)
            st.success("Resposta:")
            st.write(resposta)
        except Exception as e:
            st.error(f"Erro ao processar: {e}")
        finally:
            os.remove(temp_file_path)
