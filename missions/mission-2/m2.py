from dotenv import load_dotenv
from google import genai
import os

# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

# Create a Chat Session
chat = client.chats.create(
    model="gemini-3.6-flash"
)

print("=" * 40)
print("🤖 Charishma AI Chat")
print("=" * 40)
print("Type 'exit' anytime to quit.\n")

while True:

    question = input("🧑 You: ")

    if question.lower() == "exit":
        print("\n👋 Thank you for chatting. Goodbye!")
        break

    response = chat.send_message(question)

    print("\n🤖 AI:")
    print(response.text)