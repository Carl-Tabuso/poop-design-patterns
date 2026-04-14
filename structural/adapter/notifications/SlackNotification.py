from typing import TYPE_CHECKING
from Notification import Notification
import re

if TYPE_CHECKING:
    from SlackApi import SlackApi

class SlackNotification(Notification):
    def __init__(self, slack: SlackApi, chat_id: str) -> None:
        self.__slack = slack
        self.__chat_id = chat_id

    def send(self, title: str, message: str) -> None:
        safe_message = re.sub(r"<.*?>", "", message)
        slack_message = f"#{title} # {safe_message}"

        self.__slack.log_in()

        self.__slack.send_message(self.__chat_id, slack_message)