from django.contrib import admin
from . import models
from django.contrib.sessions.models import Session 

@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "address"] 

@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "details"]

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "vendor", "title", "details", "price"]

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "mobile"]

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "order_time"]

@admin.register(models.OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product"]


# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display = ["session_key", "expire_session", "get_session_data"]
#     list_filter = ["expire_session"]

#     def get_session_data(self, obj):
#         session = SessionStore(session_key=obj.session_key)
#         return session.load()

#     get_session_data.short_description = "Session Data"
    
    
