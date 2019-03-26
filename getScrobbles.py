import argparse
from get_scrobbles import lastfm_downloader
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()


    parser.add_argument('-username',
                        '-u',
                        help='Your last.fm username')


    parser.add_argument('-key',
                        '-k',
                        help='Your last.fm api_key')


    args = parser.parse_args()


    downloader = lastfm_downloader.LastfmDownloader()


    if args.username is not None:
        downloader.username = args.username

    if args.key is not None:
        downloader.key = args.key


    username = args.username
    key = args.key


    downloader.fetch_scrobbles(username, key)