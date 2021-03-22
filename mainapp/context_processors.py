from basketapp.models import Basket

def get_basket(request):
    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)
        return {'user_basket': user_basket}
    return {'user_basket': None}
