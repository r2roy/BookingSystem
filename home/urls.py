from .views import *
from django.urls import path,include



urlpatterns =[
    path("",HomeView.as_view(), name="home"),
    path("signup", signup, name="signup"),
    path("about", AboutView.as_view(), name="about"),
    path("booking", BookingView.as_view(), name="booking"),
    path("menu", MenuView.as_view(), name="menu"),
    path("service", ServiceView.as_view(), name="service"),
    path("team", TeamView.as_view(), name="team"),
    path("testimonial", TestimonialView.as_view(), name="testimonial"),
    path("contact", ContactView.as_view(), name="contact"),
    path("accounts/", include('django.contrib.auth.urls')),
]
