from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"fondos", views.FondosViewSet)
router.register(r"fondo_cuota", views.FondoCuotaViewSet)
router.register(r"fondo_historico", views.FondoHistoricoViewSet)
router.register(r"fondo_liquidez", views.FondoLiquidezViewSet)
router.register(r"transaccion", views.TransaccionViewSet)
router.register(r"posicion", views.PosicionViewSet)

urlpatterns = [
    path("contact/<str:name>", views.contact, name="contact"),
    path("formulario", views.index, name="fondos"),
    path("fondo_liquidez", views.fondoLiquidezFormView, name="fondo_liquidez"),
    path("", include(router.urls)),
    path("generic", views.FondosGenericView.as_view(), name="fondos_generic"),
    path("saldo_liquidez", views.saldo_liquidez, name="saldo_liquidez"),
]
