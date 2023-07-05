from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128, unique=False, default="nn")
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=48)

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.JSONField()
    date = models.DateField()

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    listing_id = models.ForeignKey(Listing, on_delete=models.PROTECT)
    bid = models.IntegerField(null=False)
    date = models.DateField()

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    bid_id = models.ForeignKey(Bid, on_delete=models.PROTECT)
    listing_id = models.ForeignKey(Listing, on_delete=models.PROTECT)
