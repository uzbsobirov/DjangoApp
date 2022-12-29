from django.urls import path
from .views import RegisterClass, login_request


app_name = 'registration'

urlpatterns = [
    path('register/', RegisterClass.as_view(), name="register"),
    path('login/', login_request, name="login")
]