class MemoryManager:
    def __init__(self):
        self.memory = []

    def add(self, query: str, answer: str):
        self.memory.append({"query": query, "answer": answer})

    def get(self):
        return self.memory
