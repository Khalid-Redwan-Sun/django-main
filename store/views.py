from django.shortcuts import get_object_or_404, render

from .models import Product, Category


# Create your views here.

<<<<<<< HEAD
=======
# after successful login , land to home page

>>>>>>> 4c91c8f0505e05f4b243f31cc1871d4815965e58

def all_products(request):
    products = Product.objects.all()  # get all products from the database
    return render(request, 'store/home.html', {'products': products})

<<<<<<< HEAD

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, is_active=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)  # get all products objects in these category
    return render(request, 'store/products/category.html', {"category": category, "products": products})
=======
>>>>>>> 4c91c8f0505e05f4b243f31cc1871d4815965e58
