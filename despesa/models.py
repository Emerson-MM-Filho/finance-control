from datetime import datetime

from django.db import models
from cartao.models import Cartao
from categoria.models import Categoria

class Despesa(models.Model):
    tipo_choices = (
        ('Crédito', 'Crédito'),
        ('Débito', 'Débito'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    categoria = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.DO_NOTHING)
    data_da_despesa = models.DateField(default=datetime.now, blank=False, null=False)
    parcelas = models.IntegerField(null=True, blank=True)
    cartao = models.ForeignKey(Cartao, null=False, blank=False, on_delete=models.DO_NOTHING, default=Cartao.objects.first().id)
    tipo = models.CharField(choices=tipo_choices, max_length=255, null=False, blank=False, default=tipo_choices[0])


    def __str__(self):
        return self.nome.capitalize()