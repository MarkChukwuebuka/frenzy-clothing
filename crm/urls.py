from django.urls import path

from crm.views import HomeView, ContactView, AboutView

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('about/', AboutView.as_view(), name="about")
]
