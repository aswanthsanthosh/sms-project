# Generated by Django 5.1.3 on 2024-12-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsystem_app', '0004_housedetails_seller_bookingrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
