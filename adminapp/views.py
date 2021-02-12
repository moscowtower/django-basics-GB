from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from adminapp.forms import AdminShopUserEditForm, ProductForm

from mainapp.models import Product, ProductCategory
from authapp.forms import ShopUser

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request,'adminapp/index.html')

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(data=request.POST, files=request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
        else:
            print(form.errors)
    else:
        form = ShopUserRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    user = ShopUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = AdminShopUserEditForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = ShopUserEditForm()
    context = {'form':form, 'user':user}
    return render(request, 'adminapp/users-update.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = ShopUser.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin:users'))

@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)

@user_passes_test(lambda u: u.is_superuser)
def products(request):
    title = 'админка/продукт'

    content = {
        'title': title,
        'products': Product.objects.all()
    }

    return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    title = 'админка/создание продукта'

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:products'))
        else:
            print(form.errors)
    else:
        form = ProductForm()

    content = {
        'title': title,
        'form': form
    }
    return render(request, 'adminapp/products-create.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'админка/изменение продукта'
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:products'))
        else:
            print(form.errors)
    else:
        form = ProductForm()

    content = {
        'title': title,
        'form': form,
        'product': product
    }
    return render(request, 'adminapp/products-update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    print(f'product {product} is deleted')
    return HttpResponseRedirect(reverse('admin:products'))
