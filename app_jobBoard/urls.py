from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="Home Page"),
    path("job_listing/<str:jobID>/", views.Job, name="Job Listing"),
    path("add_job_form/", views.AddJobForm, name="Add Job Form"),
    path("add_job/", views.AddJob, name="Add Job"),
]