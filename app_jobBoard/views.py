from django.shortcuts import render
from .models import JobListing

# Create your views here.

def HomePage(request):
    # jobListings = JobListing.objects.all()

    jobListings = [
        {
            "title": "Job Title aklsdjlf;sdkl;fsdkl;fjkl;saflk;skl;fskl;adfl;kasjf",
            "companyName": "Company Name",
            "description": "Description",
            "location": "Location",
            "applicationDeadline": "1/4/24",
        }
    ]

    return render(request, "index.html", { "jobListings": jobListings })
