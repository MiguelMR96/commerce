from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=48)
