from django.db import models

class CalculadoraInvestimento(models.Model):
    valor_economia = models.DecimalField(max_digits=10, decimal_places=2)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    data_inicio = models.DateField()
