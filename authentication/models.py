from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    class Gender(models.Choices):
        MALE = "Male"
        FEMALE = "Female"
        OTHERS = "Others"

    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name="User Image", upload_to="profile", default="default.png"
    )
    gender = models.CharField(
        max_length=100, verbose_name="Gender", choices=Gender.choices
    )

    def __str__(self):
        return str(self.user)
