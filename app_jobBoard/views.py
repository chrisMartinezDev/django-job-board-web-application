from django.shortcuts import render, redirect
from django.views import View
from .models import Job

# Create your views here.

def HomePage(request):
    # jobListings = [
    #     {
    #         "id": 1,
    #         "title": "Job Title aklsdjlf;sdkl;fsdkl;fjkl;saflk;skl;fskl;adfl;kasjf",
    #         "companyName": "Company Name",
    #         "description": "Description",
    #         "location": "Location",
    #         "applicationDeadline": "1/4/24",
    #     },
    # ]

    jobListings = Job.objects.all()

    return render(request, "index.html", { "jobListings": jobListings })

class AddJob(View):
    def get(self, request):
        return render(request, "addJob.html")
    def post(self, request):
        job = Job.objects.create(
            title = request.POST.get('title'),
            companyName = request.POST.get('company name'),
            location = request.POST.get('location'),
            applicationDeadline = request.POST.get('application deadline'),
            description = request.POST.get('description'),
        )
        job.save()

        return redirect("Home Page")

def JobDetails(request, jobID):
    context = {}
    context["job"] = Job.objects.get(id = jobID)

    return render(request, "jobListing.html", context)
