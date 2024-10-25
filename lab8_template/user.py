from template import Template

class User(Template):
    def __init__(self, email:str, username:str, password:str):
        self.email = email
        self.username = username
        self.password = password


    def query_to_save(self, data:dict):
        if data['email']:
            del data['email']
        super().query_to_save(data)


    def before_save_hook(self):
        print(f'Before saving: User email: {self.email}, username: {self.username}')

    def after_save_hook(self):
        print(f'After saving: User email: {self.email}, username: {self.username}')




