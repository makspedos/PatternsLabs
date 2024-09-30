from notification import Notification

class EmailNotification(Notification):
    def __init__(self, admin_email:str):
        self.admin_email = admin_email
    def send(self, title:str, message:str):
        print(f"Email: {title} \nfrom: {self.admin_email}.\nmessage: {message}")