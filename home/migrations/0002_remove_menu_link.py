# Generated by Django 5.0.3 on 2024-04-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="link",
        ),
    ]
