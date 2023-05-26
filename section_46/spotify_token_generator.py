import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_SCOPE = "playlist-modify-private"
REDIRECT_URI = "http://localhost:8888/callback/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SPOTIPY_SCOPE,
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        cache_path="token.txt"
    )
)


spotify_id = sp.current_user()["id"]
print(spotify_id)
