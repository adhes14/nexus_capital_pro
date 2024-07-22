from rest_framework import serializers
from .models import (
    Fondo,
    FondoCuota,
    FondoHistorico,
    FondoLiquidez,
    Posicion,
    Transaccion,
)


class FondoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fondo
        fields = "__all__"


class FondoCuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FondoCuota
        fields = "__all__"


class FondoHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FondoHistorico
        fields = "__all__"


class FondoLiquidezSerializer(serializers.ModelSerializer):
    class Meta:
        model = FondoLiquidez
        fields = "__all__"


class PosicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posicion
        fields = "__all__"


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = "__all__"
