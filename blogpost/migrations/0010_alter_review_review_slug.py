# Generated by Django 5.1.2 on 2024-12-27 10:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0009_rename_slug_review_review_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="review_slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                editable=False,
                max_length=256,
                null=True,
                populate_from="headline",
                unique=True,
            ),
        ),
    ]
