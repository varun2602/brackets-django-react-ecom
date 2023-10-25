from django.shortcuts import render
from . import serializers
from rest_framework import generics, permissions, authentication
from . import models

class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    authentication_classes = [authentication.SessionAuthentication]

    

