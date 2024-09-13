from manager import StorageSelect

class User:
    def __init__(self, username:str):
        self.username = username
        self.storage = None

    def select_storage(self, storage_type):
        selected_storage = StorageSelect()
        self.storage = selected_storage.set_storage(storage_type)

