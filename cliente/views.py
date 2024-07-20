from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo estamos en index Cliente")

# Create your views here.
from rest_framework import viewsets
from .models import Cliente, Billetera, CarteraCliente
from .serializers import ClienteSerializer, BilleteraSerializer, CarteraClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class BilleteraViewSet(viewsets.ModelViewSet):
    queryset = Billetera.objects.all()
    serializer_class = BilleteraSerializer
    
class CarteraClientesViewSet(viewsets.ModelViewSet):
    queryset = CarteraCliente.objects.all()
    serializer_class = CarteraClienteSerializer