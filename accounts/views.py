from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from accounts.services.auth_service import AuthService
from accounts.services.user_service import UserService
from services.util import CustomRequestUtil


class UserLoginView(View, CustomRequestUtil):
    template_name = 'login.html'
    extra_context_data = {
        "title": "Sign In",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        auth_service = AuthService(self.request)

        self.template_name = None
        self.template_on_error = 'login.html'

        payload = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        }

        next_url = request.POST.get('next', request.GET.get('next', '/'))

        return self.process_request(
            request, target_view=next_url, target_function=auth_service.login, payload=payload
        )


class UserSignupView(View, CustomRequestUtil):
    template_name = 'signup.html'
    extra_context_data = {
        "title": "Sign Up",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        auth_service = AuthService(self.request)
        self.template_name = None
        self.template_on_error = 'signup.html'

        payload = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'first_name': request.POST.get('first-name'),
            'last_name': request.POST.get('last-name'),
        }

        return self.process_request(
            request, target_view="login", target_function=auth_service.signup, payload=payload
        )


class UserDashboardView(View, CustomRequestUtil):
    template_name = 'dashboard.html'
    extra_context_data = {
        "title": "Dashboard",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)




class UpdateUserView(LoginRequiredMixin, View, CustomRequestUtil):
    template_name = 'settings.html'
    extra_context_data = {
        "title": "Settings",
    }

    def get(self, request, *args, **kwargs):
        return self.process_request(request)

    def post(self, request, *args, **kwargs):
        user_service = UserService(self.request)
        self.template_name = None
        self.template_on_error = 'settings.html'

        payload = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'phone': request.POST.get('phone'),
            'current_password': request.POST.get('current_password'),
            'new_password': request.POST.get('new_password'),
            'confirm_password': request.POST.get('confirm_password')
        }

        return self.process_request(
            request, target_view="dashboard", target_function=user_service.update_single, payload=payload
        )

class UserLogoutView(View, CustomRequestUtil):

    def get(self, request, *args, **kwargs):
        auth_service = AuthService(self.request)

        return self.process_request(
            request, target_function=auth_service.logout, target_view="home"
        )
