from langchain.chains import create_retrieval_chain

from rag.vector_store import get_vector_store
from rag.retriever import create_retriever
from rag.document_chain import get_document_chain


def get_rag_chain(chunks):

    vector_store = get_vector_store(chunks)

    retriever = create_retriever(vector_store)

    document_chain = get_document_chain()

    rag_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return rag_chain