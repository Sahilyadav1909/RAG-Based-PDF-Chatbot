from langchain_core.messages import HumanMessage, AIMessage

# For production/100+ users, replace this dict with a Redis client
chat_store = {}

def get_history(session_id: str):
    return chat_store.setdefault(session_id, [])

def add_message(session_id: str, role: str, content: str):
    history = get_history(session_id)
    if role == "user":
        history.append(HumanMessage(content=content))
    else:
        history.append(AIMessage(content=content))
    
    # Context window management
    if len(history) > 10:
        chat_store[session_id] = history[-10:]