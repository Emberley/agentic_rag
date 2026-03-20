# Agentic RAG

## Overview
This project is an simple agentic retrieval-augmented generation (RAG) system that combines document retrieval, memory, planning, reasoning, and tool use to answer a set of four user queries. The goal is to develop distributed agent frameworks that collaborate to solve tasks, one framework is asynchronous agent architecture.

## System Architecture
User Query  
→ Planner Agent  
→ Retrieval / Tools  
→ Memory Agent  
→ Reasoner Agent  
→ Final Response

## Project Components
- `agents/agent.py` - main agent 
- `agents/planner.py`   
- `agents/reasoner.py` 
- `agents/memory.py` 
- `agents/tools.py` - tool integration  
- `data/docs.csv` - source documents  
- `vectorstore/` - FAISS vector database  

## Installation

Clone the repository:

```bash
git clone https://github.com/Emberley/AGENTIC_RAG.git
cd AGENTIC_RAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the project:

```bash
python main.py
```

## Tech
- Python
- LangChain
- OpenAI API
- FAISS
- Pandas
- Sentence Transformers
- Python Dotenv

## Future Improvements
- Multi-agent collaboration and different framework orchestration used for Agentic systems.

## License
MIT License
