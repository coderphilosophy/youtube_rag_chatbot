import os
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_client = NVIDIAEmbeddings(
    model="nvidia/llama-3.2-nemoretriever-300m-embed-v1", 
    api_key=os.getenv("LLAMA_EMBEDDINGS_API_KEY"),
    truncate="NONE", 
)

# embedding_client = OpenAI(
#     base_url=os.getenv("LLAMA_EMBEDDINGS_BASE_URL"),
#     api_key=os.getenv("LLAMA_EMBEDDINGS_API_KEY")
# )