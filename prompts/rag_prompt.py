from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

rag_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior QA Automation Engineer.

Answer ONLY from the requirement document.

Requirement:

{context}
"""
        ),

        MessagesPlaceholder(
            variable_name="chat_history"
        ),

        (
            "human",
            "{input}"
        ),
    ]
)