from django.urls import path
from .views import contact, wishlist, signin

app_name = 'others'



urlpatterns = [
    path('', contact, name="contact"),
    path('wishlist/', wishlist, name="wishlist"),
    path('login-register/', signin, name="signin")
]