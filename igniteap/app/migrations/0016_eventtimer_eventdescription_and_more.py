# Generated by Django 4.1.2 on 2023-11-20 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_studentideaform_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtimer',
            name='Eventdescription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='eventtimer',
            name='EventName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 13, 29, 19, 703122)),
        ),
    ]