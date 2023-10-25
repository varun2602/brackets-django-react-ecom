from django.shortcuts import render
from . import serializers
from rest_framework import generics, permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import models

# Vendor CRUD 
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    authentication_classes = [JWTAuthentication]

# Product CRUD 
class ProductList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer 
    authentication_classes = [JWTAuthentication] 

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer 
    authentication_classes = [JWTAuthentication]

# Product Category crud 
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer
    authentication_classes = [JWTAuthentication] 

class ProductCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all() 
    serializer_class = serializers.ProductCategorySerializer 
    authentication_classes = [JWTAuthentication]


# To continue from 11th min of part 7

    

