from django.urls import path

from . import SignupAPIView

urlpatterns = [
    path("user/signup/", SignupAPIView.as_view(), name="signup-api"),
]
