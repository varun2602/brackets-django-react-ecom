from django.db import models
from django.contrib.auth.models import User


# Vendor Model 
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.user.username}"

class ProductCategory(models.Model):
    title = models.CharField(max_length = 200, blank = True, null = True)
    details = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.title}"
    
class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank = True, null = True, related_name="category_products")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank = True, null = True, related_name = "productvendor")
    title = models.CharField(max_length = 200)
    details = models.TextField(null = True, blank = True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title}"
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username
 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.user.username}'s order" 
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"order of {self.product} by {self.order.customer.user.username}"
    
class CustomerAddressModel(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name= "customer_addresses")
    address = models.TextField(blank = True, null = True, max_length = 200)

    def __str__(self):
        return f"Address of {self.customer.user.username}"
    
class ProductRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, related_name= "rating_customers")
    product = models.ForeignKey(Products, on_delete= models.CASCADE, related_name="product_ratings")
    rating = models.IntegerField()
    reviews = models.TextField(blank = True, null = True, max_length = 500)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviews for {self.product.title} by {self.customer.user.username}"
