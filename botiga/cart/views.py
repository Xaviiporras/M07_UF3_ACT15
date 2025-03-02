from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Cart, CartItem, User  

def afegir_al_carreto(request, user_id, product_id, quantity=1):
    # Comprovem si l'usuari existeix
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"missatge": "L'usuari no existeix"}, status=404)

    # Comprovem si l'usuari ja té un carretó
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        # Si no en té, el creem
        cart = Cart(user=user)
        cart.save()

    # Comprovem si el producte ja està al carretó
    try:
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        # Si ja està al carretó, sumem la quantitat
        cart_item.quantity += quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        # Si no està al carretó, el creem amb la quantitat indicada
        cart_item = CartItem(cart=cart, product_id=product_id, quantity=quantity)
        cart_item.save()

    return JsonResponse({
        "missatge": "Producte afegit al carretó",
        "carreto_id": cart.id,
        "producte_id": product_id,
        "quantitat": cart_item.quantity
    })