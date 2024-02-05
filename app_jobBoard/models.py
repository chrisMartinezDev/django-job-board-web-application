from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=1000)
    companyName = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=500)
    applicationDeadline = models.DateField()
