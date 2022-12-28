from django.urls import path
from .views import register

app_name = 'accounts'


urlpatterns = [
    path('login-register/', register, name="register")
]