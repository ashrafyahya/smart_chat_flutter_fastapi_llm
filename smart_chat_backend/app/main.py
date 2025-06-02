from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import LLMWrapper

# Initialisiere App und Modell
app = FastAPI()
llm = LLMWrapper()

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
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
