import pandas as pd
import spotipy
from dir_settings import DATA_PATH
from spotipy.oauth2 import SpotifyClientCredentials


class AudioFeatures:
    '''Handling AudioFeatures'''

    spotify_key = None
    spotify_secret = None


    def __init__(self):
        pass


    def save_features(self, spotify_key, spotify_secret):
        if not spotify_key:
            raise Exception('Api key not provided')

        if not spotify_secret:
            raise Exception('Api secret not provided')

        self.spotify_key = str(spotify_key)
        self.spotify_secret = str(spotify_secret)


        artist = []
        name = []
        danceability = []
        energy = []
        key = []
        loudness = []
        mode = []
        speechiness = []
        acousticness = []
        instrumentalness = []
        liveness = []
        valence = []
        tempo = []
        urri = []
        duration_ms = []

        data = self._get_uris_list()
        patches = self._create_patches(data)
        counter = 0
        for patch in patches:
            sp = self._sp_init()

            audio_features = sp.audio_features(patch)
            tracks = sp.tracks(patch)

            for audio_feature in audio_features:
                counter += 1
                print(counter)

                danceability.append(audio_feature['danceability'])
                energy.append(audio_feature['energy'])
                key.append(audio_feature['key'])
                loudness.append(audio_feature['loudness'])
                mode.append(audio_feature['mode'])
                speechiness.append(audio_feature['speechiness'])
                acousticness.append(audio_feature['acousticness'])
                instrumentalness.append(audio_feature['instrumentalness'])
                liveness.append(audio_feature['liveness'])
                valence.append(audio_feature['valence'])
                tempo.append(audio_feature['tempo'])
                urri.append(audio_feature['uri'])
                duration_ms.append(audio_feature['duration_ms'])

            for track in tracks['tracks']:
                artist.append(track['album']['artists'][0]['name'])
                name.append(track['name'])

        df = pd.DataFrame()
        df['artist'] = artist
        df['track'] = name
        df['danceability'] = danceability
        df['energy'] = energy
        df['key'] = key
        df['loudness'] = loudness
        df['mode'] = mode
        df['speechiness'] = speechiness
        df['acousticness'] = acousticness
        df['instrumentalness'] = instrumentalness
        df['liveness'] = liveness
        df['valence'] = valence
        df['tempo'] = tempo
        df['urri'] = urri
        df['duration_ms'] = duration_ms

        df.to_csv(DATA_PATH + '/audio_features.csv')


    def _get_uris_list(self):
        df = pd.read_csv(DATA_PATH + '/uris.csv')
        return df['uri'].to_list()


    def _create_patches(self, data):
        return [data[x:x + 50] for x in range(0, len(data), 50)]


    def _sp_init(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.spotify_key,
                                                              client_secret=self.spotify_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)
