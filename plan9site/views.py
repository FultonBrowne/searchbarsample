from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm


def product_search(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            products = products.filter(name__icontains=search_query)

    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'plan9site/productsearch.html', context)