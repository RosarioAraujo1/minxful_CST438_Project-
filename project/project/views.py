from django.http import HttpResponse
from django.shortcuts import render


def userdash(request):
    return render(request, 'userdash.html')


def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    return render(request, 'login.html')


def forum(request):
    return render(request, 'forum.html')


def admindash(request):
    return render(request, 'admin_dash.html')

def signup(request):
    return render(request, 'signup.html')