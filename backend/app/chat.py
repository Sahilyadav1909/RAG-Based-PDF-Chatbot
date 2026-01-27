from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .llm import chat_model
from .memory import get_history, add_message

def normal_chat(message: str, session_id: str):
    history = get_history(session_id)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | chat_model
    response = chain.invoke({"history": history, "input": message})

    add_message(session_id, "user", message)
    add_message(session_id, "assistant", response.content)

    return response.content