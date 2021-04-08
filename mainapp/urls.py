from django.urls import path

import mainapp.views as mp_views
from django.views.generic import TemplateView

app_name = 'mainapp'

urlpatterns = [
   path('', TemplateView.as_view(template_name='mainapp/index.html'), name='index'),
   path('products/', mp_views.ProductView.as_view(), name='products'),
   path('product/<int:category_id>/', mp_views.ProductView.as_view(), name='product'),
   path('product/page/<int:page>/', mp_views.ProductView.as_view(), name='page'),
   ]