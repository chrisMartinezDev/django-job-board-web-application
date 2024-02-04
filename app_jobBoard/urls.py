from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="Home Page"),
    path("job_listing", views.JobListing, name="Job Listing"),
]