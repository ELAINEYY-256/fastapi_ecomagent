from app.services.user_service import UserService

class UserController:

    @staticmethod
    def register_user(name: str, email: str, password: str, role: str):
        return UserService.register_user(name, email, password, role)

    @staticmethod
    def login_user(email: str, password: str):
        return UserService.login_user(email, password)
