from django.contrib.auth.models import AbstractUser


class LitRevuUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    """
    class Meta:
        """Meta class for the LitRevuUser model."""
        verbose_name = "Utilisateur de LITRevu"
        verbose_name_plural = "Utilisateurs de LITRevu"
        
        
    def __str__(self):
        """Return the username of the user."""
        return self.username
 