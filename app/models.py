from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    
    class Meta:
        verbose_name_plural="Categories"
    

class Product(models.Model):
    first_name = models.CharField(max_length=50) #max_length param is required
    price = models.FloatField(default=0)
    created_at=models.DateField(auto_now_add=True,null=True)
    modified_at=models.DateField(auto_now=True,null=True)
    desc=models.TextField(null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )





