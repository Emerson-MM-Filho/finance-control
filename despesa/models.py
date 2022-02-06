from datetime import datetime

from django.db import models
from categoria.models import Categoria

class Despesa(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    categoria = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.DO_NOTHING)
    data_da_despesa = models.DateField(default=datetime.now, blank=False, null=False)
    parcelas = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.nome.capitalize()