import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load keys from .env
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # still useful if you support both
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")