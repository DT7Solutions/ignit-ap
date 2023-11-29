# Generated by Django 4.1.2 on 2023-11-29 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_speakers_linkedin_url_alter_collaboration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 18, 37, 23, 171227)),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='eventtimer',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='panelist',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 18, 37, 23, 171227)),
        ),
    ]