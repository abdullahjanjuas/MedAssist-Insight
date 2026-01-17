""" Retrieve relevant context from the vector database based on user queries. """

# Importing necessary libraries
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Path where Chroma DB is stored
CHROMA_DB_DIR = "chroma_db"

# Function to get relevant context
def get_relevant_context(query: str, k: int = 3): # Params: User Query + Number of relevant documents to retrieve
    # Initializing Embedding model used for vector DB
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings
    )

    docs = vectordb.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in docs])
