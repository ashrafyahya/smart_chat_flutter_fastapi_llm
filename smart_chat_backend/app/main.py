from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

from .model import LLMWrapper

# Konfiguration laden
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)
MODEL_PATH = config["MODEL_PATH"]

# Initialisiere App und Modell
app = FastAPI()
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
