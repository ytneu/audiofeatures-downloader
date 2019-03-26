import argparse
import warnings
from get_audio_features.uris import uris_downloader
from get_audio_features.audio_features import audio_features_downloader

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
    features = audio_features_downloader.AudioFeatures()

    if args.spotify_key is not None:
        uris.spotify_key = args.spotify_key
        features.spotify_key = args.spotify_key

    if args.spotify_secret is not None:
        uris.spotify_secret = args.spotify_secret
        features.spotify_secret = args.spotify_secret

    spotify_key = args.spotify_key
    spotify_secret = args.spotify_secret


    uris.get_uris(spotify_key, spotify_secret)
    # features.save_features(spotify_key, spotify_secret)