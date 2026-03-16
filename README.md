# Agentic RAG

## Overview
This project is an aimple **Agentic Retrieval-Augmented Generation (RAG) system** that combines document retrieval, memory, planning, reasoning, and tool use to answer user queries. Instead of using a single retrieval step, the system is organized into modular agents. The goal is to create different distrubuted frameworks of agents working together, such a asynchrous agent.

## System Architecture
The system follows this workflow:
User Query  
→ Planner Agent  
→ Retrieval / Tools  
→ Memory Agent  
→ Reasoner Agent  
→ Final Response

## Project Components
- `agents/agent.py` - main agent orchestration  
- `agents/planner.py` - task planning logic  
- `agents/reasoner.py` - reasoning over retrieved context  
- `agents/memory.py` - memory handling across steps  
- `agents/tools.py` - tool integration for retrieval/actions  
- `data/docs.csv` - source documents  
- `vectorstore/` - FAISS vector database  
- `main.py` - entry point for running the system  

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

## Tech Stack
- Python
- LangChain
- OpenAI API
- FAISS
- Pandas
- Sentence Transformers
- Python Dotenv

## Future Improvements
- Multi-agent collaboration

## License
MIT License
