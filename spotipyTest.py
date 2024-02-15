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
  

print(json.dumps(user_name, sort_keys=True, indent=4)) 
  
while True: 
    
    print("Welcome to the project, " + user_name['display_name']) 
    print("0 - Exit the console") 
    print("1 - Search for a Song") 
    user_input = int(input("Enter Your Choice: ")) 
    if user_input == 1:     
        spotifyObject.start_playback(device_id=DEVICE_ID, context_uri='YOUR PLAYLIST URI', offset={'position': 0})
        print('Song playback has started') 

    elif user_input == 0: 
        print("Good Bye, Have a great day!") 
        break
    else: 
        print("Please enter valid user-input.") 