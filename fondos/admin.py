from django.contrib import admin
from fondos.models import Fondo, FondoCuota, FondoHistorico, FondoLiquidez

admin.site.register(Fondo)
admin.site.register(FondoCuota)
admin.site.register(FondoHistorico)
admin.site.register(FondoLiquidez)
