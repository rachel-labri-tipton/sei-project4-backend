# Generated by Django 4.0.4 on 2022-05-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0011_alter_blogpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.URLField(max_length=250),
        ),
    ]
