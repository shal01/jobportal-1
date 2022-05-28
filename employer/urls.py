from django.urls import path
from employer import views


urlpatterns = [
    path("home", views.EmployerHomeView.as_view(), name="emp-home"),
    path("profile/add", views.EmployerProfileCreateView.as_view(), name="emp-profile"),
    path("profile/details", views.EmployeeProfileDetailView.as_view(), name="emp-profdetail"),
    path("profile/update/<int:id>", views.EmployerProfileUpdateView.as_view(), name="emp-profupdate"),
    path("jobs/add", views.JobCreateView.as_view(), name="emp-addjob"),
    path("jobs/all", views.EmployerJobListView.as_view(), name="emp-listjob"),
    path("jobs/all/detail/<int:id>", views.JobDetailView.as_view(), name="emp-jobdetail"),
    path("jobs/all/detail/delete/<int:id>", views.job_delete, name="emp-jobdelete"),
    path("jobs/all/detail/edit/<int:id>", views.JobEditView.as_view(), name="emp-jobedit"),
    path("jobs/all/shortlist/<int:id>", views.ShortListView.as_view(), name="emp-shortlist"),
    path("jobs/all/applications/<int:id>", views.ViewApplicationsView.as_view(), name="emp-viewappl"),
    path("jobs/all/applications/profile/<int:id>", views.ApplicantProfileView.as_view(), name="emp-apptprof"),
    path("jobs/all/applications/profile/r_status/<int:id>", views.update_application, name="emp-r_status"),
    path("jobs/all/applications/profile/a_status/<int:id>", views.accept_application, name="emp-a_status"),
]