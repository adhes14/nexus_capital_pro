from django.db import models

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
    fecha = models.DateField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.fondo.nombre} - {self.fecha}'