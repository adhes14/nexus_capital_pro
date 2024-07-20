from django.contrib import admin
from .models import Cliente,Billetera,CarteraCliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'num_identificacion', 'habilitado',)
    list_filter = ('num_identificacion', 'habilitado',)
    search_fields = ('nombres', 'apellidos',)
    ordering = ('pk',)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Billetera)
admin.site.register(CarteraCliente)
