from django.urls import path

from basketapp import views as basket_views

app_name = 'basket'

urlpatterns = [
    path('basket/', basket_views.basket, name='view'),
    path('basket-add/<int:product_id>/', basket_views.basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket_views.basket_remove, name='basket_remove'),
]