# Generated by Django 4.1.2 on 2023-11-24 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_spackerscategory_alter_collaboration_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='spackers',
            new_name='Speakers',
        ),
        migrations.RenameModel(
            old_name='spackersCategory',
            new_name='SpeakersCategory',
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 19, 16, 2, 836194)),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 19, 16, 2, 820564)),
        ),
    ]
