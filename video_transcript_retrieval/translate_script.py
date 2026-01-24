from youtube_transcript_api import YouTubeTranscriptApi

video_id = "5mitUXtNL_I"  # just the ID, not full URL

ytt_api = YouTubeTranscriptApi()

fetched_transcript = ytt_api.fetch(video_id)

# list available transcripts
transcript_list = ytt_api.list(video_id)
print(transcript_list)

transcript = transcript_list.find_transcript(['en'])
translated_transcript = transcript.translate('de')
print(translated_transcript.fetch())