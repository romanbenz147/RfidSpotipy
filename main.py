import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json 
import spotipy 
import webbrowser 


username = 'YOUR USERNAME'
clientID = 'YOUR CLIENT ID'
clientSecret = 'YOUR CLIENT SECRET'
redirect_uri = 'http://google.com/callback/'
DEVICE_ID = 'YOUR DEVICE ID'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri, open_browser=False, scope='user-modify-playback-state user-read-playback-state') 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user()

reader = SimpleMFRC522()


while True: 

    print("Hold card near reader for individual playlist!")

    try:
        text = reader.read()[0]
        print(text)
    finally:
        GPIO.cleanup()

    
    if text == 671809288250:   
        spotifyObject.start_playback(device_id=DEVICE_ID, context_uri='YOUR PLAYLIST URI', offset={'position': 0})
        print('Playlist started playing.') 

    elif text == 601781254237: 
        spotifyObject.start_playback(device_id=DEVICE_ID, context_uri='YOUR PLAYLIST URI', offset={'position': 0})
        print('Playlist started playing.')

    else: 
        print("Please use a card that has been added to the script before")


