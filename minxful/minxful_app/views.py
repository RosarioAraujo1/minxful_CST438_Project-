from django.shortcuts import render
from .models import Post


def userdash(request):
    posts = Post.objects.all().order_by("pub_date")
    return render(request, "userdash.html", {"posts": posts})


def homepage(request):
    posts = Post.objects.all().order_by("pub_date")
    return render(request, "homepage.html", {"posts": posts})


def login(request):
    return render(request, "login.html")


def forum(request):
    return render(request, "forum.html")


def admindash(request):
    return render(request, "admin_dash.html")


def signup(request):
    return render(request, "signup.html")
