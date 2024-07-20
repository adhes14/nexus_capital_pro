from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'clientes', views.ClientesViewSet)
router.register(r'billetera', views.BilleteraViewSet)
router.register(r'cartera_cliente', views.CarteraClientesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]