from typing import TYPE_CHECKING
from SimpleDownloader import SimpleDownloader
from CachingDownloader import CachingDownloader

if TYPE_CHECKING:
    from Downloader import Downloader

def client_code(subject: Downloader) -> None:
    result = subject.download("http://example.com/")

    result = subject.download("http://example.com/")

if __name__ == "__main__":
    print("Executing client code with real subject:")
    real_subject = SimpleDownloader()
    client_code(real_subject)

    print("\n")

    print("Executing the same client code with a proxy:")
    proxy = CachingDownloader(real_subject)
    client_code(proxy)