from django.http import HttpResponse
from . import views


def home(request):
    return HttpResponse("hello world. You are at rianna and django home page")

def about(request):
    return HttpResponse("hello world. You are at rianna and django about page")

def contact(request):
    return HttpResponse("hello world. You are at rianna and django contact page")