# Generated by Django 4.0.2 on 2022-02-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
    ]
