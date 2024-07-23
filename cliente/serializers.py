from rest_framework import serializers
from .models import Cliente, Billetera, CarteraCliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class BilleteraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billetera
        fields = '__all__'
        
class CarteraClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteraCliente
        fields = '__all__'
        
class ReporteBilleterasCliente(serializers.Serializer):
    persona = serializers.CharField()
    billeteras = BilleteraSerializer(many=True)