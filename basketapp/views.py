from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from basketapp.models import Basket
from mainapp.models import Product

@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket = Basket.objects.get(pk=int(id))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
    content = {'baskets': baskets}
    result = render_to_string('basketapp/basket.html', content)
    return JsonResponse({'result': result})


@login_required
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


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(pk=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
