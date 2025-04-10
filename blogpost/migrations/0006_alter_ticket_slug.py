# Generated by Django 5.1.2 on 2024-12-26 21:46

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0005_alter_ticket_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                editable=False,
                max_length=256,
                null=True,
                populate_from="title",
                unique=True,
            ),
        ),
    ]
