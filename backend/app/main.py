from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import os, shutil
from .chat import normal_chat
from .rag import rag_chat
from .ingest import ingest_pdf

app = FastAPI()

# FIX: Allows Streamlit to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/chat")
def chat(message: str, session_id: str):
    return {"reply": normal_chat(message, session_id)}

@app.post("/upload-pdf")
async def upload_pdf(background_tasks: BackgroundTasks, file: UploadFile = File(...), user_id: str = ""):
    path = os.path.join(UPLOAD_DIR, f"{user_id}_{file.filename}")
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Process ingestion in background so API returns immediately
    background_tasks.add_task(ingest_pdf, path, user_id)
    return {"status": "Upload successful. Processing in background..."}

@app.post("/chat-pdf")
def chat_pdf(question: str, user_id: str):
    answer, sources = rag_chat(question, user_id)
    return {"reply": answer, "sources": sources}