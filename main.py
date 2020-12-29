import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

if __name__ == '__main__':
    with open('credentials.json') as raw:
        creds = json.load(raw)['spotify']
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=creds['client_id'],
                                                                   client_secret=creds['secret']))
        results = sp.search(q='weezer', limit=5)
        for idx, track in enumerate(results['tracks']['items']):
            print(idx, track['name'])
