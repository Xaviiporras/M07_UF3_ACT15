from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment

@api_view(['GET'])
def get_payments(request):
    payments = Payment.objects.all().values()
    return Response(list(payments), status=status.HTTP_200_OK)
