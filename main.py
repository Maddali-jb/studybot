import openai
from app.config import GROQ_API_KEY

# Point OpenAI client to Groq API
client = openai.OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# Use LLaMA 3 model instead
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": "Hello via Groq — are you working now?"}
    ]
)

print(response.choices[0].message.content)