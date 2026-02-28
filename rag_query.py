from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

def query_rag(question):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever()

    # 🔥 NEW LANGCHAIN 1.0 METHOD
    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    llm = ChatOllama(model="llama3")

    response = llm.invoke(
        f"""Answer strictly based on the context below.

Context:
{context}

Question: {question}
"""
    )

    return response.content