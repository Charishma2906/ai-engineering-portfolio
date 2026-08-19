from dotenv import load_dotenv
from google import genai
import os

# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

print("=" * 40)
print("🤖 Charishma AI Assistant")
print("=" * 40)

question = input("\nAsk me anything: ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=question
)

print("\n🤖 AI Response:\n")
print(response.text)