from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from .models import Mercado, Activo, PrecioHistorico
from rest_framework.decorators import api_view
from .serializers import MercadoSerializer, ActivoSerializer, PrecioHistoricoSerializer

def index(request):
    return HttpResponse("Hola estamos en el index de la App 'ACTIVOS'")    

#Agregando ModelsViewSet
class MercadoViewSet(viewsets.ModelViewSet):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

class ActivoViewSet(viewsets.ModelViewSet):
    queryset= Activo.objects.all()
    serializer_class = ActivoSerializer

class PrecioHistoricoViewSet(viewsets.ModelViewSet):
    queryset = PrecioHistorico.objects.all()
    serializer_class = PrecioHistoricoSerializer

# Agregando GenericAPIView 
class ActivoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer

class ActivoUpdateView(generics.UpdateAPIView):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer

class MercadoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

# Agregando Custom API
    
@api_view(['GET'])
def activos_dolar(request):
    """
    Lista de Activos en moneda Dolar
    """
    try:
        activos = Activo.objects.filter(moneda='usd')
        return JsonResponse(
            ActivoSerializer(activos, many=True).data,
            safe=False,
            status=200)
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )