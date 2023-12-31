# Generated by Django 4.1.2 on 2023-11-17 11:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_studentideaform_approved_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='studentideaform',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 17, 17, 24, 50, 275212)),
        ),
        migrations.CreateModel(
            name='Panelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='panelist_images/')),
                ('agenda_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agendaday')),
            ],
        ),
        migrations.AddField(
            model_name='agendaday',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event'),
        ),
    ]
