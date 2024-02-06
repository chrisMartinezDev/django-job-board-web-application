from django import forms
from django.forms import ModelForm
from .models import Job, Application

# Create your forms here.

class JobForm(ModelForm):
    title = forms.CharField()
    companyName = forms.CharField(label="Company Name")
    location = forms.CharField()
    applicationDeadline = forms.DateField(label="Application Deadline")
    description = forms.CharField(widget = forms.Textarea())

    class Meta:
        model = Job
        fields = ["title", "companyName", "location", "applicationDeadline", "description"]

class ApplicationForm(ModelForm):
    firstName = forms.CharField(label="First Name")
    lastName = forms.CharField(label="Last Name")
    emailAddress = forms.CharField(label="Email Address")
    phoneNumber = forms.CharField(label="Phone Number")
    resume = forms.FileField(label="Resume")

    class Meta:
        model = Application
        fields = ["firstName", "lastName", "emailAddress", "phoneNumber", "resume"]

