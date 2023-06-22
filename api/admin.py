from django.contrib import admin
from .models import Product, UserCart, Order, UserProfile

# Register your models here.
admin.site.register(Product)
admin.site.register(UserCart)
admin.site.register(Order)
admin.site.register(UserProfile)
