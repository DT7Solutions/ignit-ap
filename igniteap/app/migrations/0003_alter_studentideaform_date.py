# Generated by Django 4.1 on 2023-11-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentideaform_delete_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
