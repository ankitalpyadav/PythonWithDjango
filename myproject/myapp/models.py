from django.db import models
from django.contrib.auth.models import AbstractUser


class Register(AbstractUser):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=70, default="")
