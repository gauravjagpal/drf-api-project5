# Generated by Django 3.2.4 on 2024-11-30 11:41

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20241130_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='country',
            field=django_countries.fields.CountryField(default=None, max_length=2, null=True),
        ),
    ]
