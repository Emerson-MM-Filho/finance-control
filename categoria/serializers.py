from .models import Categoria
from rest_framework import serializers


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']