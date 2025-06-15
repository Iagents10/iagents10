import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from backend.agent import process_question

st.title("Agente CSV com LLM 🤖")

uploaded_file = st.file_uploader("Faça upload de um arquivo .zip contendo CSVs", type="zip")
question = st.text_input("Digite sua pergunta sobre os dados")

if uploaded_file and question:
    with open("temp.zip", "wb") as f:
        f.write(uploaded_file.read())
    resposta = process_question("temp.zip", question)
    st.markdown("### Resposta:")
    st.write(resposta)
