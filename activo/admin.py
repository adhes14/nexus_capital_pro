from django.contrib import admin
from .models import Mercado, Activo, PrecioHistorico

class MercadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horario',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.register(Mercado, MercadoAdmin)

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mercado', 'ticker', 'moneda',)
    list_filter = ('nombre', 'mercado', 'ticker',)
    search_fields = ('nombre', 'mercado', 'ticker', 'moneda',)
    ordering = ('nombre', 'ticker', 'moneda',)

admin.site.register(Activo, ActivoAdmin)

class PrecioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('activo', 'fecha', 'precio_cierre',)
    list_filter = ('activo', 'fecha',)
    search_fields = ('activo__nombre', 'fecha', 'precio_cierre',)
    ordering = ('activo',)

admin.site.register(PrecioHistorico, PrecioHistoricoAdmin)
