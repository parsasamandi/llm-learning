# LLM Learning

A collection of practical examples demonstrating how to work with Large Language Models using [Ollama](https://ollama.ai/) and Python.

## Features

This repository contains several examples showcasing different LLM patterns:

- **Basic Chat** - Simple conversational AI with history management
- **System Prompts** - Customized AI behavior (code review assistant)
- **Structured Output** - Extract structured data from natural language
- **RAG (Retrieval Augmented Generation)** - Question answering with document retrieval

## Prerequisites

Before running these examples, you need:

1. **Ollama** - Install from [ollama.ai](https://ollama.ai/)
2. **Python 3.10+** - With pip for package management
3. **Required Model** - Pull the model used in examples:
   ```bash
   ollama pull llama3.2
   ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/parsasamandi/llm-learning.git
   cd llm-learning
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install ollama chromadb sentence-transformers
   ```

## Usage

### 1. Basic Chat (`chat.py`)

A simple chatbot that maintains conversation history:

```bash
python chat.py
```

Features:
- Maintains full conversation context
- Type your message and get responses
- Type `quit` to exit

### 2. System Prompts (`chat_systems.py`)

A code review assistant with custom behavior:

```bash
python chat_systems.py
```

Features:
- Pre-configured as a senior Python developer
- Provides code reviews and suggestions
- Direct and concise feedback

### 3. Structured Output (`structured.py`)

Extract structured data from natural language:

```bash
python structured.py
```

This example demonstrates extracting person information (name, age, city) into JSON format.

### 4. Structured Output v2 (`structured_v2.py`)

Enhanced version with robust JSON extraction:

```bash
python structured_v2.py
```

Features:
- Handles various JSON formats
- Extracts JSON from markdown code blocks
- More resilient parsing

### 5. RAG - Retrieval Augmented Generation (`rag.py`)

Question answering system with document retrieval:

```bash
python rag.py
```

Features:
- Vector database powered by ChromaDB
- Semantic search using sentence transformers
- Context-aware answers from company documents
- Ask questions about the company info in `documents/company.txt`

## Project Structure

```
llm-learning/
├── chat.py              # Basic conversational AI
├── chat_systems.py      # AI with system prompts (code reviewer)
├── structured.py        # Structured output extraction
├── structured_v2.py     # Enhanced structured output with better parsing
├── rag.py               # RAG system with vector database
├── documents/           # Sample documents for RAG
│   └── company.txt      # Company information
└── README.md            # This file
```

## Learning Path

If you're new to LLMs, we recommend exploring the examples in this order:

1. Start with `chat.py` to understand basic LLM interactions
2. Try `chat_systems.py` to see how system prompts shape behavior
3. Experiment with `structured.py` and `structured_v2.py` for data extraction
4. Finally, explore `rag.py` to see how to build context-aware systems

## Dependencies

- `ollama` - Python client for Ollama
- `chromadb` - Vector database for RAG
- `sentence-transformers` - Embedding model for semantic search

## Notes

- All examples use the `llama3.2` model by default
- Make sure Ollama is running before executing the scripts
- The RAG example requires the `all-MiniLM-L6-v2` embedding model (automatically downloaded)

## License

This is an educational project for learning LLM concepts and patterns.
