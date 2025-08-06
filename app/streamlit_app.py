# app/streamlit_app.py

import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os

# === Load environment variables ===
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# === Streamlit Page Config ===
st.set_page_config(page_title="🤖 StudyBot", layout="wide")

# === Custom CSS for styling ===
st.markdown("""
    <style>
        .chat-bubble {
            background-color: #f7f7f9;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid #e6e6e6;
            max-width: 90%;
        }
        .chat-question {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 0.3rem;
            color: #0066cc;
        }
        .chat-answer {
            font-size: 17px;
            color: #111;
        }
        .big-title {
            font-size: 36px !important;
            text-align: center;
            margin-bottom: 10px;
        }
        .st-emotion-cache-1r6slb0 {  /* override for full-width chat input */
            position: fixed;
            bottom: 1rem;
            width: 100%;
            left: 0;
            padding: 0 2rem;
            background-color: white;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)

# === Sidebar ===
st.sidebar.title("💬 Options")
if st.sidebar.button("🔄 Clear Chat"):
    st.session_state.history = []

# === Title ===
st.markdown("<h1 class='big-title'>📚 StudyBot - Ask Bindu</h1>", unsafe_allow_html=True)
st.markdown("Ask anything from your Machine Learning course. Bindu will try to help you")

# === Initialize Chat History ===
if "history" not in st.session_state:
    st.session_state.history = []

# === Load QA Chain ===
@st.cache_resource
def load_qa_chain():
    vectorstore = FAISS.load_local(
        "faiss_index",
        HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base"),
        allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever()
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="llama3-8b-8192",
        temperature=0
    )
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)

qa_chain = load_qa_chain()

# === Display Chat History ===
for chat in st.session_state.history:
    st.markdown(f"""
        <div class="chat-bubble">
            <div class="chat-question">🧑‍🎓 You: {chat['question']}</div>
            <div class="chat-answer">🤖 StudyBot: {chat['answer']}</div>
        </div>
    """, unsafe_allow_html=True)

# === Chat Input (Like ChatGPT) ===
query = st.chat_input("Ask something about your ML course...")

# === Process User Query ===
if query:
    if query.strip().lower() in ["exit", "quit"]:
        st.success("👋 Goodbye! Thanks for using StudyBot.")
        st.session_state.history = []
        st.stop()  # stops further execution of the app this round
    else:
        with st.spinner("💡 Thinking..."):
            result = qa_chain.invoke({"query": query})
            answer = result["result"]

            st.session_state.history.append({
                "question": query,
                "answer": answer
            })
            st.session_state.history = st.session_state.history[-5:]

        st.rerun()
