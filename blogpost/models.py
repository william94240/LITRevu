from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.shortcuts import redirect
from PIL import Image
from django import forms


# Create your models here.

class Ticket(models.Model):
    """
    This class represents the Ticket model.

    Attributes:
    title: CharField
    description: TextField
    user: ForeignKey
    image: ImageField
    time_created: DateTimeField

    Methods:
        __str__(): Returns a string representation of the ticket, 
        displaying its title. 
    """
    title = models.CharField(max_length=128, verbose_name="Nom du livre ou de l'article")
    slug = AutoSlugField(unique=True, populate_from="title", max_length=256, blank=True, null=True)
    description = models.TextField(
        max_length=2048, blank=True, verbose_name="Description du livre ou de l'article")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tikets",
        verbose_name="Utilisateur",
        null=True
        )
    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de la demande de la critique sur un livre/article"
        )
    image = models.ImageField(
        null=True, blank=True,
        upload_to='ticket_images/',             
        verbose_name="Image du livre/article",        
        default="ticket_images/django.png",        
        )
    

    class Meta:
        verbose_name = "Livre ou Article"        
        ordering = ["-time_created"]

    def __str__(self):
        """Return the title of the Tiket."""
        return self.title
    
    def save(self, *args, **kwargs):
        """Override the save original method to automatically generate a slug"""
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Return the absolute url of the ticket"""
        # return reverse("ticket", kwargs={"pk": self.pk})    
        return reverse("flux:ticket-detail", kwargs={"slug": self.slug})
        

  


class Review(models.Model):
    """
    Represents a review associated with a ticket, including rating, user...

    Attributes:
        ticket: ForeignKey
        rating: PositiveSmallIntegerField (0 to 5).
        user: ForeignKey
        headline: CharField
        body: TextField
        time_created: DateTimeField

    Methods:
        __str__(): Returns a string representation of the review, indicating the associated ticket and user.
    """
    RATING_CHOICES = [
        (0, '☆☆☆☆☆'),
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),        
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ] 

    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name="reviews")
    # validates rating must be between 0 and 5
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note sur 5 étoiles",
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    headline = models.CharField(max_length=128, verbose_name="En-tête de la critique")    
    slug = AutoSlugField(populate_from="headline", unique=True, max_length=256, blank=True, null=True)
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaires ")
    time_created =models.DateTimeField(auto_now_add=True, verbose_name="Date de publication de la critique")

    class Meta:
        verbose_name = "Critique"
        ordering = ["-time_created"]
       

    def __str__(self):
        """Return a string representation of the review."""
        return f'Critique "{self.headline}" pour "{self.ticket.title}"'
    
    def save(self, *args, **kwargs):
        """Override the save method to automatically generate a slug"""
        if not self.slug:
            # self.slug = slugify(self.headline + "-" + self.ticket.title)
            self.slug = slugify(self.headline)

        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Return the absolute url of the review"""
        return reverse("flux:ticket-review-detail", kwargs={"ticket_slug": self.ticket.slug, "slug": self.slug})