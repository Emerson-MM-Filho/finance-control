from .models import Despesa
from rest_framework import serializers


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['id', 'nome', 'descricao', 'valor', 'categoria', 'data_da_despesa', 'cartao', 'tipo', 'parcelas']
