from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect("/")
        else:
            messages.error(request, 'Failed to signup!')
            return render(request, "user_account/signup.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "user_account/signup.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()
    return render(request, 'user_account/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect("/")
