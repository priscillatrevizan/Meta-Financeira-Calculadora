from django.shortcuts import render
from django.views import View
from .forms import CalculadoraInvestimentoForm

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
                # Cálculo com taxa de juros
                meses = calcular_resultado_com_taxa(valor_economia, valor_mensal, taxa_juros)
                resultado = f"Com uma taxa de juros de {taxa_juros}%, você levará {meses} meses para economizar R${valor_economia:.2f}."
            else:
                # Cálculo sem taxa de juros
                meses = calcular_resultado_sem_taxa(valor_economia, valor_mensal)
                resultado = f"Sem taxa de juros, você levará {meses} meses para economizar R${valor_economia:.2f}."

        return render(request, self.template_name, {'form': form, 'resultado': resultado})

def calcular_resultado_com_taxa(valor_economia, valor_mensal, taxa_juros):
    # Cálculo com taxa de juros
    meses = 0
    resultado = valor_mensal

    while resultado < valor_economia:
        resultado += valor_mensal
        resultado += (resultado * taxa_juros / 100)  # Juros mensais
        meses += 1

    return meses

def calcular_resultado_sem_taxa(valor_economia, valor_mensal):
    # Cálculo sem taxa de juros
    meses = valor_economia / valor_mensal
    return int(meses)