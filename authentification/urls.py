from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from authentification.views import signup_view, logout_view


urlpatterns = [    
    path("signup/", signup_view, name="signup"),
    path("login/", LoginView.as_view(template_name="authentification/login.html"), name="login"),
    # path("logout/", LogoutView.as_view(template_name="authentification/logout"), name="logout"),
    path("logout/", logout_view, name="logout"),
    path("", include("django.contrib.auth.urls"), name="auth_home"),   
]