# Generated by Django 3.2.4 on 2021-06-09 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_userprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
    ]
