import spotipy
from spotipy.oauth2 import SpotifyOAuth

#User info
SPOTIPY_CLIENT_ID = '1dd896edfada4508a234085f173714b2'
SPOTIPY_CLIENT_SECRET = '8fc0a1f205934c76a673352b0487d8cf'
SPOTIPY_REDIRECT_URI = 'http://localhost:9000'

#define scope
scope = "user-read-private user-read-playback-state user-modify-playback-state"

#Create Spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope))

#Grabs users playback status to determine wheather to play or pause music
def play_pause():
    playback_info = sp.current_playback()
    playing = playback_info['is_playing']

    if(playing):
        sp.pause_playback()
    elif(not playing):
        sp.start_playback()

#Skips to the next song queued up
def next_song():
    sp.next_track()

#Goes back to the previous song
def prev_song():
    sp.previous_track()

def get_image():
    playback_info = sp.current_playback()
    newimage = playback_info['item']['album']['images'][0]['url']
    return newimage
































    