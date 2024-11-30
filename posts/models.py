from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Post(models.Model):
    """
    Set a default image and a post model related to the owner
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_xcwblp', blank=True
    )
    country = CountryField(blank=False, null=True, default=None)  # Default to United States

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        """Override the clean method to add custom validation"""
        if not self.country:
            raise ValidationError({'country': 'Country field is required.'})

    def __str__(self):
        return f'{self.id} {self.title}'