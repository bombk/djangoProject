# Generated by Django 4.0.2 on 2022-02-19 08:15

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_news_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True),
        ),
    ]
