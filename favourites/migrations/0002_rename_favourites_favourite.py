# Generated by Django 3.2.4 on 2024-11-29 23:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favourites',
            new_name='Favourite',
        ),
    ]