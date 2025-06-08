import asyncio

from config import MODEL_PATH
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from memory import Memory
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
    context = memory.get_context()
    context_str = ""
    if context:
        context_str = "Previous conversation:\n"
        for qa in context:
            context_str += f"Q: {qa['question']}\nA: {qa['answer']}\n"
        context_str += "\n"
    summary_instruction = (
        "Answer with an abbreviated summary. "
        "Respone in the same language as the question."
        "Do not remark the answer with 'Answer: ' or similar phrases."
        "Don not remarks instruction in the answer, that was given to you."
    )
    prompt_for_model = f"{context_str}Current question:\n{user_prompt}\n\n{summary_instruction}"

    # No caching for streaming (optional: implement if needed)
    def token_stream():
        try:
            first_non_whitespace_yielded = False
            for token in llm.generate_response(prompt_for_model):
                if not first_non_whitespace_yielded:
                    # Skip leading whitespace tokens
                    if token.strip() == "":
                        continue
                    else:
                        first_non_whitespace_yielded = True
                        yield token
                else:
                    yield token
        except Exception as e:
            yield f"\n[Error: {str(e)}]"

    # Update context after streaming (optional: you may want to collect the answer)
    # For now, skip updating context in streaming mode, or buffer and update after.

    return StreamingResponse(token_stream(), media_type="text/plain")
