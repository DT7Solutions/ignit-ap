from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models
# from .app import ContentTypeRestrictedFileField

# Create your models here.

#registration form

class Registration(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Confirm_pass = models.CharField(max_length=100)


    def __str__(self):
        return self.Firstname