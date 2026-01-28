from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from .vectorstore import get_vectorstore
from .llm import chat_model
from .memory import add_message

def rag_chat(question: str, user_id: str):
    vectorstore = get_vectorstore()
    
    # Filter by user_id so users only see their own data
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4, "filter": {"user_id": user_id}}
    )

    template = """Answer the question based ONLY on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | chat_model
        | StrOutputParser()
    )

    answer = chain.invoke(question)
    add_message(user_id, "user", question)
    add_message(user_id, "assistant", answer)

    return answer, []