# Generated by Django 4.1 on 2023-11-16 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_studentideaform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 16, 12, 29, 44, 164591)),
        ),
    ]
