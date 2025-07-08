````markdown
# 🧠 Agentic Legal Assistant

A LangGraph-powered multi-agent AI system for answering legal questions grounded in uploaded contracts. This project leverages Retrieval-Augmented Generation (RAG) to extract and cite relevant sections from legal documents like contracts and agreements.

---

## ✅ Key Features

- 🔍 Accepts natural language legal questions
- 📄 Parses uploaded PDF contracts
- 🧠 Uses multi-agent LangGraph orchestration
- 📚 Retrieves relevant context with citations
- ✍️ Returns grounded summaries using OpenAI GPT-4

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[User Input: Legal Question] --> B[Chat Agent (LLM Decision)]
    B -->|Calls Tool| C[Tool Node (Retriever)]
    C --> D[Return Retrieved Context]
    D --> B
    B -->|Responds| E[Grounded Answer with Citation]
```


### Agent Workflow:

1. **User** submits a legal question.
2. **Chat Agent** decides whether to invoke a tool.
3. **Tool Node** performs retrieval from vector DB.
4. **Chat Agent** uses result to respond or loop back for more context.

---

### 🔁 LangGraph Flow (Textual View)

```text
+----------------+
|   User Input   |
+----------------+
        |
        v
+----------------+
|   Chat Agent   |
| (LLM Decision) |
+----------------+
   |      |
   | No   | Yes
   v      v
+------+  +--------------------+
| Done |  |  Tool Node         |
+------+  | (Retriever/Docs)   |
          +--------------------+
                   |
                   v
         +------------------+
         | Return to Agent  |
         +------------------+
````

---

## 🔧 Tools Used

| Role             | Tool / Method                          |
| ---------------- | -------------------------------------- |
| Language Model   | OpenAI GPT-4 via LangChain             |
| Document Parsing | `PyPDFLoader`                          |
| Embedding        | `HuggingFaceEmbeddings`                |
| Retrieval        | `Chroma` vector store                  |
| Agent Framework  | `LangGraph`                            |
| Agent Logic      | `StateGraph`, `RunnableLambda`, Memory |

---

## 📓 Notebook Demo

Interactive walkthrough:
[Colab Link](https://colab.research.google.com/github/cbratkovics/agentic-legal-assistant/blob/main/agentic_legal_assistant_demo.ipynb)

Or run locally:

```bash
jupyter notebook agentic_legal_assistant_demo.ipynb
```

---

## 📄 Example Use Case

> *“Does this contract allow early termination?”*

→ The assistant reads the contract, identifies the termination clause, and responds with citations.

---

## 🚀 Run Locally

### 1. Clone & Install

```bash
git clone https://github.com/cbratkovics/agentic-legal-assistant.git
cd agentic-legal-assistant

# Create or activate environment
conda create -n agentic python=3.10 -y
conda activate agentic

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Agent Pipeline via CLI

```bash
python src/main.py --pdf contracts/sample_contract.pdf \
                   --questions "What are the payment terms?" "Is there a termination clause?"
```

Answers saved to: `outputs/qa_log.jsonl`

---

## 🧪 Example Output

```
Q: Does this contract allow early termination?
A: Yes, the contract includes a clause that allows either party to terminate with 30 days' notice. [Page 3]
```

---

## 📁 Project Layout

```
agentic-legal-assistant/
├── contracts/                  ← Input PDFs
├── outputs/                    ← Saved Q&A logs
├── src/                        ← Core agent pipeline
├── agentic_legal_assistant_demo.ipynb
├── requirements.txt
├── README.md
└── architecture_diagram.png
```

---

## 🔒 API Key Setup

Set your OpenAI key as an environment variable:

```bash
export OPENAI_API_KEY=sk-xxxx
```

Or use a `.env` file:

```
OPENAI_API_KEY=sk-xxxx
```

And load it using `python-dotenv` in code:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 📦 `requirements.txt`

```txt
langchain
langgraph
chromadb
langchain-openai
langchain-huggingface
pypdf
ipywidgets
tqdm
python-dotenv
notebook
```

---

## 📌 TODO / Extensions

* [ ] `.docx` and `.txt` support
* [ ] Streamlit front-end
* [ ] Highlight source text
* [ ] Multi-document ingestion

---

## 📝 License

MIT License © 2025 Christopher Bratkovics