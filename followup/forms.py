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



# class TicketForm(forms.ModelForm):
#     """
#     Form for creating a new Ticket.
#     """
#     class Meta:
#         model = Ticket
#         fields = ["title", "description", "image", ]        


# class ReviewForm(forms.ModelForm):
#     """
#     Form for creating a new Review.
#     """
#     class Meta:
#         model = Review
#         fields = ["headline", "body", "rating", ]
#         widgets = {
#             "rating": forms.RadioSelect(choices=Review.RATING_CHOICES)
#         }


# class TicketCreateForm(forms.ModelForm):
#     """Form for creating a new Ticket and review all in one."""
#     class Meta:
#         model = Ticket
#         fields = ('title', 'description', 'image')
        


# class ReviewCreateForm(forms.ModelForm):
#     """Form for creating a new Review and Ticket all in one."""
#     class Meta:
#         model = Review
#         fields = ('headline', 'rating', 'body')    
