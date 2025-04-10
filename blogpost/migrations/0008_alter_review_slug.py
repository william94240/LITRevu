# Generated by Django 5.1.2 on 2024-12-26 22:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0007_alter_review_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                editable=False,
                max_length=256,
                null=True,
                populate_from="headline",
                unique_with=["ticket_title", "headline"],
            ),
        ),
    ]
