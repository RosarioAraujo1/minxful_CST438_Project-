from django.http import HttpResponse
from django.shortcuts import render
from .models import Post



def userdash(request):
    return render(request, 'userdash.html')


def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    return render(request, 'login.html')


def forum(request):
    posts = Post.objects.all().order_by('pub_date')
    return render(request, 'forum.html', {'posts': posts})


def admindash(request):
    return render(request, 'admin_dash.html')

def signup(request):
    return render(request, 'signup.html')