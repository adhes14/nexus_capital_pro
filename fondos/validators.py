from datetime import datetime
from django.core.exceptions import ValidationError


def validar_cero(value):
    if value == 0:
        raise ValidationError("El valor no puede ser cero")


def validar_fecha_futura(value):
    if value > datetime.now().date():
        raise ValidationError(f"La fecha {value} no puede ser futura")
