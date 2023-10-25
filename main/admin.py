from django.contrib import admin
from . import models

@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "address"] 

@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "details"]

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "vendor", "title", "details", "price"]
    
