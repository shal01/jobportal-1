from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from users.decorators import signin_required
from django.utils.decorators import method_decorator
from candidate.forms import CandidateProfileForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications
from candidate.filters import JobFilter


# Create your views here.

@method_decorator(signin_required, name="dispatch")
class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"

    def get(self, request, *args, **kwargs):
        filter = JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request, "cand-home.html", {"filter":filter})


@method_decorator(signin_required, name="dispatch")
class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(signin_required, name="dispatch")
class CandidateProfileDetailView(TemplateView):
    template_name = "cand-myprofile.html"


@method_decorator(signin_required, name="dispatch")
class CandidateProfileUpdateView(UpdateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-updateprofile.html"
    success_url = reverse_lazy("cand-profdetail")
    pk_url_kwarg = "id"


@method_decorator(signin_required, name="dispatch")
class CandidateJobListView(ListView):
    model = Jobs
    template_name = "cand-Listjobs.html"
    context_object_name = "jobs"


@method_decorator(signin_required, name="dispatch")
class CandidateJobDetailView(DetailView):
    model = Jobs
    template_name = "cand-jobdetail.html"
    pk_url_kwarg = "id"
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Applications.objects.filter(applicant=self.request.user, job=self.object)
        print(qs)
        context["status"] = qs
        return context


@signin_required
def apply_now(request,*args,**kwargs):
    job_id = kwargs.get("id")
    job = Jobs.objects.get(id=job_id)
    applicant = request.user
    Applications.objects.create(applicant=applicant, job=job)
    return redirect("cand-home")


@method_decorator(signin_required, name="dispatch")
class MyApplicationView(ListView):
    model = Applications
    template_name = "cand-appliedjobs.html"
    context_object_name = "applied"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)


@method_decorator(signin_required, name="dispatch")
class AcceptedApplicationsView(ListView):
    model = Applications
    template_name = "cand-accepted.html"
    context_object_name = "application"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user, status="accepted")
