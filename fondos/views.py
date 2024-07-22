from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import (
    Fondo,
    FondoLiquidez,
    FondoCuota,
    FondoHistorico,
    Posicion,
    Transaccion,
)
from .form import FondoLiquidezForm
from rest_framework import viewsets, generics
from .serializers import (
    FondoSerializer,
    FondoCuotaSerializer,
    FondoHistoricoSerializer,
    FondoLiquidezSerializer,
    PosicionSerializer,
    TransaccionSerializer,
)
from django.db.models import Sum, DecimalField
from rest_framework.decorators import api_view


def index(request):
    post_nombre = request.POST.get("nombre")
    post_fecha_inicio = request.POST.get("fecha_inicio")
    if post_nombre and post_fecha_inicio:
        q = Fondo(nombre=post_nombre, fecha_inicio=post_fecha_inicio)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Fondo.objects.filter(nombre__icontains=filtro_nombre)
    else:
        categorias = Fondo.objects.all()
    return render(request, "fondos/fondos.html", {"categorias": categorias})


def contact(request, name):
    return HttpResponse(f"Hola {name}, estamos en la App 'FONDOS'")


def fondoLiquidezFormView(request):
    form = FondoLiquidezForm()
    fondo_liquidez = None
    id_fondo_liquidez = request.GET.get("id")
    if id_fondo_liquidez:
        fondo_liquidez = get_object_or_404(FondoLiquidez, id=id_fondo_liquidez)
        form = FondoLiquidezForm(instance=fondo_liquidez)

    print(fondo_liquidez)

    if request.method == "POST":
        if fondo_liquidez:
            form = FondoLiquidezForm(request.POST, instance=fondo_liquidez)
        else:
            form = FondoLiquidezForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "fondos/fondo_liquidez_form.html", {"form": form})


class FondosViewSet(viewsets.ModelViewSet):
    queryset = Fondo.objects.all()
    serializer_class = FondoSerializer


class FondosGenericView(
    generics.ListCreateAPIView, generics.CreateAPIView, generics.UpdateAPIView
):
    queryset = Fondo.objects.all()
    serializer_class = FondoSerializer


class FondoCuotaViewSet(viewsets.ModelViewSet):
    queryset = FondoCuota.objects.all()
    serializer_class = FondoCuotaSerializer


class FondoHistoricoViewSet(viewsets.ModelViewSet):
    queryset = FondoHistorico.objects.all()
    serializer_class = FondoHistoricoSerializer


class FondoLiquidezViewSet(viewsets.ModelViewSet):
    queryset = FondoLiquidez.objects.all()
    serializer_class = FondoLiquidezSerializer


class PosicionViewSet(viewsets.ModelViewSet):
    queryset = Posicion.objects.all()
    serializer_class = PosicionSerializer


class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer


@api_view(["GET"])
def saldo_liquidez(request):
    """
    Obtiene el saldo de liquidez de un fondo
    """

    try:
        fondo_id = request.GET.get("fondo_id")
        saldo = FondoLiquidez.objects.filter(fondo_id=fondo_id).aggregate(
            Sum("importe", output_field=DecimalField())
        )["importe__sum"]
        return JsonResponse(
            {"saldo": saldo},
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            safe=False,
            status=500,
        )
