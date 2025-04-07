from django import forms

from .models import UserFollow, UserBlock


class UserFollowForm(forms.ModelForm):
    """
    ModelForm for creating or update a new UserFollows.
    """
    class Meta:
        model = UserFollow
        fields = ["user",
                  "followed_user",
                  ]
        # widgets = {
        #     "followed_user": forms.SelectMultiple(attrs={"size": 10}),
        # }


class UserBlockForm(forms.ModelForm):
    """
    ModelForm for creating or update a new UserBlocks.
    """
    class Meta:
        model = UserBlock
        fields = ["user", "blocked_user", ]
