from datetime import datetime
from django.db import models
from .app import ContentTypeRestrictedFileField
from django.contrib.auth.models import User

# Create your models here.

#Student idea form
class StudentIdeaform(models.Model):

    STATUS = (
        ('Proccing', 'Proccing'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )

    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=10)
    College_Name = models.CharField(max_length=50)
    Branch_Name = models.CharField(max_length=50)
    Idea_Description = models.CharField(max_length=500)
    Upload_url = models.URLField()
    Approved = models.CharField(choices=STATUS, max_length=30, default='Proccing')
    Reason = models.CharField(max_length=500, default="")
    Date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    file = ContentTypeRestrictedFileField(
        upload_to = 'pdf',
        content_types = ['application/pdf','application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
        max_upload_size = 2621440

    )

    def __str__(self):
        return self.Firstname
    


class EventTimer(models.Model):
    EventName = models.CharField(max_length=100)
    target_datetime = models.DateTimeField()


    def __str__(self):
        return self.EventName



from django.db import models

class Event(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    # Add other fields as needed

    def __str__(self):
        return self.title

class AgendaDay(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.event.title} - {self.date}"

class Panelist(models.Model):
    agenda_day = models.ForeignKey(AgendaDay, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    companeyName = models.CharField(max_length=255,default='')
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='panelist_images/')  #
    def __str__(self):
        return f"{self.name} - {self.name}"

# class Panel(models.Model):
#     agenda_day = models.ForeignKey(AgendaDay, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     # Add other fields as needed

#     def __str__(self):
#         return f"{self.agenda_day.event.title} - {self.agenda_day.date} - {self.title}"

