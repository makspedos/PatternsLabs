class AbstractStorage:
    def upload(self, file_name:str, saved_path:str)->str:
        pass

    def download(self, file_path: str)->str:
        pass

    def delete(self, file_path: str)->str:
        pass