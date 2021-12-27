from django import forms
from django.forms import fields
from .models import Basket



class BasketForm(forms.ModelForm):
    
    class Meta:
        model = Basket
        exclude = ['owner']