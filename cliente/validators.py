from django.core.exceptions import ValidationError


def validar_solo_numeros(value):
    if not value.isdigit():
        raise ValidationError("%(valor)s contiene otros caracteres no numéricos", params={'valor': value})
        print("La variable contiene otros caracteres además de números.")
    else:
        print("La variable contiene solo números.")
        
def validar_numeros_negativos(value):
    if value < 0:
        raise ValidationError("%(valor)s No puede ser negativo", params={'valor': value})
        print("No puede ser negativo.")
    else:
        print("La variable es positiva.")