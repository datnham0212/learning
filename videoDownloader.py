import os
import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def get_playlist_videos(playlist_url):
    try:
        response = requests.get(playlist_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract video URLs from the playlist
        video_urls = [a['href'] for a in soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})]

        return video_urls
    except Exception as e:
        print(f"An error occurred while fetching the playlist: {e}")
        return []

def download_videos_from_playlist(playlist_url, save_path='.'):
    video_urls = get_playlist_videos(playlist_url)

    if not video_urls:
        print("No videos found in the playlist.")
        return

    # Create save path if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    for video_url in video_urls:
        try:
            # Create a YouTube object
            yt = YouTube('https://www.youtube.com' + video_url)

            # Get the highest resolution stream
            video_stream = yt.streams.get_highest_resolution()

            # Download the video
            video_stream.download(save_path)

            print(f"Video '{yt.title}' downloaded successfully.")
        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")

if __name__ == "__main__":
    # Replace 'your_youtube_playlist_url' with the actual YouTube playlist URL
    playlist_url = 'your_youtube_playlist_url'

    # Replace 'your_save_path' with the directory where you want to save the downloaded videos
    download_videos_from_playlist(playlist_url, save_path='your_save_path')
