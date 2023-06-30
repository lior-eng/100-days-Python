import requests 
from twilio.rest import Client

account_sid  = ""
auth_token  = ""

class NotificationManager:
    
    def __init__(self) -> None:
        pass

    def send_sms(self, message_body: str) -> None:
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body= message_body,
                            from_= '+',
                            to= '+'
                        )
        print(message.status)
