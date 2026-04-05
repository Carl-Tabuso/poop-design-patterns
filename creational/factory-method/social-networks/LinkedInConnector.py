from SocialNetworkConnector import SocialNetworkConnector

class LinkedInConnector(SocialNetworkConnector):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def log_in(self) -> None:
        print(f"Send HTTP API request to log in user {self.email} with password {self.password}")

    def log_out(self) -> None:
        print(f"Send HTTP API request to log out user {self.email}")

    def create_post(self, content: str) -> None:
        print(f"Send HTTP API requests to create a post in LinkedIn timeline.\nContent: {content}")

    def name(self) -> str:
        return "LinkedIn"