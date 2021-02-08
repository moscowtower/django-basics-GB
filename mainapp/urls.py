from django.urls import path
from django.conf.urls import include

import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('category/<int:pk>/', mainapp.category, name='category'),
   path('product/<int:pk>/', mainapp.product, name='product'),
   ]