from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from .config import HF_TOKEN

# Using Llama 3.1 8B - Excellent for instruction following and RAG
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512, # Increased slightly for more detailed answers
    temperature=0.1,    # Lowered for higher factual accuracy in RAG
    huggingfacehub_api_token=HF_TOKEN,
    # Adding a timeout and retry logic helps with 100+ concurrent users
    timeout=300 
)

# This wrapper allows the model to handle "messages" (system, user, assistant) 
# instead of just raw strings, which is required for professional LangChain chains.
chat_model = ChatHuggingFace(llm=llm)


