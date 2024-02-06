from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="Home Page"),
    path("job_listing/<str:jobID>/", views.JobDetails, name="Job Details"),
    path("add_job/", views.AddJob.as_view(), name="Add Job"),
    path("edit_job/<str:jobID>", views.EditJob.as_view(), name="Edit Job"),
    path("delete_job/<str:jobID>", views.DeleteJob, name="Delete Job"),
    path("apply_to_job/<str:jobID>", views.ApplyToJob.as_view(), name="Apply to Job"),
]