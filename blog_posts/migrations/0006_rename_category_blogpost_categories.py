# Generated by Django 4.0.4 on 2022-05-05 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0005_alter_blogpost_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='category',
            new_name='categories',
        ),
    ]
