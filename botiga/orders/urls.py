from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Creem el router
router = DefaultRouter()
router.register(r'comandes', views.ComandaViewSet)
router.register(r'productes-comanda', views.ProducteComandaViewSet)

# Definim les URLs
urlpatterns = [
    path('', include(router.urls)),
]
