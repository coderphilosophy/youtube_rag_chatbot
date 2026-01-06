from config.embedding_client import embedding_client as client

def generate_embedding(text: str):
    embedding = client.embed_query(text)
    print(embedding)

    return embedding
