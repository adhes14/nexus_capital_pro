from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Hola mundo estamos en index Cliente")

# Create your views here.
from rest_framework import viewsets
from .models import Cliente, Billetera, CarteraCliente
from .serializers import ClienteSerializer, BilleteraSerializer, CarteraClienteSerializer, ReporteBilleterasCliente

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    


class BilleteraViewSet(viewsets.ModelViewSet):
    queryset = Billetera.objects.all()
    serializer_class = BilleteraSerializer
    
class CarteraClientesViewSet(viewsets.ModelViewSet):
    queryset = CarteraCliente.objects.all()
    serializer_class = CarteraClienteSerializer
    

class BilleteraCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView, generics.ListAPIView):
    queryset = Billetera.objects.all()
    serializer_class = BilleteraSerializer

class CarteraClientesCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = CarteraCliente.objects.all()
    serializer_class = CarteraClienteSerializer

@api_view(['GET'])
def cliente_count(request):
    """
    Cuenta la cantidad de Clientes
    """
    try:
        cantidad = Cliente.objects.count()
        return JsonResponse(
            {
                "cantidad":cantidad
            },
            safe = False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe= False,
            status=400
        )


@api_view(['GET'])
def billeteras_por_cliente(request, cliente_id):
    """
    Obtiene todas las billeteras asociadas a un cliente por su ID
    """
    try:
        cliente = get_object_or_404(Cliente, id=cliente_id)
        billeteras = Billetera.objects.filter(cliente_id=cliente_id)
        
        # Prepara los datos para el serializer
        data = {
            "persona": cliente.nombres + " " + cliente.apellidos,  # Asume que 'nombre' es el campo relevante en Cliente
            "billeteras": billeteras
        }
        
        # Serializa los datos
        serializer = ReporteBilleterasCliente(data)
        return JsonResponse(
            serializer.data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )