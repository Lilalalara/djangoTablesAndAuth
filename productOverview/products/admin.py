from django.contrib import admin
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'user')
