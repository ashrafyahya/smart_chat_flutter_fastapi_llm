import asyncio
from time import time

from config import HOST, PORT, RATE_LIMIT, RATE_PERIOD
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prompt import (PromptRequest, generate)

# Initialize FastAPI app
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

# Simple rate limiting (e.g., max. 5 requests per 10 seconds)
request_times = []

# POST endpoint for generating responses to prompts
@app.post("/generate")
async def generate_response(request: PromptRequest):
    # Rate limiting: remove old timestamps and check if limit is exceeded
    now = time()
    global request_times
    request_times = [t for t in request_times if now - t < RATE_PERIOD]
    if len(request_times) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests. Please wait a moment.")
    request_times.append(now)

    # Stream response using the imported generate function
    return await generate(request)

# Run the app with Uvicorn if this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)