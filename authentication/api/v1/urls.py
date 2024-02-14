from django.urls import path

from . import LoginAPIView, SignupAPIView

urlpatterns = [
    path("user/signup/", SignupAPIView.as_view(), name="signup-api"),
    path("user/login/", LoginAPIView.as_view(), name="login-api"),
]
