
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


def upload_clips(clips):
    CLIENT_SECRET_FILE = '<client file.json>'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    for clip in clips:
        request_body = {
            'snippet': {
                'categoryId': 23,
                'title': clip['title'],
                'description': 'subscribe :)',
                'tags': ['Twitch', 'Clips', 'Daily']
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False, 
            },
            'notifySubscribers': False
        }

        mediaFile = MediaFileUpload(clip['slug'] + ".mp4")

        response_upload = service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()


        service.thumbnails().set(
            videoId=response_upload.get('id'),
            media_body=MediaFileUpload(clips['image'])
        ).execute()