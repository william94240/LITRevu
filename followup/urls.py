from django.urls import path
from django.conf import settings


from .views import UserFollowView, UserUnfollowView



urlpatterns = [
    path("", UserFollowView.as_view(), name="follow"),
    path("<int:pk>/unfollow/", UserUnfollowView.as_view(), name="unfollow"),
]