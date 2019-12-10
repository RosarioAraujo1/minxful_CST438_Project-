from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from .models import Reply



def userdash(request):
    posts = Post.objects.all().order_by("pub_date")
    return render(request, "userdash.html", {"posts": posts})
    # return render(request, 'userdash.html')


def homepage(request):
    posts = Post.objects.all().order_by("pub_date")
    return render(request, "homepage.html", {"posts": posts})
    # comment = Reply.objects.all()
    # return render(request, "homepage.html", {"posts": posts}, {"comments": comment})

def addComment(request):
    if request.method == 'POST':
        if request.POST.get('fname'):
            post=Post()
            post.title= request.POST.get('fname')
            post.save()
            return render(request, 'homepage.html')  

        else:
            return render(request, '500.html', {})

def login(request):
    return render(request, 'login.html')

def forum(request):
    return render(request, 'forum.html')

def admindash(request):
    return render(request, 'admin_dash.html')

def signup(request):
    return render(request, 'signup.html')
