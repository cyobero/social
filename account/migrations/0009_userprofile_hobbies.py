# Generated by Django 3.2.4 on 2021-06-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210612_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hobbies',
            field=models.TextField(blank=True, null=True),
        ),
    ]
