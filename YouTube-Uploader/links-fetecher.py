import csv
import googleapiclient.discovery
import time
# Replace with your API key obtained from Google Cloud Platform
API_KEY = "AIzaSyBz8LpMoKbndRj3ef8XO9rYRt35ByhZcr4"

# Channel ID or username
channel_id = "UCwihQJIVn-6Qus5Z92zVDoQ"  # Replace with the desired channel ID

# Open CSV file for writing
with open("channel_videos.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Video Title", "Video URL"])

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

# Retrieve uploads playlist ID
request = youtube.channels().list(
    part="contentDetails", id=channel_id
)
response = request.execute()

playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

# Get video information from the uploads playlist
request = youtube.playlistItems().list(
    part="snippet", playlistId=playlist_id, maxResults=50
)  # Adjust maxResults as needed

response = request.execute()

for item in response["items"]:
    video_id = item["snippet"]["resourceId"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_title = item["snippet"]["title"]


with open("channel_videos.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Video Title", "Video URL"])

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    # Retrieve uploads playlist ID
    request = youtube.channels().list(
        part="contentDetails", id=channel_id
    )
    response = request.execute()

    playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Get video information from the uploads playlist
    request = youtube.playlistItems().list(
        part="snippet", playlistId=playlist_id, maxResults=50
    )  # Adjust maxResults as needed

    response = request.execute()

    num_videos = len(response["items"])
    print(f"Retrieved information for {num_videos} videos.")

    # Iterate through all retrieved videos
    for i, item in enumerate(response["items"]):
        video_id = item["snippet"]["resourceId"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_title = item["snippet"]["title"]

        writer.writerow([video_title, video_url])

        # Add a delay between requests (optional, adjust based on quota limits)
        time.sleep(1)

print("Video links and titles saved to 'channel_videos.csv'")