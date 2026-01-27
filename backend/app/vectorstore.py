import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-small-v2",
    encode_kwargs={"normalize_embeddings": True}
)

CHROMA_PATH = "vector_db"

def get_vectorstore():
    # Centralized DB for all users
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )