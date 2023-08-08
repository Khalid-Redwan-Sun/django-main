from django.shortcuts import get_object_or_404, render

from .models import Product, Category



def categories(request):
    return {'categories': Category.objects.all()}  