from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data): ...

    def update(self, instance, validated_data): ...


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = instance.profile.image.url
        data["gender"] = instance.profile.gender
        return data


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_old_password(self, old_password):
        user = authenticate(
            request=self.context["request"],
            username=self.context["request"].user,
            password=old_password,
        )
        if not user:
            raise serializers.ValidationError("Old password is invalid")
        return old_password

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        confirm_password = attrs.get("confirm_password")
        if new_password != confirm_password:
            raise serializers.ValidationError(
                {"password": ["The two passwords do not match"]}
            )
        return attrs

    def create(self, validated_data):
        new_password = validated_data.get("new_password")
        user = self.context["request"].user
        user.password = make_password(new_password)
        user.save()
        return user

    def update(self, instance, validated_data): ...
