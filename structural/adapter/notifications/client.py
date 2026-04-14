from typing import TYPE_CHECKING
from EmailNotification import EmailNotification
from SlackApi import SlackApi
from SlackNotification import SlackNotification

if TYPE_CHECKING:
    from Notification import Notification

def send_notification(notification: Notification) -> None:
    notification.send(
        "Website is down!",
        "<strong style='color:red;font-size: 50px;'>Alert!</strong> " +
        "Our website is not responding. Call admins and bring it up!"
    )

if __name__ == '__main__':
    print("Client code is designed correctly and works with email notifications:")
    notification = EmailNotification("developers@example.com")
    send_notification(notification)

    print("\n")

    print("The same client code can work with other classes via adapter:")
    slack_api = SlackApi("example.com", "XXXXXXXX")
    notification = SlackNotification(slack_api, "Example.com Developers")
    send_notification(notification)