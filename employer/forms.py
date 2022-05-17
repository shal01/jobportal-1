from django import forms
from employer.models import EmployerProfile


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ("user",)