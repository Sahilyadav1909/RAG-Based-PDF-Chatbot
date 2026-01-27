from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .vectorstore import get_vectorstore

def ingest_pdf(pdf_path: str, user_id: str):
    vectorstore = get_vectorstore()

    # Faster loading than PDFPlumber
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80
    )
    chunks = splitter.split_documents(documents)

    # Tag each chunk with user_id for private retrieval
    for chunk in chunks:
        chunk.metadata["user_id"] = user_id

    vectorstore.add_documents(chunks)
