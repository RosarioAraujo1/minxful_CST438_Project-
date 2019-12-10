from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        form = UserCreationForm()
    return render(request, "user_account/signup.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        form = AuthenticationForm()
    return render(request, 'user_account/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect("http://127.0.0.1:8000/")
