from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
