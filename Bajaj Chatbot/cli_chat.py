import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts')))
from agent import run_agent


print("Bajaj Finserv CLI Chatbot")
while True:
    q = input("You: ")
    if q.lower() == "exit":
        break
    print("Bot:", run_agent(q))
