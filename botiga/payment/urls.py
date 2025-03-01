from django.urls import path
from .views import get_payments, get_user_ids

urlpatterns = [
    path('payments/', get_payments, name='get_payments'),
    path('users/ids/', get_user_ids, name='get_user_ids'),
]
