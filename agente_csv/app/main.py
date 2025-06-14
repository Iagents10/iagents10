from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import zipfile, os, shutil, pandas as pd
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")

app = FastAPI()

@app.post("/ask")
async def ask_question(file: UploadFile, question: str = Form(...)):
    try:
        # Preparar diretório temporário
        temp_dir = "temp_data"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        zip_path = os.path.join(temp_dir, file.filename)
        with open(zip_path, "wb") as f:
            f.write(await file.read())

        # Descompactar
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Assumir que há apenas 1 CSV
        csv_files = [f for f in os.listdir(temp_dir) if f.endswith(".csv")]
        if not csv_files:
            return JSONResponse(content={"error": "Nenhum arquivo CSV encontrado no ZIP."}, status_code=400)

        df = pd.read_csv(os.path.join(temp_dir, csv_files[0]))

        # Gerar prompt com base nos dados e pergunta
        prompt = f"""Você é um assistente de análise de dados. Com base na tabela abaixo, responda a pergunta:

Pergunta: {question}

{df.head(20).to_string(index=False)}
"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return {"resposta": response['choices'][0]['message']['content'].strip()}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
