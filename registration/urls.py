from django.urls import path
from .views import RegisterClass, login


app_name = 'registration'

urlpatterns = [
    path('login-register/', RegisterClass.as_view(), name="register")
]