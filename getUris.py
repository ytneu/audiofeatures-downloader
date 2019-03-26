import argparse
import warnings
from get_uris import uris_downloader

warnings.filterwarnings('ignore')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-spotify_key',
                        '-sk',
                        help='Your spotify api key')


    parser.add_argument('-spotify_secret',
                        '-ss',
                        help='Your spotify secret')


    args = parser.parse_args()

    uris = uris_downloader.Uris()

    if args.spotify_key is not None:
        uris.spotify_key = args.spotify_key

    if args.spotify_secret is not None:
        uris.spotify_secret = args.spotify_secret

    spotify_key = args.spotify_key
    spotify_secret = args.spotify_secret


    uris.get_uris(spotify_key, spotify_secret)
