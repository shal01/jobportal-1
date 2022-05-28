import django_filters
from employer.models import Jobs


class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr="icontains")
    role = django_filters.CharFilter(lookup_expr="icontains")
    qualification = django_filters.CharFilter(lookup_expr="icontains")
    salary = django_filters.NumberFilter(field_name="salary", lookup_expr="lt")
    location = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Jobs
        fields = [
            "job_title",
            "role",
            "qualification",
            "salary",
            "location",
        ]
