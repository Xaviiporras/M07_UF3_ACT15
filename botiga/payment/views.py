from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from botiga.cart import user

@api_view(['GET'])
def get_payments(request):
    payments = Payment.objects.all().values()
    return Response(list(payments), status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_ids(request):
    user_ids = user.objects.values_list('id', flat=True)
    return Response(list(user_ids), status=status.HTTP_200_OK)