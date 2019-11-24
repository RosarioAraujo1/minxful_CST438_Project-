from django.http import HttpResponse

def home(request):
    return HttpResponse("home")

def homepage(request):
    return HttpResponse("homepage")