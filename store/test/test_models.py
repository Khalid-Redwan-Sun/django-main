from unicodedata import category
from django.test import TestCase
from matplotlib import image
from matplotlib.pyplot import title # Import the test case class
from store.models import Category, Product # Import the Category and Product models
from django.contrib.auth.models import User # Import the User model

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1=Category.objects.create(name='games',slug='games')
        
    def test_category_model_entry(self):
        
        data=self.data1
        self.assertTrue(isinstance(data,Category)) # Check if the data is an instance of the Category model
        
    def test_category_str_test(self):
        
        data=self.data1
        
        self.assertEqual(str(data),'games') # Check if the string representation of the data is correct
        
    def test_category_url(self):
        data_url=self.data1.get_absolute_url()
       
        self.assertEqual(data_url,'/category/games/')
        

class TestProductsModel(TestCase):
    
    def setUp(self):
        
        Category.objects.create(name='book',slug='book')
       
        User.objects.create_user(username='admin')
       
        self.data1=Product.objects.create(created_by=User.objects.get(username='admin'),category=Category.objects.get(name='book'), title='django', author='richard', description='its a book', image='images/', slug='django', price=10.00, in_stock=True, is_active=True)
       
    def test_products_model_entry(self):
     
        self.assertTrue(isinstance(self.data1,Product)) # Check if the data is an instance of the Product model
        
        
    def test_product_title(self):
        data=self.data1
        self.assertEqual(str(data),'django')
        
    def test_product_url(self):
        data_url=self.data1.get_absolute_url()
        self.assertEqual(data_url,'/product/django/')
        
        
        
        