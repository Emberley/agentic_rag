from transformers import pipeline

class Reasoner:
    def __init__(self, model_name="tiiuae/falcon-7b-instruct"):
        self.generator = pipeline(
            "text-generation",  # <--- Must be text-generation
            model=model_name,
            device=-1,          # CPU, or 0 for GPU
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7
        )

    def answer(self, query: str, context: str) -> str:
        prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""
        output = self.generator(prompt, max_new_tokens=200)
        return output[0]['generated_text'].split("Answer:")[-1].strip()
