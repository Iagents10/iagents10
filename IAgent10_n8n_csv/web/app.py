import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.agent import process_question       # CSV ZIP
from backend.agent import process_question_from_supabase  # Supabase
import streamlit as st
import tempfile
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

st.set_page_config(page_title="Agente CSV com LLM 🤖")
st.title("Agente CSV com LLM 🤖")
# escolha de origem
origem = st.selectbox("Fonte de dados:", ["CSV (ZIP)", "Supabase"])


question = st.text_input("Digite sua pergunta sobre os dados")
# quando usuário clicar
if st.button("Enviar"):
    if origem == "CSV (ZIP)":
        uploaded_file = st.file_uploader("Envie o ZIP com CSVs", type="zip")
        if not uploaded_file:
            st.error("Faça upload do arquivo ZIP!")
        else:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp:
                tmp.write(uploaded_file.read())
                zip_path = tmp.name
            resposta = process_question(zip_path, question)
            os.remove(zip_path)
            st.write(resposta)
    else:  # Supabase
        resposta = process_question_from_supabase(question)
        st.write(resposta)


