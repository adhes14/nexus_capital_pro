from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'clientes', views.ClientesViewSet)
#router.register(r'billetera', views.BilleteraViewSet)
#router.register(r'cartera_cliente', views.CarteraClientesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('carteras/', views.CarteraClientesCreateView.as_view()),
    path('billetera_cliente/', views.BilleteraCreateUpdateView.as_view()),
    path('clientes/cantidad/', views.cliente_count),
    path('clientes/cliente_billeteras/<int:cliente_id>/', views.billeteras_por_cliente),
    #path('clientes', views.ClientesViewSet.as_view()),
]