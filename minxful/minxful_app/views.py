from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect


def userdash(request):
    posts = Post.objects.all()
    return render(request, "userdash.html", {"posts": posts})


def homepage(request):
<<<<<<< HEAD
    posts = Post.objects.all().order_by("pub_date")
    return render(request, "homepage.html", {"posts": posts})
=======
    posts = list(Post.objects.all())
    return render(request, "homepage.html", {"posts": posts[::-1]})
>>>>>>> 90250a012bf37ad2b6e018657caff5b9d60479e2


def login(request):
    return render(request, "login.html")


def admindash(request):
    return render(request, "admin_dash.html")


def signup(request):
    return render(request, "signup.html")


@login_required(login_url='/user_account/login/')
def forum(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect("http://127.0.0.1:8000")

    else:
        form = forms.CreatePost()
    return render(request, 'forum.html', {'form': form})
