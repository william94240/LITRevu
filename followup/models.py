from django.db import models
from django.conf import settings


class UserFollow(models.Model):
    """UserFollows model represents the relationship between users when one user follows another.

    Attributes:
        user (ForeignKey): The user who follows another user.
        followed_user (ForeignKey): The user who is being followed.
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followings",
        verbose_name="Utilisateur suiveur",
        )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
        verbose_name="Utilisateur suivi"
        )

    class Meta:
        """Meta class for the UserFollows model."""
        # ensures we don't get multiple UserFollows instances
        # for unique (user, user_followed) pairs
        unique_together = ("user", "followed_user", )

        verbose_name = "Relation de suivi"
        verbose_name_plural = "Relations de suivi"

    def __str__(self):
        """Return a string representation of the UserFollows instance"""
        return f"{self.user} follows {self.followed_user}"

    def unfollow(self):
        """Ends the tracking relationship between users."""
        self.delete()

    @classmethod
    def is_following(cls, user, followed_user):
        """Checks if a user follows another user."""
        return cls.objects.filter(user=user, followed_user=followed_user).exists()

    # def get_absolute_url(self):
    #     """Return the absolute url of the ticket"""
    #     # return reverse("ticket", kwargs={"pk": self.pk})
    #     return reverse("flux:ticket-detail", kwargs={"slug": self.slug})


class UserBlock(models.Model):
    """Model for user blocking relationship.

    Attributes:
        user (ForeignKey): The user who is blocking another user.
        blocked_user (ForeignKey): The user who is being blocked.
    """

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="blocking",
        on_delete=models.CASCADE,
        verbose_name="Utilisateur bloquant"
        )
    blocked_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="blocked_by",
        on_delete=models.CASCADE,
        verbose_name="Utilisateur bloqué"
        )

    class Meta:
        """Meta class for the UserBlocks model."""
        unique_together = (
            "user",
            "blocked_user",
        )
        verbose_name = "Relation de blocage"
        verbose_name_plural = "Relations de blocage"

    def __str__(self):
        """Return a string representation of the UserBlocks instance."""
        return f"{self.user} blocks {self.blocked_user}"