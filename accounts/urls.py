from django.urls import path

from accounts.views import UserLoginView, UserSignupView, UserDashboardView, UserLogoutView, UpdateUserView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('signup/', UserSignupView.as_view(), name="signup"),

    path('dashboard/', UserDashboardView.as_view(), name="dashboard"),
    path('settings/', UpdateUserView.as_view(), name="settings"),
]
