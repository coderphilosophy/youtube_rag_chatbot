from langchain.text_splitter import RecursiveCharacterTextSplitter
from transcript import get_transcript
from generate_embedding import generate_embedding

def text_splitter(transcript):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([transcript])

    print(len(chunks))
    print(chunks[0])
    # print(chunks[0].page_content)

    return chunks

# transcript = get_transcript("KrOBzFwVzwA")
# chunk_0 = text_splitter(transcript)
# print(chunk_0)
# print(type(chunk_0))
# embedding = generate_embedding(chunk_0)

# print(embedding)
# https://www.youtube.com/watch?v=KrOBzFwVzwA&pp=ygUSamVycnlyaWdldmVyeXRoaW5n