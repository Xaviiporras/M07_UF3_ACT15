from rest_framework import serializers
from .models import Comanda, ProducteComanda

class ProducteComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducteComanda
        fields = ['id', 'comanda', 'producte', 'quantitat', 'preu']

class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['id', 'usuari', 'data_creacio', 'estat', 'preu_total']
        read_only_fields = ['preu_total']  # El preu_total es calcula automàticament
