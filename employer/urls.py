from django.urls import path
from employer import views


urlpatterns = [
    path("ehome", views.EmployerHomeView.as_view(), name="emp-home"),
    path("profile/add", views.EmployerProfileCreateView.as_view(), name="emp-profile"),
    path("profile/details", views.EmployeeProfileDetailView.as_view(), name="emp-profdetail"),
]