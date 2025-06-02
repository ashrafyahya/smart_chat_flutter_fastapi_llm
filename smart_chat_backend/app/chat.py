import json
import os

from config import HOST, MODEL_PATH, PORT
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .model import LLMWrapper

# Initialisiere App und Modell
app = FastAPI()

# CORS aktivieren (für Entwicklung: alle Ursprünge erlauben)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Produktion gezielt setzen!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = LLMWrapper(MODEL_PATH)

# Request-Body-Schema
class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str

# POST-Endpunkt für Fragen
@app.post("/generate", response_model=PromptResponse)
def generate(request: PromptRequest):
    try:
        answer = llm.generate_response(request.prompt)
        return PromptResponse(response=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)