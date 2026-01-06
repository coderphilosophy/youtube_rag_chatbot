from text_splitter import text_splitter
from generate_embedding import generate_embedding
from config.embedding_client import embedding_client as client
from langchain_community.vectorstores import FAISS

def create_vector_store(transcript):
    # Step 1: Split the transcript into chunks
    chunks = text_splitter(transcript)
    print(f"Transcript split into {len(chunks)} chunks.")

    # Step 2: Generate embeddings for each chunk
    # This step might take a while depending on the transcript length.
    # embeddings_list = [generate_embedding(chunk.page_content) for chunk in chunks]

    # Step 3: Create the vector store
    # FAISS.from_documents() is a convenient way to build the store.
    # It takes the text chunks and their corresponding embeddings.
    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=client
    )
    print("Vector store created successfully!")
    vector_store.save_local("faiss_index")
    return vector_store

def get_faiss_db():
    faiss_db = FAISS.load_local(
        "faiss_index",
        embeddings=client,
        allow_dangerous_deserialization=True
    )
    return faiss_db