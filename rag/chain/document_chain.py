from langchain.chains.combine_documents import create_stuff_documents_chain

from config import llm
from prompts.rag_prompt import rag_prompt


def get_document_chain():
    return create_stuff_documents_chain(
        llm,
        rag_prompt
    )