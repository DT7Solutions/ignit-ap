# Generated by Django 4.1 on 2023-11-29 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_rename_spackers_speakers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakers',
            name='linkedin_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 12, 14, 25, 712956)),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 12, 14, 25, 712956)),
        ),
    ]
