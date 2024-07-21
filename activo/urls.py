from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mercados', views.MercadoViewSet)
router.register(r'activos', views.ActivoViewSet)
router.register(r'preciosHistoricos', views.PrecioHistoricoViewSet)

urlpatterns = [
    #path('', views.index),
    path('', include(router.urls)),
    # path('activos/crear/', views.ActivoCreateView.as_view()),
    # path('activos/actualizar/', views.ActivoUpdateView.as_view()),
    # path('mercados/crear/', views.MercadoCreateView.as_view()),
    path('activos/filtrar/dolar', views.activos_dolar)
]