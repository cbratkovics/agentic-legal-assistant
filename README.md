# Agentic Legal Assistant

A **LangGraph-powered multi-agent system** that answers legal questions grounded in uploaded contracts. Uses **Retrieval-Augmented Generation (RAG)** to identify, extract, and cite relevant legal sections.

---

## ✅ Features

- Accepts natural language legal questions
- Parses PDF contracts
- Uses multi-agent orchestration with LangGraph
- Retrieves contextually relevant text with citation
- Responds with grounded answers using GPT-4

---

## 🧠 Architecture

```mermaid
flowchart TD
    A[User Input: Legal Question] --> B[Chat Agent (LLM Decision)]
    B -->|Calls Tool| C[Tool Node (Retriever)]
    C --> D[Return Retrieved Context]
    D --> B
    B -->|Responds| E[Grounded Answer with Citation]
```

---

### 🧩 Agent Workflow

1. **User** submits a question
2. **Chat Agent** (LLM) decides if retrieval is required
3. **Tool Node** fetches legal context
4. **Agent** composes and returns grounded answer

---

## 🔁 LangGraph Flow (Textual View)

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
```

---

## 🧰 Tech Stack

| Component         | Tool/Library                          |
|------------------|----------------------------------------|
| LLM              | OpenAI GPT-4 via `langchain-openai`    |
| Agent Framework  | LangGraph                              |
| Document Parsing | `PyPDFLoader`                          |
| Embedding Model  | `HuggingFaceEmbeddings`                |
| Vector Store     | `Chroma`                               |
| Orchestration    | `StateGraph`, `RunnableLambda`, Memory |

---

## 📓 Interactive Notebook

View or run via [Colab](https://colab.research.google.com/github/cbratkovics/agentic-legal-assistant/blob/main/agentic_legal_assistant_demo.ipynb)

Or run locally:

```bash
jupyter notebook agentic_legal_assistant_demo.ipynb
```

---

## 📄 Example Use Case

> “Does this contract allow early termination?”

→ The assistant finds and cites the termination clause from the PDF and responds with a summary.

---

## 🚀 Quickstart

### Step 1: Install

```bash
git clone https://github.com/cbratkovics/agentic-legal-assistant.git
cd agentic-legal-assistant

conda create -n agentic python=3.10 -y
conda activate agentic

pip install -r requirements.txt
```

### Step 2: Run the CLI Agent

```bash
python src/main.py \
  --pdf contracts/sample_contract.pdf \
  --questions "What are the payment terms?" "Is there a termination clause?"
```

Results saved to: `outputs/qa_log.jsonl`

---

## 🧪 Sample Output

```
Q: Does this contract allow early termination?
A: Yes, the contract includes a clause that allows either party to terminate with 30 days' notice. [Page 3]
```

---

## 📁 Project Structure

```
agentic-legal-assistant/
├── contracts/                  ← Input PDFs
├── outputs/                    ← Saved Q&A logs + diagrams
├── src/                        ← Core agent pipeline
├── agentic_legal_assistant_demo.ipynb
├── requirements.txt
├── architecture_diagram.png
└── README.md
```

---

## 🔐 API Key Setup

### Option 1: Export as env var

```bash
export OPENAI_API_KEY=sk-xxxx
```

### Option 2: Use `.env` file

```
OPENAI_API_KEY=sk-xxxx
```

Then load in code:

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

## 🔮 TODO

- [ ] Support `.docx` and `.txt`
- [ ] Add Streamlit front-end
- [ ] Highlight citations in original text
- [ ] Multi-document chaining

---

## 📄 License

MIT © 2025 Christopher Bratkovics
