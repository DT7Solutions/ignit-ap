# Generated by Django 4.1.2 on 2023-11-20 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_eventtimer_image_alter_studentideaform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtimer',
            name='EventName',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 13, 24, 13, 803848)),
        ),
    ]
