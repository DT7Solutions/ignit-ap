# Generated by Django 4.1.2 on 2023-11-17 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_agendaday_event_alter_studentideaform_date_panelist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 17, 32, 15, 756676)),
        ),
    ]
