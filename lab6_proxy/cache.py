from download import Download, SimpleDownload

class CacheDownload(Download):
    def __init__(self, simple_download:SimpleDownload):
        self.simple_download = simple_download
        self.cached_file = None

    def download(self, file:str)->str:
        if self.cached_file == file:
            return 'File already downloaded'
        else:
            self.cached_file = file
            return self.simple_download.download(self.cached_file)