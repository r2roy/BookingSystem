# Generated by Django 5.0.3 on 2024-04-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_delete_contactinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=500)),
                ("phone", models.CharField(max_length=500)),
                ("email", models.CharField(max_length=500)),
                ("twitter", models.URLField(blank=True, max_length=100)),
                ("facebook", models.URLField(blank=True, max_length=100)),
                ("youtube", models.URLField(blank=True, max_length=100)),
                ("linkedin", models.URLField(blank=True, max_length=100)),
            ],
        ),
    ]