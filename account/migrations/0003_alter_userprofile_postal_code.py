# Generated by Django 3.2.4 on 2021-06-07 12:36

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210606_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='postal_code',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10, null=True),
        ),
    ]
