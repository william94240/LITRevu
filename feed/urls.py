from django.urls import path

from .views import TheFeedPageView, MyFeedPageView


urlpatterns = [
    path("",TheFeedPageView.as_view(), name="feed"),
    path("my-feed/", MyFeedPageView.as_view(), name="my-feed"),
               ]