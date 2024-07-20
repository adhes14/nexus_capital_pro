from rest_framework import serializers
from .models import Mercado, Activo, PrecioHistorico

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = '__all__'

class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activo
        fields = '__all__'

class PrecioHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioHistorico
        fields = '__all__'