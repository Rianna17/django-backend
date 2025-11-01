from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
  #return HttpResponse("hello world. You are at rianna and django home page")
  return render(request, "website/index.html")

def about(request):
    return HttpResponse("hello world. You are at rianna and django about page")

def contact(request):
    return HttpResponse("hello world. You are at rianna and django contact page")