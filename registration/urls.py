from django.urls import path
from .views import register, login


app_name = 'registration'

urlpatterns = [
    path('login-register/', register, name="register")
]