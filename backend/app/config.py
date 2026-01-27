import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# Default to 0.0.0.0 for Docker compatibility
BACKEND_HOST = os.getenv("BACKEND_HOST", "0.0.0.0")
BACKEND_PORT = int(os.getenv("BACKEND_PORT", 8000))

if not HF_TOKEN:
    raise RuntimeError("Missing HUGGINGFACEHUB_API_TOKEN")