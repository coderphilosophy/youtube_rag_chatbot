from create_faiss_db import get_faiss_db

def retriever(user_prompt: str):
    vector_store = get_faiss_db()
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 8})

    retrieved_docs = retriever.invoke(user_prompt)
    print("--------------------------------------------------------------------------")
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    print(context_text)
    print("--------------------------------------------------------------------------")
    return context_text
