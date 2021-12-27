from django.contrib import admin
from .models import BasketProduct,Basket

# Register your models here.

admin.site.register(Basket)
admin.site.register(BasketProduct)