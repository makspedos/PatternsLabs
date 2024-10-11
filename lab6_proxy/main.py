from download import SimpleDownload
from cache import CacheDownload


if __name__ == '__main__':
    simple_download = SimpleDownload()
    cache_download = CacheDownload(simple_download)
    print(cache_download.download('test.txt'))
    print(cache_download.download('test2.txt'))
    print(cache_download.download('test2.txt'))
    print(cache_download.download('test.txt'))