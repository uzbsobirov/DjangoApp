from django.urls import path
from .views import contact, wishlist, signin, checkout, about_us

app_name = 'others'



urlpatterns = [
    path('contact/', contact, name="contact"),
    path('wishlist/', wishlist, name="wishlist"),
    path('checkout/', checkout, name="checkout"),
    path('about-us/', about_us, name="about_us")
]