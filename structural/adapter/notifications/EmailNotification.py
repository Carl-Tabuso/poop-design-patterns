from Notification import Notification
import re

class EmailNotification(Notification):
    def __init__(self, email: str) -> None:
        self.__email = email

    def send(self, title: str, message: str) -> None:
        # do email stuff here...
        safe_message = re.sub(r"<.*?>", "", message)
        print(f"Sent email with title '{title}' to '{self.__email}' that says '{safe_message}'.")