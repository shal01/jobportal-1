from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from django.urls import reverse_lazy
from employer.forms import EmployerProfileForm,JobForm,JobUpdateForm
from employer.models import EmployerProfile,Jobs,Applications

# Create your views here.


class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EmployeeProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"


class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user)


class JobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"


class JobEditView(UpdateView):
    model = Jobs
    form_class = JobUpdateForm
    template_name = "emp-jobedit.html"
    success_url = reverse_lazy("emp-listjob")
    pk_url_kwarg = "id"


class ViewApplicationView(ListView):
    model = Applications
    template_name = "emp-viewapplication.html"
    context_object_name = "vw_app"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"))
