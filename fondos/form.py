from django import forms
from .models import FondoLiquidez

class FondoLiquidezForm(forms.ModelForm):
    class Meta:
        model = FondoLiquidez
        fields = '__all__'