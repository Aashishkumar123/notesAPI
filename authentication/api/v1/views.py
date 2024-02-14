from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.helpers import get_tokens_for_user

from . import LoginSerializer, SignupSerializer


class SignupAPIView(APIView):
    def post(self, request):
        signup_serializer = SignupSerializer(data=request.data)
        if signup_serializer.is_valid():
            user = signup_serializer.save()
            response = {
                "status": status.HTTP_201_CREATED,
                "message": "User Created",
                "data": get_tokens_for_user(user),
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": "bad request",
            "error": signup_serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


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
                response = {
                    "status_code": status.HTTP_200_OK,
                    "message": "Login successful",
                    "data": get_tokens_for_user(user),
                }
                return Response(response, status=status.HTTP_200_OK)
            response = {
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": "unauthorized",
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        response = {
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": "bad request",
            "error": login_serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
