# Generated by Django 4.1.4 on 2022-12-26 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
