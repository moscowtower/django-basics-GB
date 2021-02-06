from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from datetime import datetime
from basketapp.models import Basket
def index(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objecs.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

            context = {
                'products': products,
                'categories': category,
                'links_menu': links_menu,
                'title': 'каталог',
                'basket': basket
            }
        return(render(request), 'mainapp/products.html', context)

    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'links_menu': links_menu,
        'title': 'каталог'
    }

    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    context = {
        'products': Product.objects.filter(category=pk),
        'categories': ProductCategory.objects.all(),
        'title': ProductCategory.objects.get(pk=pk)
    }
    return render(request, 'mainapp/products.html', context)


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)