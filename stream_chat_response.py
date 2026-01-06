from config.llm_client import llm_client as client
from config.llm_client_qwen3_instruct import llm_client_qwen3_instruct as client 

def stream_chat_completion(user_message: str):
    """Stream a user message to the chat model and yield response chunks."""
    completion = client.chat.completions.create(
        # model="qwen/qwen3-next-80b-a3b-thinking",
        model="qwen/qwen3-next-80b-a3b-instruct",
        messages=[
            {"role": "system", "content": "Please act as a helpful assistant. You are to use only the provided context to form your answers. If the information is not present, you are instructed to indicate that you don't have the answer."},
            {"role": "user", "content": user_message}
            ],
        temperature=0.6,
        top_p=0.7,
        max_tokens=4096,
        stream=True,
    )

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")  
            yield chunk.choices[0].delta.content