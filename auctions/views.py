from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid
import json
from datetime import datetime

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")

def create_listingv(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html")
    elif request.method == "POST":
        title = request.POST.get('title')
        picture = request.POST.get('img-url')
        description = request.POST.get('description')
        price = request.POST.get('price')
        print(f"price {price}")

        # Check if the required fields are provided
        if not title or not description:
            return render(request, "auctions/create_listing.html", {
                "error": "Title and description are required."
            })

        # Get the current user
        try:
            owner = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            return render(request, "auctions/create_listing.html", {
                "error": "User not found."
            })

        # Create the listing object
        listing = Listing(
            title=title,
            description={"description": description},  # Directly use the dictionary
            image_url=picture,
            owner=owner,
            # price=price
        )
        listing.save()

        # Create Bid for price of listing
        bid = Bid(
            bid=price,
            user=owner,
            listing=listing
        )

        bid.save()
        listing.price = bid
        listing.save()
        return HttpResponseRedirect(reverse("auctions:index"))
