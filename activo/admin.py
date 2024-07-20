from django.contrib import admin
from .models import Mercado, Activo, PrecioHistorico

admin.site.register(Mercado)
admin.site.register(Activo)
admin.site.register(PrecioHistorico)
