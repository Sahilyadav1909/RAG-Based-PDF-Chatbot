# 🤖 RAG-Based PDF Chatbot

A professional-grade **RAG (Retrieval-Augmented Generation)** application that allows users to upload PDF documents and have natural conversations with them. Built with a decoupled architecture using **FastAPI** for the heavy lifting and **Streamlit** for a sleek user interface.



## 🚀 Features
* **Instant PDF Ingestion:** Upload any PDF and begin chatting in seconds.
* **Contextual Memory:** The AI remembers your previous questions to provide deep insights.
* **Persistent Storage:** Using Docker Volumes to ensure your data stays safe even after restarts.
* **Scalable Architecture:** Fully containerized using Docker Compose for easy deployment.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Backend:** FastAPI (Python)
* **AI Orchestration:** LangChain
* **Vector Database:** ChromaDB
* **Models:** HuggingFace / Sentence-Transformers
* **DevOps:** Docker & Docker Compose

## 📦 Project Structure
```text
AI_chatbot/
├── backend/            # FastAPI Server (AI Logic & Vector DB)
├── frontend/           # Streamlit Web UI
├── docker-compose.yml  # Multi-container orchestration
└── .env               # API Configuration
