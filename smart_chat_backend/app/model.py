from gpt4all import GPT4All

# Du kannst den Modellnamen anpassen, wenn du einen anderen nutzt
MODEL_PATH = "mistral-7b-openorca.Q4_0.gguf"

class LLMWrapper:
    def __init__(self):
        self.model = GPT4All(model_name=MODEL_PATH)
        self.model.open()

    def generate_response(self, prompt: str) -> str:
        return self.model.generate(prompt)
