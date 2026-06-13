from UserRepository import UserRepository   
from Logger import Logger
from OnboardingNotification import OnboardingNotification
import os

if __name__ == "__main__":
    repository = UserRepository()
    repository.attach(Logger(os.path.abspath("log.txt")), "*")
    repository.attach(OnboardingNotification("1@example.com"), "users:created")

    repository.initialize(os.path.abspath("users.csv"))

    user = repository.create_user({
        "name": "John Smith",
        "email": "john99@example.com",
    })

    repository.delete_user(user)
