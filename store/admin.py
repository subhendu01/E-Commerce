from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.cutomer import Customer
from .models.orders import Orders

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCutomer(admin.ModelAdmin):
    list_display = ['first_name']

# class AdminOrders(admin.ModelAdmin):
#     list_display = ['first_name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCutomer)
admin.site.register(Orders)
