from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.id} {self.get_username()}"

class Category(models.Model):
    name = models.CharField(max_length=64, default="Default category", primary_key=True)

    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    bid = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="bids")
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name="bids", null=True)

    def __str__(self):
        return f"{self.id} bid: {self.listing.title} at {self.bid}"

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    image_url = models.CharField(max_length=30000, null=True)
    description = models.JSONField()
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True, blank=True, related_name="price_listing")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_listings")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="listings")

    def __str__(self):
        return f"{self.title} - {self.id}: {self.description} at {self.created_at} by {self.owner}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)
    review = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.id} comment: {self.review} on {self.listing.title}"
