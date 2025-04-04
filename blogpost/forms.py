from django import forms

from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    """
    ModelForm for creating or update a new Ticket.
    """
    class Meta:
        model = Ticket
        fields = ["title", "description", "image", ]
        help_texts = {
            "title": "Entrez le nom ici",
            "description": "Entrez la description ici",
        }


class ReviewForm(forms.ModelForm):
    """
    ModelForm for creating or update a new Review.
    """
    class Meta:
        model = Review
        fields = ["headline", "body", "rating", ]
        widgets = {
            "rating": forms.RadioSelect(choices=Review.RATING_CHOICES)
        }
        help_texts = {
            "headline": "Entrez la critique ici",
            "body": "Entrez le commentaire ici",
            "rating": "choisissez la note en nombre d'étoiles",
        }


class TicketCreateForm(forms.ModelForm):
    """Form for creating a new Ticket and review all in one."""
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')


class ReviewCreateForm(forms.ModelForm):
    """Form for creating a new Review and Ticket all in one."""
    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
