from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView,
    )

from authentification.views import SignupView, logout_view


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="authentification/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="authentification/logout"), name="logout"),
    path("logout-fct/", logout_view, name="logout_fct"),
        ]
