from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# ----------------------------
# Python Tool
# ----------------------------
def get_current_time():
    """Returns the current system time."""
    return datetime.now().strftime("%I:%M:%S %p")

def get_current_date():
    """Returns today's date."""
    return datetime.now().strftime("%d %B %Y")

tools = [
    get_current_time,
    get_current_date
]

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        tools=tools,
        system_instruction="""
You are Charishma's AI Assistant.

Whenever the user asks for the current time,
always use the get_current_time tool.
Whenever the user asks for the current date,
always use the get_current_date tool.
"""
    )
)

print("=" * 50)
print("🤖 Charishma AI Assistant")
print("=" * 50)
print("Type 'exit' to quit.\n")

while True:

    question = input("🧑 You: ")

    if question.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    response = chat.send_message(question)

    print("\n🤖 AI:")
    print(response.text)