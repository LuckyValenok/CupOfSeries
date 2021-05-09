from django.contrib.auth.models import User
from django.contrib.auth.models import models


class UserProfile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
