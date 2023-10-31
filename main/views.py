from django.shortcuts import render
from . import serializers
from rest_framework import generics, permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import LimitOffsetPagination
from . pagination import CustomPagination
from . import models

# Vendor CRUD 
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

# Product CRUD 
class ProductList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer 
    authentication_classes = [JWTAuthentication] 
    pagination_class = CustomPagination

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

# Product Category crud 
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer
    authentication_classes = [JWTAuthentication] 
    pagination_class = CustomPagination

class ProductCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all() 
    serializer_class = serializers.ProductCategorySerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

# Customer CRUD 
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer 
    authentication_classes = [JWTAuthentication] 
    pagination_class = CustomPagination

# Oder crud  
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     order_id = self.kwargs['pk']
    #     order = models.Order.objects.get(id = order_id)
    #     order_items = models.OrderItems.objects.filter(order=order)
    #     return order_items

# Order Item CRUD  

class OrderItemList(generics.ListCreateAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemSerializer 
    authentication_classes = [JWTAuthentication] 
    pagination_class = CustomPagination

class OrderItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    

# Customer Address CRUD
class CustomerAddressModelList(generics.ListCreateAPIView):
    queryset = models.CustomerAddressModel.objects.all()
    serializer_class = serializers.CustomerAddressModelSerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination 

class CustomerAddrressModelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomerAddressModel.objects.all()
    serializer_class = serializers.CustomerAddressModelSerializer
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination 


# Product Rating CRUD 
class ProductRatingsList(generics.ListCreateAPIView):
    queryset = models.ProductRating.objects.all()
    serializer_class = serializers.ProductRatingSerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination 

class ProductRatingsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductRating.objects.all()
    serializer_class = serializers.ProductRatingSerializer 
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

# Continue from12th video, 12th minute 












    

