# Rasboxfy 

Rasboxfy lets you play indivdual Spotify-Playlists by RFID Key-Card user identification via a Rasperry Pi and Speakers: 

Each Key-Card is assigned to a user. Using the Key-Cards ID, Rasboxfy is able to find the suiting/wished playlist for the user!

## Installation

-> Install the requirements.txt file using ```pip install -r requirements.txt```

-> Create a new project on the Spotify Developer Page. Set the Redirect URL to 'http://google.com/callback/'. Note your Client_ID, Client_Secret.

-> Make sure your Raspberry Pi is connected to Spotify Connect. The best way to do this is using [Raspotify](https://github.com/dtcooper/raspotify).

-> Once your RasPI is connected to Spotify Connect and you're able to choose it as a speaker in Spotify, go [here](https://developer.spotify.com/documentation/web-api/reference/get-a-users-available-devices) and write down your Pi's Spotify Device_ID
 
-> Install Spotifys Web API ```pip3 install Spotipy```
