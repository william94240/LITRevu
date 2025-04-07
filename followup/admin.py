from django.contrib import admin

from .models import UserFollow, UserBlock


@admin.register(UserFollow)
class UserFollowAdmin(admin.ModelAdmin):
    """
    This class customizes the display in the Django admin interface for the UserFollows model.
    """
    list_display = (
        "user",
        "followed_user",
    )
    search_fields = ("user__username", "followed_user__username")
    list_filter = ("user", "followed_user")
    autocomplete_fields = ("user", "followed_user")
    list_editable = ("followed_user", )
    list_per_page = 10


@admin.register(UserBlock)
class UserBlockAdmin(admin.ModelAdmin):
    """
    This class customizes the display in the Django admin interface for the UserBlocks model.
    """
    list_display = (
        "user",
        "blocked_user",
    )
    list_display_links = ("user", )
    search_fields = ("user__username", "blocked_user__username")
    list_filter = ("user", "blocked_user")
    autocomplete_fields = ("user", "blocked_user")
    list_editable = ("blocked_user", )
    list_per_page = 10
