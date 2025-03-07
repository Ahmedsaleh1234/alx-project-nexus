from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_decription = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='product_images')
    def __str__(self):
        return self.product_name
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField(default=1)
    