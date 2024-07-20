from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activo/', include('activo.urls')),
    path('cliente/', include('cliente.urls')),
    path('fondos/', include('fondos.urls')),
]
