from django.urls import path
from employer import views


urlpatterns = [
    path("ehome", views.EmployerHomeView.as_view(), name="emp-home"),
    path("profile/add", views.EmployerProfileCreateView.as_view(), name="emp-profile"),
    path("profile/details", views.EmployeeProfileDetailView.as_view(), name="emp-profdetail"),
    path("jobs/add", views.JobCreateView.as_view(), name="emp-addjob"),
    path("jobs/all", views.EmployerJobListView.as_view(), name="emp-listjob"),
    path("jobs/detail/<int:id>", views.JobDetailView.as_view(), name="emp-jobdetail"),
    path("jobs/edit/<int:id>", views.JobEditView.as_view(), name="emp-jobedit"),
    path("jobs/application/<int:id>", views.ViewApplicationsView.as_view(), name="emp-viewappl"),
    path("jobs/application/profile/<int:id>", views.ApplicantProfileView.as_view(), name="emp-apptprof"),
]