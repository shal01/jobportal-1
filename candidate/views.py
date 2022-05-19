from django.shortcuts import render,redirect
from django.views.generic import TemplateView


# Create your views here.

class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"