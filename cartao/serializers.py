from .models import Cartao
from rest_framework import serializers


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id', 'nome']
