# Generated by Django 3.2.4 on 2021-06-07 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blurb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blurb',
            options={'ordering': ('-edited',)},
        ),
    ]
