# Generated by Django 4.0.5 on 2022-07-30 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_bio_account_profile_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_desc',
        ),
    ]
