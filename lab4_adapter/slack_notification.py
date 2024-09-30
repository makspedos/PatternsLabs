from notification import Notification


class SlackNotification():
    def __init__(self, login:str, apiKey:str, chat_id:str):
        self.login = login
        self.apiKey = apiKey
        self.chat_id = chat_id

    def slack_sender(self, message:str):
        print(f'Chat:{self.chat_id}\t {message}')


class SlackAdapter(Notification):
    def __init__(self, slack_notification:SlackNotification):
        self.slack_notification = slack_notification

    def send(self, title:str, message:str):
        result_message = f"{title}: {message}"
        self.slack_notification.slack_sender(message=result_message)