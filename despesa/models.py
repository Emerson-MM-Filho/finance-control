from pyexpat import model
from django.db import models
from categoria.models import Categoria

class Despesa(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=8)
    categoria = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.nome} - {self.valor} - {self.categoria}'