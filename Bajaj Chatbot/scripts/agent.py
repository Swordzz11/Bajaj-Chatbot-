import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatOpenAI
from load_stock_data import get_price_stats


# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Embeddings
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Load vector DB
db = Chroma(persist_directory="chroma_store", embedding_function=embedding)

# Create retriever
retriever = db.as_retriever()

# Define transcript QA tool
@tool
def transcript_qa_tool(query: str) -> str:
    """Answers queries from Bajaj Finserv quarterly earnings transcripts."""
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join([doc.page_content for doc in docs[:3]])

# Define stock tool
@tool
def stock_price_tool(query: str) -> str:
    """Answers queries about Bajaj Finserv stock prices from a CSV file."""
    return get_price_stats(query)

# Choose LLM with fallback
def get_llm():
    try:
        return ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
    except Exception as e:
        print("⚠️ Gemini failed. Falling back to OpenAI. Error:", e)
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create agent
llm = get_llm()
tools = [transcript_qa_tool, stock_price_tool]
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# Run agent
def run_agent(query):
    return agent.run(query)
