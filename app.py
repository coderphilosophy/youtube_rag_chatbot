# import streamlit as st
# import streamlit.components.v1 as components
# from get_video_details import get_video_details
# from transcript import get_transcript
# import re
# import time
# from stream_chat_response import stream_chat_completion
# import random # For simulating responses
# from create_faiss_db import create_vector_store
# from db_data_retriever import retriever

# st.title("YouTube Video Analyzer 🔎🎬")
# st.markdown("Enter a YouTube video URL to get its preview and transcript.")

# url = st.text_input("YouTube Video URL")
# print("URL: ", url)
# if url:
#     with st.spinner('Fetching data...'):
#         metadata = get_video_details(url)
#         if 'thumbnail_url' in metadata:
#             st.subheader(metadata['title'])

#             video_id_match = re.search(r"v=([^&]+)", url)
#             print("VIDEO ID MATCH: ", video_id_match)
#             if video_id_match:
#                 video_id = video_id_match.group(1)
#                 print("VIDEO ID: ", video_id)

#                 iframe_html = f"""
#                 <iframe width="700" height="400"
#                     src="https://www.youtube.com/embed/{video_id}"
#                     frameborder="0" allow="autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
#                 </iframe>
#                 """
                
#                 components.html(iframe_html, height=400)
                
#                 st.write(f"**Views:** {metadata['views']}")
#                 st.divider()
                
#                 st.subheader("Transcript")
#                 transcript = get_transcript(video_id)
                
#                 if transcript: 
#                     vector_store = create_vector_store(transcript)

#                 st.text_area("Full Transcript", transcript, height=400)
#                 with st.sidebar:
#                     st.title("Ask Me Anything about the Video! 🤖")
                    
#                     if "messages" not in st.session_state:
#                         st.session_state.messages = []

#                     for message in st.session_state.messages:
#                         with st.chat_message(message["role"]):
#                             st.markdown(message["content"])

#                     if prompt := st.chat_input("Type your message..."):
#                         st.session_state.messages.append({"role": "user", "content": prompt})
#                         with st.chat_message("user"):
#                             st.markdown(prompt)

#                         with st.chat_message("assistant"):
#                             with st.spinner("Thinking..."):
#                                 context_text = retriever(prompt)

#                                 response_container = st.empty() 
#                                 streamed_text = ""

#                                 for chunk in stream_chat_completion(prompt + "\n\nContext: " + context_text):
#                                     streamed_text += chunk
#                                     response_container.markdown(streamed_text) 

#                                 st.session_state.messages.append({"role": "assistant", "content": streamed_text})
                
#         else:
#             st.error(metadata['error'])



#-----------------------------------------------------------------------------------
import streamlit as st
import streamlit.components.v1 as components
from get_video_details import get_video_details
from transcript import get_transcript
import re
from create_faiss_db import create_vector_store
from db_data_retriever import retriever
from stream_chat_response import stream_chat_completion

# Initialize session state variables
if "video_data" not in st.session_state:
    st.session_state.video_data = {}
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("YouTube Video Analyzer 🔎🎬")
st.markdown("Enter a YouTube video URL to get its preview and transcript.")

url = st.text_input("YouTube Video URL")

if url:
    # Use session state to cache video data and vector store
    if st.session_state.video_data.get("url") != url:
        with st.spinner('Fetching data...'):
            metadata = get_video_details(url)
            if 'thumbnail_url' in metadata:
                st.session_state.video_data["url"] = url
                st.session_state.video_data["metadata"] = metadata
                st.session_state.video_data["video_id"] = re.search(r"v=([^&]+)", url).group(1)
                st.session_state.video_data["transcript"] = get_transcript(st.session_state.video_data["video_id"])
                
                # Check if a new vector store needs to be created
                # if "vector_store" not in st.session_state.video_data or st.session_state.video_data["vector_store"] is None:
                st.session_state.video_data["vector_store"] = create_vector_store(st.session_state.video_data["transcript"])
                print("\n\nYES THIS IS BEING EXECUTED.\n\n")
                
                # Reset chat messages for the new video
                st.session_state.messages = []
            else:
                st.error(metadata['error'])
                # Clear invalid URL from session state
                st.session_state.video_data = {}
                st.stop()
    
    # Display UI components from cached data
    video_data = st.session_state.video_data
    if video_data:
        st.subheader(video_data["metadata"]['title'])
        iframe_html = f"""
        <iframe width="700" height="400"
            src="https://www.youtube.com/embed/{video_data["video_id"]}"
            frameborder="0" allow="autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
        </iframe>
        """
        components.html(iframe_html, height=400)
        st.write(f"**Views:** {video_data['metadata']['views']}")
        st.divider()
        st.subheader("Transcript")
        st.text_area("Full Transcript", video_data['transcript'], height=400)

        # Chatbot UI
        with st.sidebar:
            st.title("Ask Me Anything about the Video! 🤖")
            chat_container = st.container() # Use a container for the chat history
            with chat_container:
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

            if prompt := st.chat_input("Type your message..."):
                # Append and display user message immediately
                st.session_state.messages.append({"role": "user", "content": prompt})
                with chat_container: # Display user message in the container
                    with st.chat_message("user"):
                        st.markdown(prompt)

                # Get the assistant's response
                with chat_container:
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking..."):
                            context_text = retriever(prompt)
                            full_prompt = f"Use the following context to answer the user's question.\n\nContext: {context_text}\n\nUser's Question: {prompt}\n\nAnswer:"
                            
                            response_container = st.empty()
                            streamed_text = ""
                            for chunk in stream_chat_completion(full_prompt):
                                streamed_text += chunk
                                response_container.markdown(streamed_text) 

                        st.session_state.messages.append({"role": "assistant", "content": streamed_text})