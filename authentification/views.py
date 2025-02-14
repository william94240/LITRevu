from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.conf import settings

from .forms import CustomUserCreationForm



def signup_view(request):
    context = {}
    if request.method == "POST":
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #La redirection du LOGIN se fait à l'aide  
            # de la variable LOGIN_REDIRECT_URL = "home" 
            # dans le fichier SETTINGS.            
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            context["errors"] = form.errors

    form = CustomUserCreationForm()
    context["form"] = form

    return render(request, "authentification/signup.html", context=context)

def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def profile(request):
    return HttpResponse(f"Bienvenue {request.user.username}!")


