from django.urls import path
from . import views

app_name='store' 
 #this is used to avoid name conflict,each app has its own namespace,,so one app's url dont confilct with another app's url
 
urlpatterns = [
<<<<<<< HEAD
     path('',views.all_products,name='all_products'),
     path('product/<slug:product_slug>/',views.product_detail,name='product_detail'),
     path('category/<slug:category_slug>/',views.category_detail,name='category'),]
=======
     path('',views.all_products,name='all_products')]
     
>>>>>>> 4c91c8f0505e05f4b243f31cc1871d4815965e58
    