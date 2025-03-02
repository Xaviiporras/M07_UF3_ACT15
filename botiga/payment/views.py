from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from cart.models import user
from orders.models import Order

@api_view(['GET'])
def get_payments(request):
    payments = Payment.objects.all().values()
    return Response(list(payments), status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_ids(request):
    user_ids = user.objects.values_list('id', flat=True)
    return Response(list(user_ids), status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Orden no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    new_status = request.data.get('status')

    if not new_status or not isinstance(new_status, str):
        return Response({"error": "El estado no puede estar vacío y debe ser un texto válido."}, status=status.HTTP_400_BAD_REQUEST)

    order.status = new_status
    order.save()

    return Response({"message": "Estado actualizado correctamente", "order_id": order.id, "new_status": order.status}, status=status.HTTP_200_OK)