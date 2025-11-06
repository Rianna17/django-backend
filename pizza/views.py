from django.shortcuts import render

# Create your views here.
def all_pizza(request):
    return render(request,'pizza/all_pizza.html')