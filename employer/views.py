from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from users.decorators import signin_required
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employer.forms import EmployerProfileForm,JobForm,JobUpdateForm
from employer.models import EmployerProfile,Jobs,Applications
from django.core.mail import send_mail

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
    success_url = reverse_lazy("emp-profdetail")
    pk_url_kwarg = "id"


@method_decorator(signin_required, name="dispatch")
class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


@method_decorator(signin_required, name="dispatch")
class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user)


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
def update_application(request,*args,**kwargs):
    app_id = kwargs.get("id")
    qs = Applications.objects.get(id=app_id)
    qs.status = "rejected"
    qs.save()
    return redirect("emp-listjob")


@signin_required
def accept_application(request,*args,**kwargs):
    app_id = kwargs.get("id")
    qs = Applications.objects.get(id=app_id)
    qs.status = "accepted"
    qs.save()
    send_mail(
        'Job Notification',
        'Your resume accepted.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return redirect("emp-listjob")
# smarttv7535@gmail.com


