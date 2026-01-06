# YouTube Transcript RAG Chatbot

A RAG (Retrieval-Augmented Generation) chatbot that lets you have conversations about YouTube videos. The bot processes video transcripts, creates semantic embeddings, and answers your questions based on the actual content of the video.

## What Does This Do?

Ever watched a long YouTube video and wished you could just ask questions about it instead of scrubbing through? That's what this project does. It downloads the transcript of any YouTube video, breaks it down into chunks, and lets you chat with it using natural language queries.

## How It Works

1. **Fetch Transcript**: Uses YouTube Data API to grab the video transcript
2. **Chunk the Text**: Splits the transcript into manageable pieces using LangChain's RecursiveCharacterTextSplitter
3. **Generate Embeddings**: Converts chunks into vector embeddings using NVIDIA's Llama 3.2 NemoRetriever model
4. **Store in FAISS**: Saves embeddings in a FAISS vector database for fast similarity search
5. **Answer Questions**: When you ask something, it finds relevant chunks and uses Qwen 70B Instruct to generate natural responses

## Tech Stack

- **LLM**: Qwen 70B Instruct (for answer generation)
- **Embeddings**: nvidia/llama-3.2-nemoretriever-300m-embed-v1
- **Vector Database**: FAISS
- **Text Processing**: LangChain RecursiveCharacterTextSplitter
- **YouTube API**: Google Cloud YouTube Data API v3

## Prerequisites

Before you start, make sure you have:

- Python 3.8 or higher
- A Google Cloud account with YouTube Data API v3 enabled
- API keys for your embedding and LLM models

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-rag-chatbot.git
cd youtube-rag-chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Set up your environment variables. Create a `.env` file in the root directory:

```
YOUTUBE_API_KEY=your_youtube_api_key_here
EMBEDDING_API_KEY=your_embedding_model_key
LLM_API_KEY=your_llm_api_key
```

## Usage

Run the main script:

```bash
python app.py
```

Enter a YouTube video URL when prompted, and start asking questions about the video content!

## Configuration

You can tweak various parameters in the code:

- **Chunk size**: Adjust how the transcript is split
- **Chunk overlap**: Control context preservation between chunks
- **Top-k retrieval**: Number of relevant chunks to retrieve
- **Temperature**: Control creativity of responses

## Known Issues

- Some YouTube videos don't have transcripts available (auto-generated or otherwise)
- Very long videos might take a while to process initially
- Rate limits apply to the YouTube API


## Contributing

Feel free to open issues or submit pull requests. All contributions are welcome!

## License

MIT License - feel free to use this however you want.

---

Built because I got tired of watching hour-long tutorials when I just needed one specific piece of information.
