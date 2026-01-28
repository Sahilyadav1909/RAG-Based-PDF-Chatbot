import streamlit as st
import requests
import uuid
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("🤖 AI Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_ready" not in st.session_state:
    st.session_state.pdf_ready = False

with st.sidebar:
    st.header("📄 PDF Management")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        if "last_file" not in st.session_state or st.session_state.last_file != uploaded_file.name:
            with st.spinner("Uploading..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                res = requests.post(f"{BACKEND_URL}/upload-pdf", files=files, params={"user_id": st.session_state.session_id})
                if res.status_code == 200:
                    st.session_state.pdf_ready = True
                    st.session_state.last_file = uploaded_file.name
                    st.success("PDF ready!")

    st.session_state.use_pdf = st.toggle("📘 Use PDF Context", value=st.session_state.pdf_ready)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message the bot..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        endpoint = "/chat-pdf" if st.session_state.use_pdf else "/chat"
        payload = {
            "question" if st.session_state.use_pdf else "message": prompt, 
            "user_id" if st.session_state.use_pdf else "session_id": st.session_state.session_id
        }
        
        try:
            res = requests.post(f"{BACKEND_URL}{endpoint}", params=payload, timeout=60)
            res.raise_for_status()
            answer = res.json()["reply"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"Error: Could not reach backend at {BACKEND_URL}. Check if the service is awake.")