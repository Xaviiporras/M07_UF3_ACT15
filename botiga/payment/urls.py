from django.urls import path
from .views import get_payments, get_user_ids, update_order_status

urlpatterns = [
    path('payments/', get_payments, name='get_payments'),
    path('users/ids/', get_user_ids, name='get_user_ids'),
    path('orders/<int:order_id>/update_status/', update_order_status, name='update_order_status'),
]
