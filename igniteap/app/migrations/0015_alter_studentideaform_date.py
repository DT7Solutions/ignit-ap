# Generated by Django 4.1.2 on 2023-11-20 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_eventtimer_eventname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 13, 25, 5, 99680)),
        ),
    ]
