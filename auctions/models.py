from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128, unique=False)
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.username} - {self.id}: {self.name} at {self.email}"

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    image = models.CharField(max_length=256)
    description = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="owner")

    def __str__(self):
        return f"{self.title} - {self.id}: {self.description} at {self.date} of {self.owner}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    bid = models.IntegerField(null=False)
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT, related_name="item")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bidder")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} bid: {self.listing} at {self.bid}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT, related_name="review_object")
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name="reviewer")
    review = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.id} comment: {self.review} at {self.listing}"
