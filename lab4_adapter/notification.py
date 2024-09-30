from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, title:str, message:str):
        pass
