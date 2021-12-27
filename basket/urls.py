from django.urls import path
from .views import add_to_basket,get_basket


app_name="basket"



urlpatterns = [
    path('add/<int:pk>/' , add_to_basket, name='add_to_basket'),
    path('basket/' , get_basket, name='get_basket')
   
]