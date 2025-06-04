import asyncio
import json
import os
from time import time

from config import HOST, MODEL_PATH, PORT, RATE_LIMIT, RATE_PERIOD
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .model import LLMWrapper

# Initialize FastAPI app and model
app = FastAPI()

# Enable CORS (for development: allow all origins)
# In production, set allowed origins specifically!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this specifically for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate the language model wrapper with the given model path
llm = LLMWrapper(MODEL_PATH)

# Request body schema for prompt input
class PromptRequest(BaseModel):
    prompt: str

# Response body schema for generated response
class PromptResponse(BaseModel):
    response: str

# Simple rate limiting (e.g., max. 5 requests per 10 seconds)
request_times = []

# Simple in-memory cache for responses
response_cache = {}

# POST endpoint for generating responses to prompts
@app.post("/generate", response_model=PromptResponse)
async def generate(request: PromptRequest):
    # Rate limiting: remove old timestamps and check if limit is exceeded
    now = time()
    global request_times
    request_times = [t for t in request_times if now - t < RATE_PERIOD]
    if len(request_times) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests. Please wait a moment.")
    request_times.append(now)

    # Pass the user's question unchanged, but instruct the model to summarize its answer
    user_prompt = request.prompt
    summary_instruction = "\n\nPlease answer with a concise summary."
    prompt_for_model = f"{user_prompt}{summary_instruction}"

    # Check cache for existing response to the prompt
    if prompt_for_model in response_cache:
        return PromptResponse(response=response_cache[prompt_for_model])

    try:
        # Asynchronous processing (if generate_response is IO-bound)
        loop = asyncio.get_event_loop()
        answer = await loop.run_in_executor(None, llm.generate_response, prompt_for_model)
        # Cache the response
        response_cache[prompt_for_model] = answer
        return PromptResponse(response=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app with Uvicorn if this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)