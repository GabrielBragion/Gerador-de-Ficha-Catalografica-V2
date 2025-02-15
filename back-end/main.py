from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from extractor import extract_text
from formater import formater

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens, altere conforme necessário
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os headers
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Verifica se o arquivo é um PDF
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Apenas arquivos PDF são suportados.")
        
        # Lê o arquivo em memória
        contents = await file.read()
        
        # Extrai informações do PDF
        infos = extract_text(contents)
        
        # Formata as informações
        infos_formated = formater(infos)        
        
        return JSONResponse(content=infos_formated)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo: {str(e)}")