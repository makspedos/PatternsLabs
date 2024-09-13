from abstractmedia import SocialMedia
from message import FacebookMessage, LinkedInMessage

class FacebookConnection(SocialMedia):
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.connect()

    def connect(self):
        print(f"Connected to Facebook. Hello {self.login}")

    def create_message(self) -> FacebookMessage:
        return FacebookMessage()


class LinkedInConnection(SocialMedia):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.connect()

    def connect(self):
        print(f"Connected to LinkedIn. Hello {self.email}")

    def create_message(self) -> LinkedInMessage:
        return LinkedInMessage()
