from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


chosen_date = input("Type the date in the YYYY-MM-DD: ")
# chosen_date = "2000-08-12"

bilboard_response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{chosen_date}/")
bilboard_data = bilboard_response.content

soup = BeautifulSoup(bilboard_data, "html.parser")

all_songs_titles = soup.select("li ul li h3")


songs_titles = [song_title.getText().strip()
                for song_title in all_songs_titles]
# print(songs_titles)

SCOPE = "playlist-modify-private"
USERNAME = "tiptil"

login_token = SpotifyOAuth(scope=SCOPE, username=USERNAME)

sp = spotipy.Spotify(auth_manager=login_token)

playlist_name = f"Top100- Bilboard for date {chosen_date}"

spotify_playlist = sp.user_playlist_create(user=USERNAME, name=playlist_name,
                                           public=False, description='Top 100 Bilboard for a specific date.')
playlist_id = spotify_playlist["id"]

query_year = chosen_date.split("-")[0]
songs_uris = []

for song in songs_titles:
    query = f"track: {song} year: {query_year}"
    result_data = sp.search(q=query, limit=1, type="track", market="US")
    try:
        uri = result_data["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"Song with title {song}, not found on Spotify.")

sp.user_playlist_add_tracks(
    user=USERNAME, playlist_id=playlist_id, tracks=songs_uris)
