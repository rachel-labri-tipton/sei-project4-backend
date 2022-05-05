# Generated by Django 4.0.4 on 2022-05-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_categories', '0001_initial'),
        ('blog_posts', '0003_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='article_categories', to='blog_categories.category'),
        ),
    ]
