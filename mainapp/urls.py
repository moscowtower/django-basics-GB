from django.urls import path
from django.conf.urls import include

import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('<int:pk>/', mainapp.category, name='category'),
   path('product/<int:pk>/', mainapp.products, name='product'),
   ]