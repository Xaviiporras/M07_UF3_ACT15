from django.db import models
from catalog.models import Product

#Modelo de Usuario
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

#Modelo de Carrito
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#Modelo de Item de Carrito
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x Producto {self.product_id} en carrito {self.cart.id}"