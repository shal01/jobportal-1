from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from employer.forms import EmployerProfileForm
from employer.models import EmployerProfile

# Create your views here.


class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class EmployeeProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"

