from storage import LocalStorage, AmazonS3


class StorageSelect:
    def set_storage(self, storage_type):
        if storage_type == 'local':
            print("Connected to local storage")
            return LocalStorage()
        elif storage_type == 'amazon':
            print("Connected to amazon")
            return AmazonS3()
        else:
            return "Error to choose storage type"
