from rest_framework import serializers 
from . import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor 
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(VendorSerializer, self).__init__(*args, **kwargs)
    #     self.Meta.depth = 1

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor 
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(VendorSerializer, self).__init__(*args, **kwargs)
    #     self.Meta.depth = 1

class ProductSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = models.Products 
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer 
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order 
        fields = "__all__" 
    
    # Access the customer through the related Order
    # customer = serializers.SerializerMethodField()

    # def get_customer(self, obj):
    #     return obj.order.customer.user.username

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems 
        fields = "__all__"

class CustomerAddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddressModel 
        fields = "__all__"

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating 
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
    
    

















