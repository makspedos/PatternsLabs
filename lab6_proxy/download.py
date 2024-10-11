from abc import ABC, abstractmethod

class Download(ABC):
    @abstractmethod
    def download(self, file:str)->str:
        pass


class SimpleDownload(Download):
    def download(self, file:str)->str:
        return f'File {file} was downloaded successfully'


