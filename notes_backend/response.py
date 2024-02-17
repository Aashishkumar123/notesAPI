from rest_framework import status
from rest_framework.response import Response


def response_201(data, message):
    response = {
        "status": status.HTTP_201_CREATED,
        "message": message,
    }
    if data is not None:
        response["data"] = data
    return Response(response, status=status.HTTP_201_CREATED)


def response_200(data):
    response = {
        "status_code": status.HTTP_200_OK,
        "message": "Success",
        "data": data,
    }
    return Response(response, status=status.HTTP_200_OK)


def response_400(error):
    response = {
        "status_code": status.HTTP_400_BAD_REQUEST,
        "message": "bad request",
        "error": error,
    }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)


def response_401():
    response = {
        "status_code": status.HTTP_401_UNAUTHORIZED,
        "message": "unauthorized",
    }
    return Response(response, status=status.HTTP_401_UNAUTHORIZED)
