# Generated by Django 3.2.4 on 2024-11-30 11:28

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_filter',
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=django_countries.fields.CountryField(default='US', max_length=2),
        ),
    ]
