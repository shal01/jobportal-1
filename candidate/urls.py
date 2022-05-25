from django.urls import path
from candidate import views


urlpatterns = [
    path("home", views.CandidateHomeView.as_view(), name="cand-home"),
    path("profile/add", views.CandidateProfileCreateView.as_view(), name="cand-addprofile"),
    path("profile/detail", views.CandidateProfileDetailView.as_view(), name="cand-profdetail"),
    path("job/all", views.CandidateJobListView.as_view(), name="cand-joblist"),
    path("job/detail/<int:id>", views.CandidateJobDetailView.as_view(), name="cand-jobdetail"),
    path("application/add/<int:id>", views.apply_now, name="apply_now"),
    path("application/applied", views.MyApplicationView.as_view(), name="cand-myapplic"),
]