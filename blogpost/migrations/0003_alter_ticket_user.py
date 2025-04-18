# Generated by Django 5.1.2 on 2024-12-19 22:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0002_alter_ticket_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tikets",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Utilisateur",
            ),
        ),
    ]
