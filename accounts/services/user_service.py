from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from email_validator import validate_email

from accounts.models import User
from services.util import CustomRequestUtil, compare_password


class UserService(CustomRequestUtil):
    def create_single(self, payload):
        """Payload requirements:
        {
        email: String,
        password: String,
        first_name: String,
        last_name: String
        }
        """

        email = payload.get("email")
        password = payload.get("password")
        password2 = payload.get("password2")
        first_name = payload.get("first_name", None)
        last_name = payload.get("last_name", None)

        try:
            email_info = validate_email(email, check_deliverability=True)
            email = email_info.normalized
        except Exception as e:
            return None, self.make_error("Please enter a valid email address")

        existing_user, _ = self.find_user_by_email(email)
        if existing_user:
            return None, self.make_error("User with email already exist")

        if password != password2:
            return None, self.make_error("Password mismatch")

        user, is_created = User.objects.get_or_create(
            email=email,
            defaults=dict(
                last_name=last_name,
                first_name=first_name,
                password=make_password(password)
            )
        )

        if not is_created:
            return None, self.make_error("User already exist")

        return user, None

    def find_user_by_email(self, email):
        user = User.objects.prefetch_related("roles").filter(email__iexact=email).first()
        if not user:
            return None, self.make_error(f"User with email '{email}' not found")

        return user, None

    def update_single(self, payload):
        user = self.auth_user
        user.first_name = payload.get('first_name', user.first_name)
        user.last_name = payload.get('last_name', user.last_name)
        user.phone_number = payload.get('phone', user.phone_number)

        current_password = payload.get('current_password')
        new_password = payload.get('new_password')
        confirm_password = payload.get('confirm_password')

        if current_password:

            if new_password != confirm_password:
                return None, self.make_error("Password Mismatch")

            if not compare_password(current_password, user.password):
                return None, self.make_error("Access denied, invalid password.")

            user.set_password(payload.get("new_password"))
            user.save()

            login(self.request, user)

        message = "Your profile was updated"

        return message, None

