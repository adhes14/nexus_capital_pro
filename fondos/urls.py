from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact, name='contact'),
    path('', views.index, name='fondos'),
    path('fondo_liquidez', views.fondoLiquidezFormView, name='fondo_liquidez'),
]