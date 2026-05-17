from Middleware import Middleware

class RoleCheckMiddleware(Middleware):
    def check(self, email: str, password: str) -> bool:
        if email == "admin@example.com":
            print("RoleCheckMiddleware: Hello, admin!")

            return True
        
        print("RoleCheckMiddleware: Hello, user!")

        return super().check(email, password)