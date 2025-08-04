import streamlit as st
import os
import sys

# 👇 Fix for: ModuleNotFoundError: No module named 'scripts.agent'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))
from agent import run_agent  # after path fix

# 🎯 Streamlit App UI
st.set_page_config(page_title="Bajaj Finserv RAG Chatbot", page_icon="📊")
st.title("📊 Bajaj Finserv RAG Chatbot")

# 💬 User input
query = st.text_input("Ask your question (e.g., stock price or transcript insights):")

# 🤖 LLM response
if query:
    with st.spinner("Thinking..."):
        try:
            response = run_agent(query)
            st.success(response)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
