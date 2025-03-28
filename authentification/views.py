from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .forms import SignupForm


class SignupView(View):
    """View for signup."""    
    template_name = "authentification/signup.html"
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):        
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, {"form": form})



def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
