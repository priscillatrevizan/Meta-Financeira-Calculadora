from django import forms
from .models import CalculadoraInvestimento

class CalculadoraInvestimentoForm(forms.ModelForm):
    class Meta:
        model = CalculadoraInvestimento
        fields = ['valor_economia', 'valor_mensal', 'taxa_juros']
