from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from candidate.forms import CandidateProfileForm
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications


# Create your views here.

class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"


class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class CandidateProfileDetailView(TemplateView):
    template_name = "cand-myprofile.html"


class CandidateJobListView(ListView):
    model = Jobs
    template_name = "cand-Listjobs.html"
    context_object_name = "jobs"


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


def apply_now(request,*args,**kwargs):
    job_id = kwargs.get("id")
    job = Jobs.objects.get(id=job_id)
    applicant = request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect("cand-home")


class MyApplicationView(ListView):
    model = Applications
    template_name = "cand-appliedjobs.html"
    context_object_name = "applied"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)