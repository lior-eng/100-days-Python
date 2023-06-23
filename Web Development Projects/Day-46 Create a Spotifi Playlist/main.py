from bs4 import BeautifulSoup
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""

'''
Asking the user for a date inputwith a specific format YYYY-MM-DD
'''
while True:
    user_input = input("Which year do you want to travel to?"
                       "Type the date in this format YYYY-MM-DD:")
    pattern = r"\d{4}-\d{2}-\d{2}"
    if not re.match(pattern, user_input):
        print("Invalid input. Please enter the date in the format YYYY-MM-DD.")
        continue
    break

'''
Taking the top 100 songs from the "billboard" site,
by the date of the user input above
'''
url = f"https://www.billboard.com/charts/hot-100/{user_input}"

response = requests.get(url)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")

spans_songs = soup.select(selector= "li ul li h3")
songs = [song.getText().strip() for song in spans_songs]

'''
Creating an instance of Spotify and using SpotifyOAuth class.
user_id is the currently authenticated user.
'''
scope = "playlist-modify-private"
redirect_uri  = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= CLIENT_ID,
                                               client_secret= CLIENT_SECRET,
                                               redirect_uri= redirect_uri,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               ))#username=""
user_id = sp.current_user()["id"]

'''
Search songs in spotify by URI 
'''
songs_uri = []
for song in songs:
    search_result = sp.search(q= f"track:{song} year:{user_input.split('-')[0]}")
    try:
        uri = search_result['tracks']['items'][0]['uri'] # for URL -> "external_urls"
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} is not found")

'''
Creating a playlist in spotify
'''
try:
    playlist = sp.user_playlist_create(user= user_id,
                                    name= f"{user_input} top 100",
                                    public=False)
except IndexError:
    print("playlist was not created")

'''
Add the songs by the URI to the playlist above
'''
sp.playlist_add_items(playlist_id= playlist["id"], items= songs_uri)