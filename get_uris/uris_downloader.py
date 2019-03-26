import glob
import asyncio
from dir_settings import DATA_PATH
from asgiref.sync import sync_to_async
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



class Uris:
    '''Handling Uris'''

    spotify_key = None
    spotify_secret = None


    def __init__(self):
        pass


    def get_uris(self, spotify_key, spotify_secret):
        if not spotify_key:
            raise Exception('Api key not provided')

        if not spotify_secret:
            raise Exception('Api secret not provided')

        self.spotify_key = str(spotify_key)
        self.spotify_secret = str(spotify_secret)

        self._run_until_patcher_finish()
        self._concat_uris()


    def _run_until_patcher_finish(self):
        part = 0
        patches = self._create_patches()
        while part < len(patches):
            part = self._uris_patcher(part=part)


    def _uris_patcher(self, part=0):
        patches = self._create_patches()
        try:
            while part < len(patches):
                loop = asyncio.get_event_loop()
                future = asyncio.ensure_future(self._main(patches[part]))
                responses = loop.run_until_complete(future)
                self._save_uris(responses, part)
                part += 1
            return part
        finally:
            return part


    def _concat_uris(self):
        path = DATA_PATH + '/uri_chunks'
        all_files = glob.glob(path + "/*.csv")
        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)

        frame = pd.concat(li, axis=0, ignore_index=True)
        frame.to_csv(DATA_PATH + '/uris.csv', index=None, encoding='utf-8')


    def _sp_init(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.spotify_key,
                                                              client_secret=self.spotify_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    def _sp_search(self, q):
        sp = self._sp_init()
        print(q)
        return sp.search(q=q, type='track', limit=1)


    async def _main(self, patch):
        tasks = [asyncio.ensure_future(sync_to_async(self._sp_search)(q)) for q in patch]
        return await asyncio.gather(*tasks)


    def _get_data_from_file(self):
        df = pd.read_csv(DATA_PATH + '/scrobbles.csv')
        artist_names = df['artist'].to_list()
        track_names = df['track'].to_list()
        return artist_names, track_names


    def _get_queries(self):
        artist_names, track_names = self._get_data_from_file()
        return ['artist: ' + artist_names[i] + ' track: ' + track_names[i] for i in range(len(artist_names))]


    def _create_patches(self):
        queries = self._get_queries()
        return [queries[x:x + 1000] for x in range(0, len(queries), 1000)]


    def _save_uris(self, responses, c):
        uris = []

        for response in responses:
            print(response)
            resp_data = response['tracks']['items']
            if not resp_data:
                continue
            uri = response['tracks']['items'][0]['uri']
            uris.append(uri)

        df = pd.DataFrame()
        df['uri'] = uris
        df.to_csv(DATA_PATH + '/uri_chunks/patch' + str(c) + '.csv', index=None, encoding='utf-8')
