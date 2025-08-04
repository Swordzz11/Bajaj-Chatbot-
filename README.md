# 📊 Bajaj Finserv RAG Chatbot

An intelligent chatbot that answers questions related to **Bajaj Finserv’s stock data** and **quarterly earnings transcripts** using Retrieval-Augmented Generation (RAG). Supports answering queries such as:

- "What was the highest stock price in Jan 2024?"
- "Why is BAGIC facing headwinds in the motor insurance business?"
- "What’s the rationale for the Hero partnership?"
- "Compare Bajaj Finserv from Jan-24 to Mar-24."
- "Act as the CFO of BAGIC and draft commentary for the investor call."

---

## 🚀 Tech Stack

| Component       | Tech                                |
|----------------|-------------------------------------|
| LLM            | [OpenAI GPT-3.5 / Gemini-Pro]       |
| Embeddings     | SentenceTransformer (MiniLM-L6-v2)  |
| Vector DB      | ChromaDB                            |
| RAG Framework  | LangChain                           |
| Frontend       | Streamlit                           |
| CLI Chat       | Python                              |

---

## 📁 Project Structure

Bajaj Chatbot/
├── data/
│ └── BFS_Share_Price.csv
├── chroma_store/
│ └── (vector db will be stored here)
├── scripts/
│ ├── agent.py
│ ├── load_transcripts.py
│ └── load_stock_data.py
├── app.py
├── cli_chat.py
├── .env
└── README.md

yaml
Copy
Edit

---

## 🧪 Setup Instructions

### ✅ 1. Clone Repository
```bash
git clone https://github.com/Swordzz11/bajaj-chatbot.git
cd bajaj-chatbot
✅ 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 3. Prepare Environment
Create a .env file:

env
Copy
Edit
# For OpenAI fallback
OPENAI_API_KEY=your_openai_key_here
LLM_PROVIDER=openai

# Optional: If using Gemini
# GOOGLE_API_KEY=your_gemini_api_key_here
# LLM_PROVIDER=google
✅ 4. Embed Transcripts
bash
Copy
Edit
python scripts/load_transcripts.py
💬 Run the Chatbot
💻 CLI Interface
bash
Copy
Edit
set PYTHONPATH=.
python cli_chat.py
🌐 Web Interface
bash
Copy
Edit
streamlit run app.py
Open browser at: http://localhost:8501

🧠 Example Questions
text
Copy
Edit
What was the average stock price in Q1 FY25?
Compare Bajaj Finserv performance between Jan 2024 and Mar 2024.
Why is BAGIC facing headwinds in motor insurance?
Give me a table of Allianz stake sale discussions.
Draft a CFO commentary for BAGIC.
