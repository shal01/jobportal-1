from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from users.decorators import signin_required
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, dates
from employer.forms import EmployerProfileForm, JobForm, JobUpdateForm
from employer.models import EmployerProfile, Jobs, Applications
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


@method_decorator(signin_required, name="dispatch")
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


@method_decorator(signin_required, name="dispatch")
class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(signin_required, name="dispatch")
class EmployeeProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"


@method_decorator(signin_required, name="dispatch")
class EmployerProfileUpdateView(UpdateView):
    model = EmployerProfile
    template_name = "emp-updateprofile.html"
    form_class = EmployerProfileForm
    success_url = reverse_lazy("emp-home")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "profile has been updated")
        return super().form_valid(form)


@method_decorator(signin_required, name="dispatch")
class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        present_date = dates.timezone_today()
        print(present_date)
        last_date = form.cleaned_data.get("last_date")
        if last_date <= present_date:
            return redirect("emp-addjob")
        else:
            form.save()
        messages.success(self.request, "job has been posted")
        return super().form_valid(form)


@method_decorator(signin_required, name="dispatch")
class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by("-created_date")


@method_decorator(signin_required, name="dispatch")
class JobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"


@method_decorator(signin_required, name="dispatch")
class JobEditView(UpdateView):
    model = Jobs
    form_class = JobUpdateForm
    template_name = "emp-jobedit.html"
    success_url = reverse_lazy("emp-listjob")
    pk_url_kwarg = "id"

    # def form_valid(self, form):
    #     form.instance.posted_by = self.request.user
    #     present_date = dates.timezone_today()
    #     last_date = form.cleaned_data.get("last_date")
    #     if last_date >= present_date:
    #         form.save()
    #     else:
    #         return redirect("emp-jobedit")
    #     return super().form_valid(form)


@signin_required
def job_delete(request, *args, **kwargs):
    job_id = kwargs.get("id")
    qs = Jobs.objects.get(id=job_id)
    qs.delete()
    return redirect("emp-listjob")


@method_decorator(signin_required, name="dispatch")
class ViewApplicationsView(ListView):
    model = Applications
    template_name = "emp-viewapplication.html"
    context_object_name = "vw_app"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"), status="applied")


@method_decorator(signin_required, name="dispatch")
class ApplicantProfileView(DetailView):
    model = Applications
    template_name = "emp-applntprof.html"
    context_object_name = "apt"
    pk_url_kwarg = "id"


@signin_required
def update_application(request, *args, **kwargs):
    app_id = kwargs.get("id")
    qs = Applications.objects.get(id=app_id)
    qs.status = "rejected"
    qs.save()
    return redirect("emp-listjob")


@signin_required
def accept_application(request, *args, **kwargs):
    app_id = kwargs.get("id")
    qs = Applications.objects.get(id=app_id)
    qs.status = "accepted"
    qs.save()
    send_mail(
        'Job Notification',
        'Your resume accepted.',
        'anandtsreenivasan2000@gmail.com',
        ['anandtsreenivasan2000@gmail.com'],
        fail_silently=False,
    )
    return redirect("emp-listjob")


# from@example.com
# to@example.com

@method_decorator(signin_required, name="dispatch")
class ShortListView(ListView):
    model = Applications
    template_name = "emp-shortlist.html"
    context_object_name = "application"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"), status="accepted")

