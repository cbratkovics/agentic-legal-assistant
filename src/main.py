# === src/main.py ===

from typing import TypedDict, List
import argparse
import json
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

class AgentState(TypedDict):
    messages: List[BaseMessage]
    action: str

def agent_node(state: AgentState, qa_chain) -> AgentState:
    chat_history = [(m.content, "") for m in state["messages"][:-1] if isinstance(m, HumanMessage)]
    question = state["messages"][-1].content
    answer = qa_chain.invoke({"question": question, "chat_history": chat_history})
    state["messages"].append(AIMessage(content=answer["answer"]))
    return state

def main(pdf_path: str, questions: List[str], log_path: str):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding=embedding)
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(temperature=0)
    qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)

    def agent_step(state):
        return agent_node(state, qa_chain)

    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("agent", RunnableLambda(agent_step))
    graph_builder.set_entry_point("agent")
    graph_builder.set_finish_point("agent")
    graph = graph_builder.compile()

    chat_log = []

    for question in questions:
        print("\n--- Question ---\n", question)
        inputs = {
            "messages": [HumanMessage(content=question)],
            "action": "init"
        }
        steps = graph.invoke(inputs)
        if isinstance(steps, dict):
            last_message = steps["messages"][-1]
            if isinstance(last_message, AIMessage):
                print("\n--- AI Response ---\n", last_message.content)
                chat_log.append({
                    "timestamp": datetime.now().isoformat(),
                    "question": question,
                    "answer": last_message.content
                })

    with open(log_path, "w") as f:
        for entry in chat_log:
            f.write(json.dumps(entry) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agentic Legal Assistant")
    parser.add_argument("--pdf", type=str, required=True, help="Path to contract PDF")
    parser.add_argument("--log", type=str, default="outputs/qa_log.jsonl", help="Path to save Q&A log")
    parser.add_argument("--questions", nargs='+', help="List of questions to ask")

    args = parser.parse_args()
    if not args.questions:
        args.questions = [
            "Does this contract include a termination clause?",
            "What are the payment terms?",
            "Who are the signing parties?"
        ]

    main(args.pdf, args.questions, args.log)
