# Generated by Django 3.2.6 on 2021-08-31 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_userprofile_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_admin',
        ),
    ]
