# app/ingest.py

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings

# === 1. Load OCR text file ===
loader = TextLoader("data/ml_clean_ocr.txt", encoding="utf-8")
documents = loader.load()

if not documents:
    raise ValueError("No text found. Check the OCR output path/content.")

# === 2. Chunk the text ===
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)

if not chunks:
    raise ValueError("Chunking failed. Input may be empty or improperly formatted.")

# === 3. Initialize Instructor Embedding ===
embedding = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-base"
)

# === 4. Create FAISS vector store ===
vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embedding
)

# === 5. Save locally ===
vectorstore.save_local("faiss_index")

print(" Ingestion complete. Vector DB saved to './faiss_index'")
