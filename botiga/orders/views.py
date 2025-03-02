from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comanda, ProducteComanda
from .serializers import ComandaSerializer, ProducteComandaSerializer
from cart.models import Cart, User
from catalog.models import Product

# Vista per veure les comandes d'un usuari
class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer

    def get_queryset(self):
        # Filtrar comandes per usuari si es proporciona usuari_id
        usuari_id = self.request.query_params.get('usuari_id', None)
        if usuari_id:
            return Comanda.objects.filter(usuari_id=usuari_id)
        return Comanda.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            # Validem l'usuari i el carret
            usuari_id = request.data.get('usuari')
            carret = get_object_or_404(Cart, user_id=usuari_id)
            
            # Mirem si el carret té productes
            if not carret.items.exists():
                return Response(
                    {'error': 'El carret està buit'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validem i creem la comanda amb el serializer
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            comanda = serializer.save()

            # Afegim els productes del carret a la comanda
            for item in carret.items.all():
                producte = get_object_or_404(Product, id=item.product_id)
                ProducteComanda.objects.create(
                    comanda=comanda,
                    producte=producte,
                    quantitat=item.quantity,
                    preu=producte.precio  # Usamos el precio del producto
                )

            # Si tot ha anat be, buidem el carret
            carret.items.all().delete()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class ProducteComandaViewSet(viewsets.ModelViewSet):
    queryset = ProducteComanda.objects.all()
    serializer_class = ProducteComandaSerializer

    def get_queryset(self):
        # Filtrar productes per comanda si es proporciona comanda_id
        comanda_id = self.request.query_params.get('comanda_id', None)
        if comanda_id:
            return ProducteComanda.objects.filter(comanda_id=comanda_id)
        return ProducteComanda.objects.all()
