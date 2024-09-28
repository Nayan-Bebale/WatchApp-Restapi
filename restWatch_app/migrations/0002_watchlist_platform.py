# Generated by Django 5.1.1 on 2024-09-26 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restWatch_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="restWatch_app.streamplatform",
            ),
            preserve_default=False,
        ),
    ]