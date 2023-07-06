from django.urls import path
from . import views

app_name='store' 
 #this is used to avoid name conflict,each app has its own namespace,,so one app's url dont confilct with another app's url
 
urlpatterns = [
     path('',views.all_products,name='all_products')]
     
    