from django.urls import path
from .views import RegisterClass, LoginView


app_name = 'registration'

urlpatterns = [
    path('register/', RegisterClass.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login")
]