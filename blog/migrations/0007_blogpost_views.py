# Generated by Django 4.0.5 on 2022-08-12 05:26

from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blogpost_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
