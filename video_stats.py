import truststore
truststore.inject_into_ssl()
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"
def get_playlistId():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        #print(json.dumps(data, indent=4))

        channel_items= data['items'][0]

        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        #print(channel_playlistId)
        return channel_playlistId
    except requests.exceptions.RequestException as e:
       raise e


if __name__ == "__main__":
    get_playlistId()
