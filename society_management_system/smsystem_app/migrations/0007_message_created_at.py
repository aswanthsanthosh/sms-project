# Generated by Django 5.1.3 on 2024-12-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsystem_app', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
