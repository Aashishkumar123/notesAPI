from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.helpers import get_tokens_for_user

from . import SignupSerializer


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
