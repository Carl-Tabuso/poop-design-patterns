from Server import Server
from ThrottlingMiddleware import ThrottlingMiddleware
from UserExistsMiddleware import UserExistsMiddleware
from RoleCheckMiddleware import RoleCheckMiddleware
    
if __name__ == "__main__":
    server = Server()
    server.register("admin@example.com", "admin_pass")
    server.register("user@example.com", "user_pass")

    middleware = ThrottlingMiddleware(2)
    middleware \
        .link_with(UserExistsMiddleware(server)) \
        .link_with(RoleCheckMiddleware())
    
    server.set_middleware(middleware)

    success = False
    while not success:
        email = input("\nEnter your email:")
        password = input("Enter your password:")
        
        success = server.log_in(email, password)