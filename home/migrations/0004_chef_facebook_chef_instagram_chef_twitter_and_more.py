# Generated by Django 5.0.3 on 2024-04-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_services_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="chef",
            name="facebook",
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="chef",
            name="instagram",
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="chef",
            name="twitter",
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="menu",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]