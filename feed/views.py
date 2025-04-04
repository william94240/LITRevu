from itertools import chain
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blogpost.models import Ticket, Review
from followup.models import UserFollow


class TheFeedPageView(LoginRequiredMixin, TemplateView):
    """The feed page view."""
    template_name = 'feed/feed.html'

    def get_context_data(self, **kwargs):
        followed_users = UserFollow.objects.filter(user=self.request.user).exclude(followed_user=self.request.user)
        followed_users = followed_users.values_list('followed_user', flat=True)
        posts = chain(
            self.request.user.tickets.all(),
            self.request.user.reviews.all(),
            Ticket.objects.filter(user__in=followed_users),
            Review.objects.filter(user__in=followed_users)
            )
        kwargs['posts'] = sorted(
            posts,
            key=lambda post: post.time_created,
            reverse=True
            )
        return super().get_context_data(**kwargs)


class MyFeedPageView(LoginRequiredMixin, TemplateView):
    template_name = 'feed/my_feed.html'

    def get_context_data(self, **kwargs):
        posts = chain(self.request.user.tickets.all(), self.request.user.reviews.all())
        kwargs['posts'] = sorted(
            posts,
            key=lambda post: post.time_created,
            reverse=True
            )
        return super().get_context_data(**kwargs)

