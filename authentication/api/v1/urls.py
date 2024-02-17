from django.urls import path

from . import LoginAPIView, SignupAPIView, UserProfileAPIView

urlpatterns = [
    path("user/signup/", SignupAPIView.as_view(), name="signup-api"),
    path("user/login/", LoginAPIView.as_view(), name="login-api"),
    path("user/profile/", UserProfileAPIView.as_view(), name="user-profile-api"),
]
