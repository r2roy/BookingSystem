from .views  import *
from django.urls import path,include


urlpatterns =[
    path("",HomeView.as_view(), name="home"),
    path("signup", signup, name="signup"),
    path("accounts/", include('django.contrib.auth.urls')),
]
