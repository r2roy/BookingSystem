from .views import *
from django.urls import path,include
from .import views



urlpatterns =[
    path("",HomeView.as_view(), name="home"),
    path("signup", signup, name="signup"),
    path("about", AboutView.as_view(), name="about"),
    path("booking", BookingView.as_view(), name="booking"),
    path("menu", MenuView.as_view(), name="menu"),
    path("service", ServiceView.as_view(), name="service"),
    path("team", TeamView.as_view(), name="team"),
    path("testimonial", TestimonialView.as_view(), name="testimonial"),
    path("contact", views.contact, name="contact"),
    path("sucess", views.sucess, name="sucess"),
    path("accounts/", include('django.contrib.auth.urls')),
]
