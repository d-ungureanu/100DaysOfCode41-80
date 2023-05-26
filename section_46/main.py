from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# chosen_date = input("Type the date in the YYYY-MM-DD: ")
chosen_date = "2000-08-12"

bilboard_response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{chosen_date}/")
bilboard_data = bilboard_response.content

soup = BeautifulSoup(bilboard_data, "html.parser")

all_songs_titles = soup.select("li ul li h3")


songs_titles = [song_title.getText().strip()
                for song_title in all_songs_titles]
print(songs_titles)
