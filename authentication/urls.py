# -*- encoding: utf-8 -*-


from django.urls import path
from .views import login_view, register_user, user_logout, home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", user_logout, name="logout"),
    path("home/", home, name="home"),
]
