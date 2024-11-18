from django.contrib.auth import authenticate, login, logout

from accounts.services.user_service import UserService
from services.util import CustomRequestUtil


class AuthService(CustomRequestUtil):
    def login(self, payload):
        email = payload.get("email")
        password = payload.get("password")

        user = authenticate(self.request, email=email, password=password)

        if not user:
            return None, self.make_error("Email/Password is not correct!")

        login(self.request, user)

        message = "Login successful"

        return message, None

    def signup(self, payload):

        user, error = UserService(self.request).create_single(payload)
        if error:
            return None, error

        message = "Your signup was successful"

        return message, None

    def logout(self):

        logout(self.request)
        message = "Logout successful"

        return message, None
