from datetime import datetime

from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from basketapp.models import Basket

@method_decorator(cache_page(120), name='dispatch')
class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/products.html'
    paginate_by = 3

    def get_queryset(self):
        data = self.kwargs
        if data.get('category_id'):
            return Product.objects.filter(category_id=data['category_id'])
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = ProductCategory.objects.all()
        context['categories'] = ProductCategory.get_all()
        return context
