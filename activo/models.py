from django.db import models

class Mercado(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    horario = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Activo(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nombre

class MonedaVal(models.TextChoices):
    USD = 'usd', 'DOLAR'
    EUR = 'eur', 'EURO'

class PrecioHistorico(models.Model):
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    fecha = models.DateField()
    precio_cierre = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(
        max_length=3,
        choices=MonedaVal.choices,
        default=MonedaVal.USD,
    )


