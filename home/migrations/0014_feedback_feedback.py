# Generated by Django 5.0.3 on 2024-04-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_remove_contactinfo_instagram_remove_feedback_comment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="feedback",
            field=models.TextField(blank=True),
        ),
    ]
