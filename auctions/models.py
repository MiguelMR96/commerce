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

class Category(models.Model):
    name = models.CharField(max_length=64, default="Default category", primary_key=True)

    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    bid = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bidder")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} bid: {self.listing} at {self.bid}"

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    image_url = models.CharField(max_length=1064, null=True)
    description = models.JSONField()
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, default=0, related_name="price")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="listing_category")

    def __str__(self):
        return f"{self.title} - {self.id}: {self.description} at {self.date} of {self.owner}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.PROTECT, related_name="review_object")
    username = models.ForeignKey(User, on_delete=models.PROTECT, related_name="reviewer")
    review = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.id} comment: {self.review} at {self.listing}"
