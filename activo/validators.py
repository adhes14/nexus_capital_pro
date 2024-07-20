from django.core.exceptions import ValidationError
from datetime import time
import re


def validar_hora(valor_hora):
    if not isinstance(valor_hora, time):
        raise ValidationError(f'{valor_hora} no es un formato valido de Horario')
    
def validar_no_caracteres_especiales(texto):
    if not re.match("^[a-zA-Z0-9\s]*$", texto):
        raise ValidationError('El texto no debe contener caracteres especiales.')