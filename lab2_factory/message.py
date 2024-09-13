from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def post(self, text):
        pass


class FacebookMessage(Message):
    def post(self, text):
        print(f"Posting Facebook message: {text}")


class LinkedInMessage(Message):
    def post(self, text):
        print(f"Posting LinkedIn message: {text}")
