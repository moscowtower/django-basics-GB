from django.urls import path

from basketapp import views as basket_views

app_name = 'basket'

urlpatterns = [
    path('basket-add/<int:product_id>/', basket_views.basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket_views.basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', basket_views.basket_edit, name='basket_edit'),
]