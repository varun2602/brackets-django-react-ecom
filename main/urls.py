from django.urls import path 
from . import views

urlpatterns = [
    path("/vendor-list", views.VendorList.as_view(), name = "vendor-detail"),
    path("/vendor-details/<int:pk>", views.VendorDetail.as_view()),
    path("/product-list", views.ProductList.as_view()),
    path("/product-details/<int:pk>", views.ProductDetails.as_view()),
    path("/product-category-list", views.ProductCategoryList.as_view()),
    path("/product-category-details/<int:pk>", views.ProductCategoryDetails.as_view())
]