from ftplib import all_errors
from http.client import responses
import imp

from unicodedata import category
from unittest import skip
from urllib import request
from django.http import HttpRequest
from django.test import TestCase,Client                             
from django.contrib.auth.models import User
from store.models import Category,Product
from django.urls import reverse
from store.views import all_products



class TestViewResponses(TestCase):
    def setUp(self):
        self.c=Client()#create a client object 
        
          
        Category.objects.create(name='book',slug='book')
       
        User.objects.create_user(username='admin')
        Product.objects.create(created_by=User.objects.get(username='admin'),category=Category.objects.get(name='book'), title='django', author='richard', description='its a book', image='images/', slug='django', price=10.00, in_stock=True, is_active=True)
        
    def test_url_allowed_hosts(self):
        
        response=self.c.get('/',HTTP_HOST='mydomain.com')#check if the url is allowed
        self.assertEqual(response.status_code,200) # Check if the response code is 200

        response=self.c.get('/',HTTP_HOST='wrongdomain.com')#check if the url is allowed
        self.assertEqual(response.status_code,400) # Check if the response code is 200
    
    

    
        
    def test_product_url(self):##i did the same test in test_model.py 
        response=self.c.get(reverse('store:product_detail',args=['django']))
        self.assertEqual(response.status_code,200)
        
    def test_category_url(self):##i did the same test in test_model.py 
        response=self.c.get(reverse('store:category',args=['book']))
        self.assertEqual(response.status_code,200)
        
    def test_homepage_html(self):##to test the html file
        request=HttpRequest()#create a request object
        response=all_products(request)#call the view passing the request object
        html=response.content.decode('utf8')#get the html content ,utf8 is the encoding of the html file
        print(html)
        print(type(html))
        self.assertIn('<title>Homepage</title>',html)#check if the html file contains the text
        self.assertEqual(response.status_code,200)#check if the response code is 200
        
        
    ##read advanced testing,,,django ecommerce er first video er last er dike
        
        
    