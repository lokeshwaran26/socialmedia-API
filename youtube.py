import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

def youtube(File,File2,File3):
    CLIENT_SECRET_FILE = 'Client_Secret_file'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': File3,
            #'description': 'Love Tunes',
            #'tags': ['Love', 'True', 'Bgm', 'Tune']
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': upload_date_time,
            #'selfDeclaredMadeForKids': False,
        },
        #notifySubscribers': False
    }

    mediaFile = MediaFileUpload(File)

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload(File2)
    ).execute()
