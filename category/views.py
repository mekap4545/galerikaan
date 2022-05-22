from multiprocessing import context
from django.shortcuts import render

from store.models import Product

# Create your views here.


def index(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    
    return render(request,"index.html", context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def product(request):
    return render(request,"product.html")

