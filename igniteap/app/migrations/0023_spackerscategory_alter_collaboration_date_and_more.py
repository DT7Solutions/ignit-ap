# Generated by Django 4.1.2 on 2023-11-24 13:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_approved_event_activeevent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='spackersCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 19, 13, 10, 309191)),
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 24, 19, 13, 10, 309191)),
        ),
        migrations.CreateModel(
            name='spackers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('companeyName', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='panelist_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.spackerscategory')),
            ],
        ),
    ]
