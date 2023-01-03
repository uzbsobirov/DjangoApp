from django.urls import path
from .views import RegisterClass, LoginClass


app_name = 'registration'

urlpatterns = [
    path('register/', RegisterClass.as_view(), name="register"),
    path('login/', LoginClass.as_view(), name="login")
]