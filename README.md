#  StudyBot — ML PDF QA Chatbot

**StudyBot** is a personalized study assistant that lets you ask questions from your **Machine Learning course PDF**, either through the **command line** or an interactive **Streamlit** UI. It uses **OCR**, **FAISS**, **Instructor Embeddings**, and the **Groq LLM (LLaMA3)** to answer your questions effectively.

---

## Features

- Ask any question about your ML PDF
- OCR support for scanned/image-based PDFs with math
- Accurate document chunking + semantic search (FAISS)
- LLaMA3 via Groq for lightning-fast, accurate responses
- CLI and Web UI using Streamlit
- Chat history support in the UI

---

## Folder Structure

studybot/
├── app/
│   ├── ingest.py              # Indexes cleaned text into FAISS
│   ├── chat.py                # Command line chatbot
│   └── streamlit_app.py       # Streamlit web interface
├── data/
│   ├── Machine_Learning.pdf   # Your input PDF
│   └── ml_clean_ocr.txt       # OCR'd clean text output
├── faiss_index/               # FAISS vector DB directory
├── .env                       # For your Groq API key
├── ocr_extract.py             # Extracts text using OCR
├── temp_pages                 # Extracted temp pages from OCR are stored here
├── requirements.txt
└── README.md

---
## .env Setup
Create a `.env` file in your root directory:
GROQ_API_KEY=your_groq_api_key_here

You can get the key from [https://console.groq.com](https://console.groq.com)

---

## Installation

### 1. Clone the repository


git clone https://github.com/yourusername/studybot.git
cd studybot

### 2. Set up virtual environment

python -m venv venv
venv\Scripts\activate     # Windows
OR
source venv/bin/activate  # macOS/Linux

### 3. Install dependencies

pip install -r requirements.txt

---
## System Tools You Must Install:

1. Tesseract OCR
Required for scanned/image PDFs.

Download (Windows):
https://github.com/UB-Mannheim/tesseract/wiki

Install to default location (C:\Program Files\Tesseract-OCR)

Add it to your system PATH or hardcode in ocr_extract.py.

2. Poppler for Windows (for pdf2image)
Download:
https://github.com/oschwartz10612/poppler-windows/releases

Extract the zip

Add the poppler/bin folder to your PATH

---

## USAGE

If your PDF contains images:

1. Run OCR on PDF:

python app/ocr_extract.py
-Output saved to: data/ml_clean_ocr.txt

2. Ingest into FAISS DB
python app/ingest.py
-Will create faiss_index/ from the extracted text.

3A. Chai via Command-line
python app/chat.py
-Type questions like What is overfitting?
-Type exit or quit to stop

3B. Launch Streamlit App
streamlit run app/streamlit_app.py
-Visit: http://localhost:XXXX
-Ask questions in the input box
-Keeps last 5 interactions
-Click  Clear Chat in the sidebar to reset
