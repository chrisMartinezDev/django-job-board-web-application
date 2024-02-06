from django import forms
from django.forms import ModelForm
from .models import Job, Application

# Create your forms here.

class JobForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'job-form-input'}))
    companyName = forms.CharField(label="Company Name", widget=forms.TextInput(attrs={'class': 'job-form-input'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'job-form-input'}))
    applicationDeadline = forms.DateField(label="Application Deadline", widget=forms.TextInput(attrs={'class': 'job-form-input'}))
    description = forms.CharField(widget = forms.Textarea(attrs={'class': 'job-form-input-textarea'}))

    class Meta:
        model = Job
        fields = ["title", "companyName", "location", "applicationDeadline", "description"]

class ApplicationForm(ModelForm):
    firstName = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'application-form-input'}))
    lastName = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class': 'application-form-input'}))
    emailAddress = forms.CharField(label="Email Address", widget=forms.TextInput(attrs={'class': 'application-form-input'}))
    phoneNumber = forms.CharField(label="Phone Number", widget=forms.TextInput(attrs={'class': 'application-form-input'}))
    resume = forms.FileField(label="Resume", widget=forms.FileInput(attrs={'class': 'application-form-input'}))

    class Meta:
        model = Application
        fields = ["firstName", "lastName", "emailAddress", "phoneNumber", "resume"]

