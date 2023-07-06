from django.shortcuts import get_object_or_404, render

from .models import Product, Category


# Create your views here.

# after successful login , land to home page


def all_products(request):
    products = Product.objects.all()  # get all products from the database
    return render(request, 'store/home.html', {'products': products})

