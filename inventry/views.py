from django.shortcuts import render
from .models import Product


def home(request):
    """All products + quick filters"""
    products = Product.objects.all()
    in_stock_count = Product.objects.filter(in_stock=True).count()
    out_stock_count = Product.objects.filter(in_stock=False).count()
    return render(request, 'inventry/product_list.html', {
        'title': 'All Products',
        'products': products,
        'active': 'all',
        'in_stock_count': in_stock_count,
        'out_stock_count': out_stock_count,
    })


def in_stock(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, 'inventry/product_list.html', {
        'title': 'In‑Stock Products',
        'products': products,
        'active': 'in',
        'in_stock_count': products.count(),
        'out_stock_count': Product.objects.filter(in_stock=False).count(),
    })


def out_of_stock(request):
    products = Product.objects.filter(in_stock=False)
    return render(request, 'inventry/product_list.html', {
        'title': 'Out‑of‑Stock Products',
        'products': products,
        'active': 'out',
        'in_stock_count': Product.objects.filter(in_stock=True).count(),
        'out_stock_count': products.count(),
    })