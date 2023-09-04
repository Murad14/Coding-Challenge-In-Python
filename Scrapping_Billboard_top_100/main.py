from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "382f99c90fb54d57914dd8257b84d131"
CLIENT_SECRET = "#############################"  # removed for security purpose

DATE = input(
    "Which date do you want to travel to? Type the date in this format: YYYY-MM-DD:\n")

response = requests.get(URL + DATE)
data = response.text
soup = BeautifulSoup(data, "html.parser")

song_list = []
song_data = soup.find_all(
    name="h3", id="title-of-a-story", class_="a-no-trucate")
for song in song_data:
    song_list = song.getText().strip("\n\t")
    pprint(song_list)

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_SECRET,
#                                                redirect_uri="http://localhost:8888/callback",
#                                                scope="playlist-modify-private",
#                                                show_dialog=True,
#                                                 cache_path="token.txt"))
#
# IDs = []
# for song in song_list:
#     info = sp.search(q=f"track:{song} year:{DATE[:4]}", limit=1, type="track")
#     try:
#         IDs.append(info["tracks"]["items"][0]["uri"])
#     except IndexError:
#         continue
#
# user_id = sp.me()["id"]
# new_playlist = sp.user_playlist_create(user=user_id, name=f"Billboard {DATE}", public=False, collaborative=False)
# new_id = new_playlist["id"]
# sp.playlist_add_items(playlist_id=new_id, items=IDs, position=None)
