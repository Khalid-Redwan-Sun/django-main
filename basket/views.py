from math import prod
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from django.contrib.sessions.models import Session

from .basket import Basket

from store.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.template.defaulttags import register


# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    product_ids = get_product_ids(basket.keys())

    products = Product.objects.filter(id__in=product_ids)  # get all products from the database

    basket_qty = get_basket_qty(product_ids, basket)

    # calculatig total price
    total_price = get_total_price(basket_qty, product_ids)

    return render(request, 'store/basket/basket_summary.html', {'products': products, 'basket_qty': basket_qty, 'total_price': total_price})


@csrf_exempt  # to avoid csrf error
def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get("product_id"))
        product_qty = request.POST.get("product_qty")
        product = get_object_or_404(Product, id=product_id)
        total_qty = basket.add(product, product_qty)

        response = JsonResponse({"qty": total_qty})  # to send json response to detail.html

    if request.GET.get('action') == 'get':
        total_qty = basket.get_total_qty()

        response = JsonResponse({"qty": total_qty})

    if request.POST.get('action') == 'remove':
        id = request.POST.get("id")
        basket.remove(id)
        product_ids = get_product_ids(basket.keys())
        basket_qty = get_basket_qty(product_ids, basket)

        total_price = get_total_price(basket_qty, product_ids)
        response = JsonResponse({'total_qty': basket.get_total_qty(), 'total_price': total_price})
       

    return response





@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def get_total_price(basket_qty, product_ids):
    total_price = 0
    for i_d in product_ids:
        product = get_object_or_404(Product, id=i_d)
        print(product.price)
        print(basket_qty)
        total_price += (product.price * basket_qty[i_d])

    return total_price


def get_product_ids(basket_keys):
    for i in basket_keys:
        if i == "total_qty":
            basket_keys.remove(i)

    return list(map(int, basket_keys))


def get_basket_qty(product_ids, basket):

    basket_qty = {}
    for i in product_ids:
        basket_qty[i] = basket.basket[str(i)]['qty']
    return basket_qty



