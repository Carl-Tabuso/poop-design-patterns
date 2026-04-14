class SlackApi:
    def __init__(self, account: str, api_key: str) -> None:
        self.__account = account
        self.__api_key = api_key

    def log_in(self) -> None:
        print(f"Logged in to slack account {self.__account}.")

    def send_message(self, chat_id: str, message: str) -> None:
        print(f"Posted following message into the {chat_id} chat: {message}.")