from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Fondo, FondoLiquidez
from .form import FondoLiquidezForm

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
