from django.urls import path
from candidate import views


urlpatterns = [
    path("home", views.CandidateHomeView.as_view(), name="cand-home"),
    path("profile/add", views.CandidateProfileCreateView.as_view(), name="cand-addprofile"),
    path("profile/detail", views.CandidateProfileDetailView.as_view(), name="cand-profdetail"),
    path("profile/edit/<int:id>", views.CandidateProfileUpdateView.as_view(), name="cand-profupdate"),
    path("job/all", views.CandidateJobListView.as_view(), name="cand-joblist"),
    path("job/all/detail/<int:id>", views.CandidateJobDetailView.as_view(), name="cand-jobdetail"),
    path("application/add/<int:id>", views.apply_now, name="apply_now"),
    path("application/applied", views.MyApplicationView.as_view(), name="cand-myapplic"),
    path("application/accepted", views.AcceptedApplicationsView.as_view(), name="cand-acptjob"),
]