from django.db import models
from cart.models import User
from catalog.models import Product

# Model per les comandes
class Comanda(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    data_creacio = models.DateTimeField(auto_now_add=True)
    estat = models.CharField(max_length=20, default='pendent')
    preu_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_preu_total(self):
        total = 0
        for producte in self.productecomanda_set.all():
            total += producte.preu * producte.quantitat
        return total

    def save(self, *args, **kwargs):
        if self.pk:  # Si la comanda ja existeix
            self.preu_total = self.calcular_preu_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comanda {self.id} de {self.usuari.username}"

# Model pels productes de cada comanda
class ProducteComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    producte = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantitat = models.IntegerField()
    preu = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.comanda.save()  # Actualitzar el preu_total de la comanda

    def __str__(self):
        return f"Producte {self.producte_id} de comanda {self.comanda.id}"
