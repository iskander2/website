from django.db import models
from app.models import Product
from django.contrib.auth import get_user_model

# Create your models here.
User =get_user_model()



class Basket(models.Model):
    owner =models.ForeignKey(User,related_name='baskets',on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
  
class BasketProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='basket_product')
    cart =models.ForeignKey(Basket,on_delete=models.CASCADE,related_name='basket_product')
      
