from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "main/home.html")


def register(request):
    return render(request, "main/register.html")


def logout_request(request):
    return render(request, "main/logout.html")
