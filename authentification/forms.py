from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from authentification.models import LitRevuUser

class CustomUserCreationForm(UserCreationForm):
    """Customizes UserCreationForm with definition of model et display fields."""
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")