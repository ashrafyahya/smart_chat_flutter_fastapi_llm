import asyncio
from config import MODEL_PATH
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import LLMWrapper
from pydantic import BaseModel

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

# Simple in-memory cache for responses
response_cache = {}

# Store the last 3 question-answer pairs for context window memory
context_window = []

# POST endpoint for generating responses to prompts
async def generate(request: PromptRequest):
    # Context window: remember last 3 question-answer pairs
    global context_window
    user_prompt = request.prompt

    # Build context string from last 3 QA pairs
    context_str = ""
    if context_window:
        context_str = "Previous conversation:\n"
        for qa in context_window:
            context_str += f"Q: {qa['question']}\nA: {qa['answer']}\n"
        context_str += "\n"

    # Pass the user's question unchanged, but instruct the model to summarize its answer
    summary_instruction = "Please answer with a concise summary."
    prompt_for_model = f"{context_str}Current question:\n{user_prompt}\n\n{summary_instruction}"

    # Check cache for existing response to the prompt
    if prompt_for_model in response_cache:
        answer = response_cache[prompt_for_model]
    else:
        try:
            # Asynchronous processing (if generate_response is IO-bound)
            loop = asyncio.get_event_loop()
            answer = await loop.run_in_executor(None, llm.generate_response, prompt_for_model)
            # Cache the response
            response_cache[prompt_for_model] = answer
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Update context window with the new QA pair
    context_window.append({"question": user_prompt, "answer": answer})
    if len(context_window) > 3:
        context_window = context_window[-3:]

    return PromptResponse(response=answer)
