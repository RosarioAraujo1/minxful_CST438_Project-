from django.http import HttpResponse
from django.shortcuts import render


def userdash(request):
    return HttpResponse("userdash")


def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    return HttpResponse("login")


def forum(request):
    return HttpResponse("forum")


def admindash(request):
    return HttpResponse("admindash")

def signup(request):
    return HttpResponse("signup")