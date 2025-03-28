from django.contrib import admin

from authentification.models import LitRevuUser


@admin.register(LitRevuUser)
class LitRevuUserAdmin(admin.ModelAdmin):
    """
    This class customizes the display in the Django admin interface for the LitRevu user model.    
  
    Attributs:
        list_display (tuple): defines the fields that will be displayed in the admin interface.
        search_fields (tuple): defines the fields that will be searchable in the admin interface. 
    """
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff"
        )
    # list_display = "__all__"
    list_display_links = ("username",)
    list_editable = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff",)       
    empty_value_display = "-vide-"
    list_per_page = 10