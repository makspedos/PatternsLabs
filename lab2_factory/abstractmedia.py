from abc import ABC, abstractmethod

class SocialMedia(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create_message(self, text):
        pass
