# Generated by Django 3.2.4 on 2021-06-07 01:00

from django.db import migrations, models
import django_countries.fields
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postal_code',
            field=localflavor.us.models.USPostalCodeField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=localflavor.us.models.USStateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
