from datetime import datetime
from django.db import models
from .app import ContentTypeRestrictedFileField


# Create your models here.

#Student idea form
class StudentIdeaform(models.Model):

    STATUS = (
        (0, 'False'),
        (1, 'True')
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
    Approved = models.IntegerField(choices=STATUS, default=0)
    Date = models.DateTimeField(default=datetime.now())
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