# Agentic RAG

## Overview
This project is an **Agentic Retrieval-Augmented Generation (RAG) system** that combines document retrieval, memory, planning, reasoning, and tool use to answer user queries more effectively. Instead of using a single retrieval step, the system is organized into modular agents that can plan tasks, retrieve relevant context, reason over results, and generate responses.

## Features
- Retrieval-Augmented Generation with document search
- Modular agent-based design
- Planner, memory, reasoner, and tool components
- FAISS-based vector storage for retrieval
- Environment variable support with `.env`
- Extensible architecture for future agent workflows

## Architecture
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
- Persistent conversation memory
- PDF / website document ingestion
- Retrieval and answer quality evaluation
- Simple web interface

## License
MIT License
