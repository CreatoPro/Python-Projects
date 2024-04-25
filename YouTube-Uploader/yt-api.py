from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import datetime
import pytz
import pickle

# Authenticate with Google API
def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('youtube', 'v3', credentials=creds)

# Schedule a video
def schedule_video(youtube, video_id, publish_time):
    try:
        request = youtube.videos().update(
            part="snippet",
            body={
                "id": video_id,
                "snippet": {
                    "scheduledStartTime": publish_time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                    "publishAt": publish_time.strftime('%Y-%m-%dT%H:%M:%S%z')
                }
            }
        )
        response = request.execute()
        print("Video scheduled successfully!")
    except HttpError as e:
        print("An HTTP error occurred:", e)

# Main function
def main():
    youtube = authenticate()

    video_id = "YOUR_VIDEO_ID_HERE"
    publish_time = datetime.datetime(2024, 4, 1, 12, 0, 0, tzinfo=pytz.UTC)  # Example: April 1st, 2024 at 12:00 UTC

    schedule_video(youtube, video_id, publish_time)

if __name__ == "__main__":
    main()
