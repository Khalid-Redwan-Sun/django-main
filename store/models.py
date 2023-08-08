from email.policy import default
from unicodedata import category
from django.db import models
# from matplotlib.cbook import print_cycles
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,db_index=True)
    slug=models.SlugField(max_length=50, unique=True)
    
    class Meta:
        
        verbose_name_plural='categories'
        
    def get_absolute_url(self):
        
        return reverse("store:category", args=[self.slug])##
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='created_products',on_delete=models.CASCADE)#related_name means the name of the field in the other model
    title=models.CharField(max_length=120)
    author=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/',default='images/no image.jpg')
    ##django will automatically create a folder called images inside the media folder
    slug=models.SlugField(max_length=50, unique=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)#
    created=models.DateTimeField(auto_now_add=True) ##auto_now_add=True means that the date will be set to the current date and time when the object is first created.
    updated=models.DateTimeField(auto_now=True) ##auto_now=True means that the date will be set to the current date and time every time the object is saved.
    
    
    class Meta:
        ordering=('-created',)##ordering is used to order the objects in the database.
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])
    
        
    
    
    
    
    
    
    
    
