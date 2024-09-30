from email_notification import EmailNotification
from slack_notification import SlackAdapter, SlackNotification
from sms_notification import SMSAdapter, SMSNotification

if __name__ == '__main__':
    email_notification = EmailNotification(admin_email="testuser@gmail.com")
    email_notification.send(title="Welcome", message="Hello, User")

    print('\n')
    slack_notification = SlackNotification(login="testuser", apiKey="ekkqwjdsqk", chat_id="id21132")
    stack_adapter = SlackAdapter(slack_notification)
    stack_adapter.send(title="Welcome", message="hello")

    print('\n')
    sms_notification = SMSNotification(phone_number='+380501234567', sender="TestUser")
    sms_adapter = SMSAdapter(sms_notification)
    sms_adapter.send(title="Welcome", message="Hello")

