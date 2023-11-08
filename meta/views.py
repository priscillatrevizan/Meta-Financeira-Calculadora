from django.shortcuts import render
from django.views import View
from .forms import CalculadoraInvestimentoForm
import math

class Home(View):
    template_name = 'meta/calculadora_investimento.html'

    def get(self, request):
        form = CalculadoraInvestimentoForm()
        resultado = None
        return render(request, self.template_name, {'form': form, 'resultado': resultado})

    def post(self, request):
        form = CalculadoraInvestimentoForm(request.POST)
        resultado = None

        if form.is_valid():
            valor_economia = form.cleaned_data['valor_economia']
            valor_mensal = form.cleaned_data['valor_mensal']
            taxa_juros = form.cleaned_data['taxa_juros']

            if taxa_juros is not None and taxa_juros > 0:
                meses = calcular_resultado_com_taxa(valor_economia, valor_mensal, taxa_juros)
                resultado = f"Com uma taxa de rendimento de {taxa_juros}% ao mês, você levará aproximadamente {meses} meses para economizar R${valor_economia:.2f}."
            else:
                meses = calcular_resultado_sem_taxa(valor_economia, valor_mensal)
                resultado = f"Sem aplicar em um local com taxa de rendimento, você levará aproximadamente {meses} meses para economizar R${valor_economia:.2f}."

        return render(request, self.template_name, {'form': form, 'resultado': resultado})

def calcular_resultado_com_taxa(valor_desejado, valor_mensal, taxa_juros):
    if taxa_juros <= 0:
        return valor_desejado // valor_mensal  

    meses = 0
    resultado = valor_mensal

    while resultado < valor_desejado:
        resultado += resultado * (taxa_juros / 100)  
        resultado += valor_mensal  
        meses += 1

    return int(meses) 

def calcular_resultado_sem_taxa(valor_economia, valor_mensal):
    meses = valor_economia / valor_mensal
    return meses

