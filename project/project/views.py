from django.http import HttpResponse

def userdash(request):
    return HttpResponse("userdash")

def homepage(request):
    return HttpResponse("homepage")

def profile(request):
    return HttpResponse("profile")

def forum(request):
    return HttpResponse("forum")

def admindash(request):
    return HttpResponse("admindash")

