import unittest

from get_scrobbles.lastfm_downloader import LastfmDownloader

class TestLastfmDownloader(unittest.TestCase):
    downloader = None

    def setUp(self):
        self.downloader = LastfmDownloader()

    def test_init_defaults(self):
        self.assertIsNone(self.downloader)

    def test_download_with_no_keyword(self):
        '''Attempt to download images with no keyword should raise exception'''
        try:
            self.downloader.fetch_scrobbles("")
        except Exception as e:
            pass
        else:
            self.fail('it should have raise an exception')


if __name__ == '__main__':
    unittest.main()

