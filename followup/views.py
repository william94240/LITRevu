from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, TemplateView
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse

from .models import UserFollow


"""
Definition of views classes for the followup.
"""


class UserFollowView(LoginRequiredMixin, CreateView):
    """View for the UserFollows List ."""
    model = UserFollow
    template_name = "followup/userfollow.html"
    fields = ["followed_user", ]

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("follow:follow")

    def get_context_data(self, **kwargs):
        """Affiche les utilisateurs suivis par l'utilisateur actuel."""
        context = super().get_context_data(**kwargs)
        # Récupérer les utilisateurs que vous suivez
        followed_users = UserFollow.objects.filter(user=self.request.user).exclude(followed_user=self.request.user)
        # Récupérer les utilisateurs qui vous suivent
        users_following = UserFollow.objects.filter(followed_user=self.request.user).exclude(user=self.request.user)

        context.update(
            {
                "followed_users": followed_users,
                "users_following": users_following,
            }
                    )
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        if form.instance.followed_user == form.instance.user:
            messages.error(self.request, "Vous ne pouvez pas vous suivre vous-même.")
            return self.form_invalid(form)
        if UserFollow.objects.filter(user=form.instance.user, followed_user=form.instance.followed_user).exists():
            messages.error(self.request, f"Vous suivez déjà {form.instance.followed_user}.")
            return self.form_invalid(form)
        return super().form_valid(form)


class UserUnfollowView(LoginRequiredMixin, DeleteView):
    """Permet à un utilisateur de ne plus suivre un autre utilisateur."""

    model = UserFollow
    template_name = "followup/userunfollow.html"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse("follow:follow")