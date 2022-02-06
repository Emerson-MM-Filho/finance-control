from .models import Despesa
from rest_framework import serializers


class DespesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Despesa
        fields = ['id', 'nome', 'descricao', 'valor', 'categoria']
