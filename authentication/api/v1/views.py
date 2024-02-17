from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from authentication.helpers import get_tokens_for_user
from notes_backend.response import (
    response_200,
    response_201,
    response_400,
    response_401,
)

from . import LoginSerializer, SignupSerializer, UserProfileSerializer


class SignupAPIView(APIView):
    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            user = signup_serializer.save()
            return response_201(data=get_tokens_for_user(user), message="User Created")
        return response_400(error=signup_serializer.errors)


class LoginAPIView(APIView):
    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = authenticate(
                request,
                username=login_serializer.validated_data.get("username"),
                password=login_serializer.validated_data.get("password"),
            )
            if user is not None:
                user.last_login = datetime.now()
                user.save()
                return response_200(data=get_tokens_for_user(user))
            return response_401()
        return response_400(error=login_serializer.errors)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile_serializer = UserProfileSerializer(request.user)
        return response_200(data=user_profile_serializer.data)

    def patch(self, request): ...

    def delete(self, request):
        request.user.delete()
        return response_201(data=None, message="User account deleted!")
