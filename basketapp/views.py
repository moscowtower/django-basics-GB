from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    basket = Basket.objects.filter(user=request.user)
    content = {'baskets': basket}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        print('not baskets')
    else:
        basket = baskets.first()
    print(baskets)
    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):
    basket = Basket.objects.get(pk=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
