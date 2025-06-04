class Memory:
    def __init__(self, context_window_size=3):
        self.response_cache = {}
        self.context_window = []
        self.context_window_size = context_window_size

    def get_cached_response(self, prompt):
        return self.response_cache.get(prompt)

    def set_cached_response(self, prompt, answer):
        self.response_cache[prompt] = answer

    def add_context(self, question, answer):
        self.context_window.append({"question": question, "answer": answer})
        if len(self.context_window) > self.context_window_size:
            self.context_window = self.context_window[-self.context_window_size:]

    def get_context(self):
        return self.context_window
