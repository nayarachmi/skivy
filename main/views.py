from django.shortcuts import render
from .models import Product # type: ignore

def show_main(request):
    context = {
        'npm': '2306230685',
        'name': 'Naya Kusumahayati Rachmi',
        'class': 'PBP B',
        'store_name': 'Skivy',
    }

    return render(request, "main.html", context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main.html', context)
