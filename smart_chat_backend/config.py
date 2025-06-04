# Path to the language model file
MODEL_PATH = "D:/Downloads/mistral-7b-openorca.gguf2.Q4_0.gguf"

# Uvicorn app module path
APP_MODULE = "app.chat:app"

# Host and port for running the FastAPI server
HOST = "0.0.0.0"
PORT = 8000

# Rate limiting: maximum number of requests per period
RATE_LIMIT = 5

# Rate limiting period in seconds
RATE_PERIOD = 10  # seconds
