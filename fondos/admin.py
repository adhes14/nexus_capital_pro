from django.contrib import admin
from fondos.models import Fondo, FondoCuota, FondoHistorico, FondoLiquidez

class FondoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio')
    search_fields = ('nombre', 'fecha_inicio')
    list_filter = ('fecha_inicio',)
    ordering = ('nombre',)

admin.site.register(Fondo, FondoAdmin)

class FondoCuotaAdmin(admin.ModelAdmin):
    list_display = ('fondo', 'fecha', 'cantidad_cuotas', 'concepto')
    search_fields = ('fondo__nombre', 'fecha', 'concepto')
    list_filter = ('fondo', 'fecha')
    ordering = ('fondo', 'fecha')

admin.site.register(FondoCuota, FondoCuotaAdmin)

class FondoHistoricoAdmin(admin.ModelAdmin):
    list_display = ('fondo', 'fecha', 'valor_cuota', 'liquidez', 'cartera', 'cantidad_cuotas')
    search_fields = ('fondo__nombre', 'fecha')
    list_filter = ('fondo', 'fecha')
    ordering = ('fondo', 'fecha')

admin.site.register(FondoHistorico, FondoHistoricoAdmin)

class FondoLiquidezAdmin(admin.ModelAdmin):
    list_display = ('fondo', 'fecha', 'importe', 'concepto')
    search_fields = ('fondo__nombre', 'fecha', 'concepto')
    list_filter = ('fondo', 'fecha')
    ordering = ('fondo', 'fecha')

admin.site.register(FondoLiquidez, FondoLiquidezAdmin)
