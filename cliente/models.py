from django.db import models
from .validators import validar_solo_numeros, validar_numeros_negativos

class Cliente (models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, validators=[validar_solo_numeros])
    num_identificacion = models.CharField(max_length=20, validators=[validar_solo_numeros])
    ciudad = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    habilitado = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos
    
class Billetera (models.Model):
    fecha = models.DateField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    concepto = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cliente.nombres + " " + str(self.pk)

class CarteraCliente (models.Model):
    cant_cuotas = models.DecimalField(max_digits=10, decimal_places=5, validators=[validar_numeros_negativos])
    valor_cuota = models.DecimalField(max_digits=10, decimal_places=5, validators=[validar_numeros_negativos])
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cliente.nombres + " " + str(self.pk)
    