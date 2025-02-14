from django.contrib import admin

from .models import Ticket, Review

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    This class customizes the display in the Django admin interface for the Ticket model.
    """
    list_display = (
        "title",
        "user",
        "slug",
        "time_created"        
    )
    # list_display = "__all__"
    empty_value_display = "-vide-"
    list_display_links = ("title", )
    # list_editable = ("time_created", )
    search_fields = ("title", "user__username", "time_created")
    list_filter = ("user", )
    autocomplete_fields = ("user", )
    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    This class customizes the display in the Django admin interface for the Review model.
    """
    list_display = (
        "headline",
        "ticket",
        "slug",
        "user",
        "rating",
        "time_created"
    )
    # list_display = "__all__"
    empty_value_display = "-vide-"
    list_display_links = ("headline", )
    list_editable = ("rating",)
    search_fields = ("headline", "ticket__title", "user__username", "rating")
    list_filter = ("time_created", "user", "rating", "ticket")
    autocomplete_fields = ("ticket", "user", )
    list_per_page = 10
    
