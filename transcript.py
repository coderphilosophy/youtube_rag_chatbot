from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

transcript_cache = {}

def get_transcript(video_id):
    if video_id in transcript_cache:
        return transcript_cache[video_id]

    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id).to_raw_data()
        print(transcript_list)
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        print(transcript[:100]) # Print first 100 characters

        transcript_cache[video_id] = transcript

        return transcript
    except TranscriptsDisabled:
        print("No captions available for this video.")