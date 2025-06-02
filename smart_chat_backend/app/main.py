import os

from fastapi import FastAPI, HTTPException
from llama_cpp import Llama
from pydantic import BaseModel

MODEL_PATH = r"D:\Downloads\mistral-7b-openorca.gguf2.Q4_0.gguf"

class LLMWrapper:
    def __init__(self):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        self.model = Llama(model_path=MODEL_PATH, n_ctx=2048)

    def generate_response(self, prompt: str) -> str:
        result = self.model(prompt, max_tokens=200)
        return result["choices"][0]["text"].strip()

# Initialisiere App und Modell
app = FastAPI()
llm = LLMWrapper()

# Request-Body-Schema
class PromptRequest(BaseModel):
    prompt: str

# POST-Endpunkt für Fragen
@app.post("/chat/")
def chat(request: PromptRequest):
    try:
        response = llm.generate_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
