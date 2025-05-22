# 🩺 MedChat - Your AI Medical Assistant

Welcome to **MedChat**, your friendly AI-powered medical chatbot built with Streamlit! 💬✨  
It helps users describe their symptoms or medical concerns and get intelligent, informative responses in real-time. Perfect for preliminary guidance and healthcare awareness.  

---

## 👩‍⚕️ Features

- 🧠 **AI-Powered Responses** – Uses a powerful LLM to interpret and respond to medical queries.
- 📜 **Chat History** – Every chat is stored in sessions so users can revisit past conversations.
- ➕ **Multiple Sessions** – Start fresh conversations with one click.
- 🧍 **User-friendly Interface** – Clean, intuitive, and mobile-friendly UI using Streamlit.
- 💛 **Personal Touch** – Friendly and empathetic response style. Because we care!

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** LangChain QA Chain
- **LLM:** Groq LLM / HuggingFace (customizable)
- **Embedding:** FAISS with HuggingFace Embeddings
- **Language:** Python

---

## 🧑‍💻 How to Run Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Zoya28/medbot.git
   cd medbot


2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/scripts/activate     
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your backend (LangChain/Groq/etc.) in `backend.py`.**

5. **Run the app:**

   ```bash
   streamlit run app.py
   ```


## ⚠️ Disclaimer

> **This chatbot is for educational and informational purposes only.**
