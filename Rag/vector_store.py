""" Build a vector database from medical knowledge documents. """

# Importing necessary libraries
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Path where knowledge docs live
KNOWLEDGE_DIR = "Medical_knowledge"
CHROMA_DB_DIR = "chroma_db"

def build_vector_db():
    documents = []

    # Load all .txt files in langchain documents
    for file in os.listdir(KNOWLEDGE_DIR):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(KNOWLEDGE_DIR, file))
            documents.extend(loader.load())

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create Chroma DB
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    vectordb.persist()
    print("Vector database created successfully!")

if __name__ == "__main__":
    build_vector_db()
