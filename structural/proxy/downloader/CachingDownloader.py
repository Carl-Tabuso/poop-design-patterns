from Downloader import Downloader
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from SimpleDownloader import SimpleDownloader

class CachingDownloader(Downloader):
    __cache = {}

    def __init__(self, downloader: SimpleDownloader) -> None:
        self.__downloader = downloader

    def download(self, url: str) -> str:
        if url not in self.__cache:
            print("CacheProxy MISS.")
            result = self.__downloader.download(url)
            self.__cache[url] = result
        else:
            print("CacheProxy HIT. Retrieving result from cache.")

        return self.__cache[url]