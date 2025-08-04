import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def load_and_store_docs():
    folder = "data"
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_chunks = []

    for fname in os.listdir(folder):
        if fname.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder, fname))
            docs = loader.load()
            chunks = splitter.split_documents(docs)
            all_chunks.extend(chunks)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Chroma automatically persists now, no need for db.persist()
    Chroma.from_documents(
        documents=all_chunks,
        embedding=embedding,
        persist_directory="chroma_store"
    )

if __name__ == "__main__":
    load_and_store_docs()
