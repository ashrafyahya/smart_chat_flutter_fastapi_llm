import asyncio

from config import MODEL_PATH
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import LLMWrapper
from memory import Memory
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

# Initialize memory
memory = Memory(context_window_size=3)

# Request body schema for prompt input
class PromptRequest(BaseModel):
    prompt: str

# Response body schema for generated response
class PromptResponse(BaseModel):
    response: str

# POST endpoint for generating responses to prompts
async def generate(request: PromptRequest):
    user_prompt = request.prompt

    # Build context string from last 3 QA pairs
    context = memory.get_context()
    context_str = ""
    if context:
        context_str = "Previous conversation:\n"
        for qa in context:
            context_str += f"Q: {qa['question']}\nA: {qa['answer']}\n"
        context_str += "\n"

    # Pass the user's question unchanged, but instruct the model to summarize its answer
    summary_instruction = (
        "Answer with an abbreviated summary. "
        "Respone in the same language as the question."
    )
    prompt_for_model = f"{context_str}Current question:\n{user_prompt}\n\n{summary_instruction}"

    # Check cache for existing response to the prompt
    answer = memory.get_cached_response(prompt_for_model)
    if answer is None:
        try:
            print("Generating answer for prompt...")  # Print message to console
            # Asynchronous processing (if generate_response is IO-bound)
            loop = asyncio.get_event_loop()
            answer = await loop.run_in_executor(None, llm.generate_response, prompt_for_model)
            memory.set_cached_response(prompt_for_model, answer)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Update context window with the new QA pair
    memory.add_context(user_prompt, answer)

    return PromptResponse(response=answer)
