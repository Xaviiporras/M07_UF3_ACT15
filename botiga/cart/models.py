from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)