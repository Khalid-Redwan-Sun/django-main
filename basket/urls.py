from . import views
from django.urls import path


app_name = 'basket'
urlpatterns = [
    path('basket/', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='basket_add'),

     
   

]
