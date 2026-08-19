# 🚀 Mission 01 - Build Your First AI Assistant

## 🎯 Mission Objective

Build a simple AI Assistant using the Google Gemini API that can answer user questions from the terminal.

This is my first AI application that communicates with a Large Language Model (LLM).

---

## 📚 What I Learned

### 1. What is an API?

An API (Application Programming Interface) allows two software applications to communicate with each other.

In this mission:

Python Application
↓

Gemini API

↓

Google Gemini LLM

↓

AI Response

---

### 2. What is an API Key?

An API Key is a unique secret used to authenticate my application before it can access the Gemini API.

It proves that my application is authorized to use Google's AI services.

---

### 3. Why do we use `.env`?

The `.env` file stores sensitive information such as API keys.

Example:

GEMINI_API_KEY=YOUR_API_KEY

This keeps secrets outside the source code.

---

### 4. Why do we use `load_dotenv()`?

`load_dotenv()` loads all variables from the `.env` file into the application's environment.

This allows Python to access the API key using:

```python
os.getenv("GEMINI_API_KEY")
```

Without `load_dotenv()`, Python cannot read values from the `.env` file.

---

### 5. Why do we use `.gitignore`?

The `.gitignore` file prevents sensitive or unnecessary files from being uploaded to GitHub.

Example:

```text
.env
.venv/
__pycache__/
```

This ensures that API keys remain private.

---

### 6. What is `requirements.txt`?

`requirements.txt` contains the list of Python packages required for the project.

Example:

```text
google-genai
python-dotenv
```

Anyone can recreate the project environment by running:

```bash
pip install -r requirements.txt
```

---

### 7. What is a Client?

The Gemini Client is the object responsible for communicating with Google's AI servers.

```python
client = genai.Client(api_key=api_key)
```

Think of it as a messenger between my Python application and Google's AI.

---

### 8. What happens when I ask a question?

The complete flow is:

User

↓

Python Application

↓

Gemini SDK

↓

Internet

↓

Google Gemini API

↓

Gemini Large Language Model

↓

Generated Response

↓

Python Application

↓

Terminal Output

The AI model is running on Google's servers, not on my computer.

---

## 💻 Technologies Used

- Python
- Google Gemini API
- google-genai SDK
- python-dotenv

---

## 🏗️ Features

- Accepts user input
- Sends prompts to Gemini
- Receives AI-generated responses
- Secure API key management using `.env`
- Virtual Environment (`.venv`)
- Dependency Management (`requirements.txt`)

---

## ▶️ Sample Output

```text
========================================
🤖 Charishma AI Assistant
========================================

Ask me anything:

> What is Python?

🤖 AI Response:

Python is a high-level programming language used for web development, automation, AI, and many other applications.
```

---

## 🧠 Key Concepts

- API
- API Key
- Environment Variables
- `.env`
- `.gitignore`
- Virtual Environment
- Gemini SDK
- Large Language Model (LLM)
- Client
- Request & Response

---

## 💡 What I Understood

- My Python application does not contain the AI model.
- It communicates with Google's Gemini servers through an API.
- The API key authenticates my application.
- `.env` helps keep sensitive information secure.
- `.gitignore` prevents secrets from being committed to GitHub.
- The Gemini SDK simplifies communication with the API.

---

## 🐞 Debug Notes

### Issue

404 NOT_FOUND

Reason:

The model `gemini-2.5-flash` is no longer available for new API keys.

Solution:

Updated the model to:

```python
model="gemini-3.6-flash"
```

Lesson Learned:

Always refer to the latest official documentation instead of relying on outdated tutorials.

---

## 🚀 Mission Status

✅ Completed