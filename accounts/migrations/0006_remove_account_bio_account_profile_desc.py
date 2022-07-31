# Generated by Django 4.0.5 on 2022-07-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='bio',
        ),
        migrations.AddField(
            model_name='account',
            name='profile_desc',
            field=models.CharField(default='...', max_length=300),
        ),
    ]
