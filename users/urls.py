from django.urls import path
from users import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="users-home"),
    path("accounts/signup", views.SignUpView.as_view(), name="signup"),
    path("accounts/signin", views.SignInView.as_view(), name="signin"),
    path("accounts/signout", views.sign_out,name="signout"),
]