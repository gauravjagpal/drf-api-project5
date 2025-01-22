from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Trip(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    country = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_s10tik'
    )
    activities = models.JSONField(blank=True, default=list)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s trip"
    
def create_trip(sender, instance, created, **kwargs):
    if created:
        Trip.objects.create(owner=instance)
    

post_save.connect(create_trip, sender=User)