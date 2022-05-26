import django_filters
from employer.models import Jobs


class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Jobs
        fields = [
            "posted_by",
            "job_title",
            "role",
            "qualification",
            "salary",
            "location",
        ]
