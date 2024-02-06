from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=1000)
    companyName = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=500)
    applicationDeadline = models.DateField()

class Application(models.Model):
    job = models.ForeignKey(Job, blank = True, null = True, on_delete = models.SET_NULL)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    resume = models.FileField(upload_to="files/", null=True)