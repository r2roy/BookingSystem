# Generated by Django 5.0.3 on 2024-04-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_menu_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="logo",
            field=models.CharField(max_length=300),
        ),
    ]
