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
    class Meta:
        model = models.Products 
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = "__all__"