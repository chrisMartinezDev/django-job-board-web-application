from django.shortcuts import render, redirect
from .models import Job

# Create your views here.

def HomePage(request):
    jobListings = [
        {
            "id": 1,
            "title": "Job Title aklsdjlf;sdkl;fsdkl;fjkl;saflk;skl;fskl;adfl;kasjf",
            "companyName": "Company Name",
            "description": "Description",
            "location": "Location",
            "applicationDeadline": "1/4/24",
        },
    ]

    # jobListings = Job.objects.all()

    return render(request, "index.html", { "jobListings": jobListings })

def AddJobForm(request):
    return render(request, "addJobForm.html")

def AddJob(request):
    return redirect("index.html")

def Job(request, jobID):
    context = {}
    # context["job"] = Job.objects.get(id=jobID)

    return render(request, "jobListing.html", context)
