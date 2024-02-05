from django import forms
from django.forms import ModelForm
from .models import Job

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