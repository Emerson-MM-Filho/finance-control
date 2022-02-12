from rest_framework import viewsets

from .models import Cartao
from.serializers import CartaoSerializer


class CartaoView(viewsets.ModelViewSet):
    queryset = Cartao.objects.all().order_by('-created_at')
    serializer_class = CartaoSerializer