from django.http import HttpResponse
from django.shortcuts import render
from .models import Post



def userdash(request):
    return render(request, 'userdash.html')


def homepage(request):
    posts = Post.objects.all().order_by('pub_date')
    return render(request, 'homepage.html', {'posts': posts})
<<<<<<< HEAD
# def homepage(request):
#     return render(request, 'homepage.html', {'posts': posts})

=======
>>>>>>> master


def login(request):
    return render(request, 'login.html')


def forum(request):
<<<<<<< HEAD
=======

>>>>>>> master
    return render(request, 'forum.html')


def admindash(request):
    return render(request, 'admin_dash.html')

def signup(request):
    return render(request, 'signup.html')