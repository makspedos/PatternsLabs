from notification import Notification

class SMSNotification():
    def __init__(self, phone_number:str, sender:str):
        self.phone_number = phone_number
        self.sender = sender

    def sms_sender(self, message:str):
        print(f"Title: {message}\nTo: {self.phone_number}\nFrom: {self.sender}")

class SMSAdapter(Notification):
    def __init__(self, sms_notification:SMSNotification):
        self.sms_notification = sms_notification

    def send(self, title:str, message:str):
        message = f"{title}: {message}"
        self.sms_notification.sms_sender(message)