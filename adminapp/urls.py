import adminapp.views as adminapp
import mainapp.views as mainapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('', mainapp.index, name='index'),

    path('users/create/', adminapp.UsersCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.UsersUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UsersDeleteView.as_view(), name='user_delete'),

    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/', adminapp.ProductsListView.as_view(), name='products'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]


