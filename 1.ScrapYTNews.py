from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime

# Your YOUTUBE API Key
API_KEY = ""

# YouTube API initialization
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Define search queries
queries = [
    # Politics & Government
    "USA political news 2024 short news",
    "Congress short news USA 2024",
    "Supreme Court decisions short news USA 2024",
    "immigration policy short news USA 2024",
    "gun control short news USA 2024",
    "foreign policy short news USA 2024",
    
    # # Economy & Business
    # "USA economy short news 2024",
    # "small business short news USA 2024",
    # "startup news USA 2024 short news",
    # "real estate market short news USA 2024",
    # "cryptocurrency short news USA 2024",
    # "stock market updates short news USA 2024",
    # "financial markets short news USA 2024",
    
    # Health & Healthcare
    "healthcare policy short news USA 2024",
    "public health short news USA 2024",
    "mental health short news USA 2024",
    "opioid crisis short news USA 2024",
    "vaccine updates short news USA 2024",
    "healthcare innovations short news USA 2024",
    
    # Environment & Climate
    "environmental policy short news USA 2024",
    "renewable energy short news USA 2024",
    "wildfires short news USA 2024",
    "climate action short news USA 2024",
    "hurricane season short news USA 2024",
    "electric vehicles short news USA 2024",
    
    # Technology & Science
    "technology short news USA 2024",
    "artificial intelligence short news USA 2024",
    "space exploration short news USA 2024",
    "biotechnology short news USA 2024",
    "cybersecurity short news USA 2024",
    "robotics short news USA 2024",
    
    # Society & Culture
    "social issues short news USA 2024",
    "racial equality short news USA 2024",
    "education short news USA 2024",
    "homelessness short news USA 2024",
    "mental health short news USA 2024",
    "consumer rights short news USA 2024",
    
    # Sports & Entertainment
    "NBA short news USA 2024",
    "MLB short news USA 2024",
    "NHL short news USA 2024",
    "Olympics short news USA 2024",
    "entertainment industry short news USA 2024",
    "Hollywood short news USA 2024",
    
    # Infrastructure & Transportation
    "transportation short news USA 2024",
    "public transportation short news USA 2024",
    "infrastructure projects short news USA 2024",
    "electric vehicles short news USA 2024",
    "traffic updates short news USA 2024",
    
    # Legal & Criminal Justice
    "criminal justice short news USA 2024",
    "Supreme Court rulings short news USA 2024",
    "legal reforms short news USA 2024",
    "drug policy short news USA 2024",
    "public safety short news USA 2024",
    
    # Miscellaneous
    "space policy short news USA 2024",
    "defense short news USA 2024",
    "military short news USA 2024",
    "trade agreements short news USA 2024",
    "tariffs short news USA 2024",
    "consumer electronics short news USA 2024",
    
    # General Short News Queries
    "breaking news USA 2024 short news",
    "latest news USA 2024 short news",
    "top headlines USA 2024 short news",
    "daily news USA 2024 short news",
    "current events USA 2024 short news",
    
    # Event-Specific Queries
    "midterm elections USA 2024 short news",
    "World Series short news USA 2024",
    "awards season short news USA 2024"
]


def get_videos(query, max_results=50):
    """
    Fetches videos related to the query using the YouTube Data API.
    """
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results,
        publishedAfter="2024-01-01T00:00:00Z",  # Start of 2024
        publishedBefore="2024-12-31T23:59:59Z",  # End of 2024
        videoDuration="short"
    )
    response = request.execute()
    
    # Collect video details
    videos = []
    for item in response['items']:
        video_data = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'channel': item['snippet']['channelTitle'],
            'publish_time': item['snippet']['publishTime'],
            'video_id': item['id']['videoId'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        videos.append(video_data)
    
    return videos


# Collect data for all queries
all_videos = []
for query in queries:
    print(f"Fetching videos for query: {query}")
    videos = get_videos(query, max_results=20)  # Adjust max_results as needed
    all_videos.extend(videos)

# Save results to a CSV file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f"youtube_news_videos_2024_{timestamp}.csv"

df = pd.DataFrame(all_videos)
df.to_csv(output_file, index=False)

print(f"Scraped data saved to {output_file}")

# Fetch videos related to "TV News"
# videos = get_videos("TV News USA, Trump", max_results=10)
video_urls = [v["url"]+"\n" for v in all_videos]

# Save to a CSV file
# df = pd.DataFrame(videos)
# df.to_csv('news_videos.csv', index=False)

with open("YT_VIDEO_URLS.txt", "w") as f:
    f.writelines(video_urls)

print("News videos saved to news_videos.csv")
