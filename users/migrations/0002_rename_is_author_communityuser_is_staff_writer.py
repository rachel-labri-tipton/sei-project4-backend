# Generated by Django 4.0.4 on 2022-05-08 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communityuser',
            old_name='is_author',
            new_name='is_staff_writer',
        ),
    ]