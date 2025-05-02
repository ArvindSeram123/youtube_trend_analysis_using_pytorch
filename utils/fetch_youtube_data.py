from googleapiclient.discovery import build
import json
import datetime

# Replace with your actual API key
API_KEY = 'AIzaSyCsorX3YQ-5Y2GxxHE-XgYLw51gqm5a8Zw'
youtube = build('youtube', 'v3', developerKey=API_KEY)

def fetch_video_data(query="data science", max_results=10):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    video_data = []

    for item in response['items']:
        video_id = item['id']['videoId']
        snippet = item['snippet']

        video_details = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        ).execute()

        if video_details['items']:
            details = video_details['items'][0]
            stats = details.get('statistics', {})
            tags = details['snippet'].get('tags', [])

            video_info = {
                "video_id": video_id,
                "title": snippet['title'],
                "channel": snippet['channelTitle'],
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "tags": tags,
                "category": details['snippet'].get("categoryId", "N/A"),
            }
            video_data.append(video_info)

    return video_data

def save_to_json(data, path="youtube_data.json"):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f"{today}_{path}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    data = fetch_video_data(query="machine learning", max_results=25)
    save_to_json(data)
