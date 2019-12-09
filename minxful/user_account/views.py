from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_account/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm()

    else:
        form = AuthenticationForm()
    return render(request, 'user_account/login.html', {'form': form})