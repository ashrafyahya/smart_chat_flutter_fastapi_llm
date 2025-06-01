from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.model import LLMWrapper

app = FastAPI()
llm = LLMWrapper()

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer = llm.generate_response(req.message)
    return ChatResponse(response=answer)
