from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("youtube-video-details-api-key4")

def get_video_details(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split('v=')[1].split('&')[0]

    # Build the YouTube API service object
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Make the API call
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()
    print(response)
    if 'items' in response and response['items']:
        video_data = response['items'][0]
        title = video_data['snippet']['title']
        thumbnail_url = video_data['snippet']['thumbnails']['high']['url']
        description = video_data['snippet']['description']
        views = video_data['statistics']['viewCount']
        likes = video_data['statistics'].get('likeCount', 'N/A')
        
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Views: {views}")
        print(f"Likes: {likes}")

        return {
            'title': title,
            'description': description,
            'thumbnail_url': thumbnail_url,
            'views': views,
            'likes': likes  
        }
    else:
        print("Video not found.")



# get_video_details("https://www.youtube.com/watch?v=wzssm02u35I&t=98s")