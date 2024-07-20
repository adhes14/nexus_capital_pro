from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Mercado, Activo, PrecioHistorico
from .serializers import MercadoSerializer, ActivoSerializer, PrecioHistoricoSerializer

def index(request):
    return HttpResponse("Hola estamos en el index de la App 'ACTIVOS'")    

class MercadoViewSet(viewsets.ModelViewSet):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

class ActivoViewSet(viewsets.ModelViewSet):
    queryset= Activo.objects.all()
    serializer_class = ActivoSerializer

class PrecioHistoricoViewSet(viewsets.ModelViewSet):
    queryset = PrecioHistorico.objects.all()
    serializer_class = PrecioHistoricoSerializer