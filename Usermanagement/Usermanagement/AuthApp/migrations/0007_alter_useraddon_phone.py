# Generated by Django 5.1.2 on 2024-12-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0006_alter_useraddon_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddon',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
