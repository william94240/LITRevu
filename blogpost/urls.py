from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    TicketlistView, TikectDetailView, TicketCreateView, TicketUpdateView,
    TicketDeleteView, ReviewlistView, ReviewDetailView, ReviewCreateView,
    ReviewUpdateView, ReviewDeleteView, TicketReviewCreateAIOView
    )


urlpatterns = [
    path("tickets/", TicketlistView.as_view(), name="ticket-list"),
    path("tickets/create/", TicketCreateView.as_view(), name="ticket-create"),
    path("tickets/create-aio/", TicketReviewCreateAIOView.as_view(), name="ticket-create-aio"),
    path("tickets/<slug:slug>/", TikectDetailView.as_view(), name="ticket-detail"),    
    path("tickets/<slug:slug>/update/", TicketUpdateView.as_view(), name="ticket-update"),    
    path("tickets/<slug:slug>/delete/", TicketDeleteView.as_view(), name="ticket-delete"),
    path("tickets/<slug:ticket_slug>/reviews/", ReviewlistView.as_view(), name="ticket-review-list"),
    path("tickets/<slug:ticket_slug>/reviews/create/", ReviewCreateView.as_view(), name="ticket-review-create"),    
    path("tickets/<slug:ticket_slug>/reviews/<slug:slug>/", ReviewDetailView.as_view(), name="ticket-review-detail"),
    path("tickets/<slug:ticket_slug>/reviews/<slug:slug>/update/", ReviewUpdateView.as_view(), name="ticket-review-update"),
    path("tickets/<slug:ticket_slug>/reviews/<slug:slug>/delete/", ReviewDeleteView.as_view(), name="ticket-review-delete"),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) if settings.DEBUG else None