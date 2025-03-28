from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate

from authentification.models import LitRevuUser


class SignupForm(UserCreationForm):
    """Form for signup."""
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name")
