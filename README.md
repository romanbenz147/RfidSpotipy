# Rasboxfy 

Rasboxfy lets you play indivdual Spotify-Playlists by RFID Key-Card user identification via a Rasperry Pi and Speakers: 

Each Key-Card is assigned to a user. Using the Key-Cards ID, Rasboxfy is able to find the suiting/wished playlist for the user!

## Installation

-> Install the requirements.txt file using ```pip install -r requirements.txt```

-> Create a new project on the Spotify Developer Page. Set the Redirect URL to 'http://google.com/callback/'. Note your Client_ID, Client_Secret.

-> Make sure your Raspberry Pi is connected to Spotify Connect. The best way to do this is using [Raspotify](https://github.com/dtcooper/raspotify).

-> Once your RasPI is connected to Spotify Connect and you're able to choose it as a speaker in Spotify, go [here](https://developer.spotify.com/documentation/web-api/reference/get-a-users-available-devices) and write down your Pi's Spotify Device_ID
 
-> Install Spotifys Web API ```pip3 install Spotipy```

-> git clone this project onto your file system ```git clone https://github.com/romanbenz147/RfidSpotipy.git```

## Usage

-> Get your RFID Cards IDs by executing the getCardID.py script. Replace the Card-IDs I used in the main.py (marked by: 'xxxxxxxx') by your IDs.

-> Get the Spotify URIs of your favourite Playlists and insert them into the according placeholder in main.py

-> -> ```python3 main.py``` (Make sure you are in the right folder)

-> The first time you run this code, you should get a Spotify-Link you're ment to copy and paste into your browser to authenticate the usage of your Spotify Data. After, everthing is ready for use!!! Just continue by holding a RFID-Card you added before close to the RFID-Scanner or relaunch ```main.py```

