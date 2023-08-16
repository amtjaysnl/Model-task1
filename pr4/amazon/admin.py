from django.contrib import admin
from amazon.models import Customer
from amazon.models import Sell
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email_id','contact_number','address')

admin.site.register(Customer, CustomerAdmin)

class SellAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','upload_at','seller_contact_number','description')

admin.site.register(Sell, SellAdmin)


