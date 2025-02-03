from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.


class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trip = models.CharField(max_length=255)
    country = CountryField(blank=False, null=True, default=None)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_s10tik'
    )
    activities = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        country_display = self.get_country_display()
        return f"{self.owner.username}'s trip to {country_display}"


def create_trip(sender, instance, created, **kwargs):
    if created:
        Trip.objects.create(owner=instance)


post_save.connect(create_trip, sender=User)
