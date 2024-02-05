from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="Home Page"),
    path("job_listing/<str:jobID>/", views.JobDetails, name="Job Details"),
    path("add_job/", views.AddJob.as_view(), name="Add Job"),
]