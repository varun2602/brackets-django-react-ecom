from django.urls import path 
from . import views

urlpatterns = [
    path("/vendor-list", views.VendorList.as_view(), name = "vendor-detail"),
    path("/vendor-details/<int:pk>", views.VendorDetail.as_view()),
    path("/product-list", views.ProductList.as_view()),
    path("/product-details/<int:pk>", views.ProductDetails.as_view()),
    path("/product-category-list", views.ProductCategoryList.as_view()),
    path("/product-category-details/<int:pk>", views.ProductCategoryDetails.as_view()),
    path("/customer-list", views.CustomerList.as_view()),
    path("/customer-details/<int:pk>", views.CustomerDetails.as_view()),
    path("/order-list", views.OrderList.as_view()),
    path("/order-details/<int:pk>", views.OrderDetails.as_view()),
    path("/order-item-list", views.OrderItemList.as_view()),
    path("/order-item-details/<int:pk>", views.OrderItemDetails.as_view()),
    path("/customer-address-list", views.CustomerAddressModelList.as_view),
    path("/customer-address-details/<int:pk>", views.CustomerAddrressModelDetails.as_view()),
    path("/product-ratings-list", views.ProductRatingsList.as_view()),
    path("/product-ratings-details", views.ProductRatingsDetails.as_view())
]