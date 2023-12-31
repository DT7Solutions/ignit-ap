# Generated by Django 4.2.7 on 2023-11-20 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_eventtimer_image_alter_studentideaform_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('Brand', models.CharField(max_length=100)),
                ('Industry', models.CharField(max_length=100)),
                ('Collaboration_Type', models.CharField(max_length=25)),
                ('Date', models.DateTimeField(default=datetime.datetime(2023, 11, 20, 16, 24, 13, 62537))),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 16, 24, 13, 62537)),
        ),
    ]
