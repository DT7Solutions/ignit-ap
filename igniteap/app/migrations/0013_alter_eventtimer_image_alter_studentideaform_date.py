# Generated by Django 4.1.2 on 2023-11-20 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_eventtimer_upload_url_eventtimer_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtimer',
            name='image',
            field=models.ImageField(upload_to='event_banners/'),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 11, 12, 28, 889124)),
        ),
    ]