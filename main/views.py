from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Product # type: ignore

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'npm': '2306230685',
        'name': 'Naya Kusumahayati Rachmi',
        'class': 'PBP B',
        'store_name': 'Skivy',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'main.html', context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
