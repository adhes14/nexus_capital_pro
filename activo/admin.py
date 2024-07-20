from django.contrib import admin
from .models import Mercado, Activo, PrecioHistorico

class MercadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horario',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.register(Mercado, MercadoAdmin)

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mercado', 'ticker',)
    list_filter = ('nombre', 'mercado', 'ticker',)
    search_fields = ('nombre', 'mercado', 'ticker',)
    ordering = ('nombre', 'ticker',)

admin.site.register(Activo, ActivoAdmin)

class PrecioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('activo', 'fecha', 'precio_cierre', 'moneda',)
    list_filter = ('activo', 'fecha',)
    search_fields = ('activo__nombre', 'fecha', 'precio_cierre', 'moneda',)
    ordering = ('activo', 'moneda')

admin.site.register(PrecioHistorico, PrecioHistoricoAdmin)
