# Generated by Django 4.0.4 on 2022-05-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0002_remove_blogpost_article_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=250, null=True),
        ),
    ]
