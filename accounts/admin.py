from django.contrib import admin
from .models import Product
# Register your models here.

# Registerign Product Model
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin) 