# app/chat.py

import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_core.documents import Document
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq  # Ensure you installed: pip install langchain-groq
from dotenv import load_dotenv

# === 1. Load API key ===
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# === 2. Load vector store ===
vectorstore = FAISS.load_local(
    "faiss_index",
    HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base"),
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

# === 3. Set up Groq LLM ===
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama3-8b-8192" , # Or choose another Groq-supported model
    temperature=0
)


# === 4. Create the QA chain ===
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# === Make reusable for Streamlit ===
def ask_question(query: str) -> str:
    result = qa_chain.invoke({"query": query})
    return result["result"]
# === 5. Chat loop ===
print("\n StudyBot is ready! Ask questions about your ML course PDF. Type 'exit' to quit.\n")

if __name__ == "__main__":
    print("\n StudyBot is ready! Ask questions about your ML course PDF. Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            print("👋 Goodbye!")
            break

        result = qa_chain(query)
        answer = result['result']
        print(f"\nAnswer: {answer}")
        print("\n" + "-" * 60)
