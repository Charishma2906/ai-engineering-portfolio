from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Create Chat with System Instruction
chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "system_instruction": """
You are an interviewer.

Rules:
1. Explain concepts in simple language.
2. Always give real-world examples.
3. Be encouraging.
4. If asked about coding, explain step by step.
5. Keep answers concise.
6. If possible, provide diagrams for every question.
"""
    }
)

print("=" * 50)
print("🤖 Charishma's Personal AI Mentor")
print("=" * 50)
print("Type 'exit' to quit.\n")

while True:

    question = input("🧑 You: ")

    if question.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    response = chat.send_message(question)

    print("\n🤖 Mentor:\n")
    print(response.text)