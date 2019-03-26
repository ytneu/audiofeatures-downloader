from .lastfm_settings import LASTFM_BASE_URL
from dir_settings import DATA_PATH
import requests
import asyncio
from aiohttp import ClientSession
import pandas as pd

class LastfmDownloader:
    '''Download scrobbles from last.fm'''

    username = None
    key = None


    def __init__(self):
        pass


    def fetch_scrobbles(self, username, key):
        if not username:
            raise Exception('Username not provided')
        if not key:
            raise Exception('API key not provided')

        self.username = str(username)
        self.key = str(key)

        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self._main())
        responses = loop.run_until_complete(future)

        self._save_scrobbles(responses)


    async def _fetch(self, url, session):
        async with session.get(url) as response:
            return await response.json()


    async def _main(self):
        urls = self._get_urls()
        async with ClientSession() as session:
            tasks = [asyncio.ensure_future(self._fetch(url, session)) for url in urls]
            return await asyncio.gather(*tasks)


    def _get_total_pages(self):
        url = LASTFM_BASE_URL.format(self.username, self.key) + '&format=json'
        response = requests.get(url).json()
        total_pages = int(response['recenttracks']['@attr']['totalPages'])
        return total_pages


    def _get_urls(self):
        total_pages = self._get_total_pages()
        url = LASTFM_BASE_URL.format(self.username, self.key)
        urls = [url + '&page={}&format=json'.format(page) for page in range(1, total_pages)]
        return urls


    def _save_scrobbles(self, responses):
        path = DATA_PATH + '/scrobbles.csv'
        artist_names = []
        track_names = []

        for response in responses:
            scrobbles = response
            for scrobble in scrobbles['recenttracks']['track']:
                artist_names.append(scrobble['artist']['#text'])
                track_names.append(scrobble['name'])

        df = pd.DataFrame()
        df['artist'] = artist_names
        df['track'] = track_names

        df.drop_duplicates().to_csv(path, index=None, encoding='utf-8')
        print('saved')
