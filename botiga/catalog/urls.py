from django.urls import path
from .views import product_list, create_product, product_detail, update_product, delete_product

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/create/', create_product, name='create-product'), 
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('products/<int:pk>/update/', update_product, name='update-product'),
    path('products/<int:pk>/delete/', delete_product, name='delete-product'),
]
