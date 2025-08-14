# StudyBot — ML PDF QA Chatbot

**StudyBot** is a personalized study assistant that lets you ask questions from your **Machine Learning course PDF**, either through the **command line** or an interactive **Streamlit** UI. It uses **OCR**, **FAISS**, **Instructor Embeddings**, and the **Groq LLM (LLaMA3)** to answer your questions effectively.

## ✨ Features

- 📚 Ask any question about your ML PDF
- 🔍 OCR support for scanned/image-based PDFs with math
- 🎯 Accurate document chunking + semantic search (FAISS)
- ⚡ LLaMA3 via Groq for lightning-fast, accurate responses
- 💻 CLI and Web UI using Streamlit
- 💬 Chat history support in the UI

## 📁 Project Structure

```
studybot/
├── app/
│   ├── ingest.py              # Indexes cleaned text into FAISS
│   ├── chat.py                # Command line chatbot
│   └── streamlit_app.py       # Streamlit web interface
├── data/
│   ├── Machine_Learning.pdf   # Your input PDF
│   └── ml_clean_ocr.txt       # OCR'd clean text output
├── faiss_index/               # FAISS vector DB directory
├── temp_pages/                # Extracted temp pages from OCR
├── .env                       # For your Groq API key
├── ocr_extract.py             # Extracts text using OCR
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### Prerequisites

Before installation, you need to install these system tools:

#### 1. Tesseract OCR
Required for processing scanned/image PDFs.

**Windows:**
- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install to default location (`C:\Program Files\Tesseract-OCR`)
- Add to your system PATH or update the path in `ocr_extract.py`

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

#### 2. Poppler (for pdf2image)

**Windows:**
- Download from: https://github.com/oschwartz10612/poppler-windows/releases
- Extract the zip file
- Add the `poppler/bin` folder to your system PATH

**macOS:**
```bash
brew install poppler
```

**Linux:**
```bash
sudo apt-get install poppler-utils
```

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/studybot.git
cd studybot
```

#### 2. Set Up Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Environment Configuration
Create a `.env` file in your root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from: https://console.groq.com

## 🚀 Usage

### For PDFs with Images/Scanned Content

#### Step 1: Extract Text using OCR
```bash
python ocr_extract.py
```
- Output will be saved to: `data/ml_clean_ocr.txt`

#### Step 2: Create FAISS Vector Database
```bash
python app/ingest.py
```
- Creates `faiss_index/` directory from the extracted text

### Asking Questions

#### Option A: Command Line Interface
```bash
python app/chat.py
```
- Type questions like: "What is overfitting?"
- Type `exit` or `quit` to stop

#### Option B: Web Interface (Streamlit)
```bash
streamlit run app/streamlit_app.py
```
- Opens a web interface in your browser
- Includes chat history and better UI experience

## 🔧 Configuration

### Customizing OCR Settings
Edit `ocr_extract.py` to modify:
- OCR language settings
- Image preprocessing parameters
- Output formatting

### Adjusting Search Parameters
Edit `app/ingest.py` to modify:
- Chunk size and overlap
- Embedding model settings
- FAISS index parameters

## 📝 Example Questions

Try asking StudyBot questions like:
- "What is the difference between supervised and unsupervised learning?"
- "Explain gradient descent algorithm"
- "What are the types of neural networks?"
- "How does cross-validation work?"

## 🛠️ Troubleshooting

### Common Issues

**OCR not working:**
- Ensure Tesseract is properly installed and in PATH
- Check if Poppler is correctly installed
- Verify PDF is not password-protected

**FAISS index errors:**
- Delete `faiss_index/` directory and re-run `ingest.py`
- Check if the text file exists in `data/`

**Groq API errors:**
- Verify your API key in `.env` file
- Check your internet connection
- Ensure you haven't exceeded rate limits

## 📄 Requirements

See `requirements.txt` for the complete list of Python dependencies.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for fast LLM inference
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search
- [Instructor Embeddings](https://github.com/xlang-ai/instructor-embedding) for semantic embeddings
- [Streamlit](https://streamlit.io/) for the web interface
