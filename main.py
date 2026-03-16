import os
from dotenv import load_dotenv

# Force load .env
load_dotenv(override=True)

# Debug check
print("OPENAI_API_KEY loaded:", os.getenv("OPENAI_API_KEY") is not None)

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is NOT loaded!")

from agents.agent import Agent
from agents.memory import MemoryManager
from vectorstore.faiss_store import VectorStore


# Load vector store
vs = VectorStore("data/docs.csv")
memory = MemoryManager()
agent = Agent(vs, memory)

# Example queries
queries = [
    "What is Python?",
    "Tell me about RAG systems",
    "calculate 2 + 2",
    "search LangChain tools"
]

for q in queries:
    print(f"Query: {q}")
    print(f"Answer: {agent.act(q)}\n")

# Print conversation memory
print("Conversation Memory:")
for item in memory.get():
    print(item)
