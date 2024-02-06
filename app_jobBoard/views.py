from django.shortcuts import render, redirect
from django.views import View
from .models import Job
from .forms import JobForm, ApplicationForm

# Create your views here.

def HomePage(request):
    jobListings = Job.objects.all()

    return render(request, "index.html", { "jobListings": jobListings })

def JobDetails(request, jobID):
    context = {}
    context["job"] = Job.objects.get(id = jobID)

    return render(request, "jobDetails.html", context)

class AddJob(View):
    def get(self, request):
        jobForm = JobForm()
        context = {}
        context["jobForm"] = jobForm
        context["mode"] = "add"

        return render(request, "addEditJob.html", context)

    def post(self, request):
        jobForm = JobForm(request.POST)

        if jobForm.is_valid():
            jobForm.save()

            return redirect('Home Page')
    
class EditJob(View):
    def get(self, request, jobID):
        job = Job.objects.get(id = jobID)
        jobForm = JobForm(instance = job)
        context = {}
        context["jobForm"] = jobForm
        context["job"] = job
        context["mode"] = "edit"

        return render(request, "addEditJob.html", context)

    def post(self, request, jobID):
        job = Job.objects.get(id = jobID)
        jobForm = JobForm(request.POST, instance = job)

        if jobForm.is_valid():
            jobForm.save()

            return redirect('Home Page')

def DeleteJob(request, jobID):
    job = Job.objects.get(id = jobID)
    job.delete()

    return redirect("Home Page")

class ApplyToJob(View):
    def get(self, request, jobID):
        job = Job.objects.get(id = jobID)
        applicationForm = ApplicationForm()
        context = {}
        context["job"] = job
        context["applicationForm"] = applicationForm

        return render(request, "applyToJob.html", context)
    
    def post(self, request, jobID):
        job = Job.objects.get(id = jobID)
        applicationForm = ApplicationForm(request.POST, request.FILES)
        context = {}
        context["job"] = job

        if applicationForm.is_valid():
            form = applicationForm.save(commit = False)
            form.job = job
            form.save()

        return render(request, 'jobDetails.html', context)
