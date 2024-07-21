from django.db import models
from activo.models import Activo
from .validators import validar_cero, validar_fecha_futura


class Fondo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre
    
class FondoCuota(models.Model):
    fondo = models.ForeignKey(Fondo, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad_cuotas = models.IntegerField()
    concepto = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.fondo.nombre} - {self.fecha}'
    
class FondoHistorico(models.Model):
    fondo = models.ForeignKey(Fondo, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor_cuota = models.DecimalField(max_digits=10, decimal_places=2)
    liquidez = models.DecimalField(max_digits=10, decimal_places=2)
    cartera = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_cuotas = models.IntegerField()

    def __str__(self):
        return f'{self.fondo.nombre} - {self.fecha}'
    
class FondoLiquidez(models.Model):
    fondo = models.ForeignKey(Fondo, on_delete=models.CASCADE)
    fecha = models.DateField(validators=[validar_fecha_futura])
    importe = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_cero])
    concepto = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.fondo.nombre} - {self.fecha}'
    
class Posicion(models.Model):
    fondo = models.ForeignKey(Fondo, on_delete=models.CASCADE)
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    abierta = models.BooleanField()

    def __str__(self):
        return f'{self.fondo.nombre} - {self.activo.nombre}'

class TipoTransaccion(models.TextChoices):
    COMPRA = 'compra', 'COMPRA'
    VENTA = 'venta', 'VENTA'

class Transaccion(models.Model):
    posicion = models.ForeignKey(Posicion, on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=6,
        choices=TipoTransaccion.choices,
    )
    fecha = models.DateField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=5)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    comision = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.posicion.fondo.nombre} - {self.posicion.activo.nombre} - {self.fecha}'