"""
URL configuration for botiga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cart import views as cart_views
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('payment/', include('payment.urls')),  # URLs de payment al mismo nivel que catalog
    path('api/', include([
        path('cart/add/<int:user_id>/<int:product_id>/', cart_views.afegir_al_carreto, name='add_to_cart'),
        path('', include('orders.urls')),  # Incluye todas las URLs de orders
    ])),
    # Afegim l'API browser de DRF
    path('api-auth/', include('rest_framework.urls')),
]
