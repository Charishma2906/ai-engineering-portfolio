# 🚀 Mission 02 - Build AI Chat Assistant

## 🎯 Mission Objective

Upgrade the AI Assistant built in Mission 01 into a real conversational chatbot that remembers previous messages within the same chat session.

---

## 📚 What I Learned

### 1. Chat Session

A chat session stores the conversation history so the AI can remember previous questions and answers.

Example:

You: My name is Charishma.

AI: Nice to meet you!

You: What is my name?

AI: Your name is Charishma.

This is possible because the same chat session is maintained.

---

### 2. Difference Between `generate_content()` and `chat.send_message()`

#### generate_content()

- One-time request
- No memory
- Every question is independent

Example:

Question → AI → End

---

#### chat.send_message()

- Maintains conversation history
- Remembers previous messages
- Suitable for chatbot applications

Example:

Question 1
↓

Question 2

↓

Question 3

↓

AI remembers everything

---

### 3. Why `while True`?

The chatbot should continuously accept questions until the user exits.

Without a loop:

Ask once

↓

Program ends

With `while True`:

Ask

↓

Answer

↓

Ask again

↓

Answer

↓

Continue...

---

### 4. Why `break`?

When the user types:

exit

the loop stops and the application closes gracefully.

---

## 💻 Technologies Used

- Python
- Gemini API
- google-genai
- python-dotenv

---

## 🏗️ Features

- AI Chat
- Conversation Memory
- Infinite Chat Loop
- Exit Command
- Secure API Key using `.env`

---

## ▶️ Sample Output

========================================

🤖 Charishma AI Chat

========================================

You: Hello

AI:
Hello! 👋

You: My name is Charishma.

AI:
Nice to meet you!

You: What is my name?

AI:
Your name is Charishma.

You: exit

Goodbye!

---

## 🧠 Key Concepts

- Chat Session
- Conversation Memory
- Context
- API Calls
- Infinite Loop
- User Interaction

---

## 💡 What I Understood

- A chat application is different from a single AI request.
- The AI remembers previous messages because the chat session stores conversation history.
- The Large Language Model still runs on Google's servers.
- My Python application acts as a client that sends messages and receives responses.

---

## 🐞 Debug Notes

### Issue

`404 NOT_FOUND`

Reason:

The model `gemini-2.5-flash` was deprecated for new users.

Solution:

Updated the model to:

```python
model="gemini-3.6-flash"
```

Lesson:

Always refer to the latest official documentation instead of older tutorials.

---

## 🚀 Mission Status

✅ Completed