from django.urls import path
from . import views

#localhost:8000/pizza
#localhost:8000/pizza/order
urlpatterns = [
    path('',views.all_pizza , name='all_pizza '),
   
]
