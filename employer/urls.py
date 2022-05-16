from django.urls import path
from employer import views


urlpatterns = [
    path("ehome", views.EmployerHomeView.as_view(), name="emp-home")
]