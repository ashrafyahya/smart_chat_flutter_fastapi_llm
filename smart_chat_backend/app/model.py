import os

from llama_cpp import Llama


class LLMWrapper:
    def __init__(self, model_path: str):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        self.model = Llama(model_path=model_path, n_ctx=2048)

    def generate_response(self, prompt: str) -> str:
        result = self.model(prompt, max_tokens=200)
        return result["choices"][0]["text"].strip()
