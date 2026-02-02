from django.urls import path

from .views import register, login

urlpatterns = [
    path("register/", register, name="auth-register"),
    path("login/", login, name="auth-login"),
]
