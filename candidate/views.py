from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from candidate.forms import CandidateProfileForm
from django.views.generic import TemplateView,CreateView
from candidate.models import CandidateProfile


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