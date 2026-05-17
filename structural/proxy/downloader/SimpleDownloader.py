from Downloader import Downloader
from urllib.request import urlopen

class SimpleDownloader(Downloader):
    def download(self, url: str) -> str:
        print("Downloading a file from the Internet.")
        result = urlopen(url).read().decode()
        print(f"Downloaded bytes: {len(result)}")

        return result