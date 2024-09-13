from singleton import Singleton
from abstractstorage import AbstractStorage


class LocalStorage(AbstractStorage, metaclass=Singleton):
    def upload(self, file_name: str, saved_path: str) -> str:
        print(f"Uploading {file_name} to {saved_path} in local storage")
        return "File uploaded"

    def download(self, file_path: str) -> str:
        print(f"Downloading file from {file_path} in local storage")
        return "File downloaded"

    def delete(self, file_path: str) -> str:
        print(f"Deleting file from {file_path} in local storage")
        return "File deleted"


class AmazonS3(AbstractStorage, metaclass=Singleton):
    def upload(self, file_name: str, saved_path: str) -> str:
        print(f"Uploading {file_name} to {saved_path} in Amazon S3")
        return "File uploaded to S3"

    def download(self, file_path: str) -> str:
        print(f"Downloading file from {file_path} in Amazon S3")
        return "File downloaded from S3"

    def delete(self, file_path: str) -> str:
        print(f"Deleting file from {file_path} in Amazon S3")
        return "File deleted from S3"
