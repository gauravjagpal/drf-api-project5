# Generated by Django 3.2.4 on 2025-02-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_auto_20250128_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip',
            field=models.CharField(max_length=255),
        ),
    ]
