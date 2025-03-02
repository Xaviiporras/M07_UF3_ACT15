from django.db import models
from orders.models import Comanda
from cart.models import User

class Payment(models.Model):
    order_id = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name="payments")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    numero_tarjeta = models.CharField(max_length=16)
    fecha_caducidad = models.CharField(max_length=5) 
    cvc = models.CharField(max_length=3)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('fallido', 'Fallido')])
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago {self.id} - Order_id: {self.order_id} - Estado: {self.estado}'
