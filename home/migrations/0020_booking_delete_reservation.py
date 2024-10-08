# Generated by Django 5.0.3 on 2024-08-06 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_reservation_delete_booking"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("date", models.DateTimeField()),
                ("number_of_people", models.IntegerField()),
                ("special_request", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Reservation",
        ),
    ]
