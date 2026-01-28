from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from .config import HF_TOKEN

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512, 
    temperature=0.1,   
    huggingfacehub_api_token=HF_TOKEN,
    timeout=300 
)

chat_model = ChatHuggingFace(llm=llm)


