# Generated by Django 5.1.2 on 2024-12-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0004_alter_email_temporary_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_temporary',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
