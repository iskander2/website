from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Category, Product
from profiles.forms import CommentForm
# Create your views here.
def main(request):
    form = CommentForm(request.user)
    products= Product.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products =products.filter(Category_id=category_id)    
    categories = Category.objects.all().order_by('name')
    return render(request,'main.html', {"categories":categories,"products": products})

def detail(request,pk):
    form = CommentForm()
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all().order_by('name')
    return render(request, 'detail.html', {"categories":categories,'product': product,"form":form})


        

