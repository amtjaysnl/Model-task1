from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=254)
    contact_number = models.IntegerField()
    address = models.TextField()

class Sell(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    upload_at = models.DateTimeField(auto_now=True)
    seller_contact_number = models.IntegerField()
    description = models.TextField()
