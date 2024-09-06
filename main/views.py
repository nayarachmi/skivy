from django.shortcuts import render

def show_main(request):
    context = {
        'price' : '100.000',
        'name': 'Hatomugi Toner',
        'description': 'A Hydrating Toner',
        'skin_type': 'All Skin Type'
    }

    return render(request, "main.html", context)

# Create your views here.
