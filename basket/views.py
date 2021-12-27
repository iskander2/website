from django.shortcuts import redirect, render
from basket.models import BasketProduct
from .basket import Cart
from app.models import Product
from .forms import BasketForm

# Create your views here.
def add_to_basket(request,pk):
    if not request.user.is_authenticated:
        return redirect("profiles:signup")
    product = Product.objects.get(pk=pk)
    cart =Cart(request)
    cart.add(product)
    return redirect("app:main")    


def get_basket(request):
    cart = Cart(request)
    product_ids = cart.get_products()
    form = BasketForm(request.POST or None)
    products = Product.objects.filter(id__in=product_ids)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        basket_products = [BasketProduct(product=product, basket=instance) for product in products]
        BasketProduct.objects.bulk_create(basket_products)
        cart.clear()
        return redirect("app:main")
    return render(request, 'basket.html', {'products': products, 'form': form})